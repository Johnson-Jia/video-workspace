# 2026年7月第29周 GitHub 热门开源项目盘点

> 本周（7月6日-13日）GitHub 被 AI agent 工具全面占领——从多 agent 并行编排、Claude 技能生态爆发，到 AI 自动渗透测试、agent 接管 Office 文件。agent 不再是单点工具，而成体系：编排、技能、安全、应用四层俱全。

## 本周趋势速览

| 趋势 | 说明 |
|------|------|
| 最大赢家 | iOfficeAI/OfficeCLI 周涨 +6,978 星（AI agent 操作 Office 文件） |
| 涨星王（总盘） | asgeirtj/system_prompts_leaks 周涨 +7,155（提示词泄露合集，涉版权本文不收） |
| 新面孔 | stablyai/orca、ogulcancelik/herdr、bradautomates/claude-video、TencentCloud/CubeSandbox 等 8 个首次上榜 |
| 持续热门 | JuliusBrussee/caveman（总星 88.5K，省词元 skill 持续火爆） |
| 主旋律 | AI agent 基础设施化——编排 + 技能 + 安全 + 应用四层齐备 |

## 项目详细解读

### 一、AI Agent 编排（让多个 agent 协同干活）

#### 1. [stablyai/orca](https://github.com/stablyai/orca)

**项目简介：** Orca 是一个面向"agent 编排"的桌面端开发环境（ADE），让你能用自己的订阅同时并行跑多个编程 agent。YC 孵化项目，桌面和移动端都能用。

**核心亮点：**
- 多 agent 并行：一个工作台同时跑若干编程 agent，worktree 隔离互不干扰
- 自带订阅：不用额外买企业版，连你自己的 Claude/Codex 订阅即可
- 跨端：桌面 + 移动端远程查看 agent 进度

**快速上手：** 官网下载桌面端，连接你的 coding agent 订阅即可起手。

**适合人群：** 同时跑多个 AI 编程任务、想榨干订阅价值的开发者

> Star: 16,960 | Fork: 1,330 | 协议: MIT | 语言: TypeScript | 本周涨幅: +4,481 | 创建: 2026-03

#### 2. [ogulcancelik/herdr](https://github.com/ogulcancelik/herdr)

**项目简介：** herdr 是一个住在终端里的 agent 多路复用器——可以理解成 tmux 之于 shell，herdr 之于 AI agent。一个窗口同时管多个 agent 会话。

**核心亮点：**
- 终端多路复用：单窗口切多个 agent，会话隔离
- 工作区管理：每个 agent 独立工作区，文件不串
- 轻量 Rust 实现，启动快、内存省

**快速上手：** `cargo install herdr` 或下载预编译二进制。

**适合人群：** 习惯终端工作流、同时开多个 agent 的开发者

> Star: 15,788 | Fork: 1,059 | 协议: NOASSERTION | 语言: Rust | 本周涨幅: +3,928 | 创建: 2026-03

#### 3. [openai/codex-plugin-cc](https://github.com/openai/codex-plugin-cc)

**项目简介：** 一个让 Claude Code 调用 Codex 的插件——在 Claude Code 里直接派任务给 Codex 审代码，两个 coding agent 互相校验。

**核心亮点：**
- 双 agent 互审：Claude 写，Codex 审，减少单 agent 盲区
- 委派任务：复杂子任务从 Claude Code 一键派给 Codex
- 轻量插件，装即用

**快速上手：** 在 Claude Code 里安装该插件，配置 Codex 凭证。

**适合人群：** 用 Claude Code 主力开发、想引入第二视角审代码的开发者

> Star: 28,056 | Fork: 1,836 | 协议: Apache-2.0 | 语言: JavaScript | 本周涨幅: +2,803 | 创建: 2026-03

### 二、Claude 技能生态（给 AI 装可复用技能）

#### 4. [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)

**项目简介：** 一个收录 345 个 Claude Code 技能与插件的合集——涵盖工程、营销、产品、合规、研究、日常效率等方向，适配 Claude Code、Codex、Gemini CLI、Cursor 等 12+ coding agent。

**核心亮点：**
- 数量全：345 个 skill + 30+ agent + 70+ 自定义命令
- 跨平台：不只 Claude Code，主流 coding agent 通用
- 分类清晰：按工程/营销/合规等分域，按需取用

**快速上手：** clone 仓库，把需要的 skill 目录复制到你的 agent 配置目录。

**适合人群：** 想快速给 coding agent 装上"职业技能"的所有用户

> Star: 22,376 | Fork: 3,120 | 协议: MIT | 语言: Python | 本周涨幅: +1,993 | 创建: 2025-10

#### 5. [bradautomates/claude-video](https://github.com/bradautomates/claude-video)

**项目简介：** 让 Claude 能"看"视频——一条 `/watch` 命令，自动下载视频、抽帧、转写文字，把视觉和文字内容都交给 Claude 分析。

**核心亮点：**
- 全流程一条命令：下载 + 抽帧 + 转写 + 喂给 Claude
- 多模态：Claude 既看画面帧又读字幕，理解更全
- 适合教程/会议/演示视频的内容提取

**快速上手：** 装好 skill 后在 Claude Code 里对任意视频链接发 `/watch`。

**适合人群：** 需要从视频里提炼知识、做摘要、做二创的内容工作者

> Star: 7,828 | Fork: 875 | 协议: MIT | 语言: Python | 本周涨幅: +4,353 | 创建: 2026-04

#### 6. [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)

**项目简介：** 一个让 Claude Code"用穴居人语气说话"的 skill——通过简化输出句式，砍掉冗长解释，实测能省 65% 的词元消耗。总星已到 88.5K，本周再涨近 4K。

**核心亮点：**
- 省 65% 词元：少废话、短输出，对话成本直接砍半
- 意外有效：穴居人语气反而逼迫模型给关键结论
- 轻量 skill，装即用，可随时关

**快速上手：** 把 caveman skill 装进 Claude Code，需要省词元时启用。

**适合人群：** 高频用 Claude Code、词元消耗大的开发者

> Star: 88,535 | Fork: 5,088 | 协议: MIT | 语言: JavaScript | 本周涨幅: +3,992 | 创建: 2026-04

#### 7. [tt-a1i/archify](https://github.com/tt-a1i/archify)

**项目简介：** 一个一句话生成架构图的 skill——用自然语言描述系统，自动出带深浅主题切换、支持 PNG/JPEG/WebP/SVG 导出的架构图，是 Mermaid 之外的轻量替代。

**核心亮点：**
- 自然语言出图：说一句"用户登录流程"，自动画
- 多格式导出：PNG/JPEG/WebP/SVG 全支持
- 深浅主题切换，适配不同文档场景

**快速上手：** 装好 skill，在 Claude Code 里描述你要画的架构。

**适合人群：** 写技术文档、做方案评审需要快速出架构图的开发者

> Star: 3,911 | Fork: 378 | 协议: MIT | 语言: JavaScript | 本周涨幅: +1,180 | 创建: 2026-04

### 三、AI 安全（让 agent 既敢用又不闯祸）

#### 8. [usestrix/strix](https://github.com/usestrix/strix)

**项目简介：** 开源的 AI 渗透测试工具——用 agent 自动找出你应用里的安全漏洞并给出修复建议，把过去要请安全团队做的活，部分自动化。

**核心亮点：**
- AI 自动找漏洞：扫描应用，定位常见 Web/接口漏洞
- 给修复建议：不只报问题，还给出改法
- 开源自部署，数据不外传

**快速上手：** 按仓库 README 部署，指向你的测试环境（请只在授权范围内使用）。

**适合人群：** 想做安全自检的中小团队、安全工程师

> Star: 40,854 | Fork: 4,313 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +4,143 | 创建: 2025-08

#### 9. [vxcontrol/pentagi](https://github.com/vxcontrol/pentagi)

**项目简介：** 一个能执行复杂渗透测试任务的全自动 AI agent 系统——多 agent 协作完成从信息收集到漏洞利用的全流程，自托管、可扩展。

**核心亮点：**
- 全自动多 agent：从侦察到利用，一条龙
- 自托管：测试数据留在内网
- 可扩展：支持自定义 agent 与工具链

**快速上手：** Docker 一键起，按文档配置目标（仅限授权测试）。

**适合人群：** 企业安全团队、专业渗透测试人员

> Star: 20,162 | Fork: 2,685 | 协议: MIT | 语言: Go | 本周涨幅: +1,989 | 创建: 2025-01

#### 10. [TencentCloud/CubeSandbox](https://github.com/TencentCloud/CubeSandbox)

**项目简介：** 给 AI agent 用的即时、并发、安全、轻量沙箱——让 agent 在隔离环境里执行代码，既不污染宿主机，也防恶意代码逃逸。

**核心亮点：**
- 即起即用：agent 要跑代码，秒级开沙箱
- 并发隔离：多个 agent 各跑各，互不干扰
- 轻量 Rust 实现，资源占用低

**快速上手：** 按仓库 README 接入你的 agent 框架。

**适合人群：** 做 coding agent 平台、需要安全执行环境的团队

> Star: 9,801 | Fork: 963 | 协议: NOASSERTION | 语言: Rust | 本周涨幅: +2,490 | 创建: 2026-04

### 四、Agent 应用（agent 接管真实办公场景）

#### 11. [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)

**项目简介：** 一个专为 AI agent 设计的 Office 套件——单文件、免装 Office，让 agent 直接读写自动化 Word/Excel/PowerPoint 文件。本周周涨近七千，是本周涨星王。

**核心亮点：**
- 单文件免装：一个二进制搞定，不依赖本机 Office
- 三件套通吃：Word/Excel/PPT 都能读写
- 命令行友好：agent 用 CLI 就能批量处理文档

**快速上手：** 下载单文件，按 README 的 CLI 命令操作文档。

**适合人群：** 要让 AI agent 批量处理办公文档、做报表自动化的开发者和办公族

> Star: 15,417 | Fork: 1,051 | 协议: Apache-2.0 | 语言: C# | 本周涨幅: +6,978 | 创建: 2026-03

#### 12. [alibaba/page-agent](https://github.com/alibaba/page-agent)

**项目简介：** 一个网页内的 GUI agent——用自然语言控制网页界面，"点这个按钮""填这个表单"，agent 自动定位并操作。

**核心亮点：**
- 自然语言操控：不用写选择器，说人话即可
- 网页内嵌：注入页面即可用，适配各类站点
- 适配 agent 编排，可接入 MCP

**快速上手：** 按仓库 README 把 agent 注入目标页面。

**适合人群：** 做网页自动化、RPA、想让 agent 操作 Web 界面的开发者

> Star: 26,218 | Fork: 2,414 | 协议: MIT | 语言: TypeScript | 本周涨幅: +2,666 | 创建: 2025-09

### 五、设计系统（agent 时代的设计语言）

#### 13. [facebook/astryx](https://github.com/facebook/astryx)

**项目简介：** 一个开源、可深度定制且"agent 就绪"的设计系统——把设计规范做成 agent 能直接理解和执行的格式，让 AI 生成的前端更"守规矩"。

**核心亮点：**
- agent 就绪：设计 token + 组件规范结构化，agent 可读
- 高度可定制：主题、组件都可改
- 开源，适配主流前端框架

**快速上手：** clone 仓库，按文档接入你的前端项目。

**适合人群：** 用 AI 生成前端、想让产出遵守统一设计规范的前端团队

> Star: 8,179 | Fork: 690 | 协议: MIT | 语言: TypeScript | 本周涨幅: +2,397 | 创建: 2026-01

## 本周总结

本周 GitHub 周榜几乎被 AI agent 工具"包场"——这不是某个单点项目的爆发，而是 agent 生态的成层化：**编排层**（orca/herdr 让多 agent 协同）、**技能层**（claude-skills/caveman 让 agent 武装到牙齿）、**安全层**（strix/CubeSandbox 让 agent 敢用又不闯祸）、**应用层**（OfficeCLI/page-agent 让 agent 接管真实办公）。

如果只关注两个，建议看 **iOfficeAI/OfficeCLI**（涨星王，AI 接管办公文档的刚需场景）和 **stablyai/orca**（多 agent 并行编排，代表 agent 从"单个助手"走向"agent 舰队"的方向）。

agent 不再只是聊天框里那个"助手"，它正在变成一套完整的基础设施。

---

**数据来源：** GitHub Trending Weekly 页面（2026-07-13 抓取），周涨幅以 Weekly 页面为准。项目真实性与活跃度经 gh API 交叉验证。文中项目链接均指向 GitHub 官方仓库。本文涉及的安全工具（strix/pentagi）仅介绍功能价值，实际使用请严格遵守授权范围与当地法律。
