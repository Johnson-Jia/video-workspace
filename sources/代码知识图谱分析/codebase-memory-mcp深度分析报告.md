# Codebase Memory MCP 深度分析报告

## 一、项目概述

**项目名称**: Codebase Memory MCP (io.github.DeusData/codebase-memory-mcp)
**版本**: v0.6.1
**许可证**: MIT License (Copyright 2025 DeusData)
**仓库**: https://github.com/DeusData/codebase-memory-mcp
**定位**: 持久化代码库知识图谱 — 支持 155 种语言，亚毫秒级查询，比 grep 减少 99% 的 token 消耗

Codebase Memory MCP 是一个纯 C 语言编写的代码智能引擎，作为 MCP (Model Context Protocol) 服务器运行，为 AI 编程助手（Claude Code、Codex CLI、Gemini CLI 等）提供结构化的代码库知识图谱。它通过 tree-sitter AST 解析提取代码实体和关系，存储在 SQLite 数据库中，并支持 Cypher 查询语言进行图遍历和模式匹配。

## 二、设计哲学

### 2.1 极致性能优先

项目以**纯 C 语言**从零构建，而非选择 Python/TypeScript 等高级语言。这一决策体现了对性能的极致追求：

- **内存分配**: 使用 mimalloc 替代系统 malloc，统一追踪所有 C/C++ 分配，默认使用 50% 物理内存 (`MAIN_RAM_FRACTION = 0.5`)
- **零拷贝设计**: 字符串内联 (str_intern)、arena 分配器、slab 分配器等多层内存管理
- **LZ4/Zstd 压缩**: 图数据压缩存储，减少 I/O 瓶颈
- **亚毫秒查询**: SQLite WAL 模式 + mmap(64MB 默认) + 批量操作优化

### 2.2 无外部依赖哲学

项目采用**全量内嵌 (vendoring)** 策略，所有依赖均打包在源码树中：

| 依赖库 | 用途 | 内嵌路径 |
|--------|------|----------|
| tree-sitter | 155 语言 AST 解析 | `vendored/tree-sitter/` |
| sqlite3 | 图数据库引擎 | `vendored/sqlite3/` |
| yyjson | 高性能 JSON 解析 | `vendored/yyjson/` |
| xxhash | 超高速哈希函数 | `vendored/xxhash/` |
| mimalloc | 内存分配器 | `vendored/mimalloc/` |
| mongoose | 嵌入式 HTTP 服务器 | `vendored/mongoose/` |
| LZ4 | 快速压缩 | `vendored/lz4/` |
| zstd | 高比压压缩 | `vendored/zstd/` |

这意味着**编译产物是单个二进制文件**，无运行时依赖，简化了分发和部署。

### 2.3 安全第一

项目声称达到 **SLSA Level 3** 安全标准：
- 7 层安全审计（Makefile.cbm 中定义）
- ASan/UBSan/TSan 三重内存安全检测
- clang-tidy + cppcheck 静态分析
- 代码签名和可重复构建

## 三、架构设计

### 3.1 整体架构

```
┌──────────────────────────────────────────────────────────────┐
│                     main.c (入口)                             │
│   ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌─────────────┐  │
│   │ MCP协议  │  │ Watcher  │  │ HTTP UI  │  │  CLI 模式   │  │
│   │ JSON-RPC │  │ 后台线程  │  │ 后台线程  │  │  单次调用   │  │
│   └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬──────┘  │
│        │             │             │               │          │
│   ┌────▼─────────────▼─────────────▼───────────────▼──────┐  │
│   │                    Store (SQLite)                      │  │
│   │   nodes / edges / projects / file_hashes / vectors    │  │
│   └───────────────────────┬───────────────────────────────┘  │
│                           │                                    │
│   ┌───────────────────────▼───────────────────────────────┐  │
│   │                Pipeline (索引管线)                      │  │
│   │  Discover → Extract → Registry → Calls → Usages →     │  │
│   │  Semantic → Tests → Communities → HTTP → Config →      │  │
│   │  GitHistory → Similarity → SemanticEdges → Dump        │  │
│   └───────────────────────┬───────────────────────────────┘  │
│                           │                                    │
│   ┌───────────────────────▼───────────────────────────────┐  │
│   │                Foundation (基础设施)                    │  │
│   │  arena / mem / hash_table / str_intern / yaml / log   │  │
│   └───────────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

### 3.2 模块职责

#### 3.2.1 入口层 (`src/main.c`)

`main()` 函数实现了多模式启动：

1. **MCP 服务器模式**（默认）: 在 stdin/stdout 上运行 JSON-RPC 2.0 协议
2. **CLI 模式**: `cli <tool> <json>` 直接执行单个工具调用
3. **安装/卸载/更新**: `install`/`uninstall`/`update` 子命令
4. **配置管理**: `config <list|get|set|reset>`

信号处理 (SIGTERM/SIGINT) 实现优雅关闭：取消运行中的管线、释放管线锁、关闭 stdin 解除阻塞、停止 watcher 和 HTTP UI 线程。

#### 3.2.2 MCP 协议层 (`src/mcp/mcp.c`)

实现了完整的 MCP 工具调用协议，提供 **14 个图分析工具**：

| 工具名 | 功能 |
|--------|------|
| `index_repository` | 索引代码仓库 |
| `search_graph` | 图谱搜索（正则、标签、文件模式） |
| `query_graph` | Cypher 查询 |
| `trace_path` | 路径追踪（BFS 遍历） |
| `get_code_snippet` | 获取代码片段 |
| `get_graph_schema` | 图谱模式 |
| `get_architecture` | 架构分析 |
| `search_code` | 代码搜索 |
| `list_projects` | 列出项目 |
| `delete_project` | 删除项目 |
| `index_status` | 索引状态 |
| `detect_changes` | 变更检测 |
| `manage_adr` | 架构决策记录管理 |
| `ingest_traces` | 导入追踪数据 |

MCP 服务器支持**空闲存储逐出**机制 (`cbm_mcp_server_evict_idle`)：当存储空闲超时后自动释放内存。

#### 3.2.3 索引管线 (`src/pipeline/`)

管线采用**多遍 (multi-pass) 架构**，从 `pipeline.h` 注释可见完整的 7 阶段流程：

1. **Structure**: 创建 Project/Folder/Package/File 节点
2. **Definitions**: 提取 + 写入节点 + 构建注册表
3. **Imports**: 解析 import 边
4. **Calls**: 调用解析（注册表 + LSP）
5. **Usages**: 使用/类型引用边
6. **Semantic**: 继承/装饰/实现
7. **Post**: 测试、社区、HTTP 链接、配置、Git 历史

**并行执行优化**: `pass_parallel.c` 实现了两阶段并行：
- Phase 3A: 并行提取 + 创建定义节点（per-worker graph buffer，然后合并）
- Phase 4: 并行调用/使用/语义解析

**增量索引** (`pipeline_incremental.c`): 基于 mtime+size 分类文件，仅重新解析变更文件。

#### 3.2.4 存储层 (`src/store/store.c`)

基于 SQLite 的图存储引擎，核心数据模型：

```c
// 节点: 实体 (函数/类/方法/模块/文件/路由等)
cbm_node_t { id, project, label, name, qualified_name, file_path, start_line, end_line, properties_json }

// 边: 关系 (CALLS, IMPORTS, EXTENDS, IMPLEMENTS, HTTP_CALLS, SIMILAR_TO, SEMANTICALLY_RELATED 等)
cbm_edge_t { id, project, source_id, target_id, type, properties_json }
```

**关键优化**：
- **批量写入模式** (`begin_bulk/end_bulk`): 关闭同步、扩大缓存，保留 WAL 模式保证崩溃安全
- **索引管理** (`drop_indexes/create_indexes`): 批量插入时临时移除索引
- **WAL 检查点** + PRAGMA optimize
- **mmap 配置**: 默认 64MB，通过 `CBM_SQLITE_MMAP_SIZE` 环境变量调整

**高级查询能力**：
- BFS 图遍历（支持方向过滤、边类型过滤、深度限制）
- 影响分析（hop 深度 → 风险等级映射: Critical/High/Medium/Low）
- Louvain 社区发现算法
- 架构分析（语言统计、包摘要、入口点、路由、热点、跨包边界、服务链接、层级）
- 向量搜索（基于 RI 向量的余弦相似度）
- ADR (Architecture Decision Record) 存储

#### 3.2.5 Cypher 查询引擎 (`src/cypher/cypher.c`)

实现了 Cypher 查询语言的子集，支持：
- `MATCH` 模式匹配（节点模式、关系模式、变长路径 `*min..max`）
- `WHERE` 条件过滤（AND/OR/NOT/XOR 表达式树、正则匹配 `=~`、IN 列表、IS NULL/IS NOT NULL）
- `RETURN` 投影（聚合函数 COUNT/SUM/AVG/MIN/MAX/COLLECT、CASE 表达式、DISTINCT）
- `ORDER BY` / `SKIP` / `LIMIT`
- `OPTIONAL MATCH` / `WITH` / `UNION`

完整的四阶段处理：Lexer → Parser (AST) → Planner → Executor

#### 3.2.6 语义分析 (`src/semantic/semantic.c`)

这是项目最独特的模块之一 — **无外部模型的算法化代码嵌入**，组合 11 种信号：

1. TF-IDF 元数据词元重叠
2. Random Indexing 共现向量（同义词桥接）
3. MinHash 结构指纹
4. API 签名向量（相同被调函数 → 相关）
5. 类型签名向量（相同参数/返回类型 → 相关）
6. 模块邻近度（同目录 → 加权提升）
7. 装饰器模式向量
8. AST 结构特征（控制流形状、表达式类型，25 维）
9. 近似数据流（params→return, params→condition）
10. 图扩散（邻居混合的传递闭包）
11. Halstead-Lite 复杂度特征

使用 768 维向量（与 nomic-embed-code 对齐），通过余弦相似度计算分数，默认阈值 0.75。

#### 3.2.7 文件监控 (`src/watcher/watcher.c`)

自适应轮询机制：
- 基础间隔 5 秒
- 每增加 500 文件增加 1 秒
- 上限 60 秒
- 检测 git HEAD 移动和工作目录变更

#### 3.2.8 基础设施层 (`src/foundation/`)

| 模块 | 功能 |
|------|------|
| `arena.c` | Arena 分配器（批量释放） |
| `mem.c` | mimalloc 封装，50% RAM 预算 |
| `hash_table.c` | 通用哈希表 |
| `str_intern.c` | 字符串去重 |
| `slab_alloc.c` | Slab 分配器 |
| `vmem.c` | 虚拟内存管理 |
| `yaml.c` | YAML 解析 |
| `log.c` | 日志系统 |
| `profile.c` | 性能分析 |
| `diagnostics.c` | 诊断系统 |
| `compat.c` | 跨平台兼容（Windows/macOS/Linux） |
| `platform.c` | 平台检测 |

#### 3.2.9 HTTP UI (`src/ui/`)

可选的嵌入式 HTTP 服务器（mongoose），提供图可视化界面：
- 端口可配置（默认 9749）
- 嵌入式前端资源 (`embedded_assets.h`)
- 3D 布局引擎 (`layout3d.c`)

### 3.3 管线 Pass 详解

项目实现了丰富的管线 pass（22 个）：

| Pass | 文件 | 功能 |
|------|------|------|
| Structure | `pipeline.c` | 创建目录/包/文件节点 |
| Definitions | `pass_definitions.c` | tree-sitter AST 提取函数/类/方法/变量 |
| Registry | `registry.c` | 全局符号注册表 |
| Calls | `pass_calls.c` | 调用边解析 |
| Imports | 内嵌于 definitions | import 边构建 |
| Usages | `pass_usages.c` | 使用/类型引用边 |
| Semantic | `pass_semantic.c` | 继承/装饰/实现边 |
| Semantic Edges | `pass_semantic_edges.c` | 算法语义相似边 |
| Similarity | `pass_similarity.c` | MinHash SIMILAR_TO 边 |
| Tests | `pass_tests.c` | 测试函数/文件识别 |
| Communities | 内嵌 | Louvain 社区发现 |
| HTTP Links | `pass_route_nodes.c` | HTTP 路由节点 |
| Config | `pass_configures.c` | 配置文件分析 |
| Config Link | `pass_configlink.c` | 配置↔代码链接 |
| Git History | `pass_githistory.c` | 变更耦合分析 |
| Git Diff | `pass_gitdiff.c` | 增量 diff 解析 |
| Infra Scan | `pass_infrascan.c` | Docker/Terraform/K8s 基础设施分析 |
| Env Scan | `pass_envscan.c` | 环境变量 URL 扫描 |
| Cross-Repo | `pass_cross_repo.c` | 跨仓库依赖 |
| LSP Cross | `pass_lsp_cross.c` | LSP 类型感知调用解析 |
| Pkg Map | `pass_pkgmap.c` | 包映射（tsconfig/jsconfig） |
| Compile Commands | `pass_compile_commands.c` | compile_commands.json 解析 |
| Enrichment | `pass_enrichment.c` | 装饰器标签富化 |
| FastAPI Depends | `pass_calls.c` | FastAPI 依赖注入边 |
| K8s | `pass_k8s.c` | Kubernetes 清单分析 |

## 四、技术栈

### 4.1 核心技术

| 技术 | 版本/说明 | 用途 |
|------|-----------|------|
| C 语言 | C11 标准 | 核心实现语言 |
| tree-sitter | vendored | 155 语言 AST 解析 |
| SQLite 3 | vendored | 图数据库引擎 |
| yyjson | vendored | JSON 解析 |
| xxhash | vendored | 哈希函数 |
| mimalloc | vendored | 内存分配器 |
| mongoose | vendored | 嵌入式 HTTP 服务器 |
| LZ4 | vendored | 快速压缩 |
| zstd | vendored | 高比压压缩 |

### 4.2 构建系统

- **Makefile.cbm**: 650 行构建脚本
- **编译器**: 支持 GCC/Clang
- **Sanitizers**: ASan (地址)、UBSan (未定义行为)、TSan (线程)
- **静态分析**: clang-tidy、cppcheck、clang-format
- **安全审计**: 7 层检查

### 4.3 跨平台支持

从 `server.json` 可见支持 5 个平台：
- macOS ARM64
- macOS AMD64
- Linux AMD64
- Linux ARM64
- Windows AMD64

从 `compat.c`/`compat_fs.c`/`compat_thread.c` 可见实现了完整的跨平台抽象层。

## 五、使用场景

### 5.1 AI 编程助手集成

项目支持广泛的 AI 编程工具：

| 工具 | 集成方式 |
|------|----------|
| Claude Code | MCP 协议 |
| Codex CLI | MCP 协议 |
| Gemini CLI | MCP 协议 |
| Zed 编辑器 | MCP 协议 |
| VS Code | MCP 协议 |
| Aider | MCP 协议 |
| KiloCode | MCP 协议 |
| Kiro | MCP 协议 |
| OpenCode | MCP 协议 |
| Antigravity | MCP 协议 |

### 5.2 代码智能查询

1. **影响分析**: 修改某个函数前，评估影响范围和风险等级
2. **依赖追踪**: 追踪调用链路，理解代码依赖关系
3. **架构理解**: 获取项目架构概览（语言、包、入口点、热点）
4. **代码搜索**: 基于正则、标签、文件模式的图搜索
5. **变更检测**: 分析 git diff 影响的符号和执行流程

### 5.3 DevOps 场景

- **基础设施分析**: Dockerfile、Terraform、K8s 清单解析
- **变更耦合分析**: 识别经常一起变更的文件对
- **环境变量扫描**: 检测 URL 绑定和密钥

### 5.4 知识管理

- **ADR 管理**: 存储和查询架构决策记录
- **图可视化**: HTTP UI 提供 3D 图谱可视化

## 六、软硬件要求

### 6.1 硬件要求

| 资源 | 最低要求 | 推荐配置 |
|------|----------|----------|
| 内存 | 2 GB 可用 | 8 GB+ (默认使用 50% 物理内存) |
| CPU | 单核 | 多核 (并行提取) |
| 磁盘 | 100 MB (二进制) | 1 GB+ (数据库) |

### 6.2 软件要求

- **操作系统**: macOS / Linux / Windows
- **运行时依赖**: 无 (单个二进制文件)
- **构建依赖** (仅开发):
  - C 编译器 (GCC 或 Clang)
  - GNU Make
  - 可选: clang-tidy、cppcheck (静态分析)

### 6.3 数据规模

- 支持 155 种编程语言的 AST 解析
- 单项目可处理数万级节点和边
- 向量搜索支持 <500K 函数
- 查询响应时间: 亚毫秒级

## 七、可扩展性分析

### 7.1 语言扩展

tree-sitter 语法是声明式的，添加新语言只需添加对应的 `.so` 语法文件。目前内嵌了 155 种语言的 tree-sitter 语法。

### 7.2 Pipeline Pass 扩展

管线采用 pass 注册机制 (`pass_*.c`)，每个 pass 是独立模块，可以添加新的 pass 而不影响现有逻辑。新增 pass 只需：
1. 实现 `cbm_pipeline_pass_xxx(ctx, files, count)` 函数
2. 在 `pipeline.c` 的 run 流程中调用
3. 在 `pipeline_internal.h` 中声明原型

### 7.3 存储扩展

SQLite 作为存储引擎，天然支持：
- 添加新的节点标签和边类型
- 扩展 properties_json 字段
- 自定义索引

### 7.4 查询扩展

Cypher 引擎支持扩展：
- 新的聚合函数
- 新的字符串函数
- 新的条件操作符

### 7.5 语义信号扩展

11 种语义信号通过 `cbm_sem_config_t` 权重配置，可以调整或添加新信号。

## 八、安全性分析

### 8.1 内存安全

- **mimalloc**: 统一内存追踪，消除内存泄漏盲区
- **ASan/UBSan/TSan**: 编译时内存安全检测
- **Arena 分配器**: 批量释放，避免 use-after-free
- **信号安全**: `signal_handler` 只执行原子操作

### 8.2 数据安全

- **WAL 模式**: 崩溃安全（崩溃后自动恢复）
- **mmap 防护**: 负值 clamp 到 0，切换到 read()/pread() I/O 避免 SIGBUS
- **完整性检查**: `cbm_store_check_integrity()` 检测数据库损坏

### 8.3 构建安全

- **SLSA Level 3**: 可重复构建、代码签名
- **7 层安全审计**: Makefile.cbm 中定义的完整审计流程
- **vendored 依赖**: 锁定依赖版本，避免供应链攻击

### 8.4 运行时安全

- **无网络暴露**: MCP 服务器仅通过 stdin/stdout 通信
- **HTTP UI 仅本地**: 仅监听 localhost
- **索引锁**: 防止并发管线运行导致数据库损坏

## 九、与同类项目对比

### 9.1 对比表

| 特性 | Codebase Memory MCP | Sourcegraph | ctags | LSP (Language Server) |
|------|---------------------|-------------|-------|----------------------|
| 实现语言 | 纯 C | Go/TypeScript | C | 各语言不同 |
| 知识图谱 | 是 (Neo4j 风格) | 否 (索引+搜索) | 否 (标签) | 否 |
| 查询语言 | Cypher 子集 | 自定义 API | 无 | 无 |
| AI 集成 | MCP 协议 (原生) | API | 无 | LSP 协议 |
| 语义分析 | 11 信号算法化嵌入 | 无 | 无 | 类型推断 |
| 155 语言 | 是 (tree-sitter) | 是 | 是 | 需逐语言实现 |
| 离线运行 | 是 | 否 (需服务端) | 是 | 是 |
| 影响分析 | 内置 (BFS+风险) | 无 | 无 | 部分支持 |
| 基础设施分析 | Docker/Terraform/K8s | 无 | 无 | 无 |
| 增量索引 | 是 | 是 | 是 | 实时 |
| 变更耦合 | 是 | 无 | 无 | 无 |
| 社区发现 | Louvain 算法 | 无 | 无 | 无 |

### 9.2 核心差异

1. **图数据模型**: 与 ctags/LSP 的扁平标签不同，使用属性图模型（节点+边+属性）
2. **算法化语义**: 不依赖外部 ML 模型，通过 11 种算法信号实现代码相似性
3. **AI 原生**: 通过 MCP 协议直接集成 AI 编程助手，而非面向人类搜索
4. **单二进制**: 无运行时依赖，零配置启动
5. **Cypher 查询**: 提供图查询语言，表达能力远超 ctags 的标签查询

### 9.3 优势

- **极致性能**: 纯 C + mimalloc + SQLite WAL + mmap
- **丰富语义**: 11 种语义信号，无需 GPU/ML 模型
- **广泛兼容**: 155 语言，10+ AI 工具
- **基础设施感知**: 不仅分析代码，还分析 Dockerfile、Terraform、K8s
- **变更耦合**: 独特的 git 历史分析能力

### 9.4 局限性

- **学习曲线**: Cypher 查询语言需要学习
- **语言深度**: tree-sitter 提取的语义深度不如完整的语义分析器 (如 Java 的 javac)
- **单机架构**: SQLite 单机存储，不支持分布式
- **只读查询**: Cypher 引擎不支持写操作 (CREATE/DELETE/MERGE 被 recognize 但不支持)
- **内存预算**: 默认占用 50% 物理内存，对资源受限环境可能过大

## 十、代码质量评估

### 10.1 代码组织

项目采用**严格的模块化**设计：
- 每个模块有独立的 `.h`/`.c` 文件对
- 头文件注释清晰说明模块职责和依赖关系
- 公共 API 与内部 API 分离（`pipeline.h` vs `pipeline_internal.h`）
- 命名一致：所有公共函数使用 `cbm_` 前缀

### 10.2 代码规范

- **消除魔术数字**: `constants.h` 为所有字面量定义命名常量
- **类型安全**: 使用 `typedef` 定义不透明句柄 (opaque handle)
- **NULL 安全**: 明确标注 NULL-safe 的 free 函数
- **错误处理**: 统一返回码 (`CBM_STORE_OK`, `CBM_STORE_ERR`, `CBM_STORE_NOT_FOUND`)

### 10.3 测试覆盖

从目录结构可见：
- `tests/` - 单元测试
- `test-infrastructure/` - 测试基础设施
- Store 层暴露了测试辅助函数 (`cbm_store_get_db`, `cbm_mcp_server_store`)
- 构建系统包含 valgrind 集成

### 10.4 文档质量

- README.md 530 行，覆盖功能、架构、性能、安装、工具、数据模型
- 每个头文件顶部有模块级注释
- API 函数有注释说明参数语义和所有权
- 内部头文件明确标注 "NOT a public header"

## 十一、项目活跃度与演进

### 11.1 版本信息

- **当前版本**: v0.6.1
- **许可证年份**: 2025
- **5 平台二进制分发**: macOS (arm64/amd64)、Linux (amd64/arm64)、Windows (amd64)
- **MCP 协议版本**: 2025-12-11 (最新 schema)

### 11.2 技术成熟度指标

- 65 个 C 源文件 + 45 个头文件 = **110 个源码文件**
- 22 个管线 pass = **丰富的分析能力**
- 14 个 MCP 工具 = **全面的查询接口**
- 11 种语义信号 = **先进的代码理解能力**
- Louvain 社区发现 = **图算法集成**
- Cypher 查询引擎 = **专业级图查询**
- 增量索引 = **生产就绪**

### 11.3 发展方向

从代码结构可以推断的未来方向：
- 更多管线 pass（webpack/vite 风格的路径别名）
- 更多基础设施扫描（GitHub Actions、GitLab CI）
- LSP 跨文件类型解析增强
- 向量搜索优化（当前是暴力扫描，可引入 ANN 索引）
- 分布式存储（可能迁移到 Client-Server 架构）

## 十二、总结

### 核心亮点

1. **工程水准极高**: 纯 C 语言、mimalloc、ASan/UBSan/TSan、SLSA Level 3 — 展现了系统编程的工业标准
2. **架构设计精良**: 多遍管线、并行执行、增量索引、自适应监控 — 兼顾性能与正确性
3. **语义分析创新**: 11 种无模型算法信号，在无需 GPU/ML 的条件下实现代码相似性检测
4. **AI 原生设计**: MCP 协议直接集成，为 AI 编程助手提供结构化知识而非原始文本
5. **一站式代码智能**: 从 AST 解析到基础设施扫描，从影响分析到变更耦合，覆盖代码理解的多个维度

### 风险提示

1. **单点依赖**: 项目由 DeusData 独立开发，社区规模和长期维护存在不确定性
2. **语言深度权衡**: tree-sitter 的语义深度不如完整的语言分析器
3. **内存需求**: 50% RAM 预算对 CI/CD 环境可能过高
4. **查询语言局限**: Cypher 子集不支持写操作，灵活性受限

### 适用场景推荐

- **大型代码库的 AI 辅助开发**: 充分利用知识图谱加速 AI 编程助手
- **代码审查和影响分析**: 利用 BFS + 风险等级进行变更评估
- **架构理解和文档**: 利用架构分析和 ADR 管理能力
- **DevOps 基础设施审计**: 利用 Docker/Terraform/K8s 分析能力
