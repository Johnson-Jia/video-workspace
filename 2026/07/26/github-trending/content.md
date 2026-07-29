# 内容摘要

## 来源
分类数据：raw_trending.json（GitHub Trending daily，2026-07-26，18 个项目，16/18 活跃）

## 核心主题
今天不聊连续霸榜的 AI Agent。榜上一个蓝牙 mesh 离线聊天工具单日冲上近两千星——断网、无 SIM 卡、无 WiFi 也能群聊。围绕「不依赖云端和运营商、自己掌控」的主轴，串联去中心化通信、离线隐私工具、本地创作软件、大厂开发者基建、游戏自托管五个方向。

## 关键信息点
- **permissionlesstech/bitchat**（核心反直觉）：蓝牙 mesh + Nostr 双传输去中心化聊天，无账号、无手机号、无中心服务器，iOS/macOS 原生 app，断网多跳中继，端到端加密，IRC 风格命令。场景：抗议、灾难、偏远地区离线通信。今日 +1720 星。
- **palmier-io/palmier-pro**：为 AI 而生的 macOS 视频编辑器，苹果电脑原生桌面 app，本地创作。今日 +412 星，新上榜。
- **Automattic/harper**：离线、隐私优先的语法检查器，Rust 驱动，文字不上传云端。浏览器扩展 + 桌面。WordPress 母公司维护，多贡献者。今日 +503 星。
- **alibaba/open-code-review**：阿里开源的混合架构代码审查工具，确定性流水线 + AI agent 双引擎，精确到行级评论，内置精调规则集（空指针、线程安全、XSS、SQL 注入）。今日 +431 星，新上榜。
- **block/buzz**（一带而过）：蜂群思维通信平台，人和 AI 在同一个工作区协作，底层 Nostr 自托管 relay。今日 +2491 星（榜首），与 bitchat 同用 Nostr 协议。24 期「AI 队友」角度已展开，本期只提增量 + 协议协同。
- **Pumpkin-MC/Pumpkin**（一带而过）：Rust 重写的 Minecraft 服务器，更快更省资源，Docker 一键自托管。今日 +358 星。24 期已展开，本期一带而过。

## 数据（gh api 核实，2026-07-26）
| 项目 | 语言 | 总星 | 今日 | forks | watchers | 受众 |
|------|------|------|------|-------|----------|------|
| permissionlesstech/bitchat | Swift | 28.8K | +1720 | 4319 | 275 | A |
| block/buzz | Rust | 12.0K | +2491 | 964 | 65 | B |
| Automattic/harper | Rust | 13.4K | +503 | 512 | 32 | A |
| palmier-io/palmier-pro | Swift | 12.2K | +412 | 895 | 37 | A |
| alibaba/open-code-review | Go | 13.0K | +431 | 888 | 50 | B/C |
| Pumpkin-MC/Pumpkin | Rust | 9.7K | +358 | 657 | 60 | A |

## 真实性核实（gh api，0 HARD）
- bitchat：owner 账号 2025-07 创建（>30 天），1659 followers，多人贡献（jackjackbits 617 / nothankyou1 128 / qalandarov 97），star/fork=6.65:1，watcher 比例 0.95%，仓库 114MB，App Store 上架 ✅
- palmier-pro：owner 2024-06，131 followers，htin1 主导 + 多人，star/fork=13.7:1 ⚠️ 1 警告（watcher 0.3%）0 HARD ✅
- open-code-review：阿里官方（2012，20453 followers，540 repos），star/fork=14.7:1，多贡献者 ✅
- harper：Automattic（WordPress 母公司，2011），elijah-potter 2205 + hippietrail 1184 多贡献者 ✅
- buzz：block（Square/CashApp 母公司，2024-10），1701 followers，wesbillman 545 + 多人，404MB 仓库 ✅
- Pumpkin：Pumpkin-MC org，Snowiiii 1026 + 多贡献者，star/fork=14.8:1 ✅

## 原始素材路径
- raw_trending.json（18 项目，本日 gh api + python requests 抓取，cache_warning=false，10 overlapping + 8 new）
- assets/avatars/（owner avatar 已预下载）

## 选题合规
- 永久排除：ruvnet/RuView（未上榜，无影响）
- 不活跃过滤：shiyu-coder/Kronos（pushed 2026-04-13）、Lordog/dive-llms（pushed 2025-10-10）active=false 不入选
- avoid_recent 遵守：citrolabs/ego-lite(25)、mattpocock/skills(25)、CoreBunch/Instatic(25)、OtterMind/Chat2DB(25)、andrewyng/aisuite（主题撞 23 期）均不入选；block/buzz、Automattic/harper、Pumpkin-MC/Pumpkin 为 24 期已展开项目，本期按连续霸榜规则一带而过（3-4s 增量）
- 受众配比：A 档 4（bitchat/palmier-pro/harper/Pumpkin）/ B 档 2（buzz/open-code-review）—— A 档占 4/6 超半 ✓，无 C 档开发者库扎堆 ✓
- 跨领域：去中心化通信 / 本地创作 / 离线隐私 / 开发者基建 / 游戏自托管，5 个方向 ✓
