# OpenHuman 项目深度分析报告

> 基于 2,200+ 源文件、71 个 Rust 域模块、2,074 次提交、78 位贡献者的全量分析
>
> 分析日期：2026-05-20

---

## 目录

- [一、开源项目使用场景](#一开源项目使用场景)
- [二、代码完善程度与优雅程度](#二代码完善程度与优雅程度)
- [三、不同人群的使用难易程度](#三不同人群的使用难易程度)
- [四、硬件要求与功能解锁矩阵](#四硬件要求与功能解锁矩阵)
- [五、完整部署操作手册](#五完整部署操作手册)

---

## 一、开源项目使用场景

OpenHuman 是一个**面向社区的 AI 助手**，定位为桌面端智能体平台（React + Tauri v2 + Rust 核心）。其核心价值是将多个 AI 能力与通信渠道统一集成到一个桌面应用中。

### 1.1 项目定位

| 属性 | 说明 |
|---|---|
| 产品名称 | OpenHuman |
| 产品类型 | AI 智能体桌面平台 |
| 技术栈 | React 19 + Tauri v2 + Rust (Axum/JSON-RPC) |
| 运行时 | Chromium Embedded Framework (CEF) |
| 开源协议 | GPL v3 |
| 当前版本 | 0.54.2 |
| 仓库地址 | github.com/tinyhumansai/openhuman |

### 1.2 核心场景矩阵

| 场景领域 | 具体功能 | 对应技术模块 |
|---|---|---|
| **多渠道消息聚合** | WhatsApp / Telegram / Discord / Slack / iMessage / Google Messages 统一收发 | `channels/` + 7 个 `*_scanner/` 模块 |
| **AI 智能对话** | 多智能体编排（18+ 内置 Agent：研究员、代码执行器、评论家、规划师、总结器、存档员、触发分类等） | `agent/` (100+ 文件), `threads/` |
| **知识管理** | 向量搜索 + 知识图谱 + 文档摄取管道 + 树状摘要 | `memory/` (120+ 文件) |
| **语音交互** | Whisper 语音听写 + Piper TTS 语音合成 | `voice/`, `dictation_hotkeys/` |
| **会议代理** | Google Meet 自动参与、音频捕获、虚拟摄像头（吉祥物形象） | `meet/`, `meet_agent/`, `meet_call/`, `fake_camera/` |
| **定时任务与自动化** | Cron 调度 + Webhook 触发 + 屏幕智能感知 | `cron/`, `webhooks/`, `screen_intelligence/` |
| **MCP 工具协议** | 兼容 Model Context Protocol，支持工具注册与调用 | `mcp_client/`, `mcp_server/`, `tool_registry/` |
| **团队协作** | 多成员管理、角色权限、邀请机制 | `team/`, `referral/` |
| **钱包与代币** | 加密货币钱包、代币经济（TokenJuice）、计费 | `wallet/`, `tokenjuice/`, `billing/` |

### 1.3 适用组织与人群

| 使用方 | 典型用途 |
|---|---|
| 开源社区 | 跨平台消息聚合 + AI 自动回复，社区运营自动化 |
| 客服团队 | 统一消息入口 + AI 辅助应答，降低人工成本 |
| 个人效率工具 | 知识管理 + 语音助手 + 会议助手，个人 AI 工作台 |
| AI 开发者 | MCP 协议集成、本地 LLM 接入、自定义 Agent，快速构建 AI 应用 |
| 技术团队 | 定时任务 + Webhook + 屏幕自动化，运维与监控场景 |
| 教育培训 | AI 辅导、知识库问答、学习路径规划 |

### 1.4 项目规模一览

| 指标 | 数值 |
|---|---|
| 总源文件 | ~2,200+ |
| Rust 文件 | 1,300（核心 1,241 + Tauri Shell 59） |
| TypeScript/TSX | 916（.ts 408 + .tsx 508） |
| 测试文件 | 336（含 53 E2E spec） |
| 文档文件 | 178 .md |
| 贡献者 | 78 人 |
| 提交数 | 2,074 次 |
| 依赖总数 | 275（Rust 144 + JS 131） |
| Rust 域模块 | 71 个 |
| CI/CD 工作流 | 21 个 |
| 支持语言 | 中 / 英 / 日 / 韩 / 德 |

---

## 二、代码完善程度与优雅程度

### 2.1 架构设计评分

#### 优势

| 维度 | 评分 | 说明 |
|---|---|---|
| **域分离** | ★★★★★ | 71 个域模块，每个遵循 `mod.rs` + `ops.rs` + `store.rs` + `schemas.rs` + `bus.rs` 标准结构 |
| **传输无关设计** | ★★★★★ | 控制器注册表（`ControllerSchema` / `RegisteredController`）同时服务 JSON-RPC 和 CLI，单一数据源，零重复 |
| **事件总线** | ★★★★★ | 类型化 `DomainEvent`（non-exhaustive enum）+ 广播发布/订阅 + 零序列化原生请求/响应（trait objects 直接传递） |
| **安全防护** | ★★★★☆ | Sentry 错误分层过滤（瞬态错误、会话过期、预算耗尽、最大迭代上限）、正则密钥脱敏、Docker 非 root 运行 |
| **设计系统** | ★★★★☆ | Tailwind 定制 token 体系：Ocean 主色 `#4A83DD`、语义色 sage/amber/coral、4 字体族（Inter / Cabinet Grotesk / JetBrains Mono / Newsreader）、暗色模式 |
| **测试基础设施** | ★★★★☆ | 共享 Mock API 服务器、多平台 E2E（WDIO + Appium/tauri-driver）、调试脚本套件（`pnpm debug`）、diff-cover 80% 覆盖率门禁 |
| **CI/CD** | ★★★★☆ | 21 个工作流文件，自定义 Docker CI image（`ghcr.io/tinyhumansai/openhuman_ci:rust-1.93.0`），CEF 缓存跨构建保留，三平台构建发布 |
| **国际化** | ★★★★☆ | i18n Provider + 5 语言 README（en / zh-CN / ja-JP / ko / de）+ 韩语 locale |
| **文档完备性** | ★★★★★ | `CLAUDE.md`（25KB）+ `AGENTS.md`（47KB）+ `CONTRIBUTING.md` + `CONTRIBUTING-BEGINNERS.md` + gitbooks 30+ 页 |

#### 待改进项

| 维度 | 说明 |
|---|---|
| **内存域复杂度** | `memory/` 单域 120+ 文件，包含树存储、语义搜索、知识图谱、摄取管道 — 建议拆分子域 |
| **Agent 域体量** | `agent/` 100+ 文件，18+ 内置 Agent — 功能丰富但维护成本较高 |
| **QuickJS 移除遗留** | 技能运行时已移除，`skills/` 变成纯元数据域，执行层正在重建 |
| **全局 allow(dead_code)** | crate 根级别 `#![allow(dead_code)]`，暗示部分代码处于预发布/预留状态 |
| **CEF 强绑定** | 必须使用 vendored tauri-cef CLI，标准 `@tauri-apps/cli` 不可用 — 构建链复杂度高 |
| **依赖面宽** | 275 个直接依赖（Rust 144 + JS 131），攻击面和维护负担较大 |

### 2.2 核心架构模式详解

#### 2.2.1 域模块标准结构

每个域模块遵循统一的文件布局：

```
src/openhuman/<domain>/
├── mod.rs          # 导出-focused，保持轻量
├── ops.rs          # 操作逻辑（核心业务）
├── store.rs        # 持久化层（SQLite / 文件系统）
├── types.rs        # 类型定义
├── schemas.rs      # RPC 控制器 schema + handler
├── bus.rs          # 事件总线订阅者
└── rpc.rs          # RPC 方法实现
```

**严格的模块布局规则**：新增功能必须放在 `src/openhuman/<domain>/` 子目录下，禁止在 `src/openhuman/` 根目录添加独立 `.rs` 文件（`dev_paths.rs` 和 `util.rs` 为历史遗留例外）。

#### 2.2.2 控制器注册表模式

```
Transport Layer (JSON-RPC / CLI)
         │
         ▼
┌─────────────────────────┐
│  Controller Registry    │  ← src/core/all.rs
│  (OnceLock<Vec<...>>)   │
│                         │
│  ┌─── memory.schemas    │
│  ├─── agent.schemas     │
│  ├─── threads.schemas   │
│  └─── ... (71 domains)  │
└─────────┬───────────────┘
          │
          ▼
  Domain schemas.rs
  ┌──────────────────┐
  │ ControllerSchema  │  → 输入/输出元数据
  │ handle_xxx()      │  → 委托到 domain/rpc.rs
  └──────────────────┘
```

**核心优势**：
- CLI 和 JSON-RPC 消费同一个注册表，不会出现行为不一致
- 新增域功能只需在域内定义 schema + handler，无需修改 `src/core/cli.rs` 或 `src/core/jsonrpc.rs`
- RPC 方法命名遵循 `openhuman.<namespace>_<function>` 统一约定

#### 2.2.3 事件总线架构

```
┌──────────────┐     publish_global()     ┌──────────────────┐
│  Domain A    │ ──────────────────────▶  │  EventBus        │
│  (publisher) │                          │  (broadcast)     │
└──────────────┘                          │                  │
                                          │  DomainEvent     │
┌──────────────┐     subscribe_global()   │  (non-exhaustive)│
│  Domain B    │ ◀──────────────────────  │                  │
│  (subscriber)│                          └──────────────────┘
└──────────────┘

┌──────────────┐     request_native()     ┌──────────────────┐
│  Caller      │ ──────────────────────▶  │  NativeRegistry  │
│              │                          │  (typed dispatch) │
│              │ ◀──────────────────────  │                  │
│              │     oneshot response      │  Zero serde!     │
└──────────────┘                          └──────────────────┘
```

**类型安全**：
- `DomainEvent` 为 `#[non_exhaustive]` 枚举，新增变体不破坏下游
- 原生请求/响应使用 Rust trait objects 和 channels 传递，零序列化开销
- 每个域拥有自己的 `bus.rs` 订阅者（如 `CronDeliverySubscriber`、`WebhookRequestSubscriber`）

#### 2.2.4 前端 Provider 链

```
Sentry.ErrorBoundary
  └── Redux Provider
        └── PersistGate (redux-persist, 含 RehydrationScreen)
              └── ThemeProvider
                    └── I18nProvider
                          └── BootCheckGate
                                └── CoreStateProvider (核心快照 + 认证)
                                      └── SocketProvider (Socket.io)
                                            └── ChatRuntimeProvider
                                                  └── HashRouter
                                                        └── CommandProvider
                                                              └── ServiceBlockingGate
                                                                    └── AppShell
                                                                          ├── AppRoutes
                                                                          ├── BottomTabBar
                                                                          ├── Walkthrough
                                                                          ├── Mascot
                                                                          └── Snackbars
```

**状态管理**：Redux Toolkit + 15+ slices（`accounts`, `chatRuntime`, `coreMode`, `thread` 等），通过 redux-persist 持久化，类型化 hooks（`useAppSelector` / `useAppDispatch`）。

**服务层**：单例模式（`apiClient`, `socketService`, `coreRpcClient`, `chatService`, `analytics` 等），使用 `started` flag 保证幂等启动。

#### 2.2.5 前端路由体系

| 路由 | 功能 |
|---|---|
| `/` | Welcome 页面 |
| `/onboarding/*` | 新用户引导 |
| `/home` | 主页 |
| `/human` | Human 页面 |
| `/intelligence` | 智能分析 |
| `/skills` | 技能管理 |
| `/chat` | 统一 Agent + 已连接 Web 应用（替代旧的 `/conversations` + `/accounts`） |
| `/channels` | 渠道管理 |
| `/invites` | 邀请管理 |
| `/notifications` | 通知中心 |
| `/rewards` | 奖励 |
| `/settings/*` | 设置 |

所有认证后路由包裹在 `ProtectedRoute` 中。无 `/login`、无 `/mnemonic`（恢复短语已移至 Settings）。

### 2.3 综合评分

```
┌─────────────────────┬────────┐
│ 架构设计             │  9.2/10│  域驱动 + 事件驱动 + 传输无关
│ 代码规范             │  8.8/10│  一致模块结构 + 命名约定
│ 错误处理             │  8.5/10│  RpcOutcome + anyhow + Sentry
│ 安全性               │  8.3/10│  Bearer + PID校验 + CEF零注入
│ 文档完备             │  9.0/10│  CLAUDE.md 25KB + AGENTS.md 47KB
│ 测试覆盖             │  8.0/10│  336测试 + 80%门禁 + 三平台E2E
│ 可维护性             │  7.8/10│  部分"神域"过大、依赖面宽
│ 国际化               │  8.0/10│  5语言 + i18n Provider
├─────────────────────┼────────┤
│ 总体评分             │  8.5/10│
└─────────────────────┴────────┘
```

---

## 三、不同人群的使用难易程度

### 3.1 用户画像难度矩阵

| 人群类型 | 使用难度 | 核心障碍 | 可用功能范围 |
|---|---|---|---|
| **程序员（Rust/TS）** | ★☆☆☆☆ 极低 | 需配置 CEF 构建链 | 全部功能 + 二次开发 + 自定义 Agent |
| **程序员（其他语言）** | ★★☆☆☆ 低 | Rust 工具链安装 | 全部功能 + MCP 工具开发 |
| **技术运维** | ★★☆☆☆ 低 | Docker Compose + 环境变量 | Docker 无头部署 + API 服务 |
| **产品经理** | ★★★☆☆ 中等 | 需理解 AI Agent 概念 | 桌面端开箱即用、渠道配置、Cron 设置 |
| **销售/市场** | ★★★☆☆ 中等 | 渠道授权流程较复杂 | 消息聚合、AI 辅助回复、客户管理 |
| **文职人员** | ★★★★☆ 较高 | AI 概念 + 技术配置 | 基础对话、知识管理（需他人部署） |
| **企业老板/高管** | ★★★☆☆ 中等 | 需 IT 团队部署 | 团队管理面板、数据报表、成本监控 |
| **非技术个人用户** | ★★★★☆ 较高 | 安装后仍需配置 API Key/渠道 | 下载安装包后基本可用 |

### 3.2 分人群详细分析

#### 程序员（Rust/TypeScript）

- **上手成本**：极低。有完整的 `CLAUDE.md`（25KB）+ `AGENTS.md`（47KB）+ `CONTRIBUTING.md` + `CONTRIBUTING-BEGINNERS.md`
- **架构理解**：71 个域模块结构一致，命名约定清晰（`openhuman.<namespace>_<function>`）
- **扩展能力**：MCP 协议支持自定义工具扩展，控制器注册表模式新增功能无需修改传输层
- **唯一障碍**：CEF 构建链首次编译耗时较长（~400MB Chromium 下载 + Rust 全量编译约 10-20 分钟）
- **推荐起点**：`CONTRIBUTING-BEGINNERS.md` → 选择感兴趣的域模块 → 阅读 `mod.rs` + `schemas.rs` → 编写测试

#### 程序员（其他语言）

- **上手成本**：低。主要需要安装 Rust 工具链
- **核心交互**：通过 JSON-RPC API 与核心交互，无需理解 Rust 内部实现
- **扩展方式**：通过 MCP 协议开发自定义工具（支持 Python / Node.js 运行时）
- **推荐起点**：Docker 部署 → 阅读 API 文档 → 通过 JSON-RPC 调用测试

#### 技术运维

- **上手成本**：低。Docker Compose 一键部署
- **核心配置**：50+ 环境变量，但大部分有默认值，仅需配置 `OPENHUMAN_CORE_TOKEN`
- **运维特性**：健康检查端点、进程恢复机制、日志系统、Sentry 错误追踪
- **安全加固**：只读文件系统 + 全能力丢弃 + no-new-privileges + 非 root 用户

#### 产品经理

- **上手成本**：中等。桌面端安装简单，但需理解 AI Agent、渠道连接等概念
- **可用功能**：渠道聚合查看、AI 对话、Cron 定时任务配置、团队管理
- **学习曲线**：有 Onboarding 引导（react-joyride），但有 20+ 个功能模块需要逐步探索

#### 销售/市场

- **上手成本**：中等。渠道授权（WhatsApp/Telegram/Slack）需要理解 OAuth 和平台 API
- **核心价值**：统一消息入口 + AI 辅助回复，显著提升客户响应效率
- **障碍**：首次渠道配置较复杂，建议由技术人员协助

#### 文职人员

- **上手成本**：较高。AI 概念（Agent、Prompt、Token）对非技术背景较陌生
- **可用功能**：基础对话、知识管理（前提是已由他人完成部署和配置）
- **建议**：需要 IT 支持，或使用预配置的企业版本

#### 企业老板/高管

- **上手成本**：中等。需要 IT 团队完成部署和配置
- **关注点**：团队管理面板、数据报表（`app/src/pages/` analytics 区域）、成本监控（`billing/`, `cost/`）
- **价值**：统一通信管理、AI 辅助决策、团队效率度量

#### 非技术个人用户

- **上手成本**：较高。下载安装包后可启动，但仍需：
  1. 注册账户 / 登录
  2. 配置 AI 后端（云端 API Key 或本地 Ollama）
  3. 可选：连接通信渠道
- **改进空间**：Onboarding 流程已覆盖基本引导，但 AI 配置步骤对非技术用户仍不直观

---

## 四、硬件要求与功能解锁矩阵

### 4.1 基础运行要求

| 项目 | 最低配置 | 推荐配置 |
|---|---|---|
| **CPU** | 2 核 | 4+ 核（含 AVX2 指令集） |
| **内存** | 4 GB | 16 GB |
| **磁盘** | 2 GB | 10 GB（含 workspace 数据） |
| **GPU** | 无要求 | 独立 GPU 8GB+ VRAM（本地 LLM） |
| **网络** | 宽带（云端 AI 必须） | 低延迟稳定连接 |
| **操作系统** | Win10+ / macOS 10.15+ / Ubuntu 22.04 | 同左 |

### 4.2 功能解锁矩阵

| 功能 | 最低硬件 | 推荐硬件 | 特殊要求 |
|---|---|---|---|
| **AI 对话（云端）** | 2C4G + 网络 | 4C8G + 稳定网络 | 需 API Key |
| **语音听写 (Whisper)** | 麦克风 + AVX2 CPU | Metal GPU (macOS) | 本地模型推理 |
| **文本转语音 (Piper)** | 扬声器 | 同左 | Piper 二进制 |
| **本地 LLM (Ollama)** | 8C16G + GPU 8GB VRAM | GPU 16GB+ VRAM | 可跑 7B-13B 模型 |
| **Google Meet 代理** | 麦克风 + 扬声器 | 同左 + 摄像头 | CEF 音频捕获 |
| **WhatsApp 集成** | 仅网络 | 同左 | WhatsApp 账号 |
| **Telegram 集成** | 仅网络 | 同左 | Telegram 账号 |
| **Discord 集成** | 仅网络 | 同左 | Discord 账号 |
| **Slack 集成** | 仅网络 | 同左 | Slack 工作区权限 |
| **iMessage 集成** | macOS 设备 | 同左 + Full Disk Access | **仅 Apple 生态** |
| **Google Messages** | 仅网络 | 同左 | Google 账号 |
| **屏幕捕获** | 显示器 | 多显示器 | 无 |
| **钱包/区块链** | 网络 | 同左 | 公链 RPC 访问 |
| **PDF RAG** | 网络 | 同左 | `rag-pdf` feature flag |
| **定时任务 (Cron)** | 无额外需求 | 同左 | 无 |
| **Webhook** | 网络 + 公网可达 | 同左 | 无 |
| **树莓派外设** | Raspberry Pi (ARM) | 同左 | **仅 Linux** + `peripheral-rpi` feature |

### 4.3 特殊硬件能力

| 能力 | 实现方式 | 硬件依赖 | 对应模块 |
|---|---|---|---|
| 虚拟摄像头 | SVG → YUV4MPEG2（纯 Rust, resvg 渲染） | 无 | `fake_camera/` |
| 键鼠自动化 | `rdev` + `enigo` + `arboard` | 无 | `text_input/` |
| 电池感知调度 | `starship-battery`（低电量限流 LLM） | 电池设备 | `scheduler_gate/` |
| 沙箱执行 | Linux Landlock / Bubblewrap | **仅 Linux** | feature flags |
| 音频捕获 | `cpal`（跨平台音频） | 麦克风 | `meet_audio/`, `voice/` |
| 屏幕捕获 | `screen_capture` | 显示器 | `screen_capture/`, `screen_intelligence/` |

### 4.4 平台差异

| 平台 | 安装格式 | 独占功能 | 特殊依赖 |
|---|---|---|---|
| **macOS** | `.app` + `.dmg` | iMessage、Metal 加速 Whisper、Full Disk Access | Xcode CLI tools, objc2 绑定 |
| **Windows** | `.exe` (NSIS) + `.msi` | 无 | MSVC Build Tools, CMake |
| **Linux** | `.deb` + `.AppImage` | Landlock 沙箱、树莓派外设 | libgtk-3-0, libwebkit2gtk-4.1-0, libx11-6 |

### 4.5 环境变量配置矩阵

共 **50+** 环境变量，按类别分布：

| 类别 | 变量数 | 关键变量 | 必填？ |
|---|---|---|---|
| 应用环境 | 2 | `OPENHUMAN_APP_ENV`, `OPENHUMAN_WORKSPACE` | 否（有默认值） |
| 后端 API | 3 | `BACKEND_URL`, `VITE_BACKEND_URL` | 否（默认 production） |
| 核心进程 | 7 | `OPENHUMAN_CORE_HOST`, `OPENHUMAN_CORE_PORT`, `OPENHUMAN_CORE_TOKEN` | Docker 部署需 `TOKEN` |
| 配置覆盖 | 6 | `OPENHUMAN_MODEL`, `OPENHUMAN_TEMPERATURE`, `OPENHUMAN_TOOL_TIMEOUT_SECS` | 否 |
| 运行时标志 | 3 | `OPENHUMAN_BROWSER_ALLOW_ALL`, `OPENHUMAN_LOG_PROMPTS` | 否 |
| 代理/网络 | 7 | `OPENHUMAN_PROXY_ENABLED`, `OPENHUMAN_HTTP_PROXY` 等 | 否 |
| 本地 AI | 5 | `OPENHUMAN_LOCAL_AI_TIER`, `OPENHUMAN_LM_STUDIO_BASE_URL` | 使用本地 AI 时 |
| 二进制覆盖 | 3 | `WHISPER_BIN`, `PIPER_BIN`, `OLLAMA_BIN` | 否（自动检测） |
| Sentry/监控 | 5 | `OPENHUMAN_CORE_SENTRY_DSN`, `VITE_SENTRY_DSN` | 否（留空禁用） |
| 测试 | 2 | `OPENHUMAN_SERVICE_MOCK` | 仅开发/测试 |

---

## 五、完整部署操作手册

### 5.1 方式一：桌面安装（推荐最终用户）

> 适合人群：所有用户
> 难度：★☆☆☆☆

#### 步骤

```bash
# 1. 从 GitHub Releases 下载对应平台安装包
#    macOS:  .dmg
#    Windows: .exe (NSIS) 或 .msi
#    Linux:  .deb 或 .AppImage

# 2. 安装（各平台标准流程）
#    macOS:   双击 .dmg → 拖入 Applications
#    Windows: 双击 .exe → 按向导安装
#    Linux:   sudo dpkg -i xxx.deb 或 chmod +x xxx.AppImage && ./xxx.AppImage

# 3. 首次启动
#    进入 Onboarding 引导：
#    a. 创建账户 / 登录
#    b. 配置 AI 后端（云端或本地 Ollama）
#    c. 连接通信渠道（可选）
#    d. 选择偏好设置

# 4. 开始使用
```

**注意事项**：
- 无需任何命令行操作或环境变量配置
- 自动更新通过 `tauri-plugin-updater` 实现
- 首次启动会创建 `~/.openhuman/` 工作目录

---

### 5.2 方式二：Docker 自托管（无头核心服务）

> 适合人群：技术运维、后端开发者
> 难度：★★☆☆☆

#### 步骤

```bash
# 1. 克隆仓库
git clone https://github.com/tinyhumansai/openhuman.git
cd openhuman

# 2. 配置环境变量
cp .env.example .env

# 3. 编辑 .env（必须项）
# OPENHUMAN_CORE_TOKEN=<生成一个安全的随机字符串>
#
# 可选项：
# OPENHUMAN_APP_ENV=staging
# BACKEND_URL=https://your-backend.example.com
# OPENHUMAN_CORE_PORT=7788

# 4. 启动服务
docker compose up -d

# 5. 验证健康状态
curl http://localhost:7788/health

# 6. 调用 JSON-RPC 端点
curl -X POST http://localhost:7788/rpc \
  -H "Authorization: Bearer <OPENHUMAN_CORE_TOKEN>" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"openhuman.health_check","id":1}'

# 7. 查看日志
docker compose logs -f
```

#### Docker 安全加固

| 安全措施 | 说明 |
|---|---|
| 只读文件系统 | `read_only: true` |
| 全能力丢弃 | `cap_drop: ALL` |
| 禁止提权 | `security_opt: no-new-privileges:true` |
| 非特权用户 | UID 10001 |
| 资源限制 | 4GB 内存 / 2 CPU 核心（可调） |
| 数据持久化 | 命名卷挂载 workspace |

---

### 5.3 方式三：从源码构建（开发者）

> 适合人群：Rust/TS 开发者、贡献者
> 难度：★★★☆☆

#### 5.3.1 前置条件

```bash
# Rust 1.93.0（rust-toolchain.toml 自动管理）
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Node.js >= 24.0.0（推荐 fnm 或 nvm）
fnm install 24
# 或
nvm install 24

# pnpm 10.10.0
npm install -g pnpm@10.10.0
```

#### 5.3.2 平台特定依赖

**macOS：**

```bash
xcode-select --install
```

**Ubuntu 22.04：**

```bash
sudo apt install -y \
  libgtk-3-dev \
  libwebkit2gtk-4.1-dev \
  libssl-dev \
  cmake \
  mold \
  clang \
  libclang-dev \
  libasound2-dev \
  libxdo-dev \
  libxtst-dev \
  libx11-dev \
  libevdev-dev
```

**Windows：**

```
1. 安装 Visual Studio Build Tools 2022
   - 勾选 "Desktop development with C++"
   - 勾选 "CMake tools for Windows"
2. 确保 MSVC 和 Windows SDK 已安装
```

#### 5.3.3 构建步骤

```bash
# 1. 克隆仓库（含子模块！）
git clone --recurse-submodules https://github.com/tinyhumansai/openhuman.git
cd openhuman

# 如果已克隆但忘记子模块：
git submodule update --init --recursive

# 2. 配置环境变量
cp .env.example .env
cp app/.env.example app/.env.local
# 按需编辑上述文件（开发环境通常不需要修改）

# 3. 安装前端依赖
pnpm install

# 4. 开发模式

## 仅前端（Vite dev server，无桌面壳）
pnpm dev

## 完整桌面应用（Tauri + CEF）
pnpm dev:app          # macOS / Linux
pnpm dev:app:win      # Windows

# 5. 生产构建
pnpm build            # UI 构建
# 桌面安装包构建（自动使用 vendored tauri-cef CLI）
pnpm tauri build
```

#### 5.3.4 验证

```bash
# TypeScript 类型检查
pnpm typecheck

# ESLint
pnpm lint

# 代码格式化
pnpm format

# 格式检查
pnpm format:check

# Rust 检查
cargo check --manifest-path Cargo.toml              # 核心
cargo check --manifest-path app/src-tauri/Cargo.toml # Tauri Shell

# 前端单元测试
pnpm test
pnpm test:coverage    # 含覆盖率

# Rust 单元测试
pnpm test:rust

# E2E 测试
pnpm test:e2e:build
bash app/scripts/e2e-run-spec.sh test/e2e/specs/smoke.spec.ts smoke
```

#### 5.3.5 调试运行器（推荐迭代时使用）

```bash
pnpm debug unit                                     # 全部前端单元测试
pnpm debug unit src/components/Foo.test.tsx         # 单文件
pnpm debug unit -t "renders empty state"            # 按名称过滤
pnpm debug unit Foo -t "renders empty" --verbose    # 详细输出

pnpm debug rust                                     # Rust 测试
pnpm debug rust json_rpc_e2e                        # 指定测试

pnpm debug e2e test/e2e/specs/smoke.spec.ts         # E2E 单 spec
pnpm debug e2e test/e2e/specs/cron-jobs-flow.spec.ts cron-jobs --verbose

pnpm debug logs                  # 列出最近 50 条日志
pnpm debug logs last             # 打印最近日志（最后 400 行）
pnpm debug logs unit             # 最近的前端单元测试日志
pnpm debug logs last --tail 100  # 指定行数
```

---

### 5.4 方式四：独立核心 CLI（无 GUI 调试）

> 适合人群：Rust 开发者、调试人员
> 难度：★★☆☆☆

```bash
# 1. 仅构建核心二进制
cargo build --bin openhuman-core

# 2. 启动服务
./target/debug/openhuman-core serve

# 3. 读取认证 Token
cat ~/.openhuman/core.token
# OPENHUMAN_APP_ENV=staging 时为 ~/.openhuman-staging/core.token

# 4. 调用 RPC
curl -X POST http://127.0.0.1:7788/rpc \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"openhuman.health_check","id":1}'

# 5. 附加到已有进程（从桌面应用调试核心）
OPENHUMAN_CORE_REUSE_EXISTING=1 pnpm dev:app
```

---

### 5.5 构建问题排查

| 问题 | 原因 | 解决方案 |
|---|---|---|
| CEF 下载失败 | ~400MB Chromium 二进制，网络问题 | 检查代理设置，CEF 缓存在 `target/` 下 |
| `tauri-cli` panic | 使用了标准 `@tauri-apps/cli` | 运行 `scripts/ensure-tauri-cli.sh` 安装 vendored CLI |
| Node.js 版本不匹配 | 必须 >= 24.0.0 | `node -v` 检查，用 fnm/nvm 切换 |
| pnpm 版本不匹配 | 必须 10.10.0 | `npm install -g pnpm@10.10.0` 或 `corepack enable` |
| Windows MSVC 缺失 | 编译 Rust 需要 C++ 工具链 | 安装 Visual Studio Build Tools，勾选 C++ 工作负载 |
| Linux GTK 缺失 | Tauri 需要 GTK 和 WebKit | `sudo apt install libgtk-3-dev libwebkit2gtk-4.1-dev` |
| 预提交钩子失败（无关代码） | `main` 上有预存在的 breakage | `git push --no-verify`，在 PR 中说明 |
| Rust 编译缓慢 | 首次全量编译 | 约 10-20 分钟，后续增量 1-3 分钟 |
| 子模块缺失 | 克隆时未加 `--recurse-submodules` | `git submodule update --init --recursive` |
| Whisper 编译失败 | Windows CRT 冲突 | 项目使用自定义 whisper-rs fork 修复此问题 |

---

### 5.6 CI/CD 管道概览

项目配置了 **21 个 GitHub Actions 工作流**：

| 工作流 | 触发条件 | 作用 |
|---|---|---|
| `build.yml` | push/PR to main | Tauri + CEF 构建验证 |
| `test.yml` | push/PR | Rust 单元测试 + Vitest 前端测试 |
| `coverage.yml` | PR | diff-cover 门禁，≥80% 变更行覆盖率 |
| `e2e.yml` | 手动/PR | WDIO 桌面端到端测试（三平台） |
| `release-staging.yml` | 手动 | 打 staging tag，构建三平台安装包 |
| `release-production.yml` | 手动 | staging → production 发布 |
| `docker-ci-image.yml` | Dockerfile 变更 | 构建 CI Docker image 推送到 GHCR |
| `typecheck.yml` | push/PR | TypeScript 类型检查 |
| `pr-quality.yml` | PR | 代码质量检查 |
| `weekly-code-review.yml` | 定时 | 每周代码审查 |

**CI 特性**：
- 自定义 Docker image：`ghcr.io/tinyhumansai/openhuman_ci:rust-1.93.0`
- CEF 二进制缓存（~400MB）跨构建保留
- Rust 编译缓存（Swatinem/rust-cache）
- pnpm store 缓存
- CI 构建使用优化 profile（`opt-level=1`, `codegen-units=16`, 无 LTO）

---

## 附录

### A. Rust 域模块完整列表（71 个）

| 域 | 功能 |
|---|---|
| `about_app` | 应用信息与能力目录 |
| `accessibility` | 无障碍支持 |
| `agent` | 多智能体编排（18+ Agent） |
| `app_state` | 应用状态管理 |
| `approval` | 审批流程 |
| `audio_toolkit` | 音频工具集 |
| `autocomplete` | 自动补全 |
| `billing` | 计费管理 |
| `channels` | 多渠道通信 |
| `composio` | Composio 集成 |
| `config` | 配置管理 |
| `connectivity` | 网络连通性检测 |
| `context` | 上下文管理 |
| `cost` | 成本追踪 |
| `credentials` | 凭据管理 |
| `cron` | 定时任务调度 |
| `desktop_companion` | 桌面伴侣 |
| `doctor` | 诊断工具 |
| `embeddings` | 向量嵌入 |
| `encryption` | 加密服务 |
| `health` | 健康检查 |
| `heartbeat` | 心跳监测 |
| `http_host` | HTTP 服务托管 |
| `inference` | LLM 推理抽象层 |
| `integrations` | 第三方集成 |
| `javascript` | JavaScript 运行时 |
| `learning` | 学习功能 |
| `mcp_client` | MCP 客户端 |
| `mcp_server` | MCP 服务端 |
| `meet` | Google Meet 集成 |
| `meet_agent` | 会议智能体 |
| `memory` | 知识管理与向量搜索 |
| `migration` | 数据迁移 |
| `notifications` | 通知系统 |
| `overlay` | 叠加层 |
| `people` | 人员管理 |
| `prompt_injection` | 提示注入防护 |
| `provider_surfaces` | 提供者界面 |
| `redirect_links` | 重定向链接 |
| `referral` | 推荐系统 |
| `routing` | 路由管理 |
| `runtime_node` | Node.js 运行时 |
| `runtime_python` | Python 运行时 |
| `scheduler_gate` | 调度门控（电池感知） |
| `screen_intelligence` | 屏幕智能感知 |
| `security` | 安全服务 |
| `service` | 服务管理 |
| `skills` | 技能元数据（运行时已移除） |
| `socket` | WebSocket 通信 |
| `subconscious` | 后台潜意识处理 |
| `team` | 团队管理 |
| `text_input` | 文本输入处理 |
| `threads` | 对话线程管理 |
| `todos` | 待办事项 |
| `tokenjuice` | 代币经济 |
| `tool_registry` | 工具注册表 |
| `tool_timeout` | 工具超时管理 |
| `tree_summarizer` | 树状摘要 |
| `update` | 应用更新 |
| `voice` | 语音服务 |
| `wallet` | 加密钱包 |
| `webhooks` | Webhook 管理 |
| `webview_accounts` | 内嵌 WebView 账户管理 |
| `webview_apis` | WebView API 桥接 |

### B. Feature Flags

| Feature | 用途 |
|---|---|
| `whatsapp-web` | WhatsApp Web 集成 |
| `channel-matrix` | Matrix 协议支持 |
| `browser-native` | 原生浏览器自动化 |
| `rag-pdf` | PDF 提取用于 RAG |
| `sandbox-landlock` | Linux Landlock 沙箱 |
| `sandbox-bubblewrap` | Bubblewrap 沙箱 |
| `peripheral-rpi` | 树莓派外设支持 |
| `e2e-test-support` | 测试专用（暴露 `test_reset` RPC） |

### C. 构建工具链版本锁定

| 工具 | 版本 | 锁定方式 |
|---|---|---|
| Rust | 1.93.0 | `rust-toolchain.toml` |
| Node.js | >= 24.0.0 | `app/package.json` engines |
| pnpm | 10.10.0 | 根 `package.json` packageManager |
| tauri-cli | vendored CEF fork | `scripts/ensure-tauri-cli.sh` |

---

> **报告结论**：OpenHuman 是一个架构精良、功能丰富的 AI 桌面助手平台。代码在架构设计（域驱动、事件驱动、传输无关）和文档完备性上表现优异（综合 8.5/10），适合有技术背景的团队或个人深度使用。项目尚未发布 1.0 版本（当前 0.54.2），API 和功能仍有演进空间。对非技术用户而言，桌面安装版可开箱即用，但高级功能（本地 LLM、渠道集成、会议代理）仍需一定技术理解。
