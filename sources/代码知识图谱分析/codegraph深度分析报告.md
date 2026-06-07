# CodeGraph 深度分析报告

> **项目**: `@colbymchenry/codegraph` v0.9.4
> **作者**: Colby McHenry (主要), 社区贡献 20+
> **协议**: MIT License
> **仓库活跃期**: 2026-01-18 ~ 2026-05-24 (4个月, 327 commits)

---

## 一、项目概览

CodeGraph 是一个 **本地优先 (local-first)** 的代码智能系统，由三个角色组成：**代码知识图谱库** + **CLI 工具** + **MCP Server**。它通过 tree-sitter WASM 解析代码库的 AST，将符号(函数、类、方法等)和关系(调用、导入、继承等)存储到 SQLite FTS5 数据库中，形成一个完整的代码知识图谱，并通过 MCP (Model Context Protocol) 暴露给 AI 编码代理 (Claude Code、Cursor、Codex CLI、opencode、Hermes Agent)。

**核心价值主张**：让 AI 代理用 **1-5 次 codegraph 调用 + 0 次 Read/Grep** 回答结构性/流程性问题，替代传统的 grep+read 多轮探索。基准测试显示：**35% 成本降低、57% token 减少、46% 时间缩短、71% 工具调用减少**。

**发布形态**：
- npm 包 `@colbymchenry/codegraph` (thin installer)
- 自包含 Node 运行时打包 (平台特定 bundles: macOS/Linux/Windows)
- 无需本地编译，零 native 依赖

---

## 二、设计哲学

### 2.1 本地优先 (Local-First)

CodeGraph 的设计哲学深植于"一切皆本地"的理念：

- **数据处理完全本地**：所有代码解析、索引、查询均在本地机器完成，不向外部服务发送任何代码或遥测数据
- **存储完全本地**：数据存储在项目目录下的 `.codegraph/` 文件夹中，基于 SQLite，无需远程数据库
- **执行完全本地**：tree-sitter WASM 在 V8 引擎内运行 AST 解析，不需要编译原生模块

### 2.2 确定性优于启发式 (Deterministic over Heuristic)

- **AST 提取是确定性的**：所有节点和边都从 tree-sitter 的 AST 分析结果导出，不依赖 LLM 摘要
- **启发式仅用于动态分派桥接**：回调合成、React 重渲染、JSX 子组件等通过启发式边 (`provenance: 'heuristic'`) 补充，但这些边都被明确标注
- **宁可沉默不可错误**："partial coverage is WORSE than none" — 不完整的流桥接比没有桥接更糟糕，因为部分覆盖会误导代理进行更多 Read

### 2.3 适配代理而非改变代理 (Adapt to the Agent, Don't Change It)

这是 CodeGraph 最独特的设计决策：

- **核心洞察**：通过 server-instructions 或 tool descriptions 改变代理行为是**低效的** (已验证：trace-first steering 无法通过指令复制，需要 `--append-system-prompt` 才有效)
- **正确策略**：让工具在代理已经选择的调用模式中**做得更多**
  - `codegraph_trace` 内联每跳的源码 + 目标的被调用者，一次调用结束整个流调查
  - `codegraph_explore` 的 explore-flow 在代理可靠使用的调用中，通过已命名的符号组合交付 trace 级别的流信息
  - 新工具通常被代理**低估** (trace 很少被主动选择)，所以优化已有工具比添加新工具更有效

### 2.4 性能即正确性 (Performance is Correctness)

- **Wall-clock 延迟 + 工具调用数**是唯一优化目标 (不是 token 成本)
- **机制**：更少的 turn × 更小的累积 context = 更快 + 更便宜
- **Explore budget 单调性**：更大的代码库 tier 永远不能获得比更小 tier 更小的 `maxCharsPerFile` (否则代理被迫 Read)

---

## 三、技术架构

### 3.1 分层管线 (Layered Pipeline)

```
文件系统 → ExtractionOrchestrator (tree-sitter WASM) → SQLite DB (nodes/edges/files)
                           ↓
              ReferenceResolver (imports, name-matching, framework patterns)
                           ↓
              GraphQueryManager / GraphTraverser (BFS/DFS, impact radius)
                           ↓
              ContextBuilder (Markdown/JSON → AI 消费)
```

### 3.2 核心模块详解

#### 3.2.1 提取层 (`src/extraction/`)

**ExtractionOrchestrator** 是核心调度器：
- 并行读取文件 (I/O batch = 10)
- 通过 Worker 线程执行 tree-sitter WASM 解析
- Worker 回收策略：每 250 个文件重建一次 (解决 WASM 线性内存不缩小的限制)
- 单文件解析超时：10 秒 (防止 WASM OOM 冻结整个索引)
- 自动跳过 `.gitignore` 中的文件 (零配置)

**语言支持** (19 种 tree-sitter 语法 + 3 种专用提取器)：

| 语言 | 提取器文件 | 特殊处理 |
|------|-----------|---------|
| TypeScript/TSX | `typescript.ts` | JSX, 装饰器, 类型推导 |
| JavaScript/JSX | `javascript.ts` | CommonJS + ESM |
| Python | `python.ts` | 装饰器, 类型注解 |
| Go | `go.ts` | goroutine, interface 满足 |
| Rust | `rust.ts` | trait, impl, macro |
| Java | `java.ts` | 注解, 泛型 |
| C/C++ | `c-cpp.ts` | 头文件, 模板 |
| C# | `csharp.ts` | LINQ, async |
| Ruby | `ruby.ts` | block, module |
| PHP | `php.ts` | trait, namespace |
| Swift | `swift.ts` | protocol, extension |
| Kotlin | `kotlin.ts` | 协程, sealed class |
| Dart | `dart.ts` | Flutter setState 合成 |
| Scala | `scala.ts` | case class, implicit |
| Lua/Luau | `lua.ts` / `luau.ts` | Roblox Luau 支持 |
| Pascal | `pascal.ts` | Delphi DFM |
| Svelte | `svelte-extractor.ts` | 非 tree-sitter, 正则提取 |
| Vue | `vue-extractor.ts` | SFC 模板解析 |
| Liquid | `liquid-extractor.ts` | Shopify 模板 |

#### 3.2.2 数据库层 (`src/db/`)

**Schema 设计** (SQLite + FTS5)：

- **nodes 表**：21 种 NodeKind (file, module, class, struct, interface, trait, function, method, property, route, component 等)
- **edges 表**：12 种 EdgeKind (contains, calls, imports, extends, implements, references, type_of, returns 等)
- **files 表**：跟踪已索引文件的内容哈希、语言、大小
- **unresolved_refs 表**：延迟解析的引用
- **nodes_fts 虚拟表**：FTS5 全文搜索 (name, qualified_name, docstring, signature)
- **索引策略**：精心优化的复合索引 (edges 的 `source+kind`, `target+kind` 组合索引替代单独索引)

**存储后端**：
- v0.9.0 起使用 `node:sqlite` (Node 内置 SQLite)，不再依赖 `better-sqlite3` (原生编译) 或 WASM 回退
- WAL 模式支持并发读取不阻塞
- 自包含 Node 运行时打包，无 native 编译步骤

#### 3.2.3 引用解析层 (`src/resolution/`)

**三层解析策略**：

1. **Import Resolver** (`import-resolver.ts`)：跟踪 import/require/re-export 链，支持 tsconfig path aliases 和 Cargo workspace member globs
2. **Name Matcher** (`name-matcher.ts`)：基于名称的模糊匹配，处理 qualified names、built-in 过滤
3. **Framework Resolvers** (18 个框架解析器)：

| 框架 | 解析器 | 能力 |
|------|--------|------|
| Express | `express.ts` | Route 映射 |
| NestJS | `nestjs.ts` | 装饰器路由 |
| React | `react.ts` | setState→render 合成 |
| Vue/Nuxt | `vue.ts` | SFC 事件绑定、kebab→Pascal 转换 |
| Svelte/SvelteKit | `svelte.ts` | 响应式声明 |
| Django | `python.ts` | ORM 描述符、URL patterns |
| Flask | `python.ts` | 路由装饰器 |
| FastAPI | `python.ts` | APIRouter |
| Rails | `ruby.ts` | routes.rb 解析 |
| Laravel | `laravel.ts` | Route facade |
| Spring | `java.ts` | @RequestMapping |
| Play | `play.ts` | 路由文件 |
| Go (net/http, Gin, etc.) | `go.ts` | http.HandleFunc |
| Rust (Axum, Actix) | `rust.ts` | 路由宏 |
| ASP.NET | `csharp.ts` | Controller 路由 |
| SwiftUI/UIKit | `swift.ts` | View body |
| Vapor | `swift.ts` | 路由 |
| Drupal | `drupal.ts` | routing.yml |

#### 3.2.4 回调合成器 (`callback-synthesizer.ts`)

这是 CodeGraph 最精巧的组件之一，用于桥接静态分析无法捕获的动态分派：

**Phase 1 — Field-backed Observer**：
- 识别注册器模式 (`onUpdate(cb) { this.callbacks.add(cb) }`)
- 识别分派器模式 (`triggerUpdate() { for (cb of this.callbacks) cb() }`)
- 配对注册调用 (`scene.onUpdate(this.triggerRender)`) 合成边

**Phase 2 — String-keyed EventEmitter**：
- 解析 `.on('event', handler)` 注册
- 解析 `.emit('event')` 分派
- 按事件名配对 (跳过过于通用的 `error` 等事件，fan-out > 6 则跳过)

**Phase 3 — React/UI 特殊通道**：
- `setState → render` 合成 (React/Flutter)
- JSX child 合成 (`<Component/>` → Component render)
- Vue SFC template：kebab-case 子组件、事件绑定 (`@click="fn"`)
- Vue composable 解构 (`const { close } = useSidebarControl()`)

#### 3.2.5 图查询层 (`src/graph/`)

- **GraphTraverser**：BFS/DFS 遍历，支持方向、深度、边类型过滤
- **GraphQueryManager**：高级查询 (callers, callees, impact radius, path finding)
- 遍历限制：默认 max 1000 节点，可配置

#### 3.2.6 上下文构建层 (`src/context/`)

- **ContextBuilder**：组合 FTS 搜索 + 图遍历构建结构化上下文
- 从自然语言查询中提取符号名 (CamelCase, snake_case, dot.notation)
- 输出格式：Markdown (供 AI 消费) 或 JSON

### 3.3 MCP Server (`src/mcp/`)

通过 MCP 协议暴露 10 个工具：

| 工具 | 用途 |
|------|------|
| `codegraph_search` | 按名称搜索符号 |
| `codegraph_context` | **主要工具** — 搜索+节点+callers+callees 一体化 |
| `codegraph_trace` | **流程追踪** — 从→到 的完整调用路径，含动态分派跳 |
| `codegraph_explore` | **探索** — 一次调用返回多个相关符号的源码，按文件分组 |
| `codegraph_callers` | 谁调用了我 |
| `codegraph_callees` | 我调用了谁 |
| `codegraph_impact` | **变更影响** — 爆炸半径分析 |
| `codegraph_node` | 单个符号详情 |
| `codegraph_files` | 目录列表 |
| `codegraph_status` | 索引状态 |

**自适应 Explore Budget**：

| 代码库大小 (文件数) | explore 调用数 | 每次输出字符 | 每文件字符 |
|---------------------|---------------|-------------|-----------|
| < 500 | 1 | 18K | 3,800 |
| 500 - 5,000 | 2 | 28K | 6,500 |
| 5,000 - 15,000 | 3 | 35K | 7,000 |
| 15,000 - 25,000 | 4 | 38K | 7,000 |
| ≥ 25,000 | 5 | 38K | 7,000 |

### 3.4 多代理安装器 (`src/installer/`)

**AgentTarget 接口**设计精巧，支持 5 种 AI 编码代理：

| 代理 | 目标文件 | 配置格式 | 特殊处理 |
|------|---------|---------|---------|
| Claude Code | `claude.ts` | `.claude/settings.json` + `CLAUDE.md` | auto-allow permissions |
| Cursor | `cursor.ts` | `.cursor/mcp.json` + `.cursor/rules/codegraph.mdc` | `--path` 注入解决 cwd 问题 |
| Codex CLI | `codex.ts` | `~/.codex/AGENTS.md` + TOML config | 手写 TOML 序列化器 |
| opencode | `opencode.ts` | `opencode.jsonc` | jsonc-parser 保留注释/格式 |
| Hermes Agent | `hermes.ts` | Hermes 配置 | — |

**添加新代理 = 一个新文件 + 一行注册**，这是极佳的可扩展设计。

---

## 四、代码实现质量

### 4.1 代码规模与结构

- **总源文件**：100 个 TypeScript 文件
- **总代码行数**：约 33,358 行
- **测试文件**：30+ 个测试文件
- **文档文件**：7 个设计文档 + 基准测试报告
- **模块划分**：清晰的 9 层模块 (extraction → db → resolution → graph → context → search → sync → mcp → installer)

### 4.2 TypeScript 严格模式

- `strict: true` + 所有严格子选项启用
- `noUncheckedIndexedAccess: true` — 额外的数组索引安全检查
- `noImplicitReturns: true` — 所有代码路径必须返回
- ES2022 target, commonjs 模块

### 4.3 性能优化

1. **Worker 线程解析**：重型 tree-sitter 解析在独立线程运行
2. **Worker 回收**：每 250 文件重启 worker 释放 WASM 内存
3. **SQLite WAL 模式**：并发读取不阻塞
4. **FTS5 全文搜索**：毫秒级符号查找
5. **Prepared Statements**：所有查询使用预编译语句
6. **LRU 缓存**：解析器结果缓存 (默认 5,000 条)
7. **批量文件 I/O**：10 个文件并行读取
8. **增量同步**：只重新索引内容哈希变化的文件

### 4.4 安全设计

1. **路径验证**：`validatePathWithinRoot` 防止目录遍历攻击
2. **敏感目录保护**：`SENSITIVE_PATHS` 列表拒绝 `/etc`, `/proc`, `C:\Windows` 等
3. **输入大小限制**：`MAX_INPUT_LENGTH = 10,000`, `MAX_PATH_LENGTH = 4,096`
4. **Symlink 安全**：session marker 写入时拒绝跟随符号链接 (Windows 特殊处理)
5. **输出截断**：`MAX_OUTPUT_LENGTH = 15,000` 防止 context bloat

### 4.5 跨平台支持

- **原生文件监视器**：FSEvents (macOS) / inotify (Linux) / ReadDirectoryChangesW (Windows)
- **WSL2 特殊处理**：检测 `/mnt` 挂载并禁用监视器 (回退到 git hooks)
- **Windows 验证**：通过 Parallels VM + SSH 进行真实 Windows 测试
- **路径规范化**：处理 `file://` URI、Windows 驱动器号路径
- **平台特定测试门控**：`it.runIf(process.platform === 'win32')`

---

## 五、使用场景

### 5.1 AI 编码代理的代码导航

**主要场景**：为 Claude Code、Cursor 等 AI 代理提供结构化代码上下文，替代传统的 grep + read 多轮探索。

**典型工作流**：
1. 代理收到 "这个函数怎么工作的?" 类型问题
2. 调用 `codegraph_context` 获取符号的完整上下文 (定义 + 调用者 + 被调用者)
3. (可选) 调用 `codegraph_trace` 获取跨文件的完整调用链
4. **不需要** Read/Grep 任何文件

### 5.2 代码库入职/理解

- 新开发者快速理解代码库结构
- 架构理解：通过 `codegraph_explore` 浏览模块关系
- 调用链追踪：理解数据如何从入口流向出口

### 5.3 重构影响分析

- `codegraph_impact` 分析变更的爆炸半径
- `codegraph_callers` 查看谁依赖了目标符号
- 重构前评估风险等级

### 5.4 代码审查辅助

- PR 审查时理解变更的上下游影响
- 追踪 bug 修复影响的代码路径
- 验证重构没有破坏隐式依赖

### 5.5 CI/CD 集成

- 通过 CLI 的 `codegraph affected` 命令确定受影响的文件/测试
- git hooks (post-commit, post-merge, post-checkout) 触发增量索引

---

## 六、软硬件要求

### 6.1 硬件要求

| 维度 | 最低要求 | 推荐配置 |
|------|---------|---------|
| CPU | 任意现代 CPU (x64/ARM64) | 4 核以上 |
| 内存 | 2 GB RAM | 8 GB+ RAM (大型代码库) |
| 磁盘 | ~100 MB (安装) + 项目大小的 2-5% (索引) | SSD 推荐 |
| 网络 | 安装时需要 (npm/download)，运行时完全离线 | — |

### 6.2 软件要求

| 组件 | 要求 |
|------|------|
| 操作系统 | macOS 12+, Linux (glibc 2.31+), Windows 10+ |
| Node.js | >= 20.0.0 < 25.0.0 (自包含 bundle 不需要本地 Node) |
| 运行时 | 无需 Python, 无需 C++ 编译工具链 |
| 数据库 | SQLite (内置, 无需安装) |

### 6.3 支持的 AI 代理平台

| 代理 | 最低版本要求 |
|------|-------------|
| Claude Code | 当前版本 |
| Cursor | 当前版本 |
| Codex CLI | 当前版本 |
| opencode | 当前版本 |
| Hermes Agent | 当前版本 |

---

## 七、可扩展性

### 7.1 新语言支持

添加新语言支持需要：
1. 在 `src/extraction/languages/` 下创建语言提取器文件
2. 在 `grammars.ts` 中注册 WASM 语法文件和文件扩展名映射
3. 将 `.wasm` 文件放入 `src/extraction/wasm/`

**当前 19 种语言的覆盖已包含主流编程语言**。

### 7.2 新框架支持

添加新框架路由解析需要：
1. 在 `src/resolution/frameworks/` 下创建框架解析器
2. 在 `frameworks/index.ts` 中注册

**18 个框架解析器已覆盖主流 Web 框架**。

### 7.3 新 AI 代理支持

添加新代理目标需要：
1. 在 `src/installer/targets/` 下创建一个实现 `AgentTarget` 接口的文件
2. 在 `registry.ts` 中添加一行注册

**这种"一个文件 + 一行注册"的扩展模式是极佳的 API 设计**。

### 7.4 MCP 工具扩展

- 工具定义在 `src/mcp/tools.ts`
- Server 指令在 `src/mcp/server-instructions.ts`
- 支持 `CODEGRAPH_MCP_TOOLS` 环境变量控制启用哪些工具

---

## 八、与竞品对比

### 8.1 vs Sourcegraph (Cody)

| 维度 | CodeGraph | Sourcegraph |
|------|-----------|-------------|
| 部署模式 | 完全本地 | 云端 + 本地 |
| 索引方式 | tree-sitter WASM | SCIP 索引器 |
| 数据存储 | SQLite 本地文件 | PostgreSQL (云端) |
| 隐私性 | 代码不出本地 | 代码发送到云端 (精确匹配) |
| 适用规模 | 单项目 ~50K 文件 | 全企业代码库 |
| 集成方式 | MCP 协议 | 专有 API |
| 成本 | 免费开源 | 免费层 + 付费 |

### 8.2 vs Aider/Grep-based 方案

| 维度 | CodeGraph | Grep/Read 循环 |
|------|-----------|---------------|
| 查询类型 | 结构化图查询 | 文本模式匹配 |
| 调用链追踪 | 自动 (含动态分派) | 手动跟踪 |
| 工具调用数 | 1-5 次 | 10-50 次 |
| 精确度 | 精确到符号级别 | 行级别匹配 |
| 设置成本 | 一次性索引 | 无 |

### 8.3 vs LSP (Language Server Protocol)

| 维度 | CodeGraph | LSP |
|------|-----------|-----|
| 语言支持 | 19 种 | 通常 1-3 种/服务器 |
| 需要项目编译 | 不需要 | 通常需要 |
| 跨语言支持 | 支持 (同一数据库) | 每语言独立服务器 |
| 离线能力 | 完全离线 | 依赖语言服务器 |
| AI 集成 | 原生 MCP | 需要适配 |

### 8.4 vs GitHub Copilot 代码搜索

| 维度 | CodeGraph | Copilot 搜索 |
|------|-----------|-------------|
| 搜索方式 | 语义图遍历 | 关键词 + AI 排序 |
| 关系查询 | 支持 (callers, impact) | 不支持 |
| 本地运行 | 是 | 否 (云端) |
| 定制化 | 完全可定制 | 黑盒 |

---

## 九、项目活跃度与演进

### 9.1 开发节奏

- **项目启动**：2026-01-18
- **当前版本**：v0.9.4 (2026-05-24)
- **总提交数**：327
- **活跃开发天数**：~4 个月
- **贡献者**：主要作者 Colby McHenry (373 commits) + 社区贡献者 (Olaf Monien 16, andreinknv 7, Martin Oehlert 4 等)

### 9.2 版本演进

| 版本 | 日期 | 里程碑 |
|------|------|--------|
| 0.7.x | ~2026-03 | Claude 专属 installer |
| 0.8.0 | ~2026-04 | NestJS 路由, 自适应 explore budget |
| 0.9.0 | 2026-05-21 | **重大**: 自包含 Node 运行时打包, `node:sqlite` 替代 `better-sqlite3`, Lua/Luau 支持 |
| 0.9.1 | 2026-05-21 | curl install 修复 |
| 0.9.2 | 2026-05-22 | Drupal 支持, 零配置 .gitignore 索引 |
| 0.9.3 | 2026-05-22 | uninstall 命令, OOM 崩溃修复 |
| 0.9.4 | 2026-05-24 | **框架感知路由解析, 动态分派流合成** |

### 9.3 社区参与

- 多个社区 PR 被合并 (Drupal 支持, CLI callers/callees 命令, 安全修复, Windows 修复)
- GitHub Issues 活跃 (安全报告、功能请求)
- 最近添加了 Starlight 文档站点

### 9.4 测试覆盖

- **单元测试**：30+ 测试文件，使用 vitest
- **集成测试**：`__tests__/integration/` (全管线, LRU 缓存, MCP 输入限制)
- **评估套件**：`__tests__/evaluation/` (自动化评分)
- **安装器测试**：47 个参数化合约测试
- **无 DB Mock**：测试使用真实 SQLite + 真实文件系统
- **Windows 测试**：通过 Parallels VM 真实验证

---

## 十、创新亮点

### 10.1 动态分派流合成

这是 CodeGraph 的核心创新 — 通过静态分析桥接动态语言的间接调用：

- **回调/观察者模式**：识别 `onX(cb)` + `triggerX()` 配对
- **EventEmitter 模式**：按事件名配对 `on('event', handler)` + `emit('event')`
- **React 重渲染**：`setState → render` 自动桥接
- **JSX 子组件**：`<Component/>` 自动关联到 Component 的 render
- **Vue SFC**：kebab-case 子组件 + 事件绑定解析

### 10.2 自适应输出预算

根据代码库大小动态调整 explore 工具的输出：
- 小项目：更紧凑的输出，更紧密的聚类
- 大项目：更慷慨的输出，更多的文件覆盖
- **单调性保证**：更大的 tier 永远不会获得更小的 per-file 限制

### 10.3 Worker 内存管理

- WASM 线性内存只能增长不能缩小 (WebAssembly 规范限制)
- 每 250 个文件回收 Worker 线程释放 V8 isolate
- 10 秒超时防止单文件解析冻结整个索引

### 10.4 多代理统一安装器

- **一个 AgentTarget 接口** 统一 5 种代理
- 安装/卸载/检测/打印配置 完整生命周期
- 幂等性保证 (byte-identical re-run → unchanged)
- 兄弟 MCP 服务器保留 (卸载不影响其他配置)

### 10.5 完全自包含发布

- 自 Node v0.9.0 起，每个平台 (macOS/Linux/Windows × x64/ARM64) 打包一个完整的 Node 运行时
- 用户**不需要安装 Node.js**
- 不需要 native 编译 (没有 `node-gyp`, 没有 C++ 工具链)
- `node:sqlite` 内置，不需要 `better-sqlite3`

---

## 十一、局限与挑战

### 11.1 静态分析固有限制

- **无法追踪运行时多态**：接口到具体实现的映射在运行时才能确定
- **无法追踪局部变量数据流**：跟踪每个局部变量会导致图爆炸
- **反射/元编程**：无法静态分析 `eval()`, `new Function()` 等

### 11.2 规模限制

- 单项目设计 (~50K 文件是已知上限)
- 不支持跨仓库查询 (与 Sourcegraph 的企业级能力不同)
- 大型 monorepo 可能需要较长的首次索引时间

### 11.3 实时性

- 文件监视有 ~1 秒延迟 (防抖机制)
- 编辑后立即查询可能返回过时结果
- 大规模重构后建议手动触发 `codegraph sync`

### 11.4 语言/框架覆盖

- 19 种语言但不是所有语言提取深度相同
- 框架解析器只覆盖主流框架，小众框架可能不被识别
- 跨语言调用链 (如 JS 调用 Python via IPC) 无法追踪

---

## 十二、总结

CodeGraph 是一个**工程成熟度极高**的项目，它不是简单的代码搜索工具，而是一个完整的**代码知识图谱系统**。其核心价值在于：

1. **设计哲学清晰**：本地优先、确定性优先、适配代理而非改变代理
2. **架构分层合理**：提取 → 解析 → 图查询 → 上下文构建，每层职责明确
3. **动态分派合成**：这是区别于所有竞品的杀手级特性，让静态分析能追踪动态语言的间接调用
4. **多代理生态**：统一的安装器接口，一个接口适配 5 种 AI 编码代理
5. **完全自包含**：零 native 依赖，零外部服务，完全离线运行
6. **性能导向**：自适应预算、Worker 内存管理、FTS5 索引，一切为了"让 AI 不需要 Read/Grep"

**适用场景评估**：
- **最适合**：使用主流语言和框架的项目，需要 AI 代理深度理解代码结构的场景
- **不太适合**：严重依赖运行时动态特性的项目、需要跨仓库搜索的企业场景

**总体评价**：CodeGraph 在 4 个月内从零到 v0.9.4，代码质量高，测试覆盖充分，文档详尽。它代表了 AI 编码工具链中"代码智能"层的一个重要方向 — 通过结构化的代码知识图谱，让 AI 代理在理解代码时不再依赖低效的文本搜索。
