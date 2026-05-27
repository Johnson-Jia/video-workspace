# 2026年5月第3周 GitHub 热门开源项目盘点

> 本周 GitHub 呈现鲜明的「AI Agent 生态爆发」特征——从技能框架、持久记忆、编码路由到内容营销、金融交易，AI 智能体相关项目占据半壁江山。数据来源：GitHub Weekly Trending 页面 + 每日 Trending 本地记录交叉验证。

## 本周趋势速览

| 趋势 | 说明 |
|------|------|
| 最大赢家 | [mattpocock/skills](https://github.com/mattpocock/skills) 本周涨星 18,795，远超第二名 |
| 新面孔 | 9router、AiToEarn、financial-services、react-doctor、academic-research-skills 等 9 个项目首次出现在本周榜单 |
| 持续热门 | openhuman（连续 3 天日榜）、RuView（连续 3 天）、supertonic（连续 3 天） |
| 核心主题 | AI Agent 相关项目占据 60% 以上，技能框架、记忆方案、编码路由等基础设施集中涌现 |
| 跨界融合 | 金融交易（AI-Trader）、内容营销（AiToEarn）、WiFi 感知（RuView）等传统领域被 AI 重构 |

---

## 一、AI Agent & 智能体生态

### 1. [mattpocock/skills](https://github.com/mattpocock/skills) — 本周涨幅冠军

**项目简介：** TypeScript 社区知名开发者 Matt Pocock 发布的编程代理技能集合。内容直接来自他个人的 `.claude` 配置目录，包含经过实战打磨的代理技能，旨在让 AI 编程助手具备真正的软件工程能力。

**核心亮点：**
- 技能体系完整覆盖开发全流程：需求分析 → 设计 → 实现 → 测试 → 代码审查
- 基于真实开发场景打磨，不是 Demo 级别的示例代码
- 支持 Claude Code、Codex CLI、Gemini CLI 等多种编程代理

**快速上手：**
```bash
# 通过 Claude Code 插件市场安装
/plugin install mattpocock/skills
```

**适合人群：** AI 编程工具用户、追求工程化开发流程的全栈工程师

> Star: 86,895 | Fork: 7,567 | 协议: MIT | 语言: Shell | 本周涨幅: +18,795

---

### 2. [superpowers](https://github.com/obra/superpowers) — 近 20 万 Star 的代理技能方法论

**项目简介：** 一个面向 AI 编程代理的完整软件开发方法论。不只是技能集合，更是一套经过验证的工作流——从需求澄清、规格设计、TDD 实现到子代理驱动开发，让 AI 代理像资深工程师一样工作。

**核心亮点：**
- 独创的「子代理驱动开发」模式，AI 可自主工作数小时不偏离计划
- 强调 TDD、YAGNI、DRY 原则，将工程最佳实践内化到代理行为中
- 社区活跃度极高，276 个 Open Issues 说明参与度和反馈量大

**快速上手：**
```bash
# Claude Code 安装
/plugin install superpowers
# 或通过技能市场
npx skills add obra/superpowers
```

**适合人群：** AI Agent 开发者、对 LLM 应用工程化落地感兴趣的团队

> Star: 194,056 | Fork: 17,263 | 协议: MIT | 语言: Shell | 日榜连续 3 天

---

### 3. [agentmemory](https://github.com/rohitg00/agentmemory) — AI 编程代理的持久记忆

**项目简介：** 专为 AI 编程代理设计的持久化记忆方案。在真实世界基准测试中排名第一，让 Claude Code、Cursor、Copilot 等工具能记住之前的工作上下文，实现跨会话连续工作。

**核心亮点：**
- 基于真实世界基准测试验证，记忆准确度和检索效率领先
- 支持多种 AI 编程代理：Claude Code、Cursor、Copilot、Cline 等
- 轻量级集成，npm 一行安装即可启用

**快速上手：**
```bash
npm install agentmemory
# 或作为 Claude Code 技能使用
```

**适合人群：** 频繁使用 AI 编程工具的开发者，大型项目的跨会话协作场景

> Star: 10,355 | Fork: 868 | 语言: TypeScript | 本周涨幅: +6,907

---

### 4. [9router](https://github.com/decolua/9router) — AI 编码路由与 Token 节省器

**项目简介：** 一个 AI 编码工具的统一路由网关。连接 Claude Code、Codex、Cursor、Cline 等 10+ 编程工具到 40+ AI 提供商，自动在订阅额度 → 低价 API → 免费模型之间切换，同时通过 RTK 技术节省 20-40% 的 Token 消耗。

**核心亮点：**
- 自动 fallback 机制：订阅用完自动切换到低成本方案，零中断编码
- RTK Token 压缩：自动压缩工具输出内容，大幅减少不必要的 Token 消耗
- 多账号轮询：同一提供商多个账号之间负载均衡

**快速上手：**
```bash
npm install -g 9router
# 或 Docker 一键部署
docker run -p 3000:3000 decolua/9router
```

**适合人群：** 多 AI 工具使用者、需要控制 API 成本的团队和个人开发者

> Star: 11,123 | Fork: 1,704 | 协议: MIT | 语言: JavaScript | 本周涨幅: +4,798

---

### 5. [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) — 学术研究全流程代理技能

**项目简介：** 为 AI 编程代理设计的学术研究全流程技能集合。覆盖从文献检索、论文撰写、同行评审到格式排版的完整学术出版流水线。特别值得注意的是，项目内置了引用幻觉检测机制，基于对 1.11 亿条引用的审计研究设计。

**核心亮点：**
- 覆盖 research → write → review → revise → finalize 完整学术出版流程
- 内置 7 模式阻断检查清单，防止 AI 生成虚假引用和编造结论
- 支持 APA 7.0 格式输出、DOCX/PDF 导出

**快速上手：**
```bash
/plugin marketplace add Imbad0202/academic-research-skills
/plugin install academic-research-skills
# 然后使用 /ars-plan 开始规划论文结构
```

**适合人群：** 学术研究者、研究生、需要辅助文献综述和论文撰写的科研人员

> Star: 8,114 | Fork: 910 | 协议: CC BY-NC 4.0 | 语言: Python | 本周涨幅: +2,769

---

### 6. [react-doctor](https://github.com/millionco/react-doctor) — AI 代理写的 React 代码质量检测

**项目简介：** 专为 AI 生成代码设计的 React 项目健康检查工具。一行命令扫描整个代码库，输出 0-100 的健康评分和可执行的诊断建议。自动检测状态管理、副作用、性能、架构、安全和无障碍等问题。

**核心亮点：**
- 自动识别 AI 代理常见的 React 编程反模式
- 支持 Next.js、Vite、React Native 三大框架
- 可安装为代理技能，让 AI 在写代码时就遵循最佳实践

**快速上手：**
```bash
npx -y react-doctor@latest .
# 评分 75+ 优秀，50-74 需改进，50 以下严重问题
# 也可安装为代理技能
npx -y react-doctor@latest install
```

**适合人群：** React 开发者、使用 AI 编程工具的前端工程师

> Star: 9,777 | Fork: 304 | 协议: MIT | 语言: TypeScript | 本周涨幅: +2,643

---

## 二、AI 应用 & 商业落地

### 7. [AiToEarn](https://github.com/yikart/AiToEarn) — 一人公司的 AI 内容营销智能体

**项目简介：** 面向 OPC（One-Person Company，一人公司）的 AI 内容营销自动化平台。通过 AI Agent 自动完成内容创作和多平台分发，支持抖音、小红书、快手、B 站、视频号、TikTok、YouTube 等 12+ 国内外平台的自动发布。

**核心亮点：**
- 全链路自动化：内容生成 → 多平台适配 → 一键发布 → 数据追踪
- 支持中文主流平台（抖音、小红书、快手等）的 API 对接
- 提供 Web 界面、MCP 集成、Docker 私有部署三种使用方式

**快速上手：**
```bash
# 方式 1：直接访问 aitoearn.ai 网站
# 方式 2：Docker 部署
docker run -p 3000:3000 yikart/aitoearn
# 方式 3：在 Claude/Cursor 中通过 MCP 协议使用
```

**适合人群：** 个人创作者、自媒体运营者、小型内容团队

> Star: 14,286 | Fork: 2,405 | 协议: MIT | 语言: TypeScript | 本周涨幅: +4,765

---

### 8. [UI-TARS-desktop](https://github.com/bytedance/UI-TARS-desktop) — 多模态 AI Agent 技术栈

**项目简介：** 一个开源的多模态 AI Agent 技术栈，包含 Agent TARS（通用多模态代理）和 UI-TARS Desktop（桌面端 GUI 代理）两个核心项目。通过视觉理解和 GUI 操作能力，让 AI 代理能像人类一样操作电脑和浏览器。

**核心亮点：**
- 双引擎架构：Agent TARS（CLI + Web UI）+ UI-TARS Desktop（桌面应用）
- 支持 MCP 工具集成，可连接各种外部服务和数据源
- 提供本地和远程两种运行模式，灵活适配不同场景

**适合人群：** AI Agent 开发者、GUI 自动化工程师、多模态 AI 研究者

> Star: 34,236 | Fork: 3,415 | 协议: Apache-2.0 | 语言: TypeScript | 本周涨幅: +3,105

---

### 9. [AI-Trader](https://github.com/HKUDS/AI-Trader) — 100% 自动化的 Agent 原生交易平台

**项目简介：** 香港大学数据科学实验室推出的 Agent 原生模拟交易平台。让 AI 代理像人类交易员一样在平台上交易、竞争和学习。任何 AI 代理只需发送一条消息即可加入平台，支持 OpenClaw、Claude Code、Codex 等主流代理。

**核心亮点：**
- AI 代理注册零门槛：只需让代理读取一个 SKILL.md 文件即可接入
- 支持模拟交易（Polymarket 实时数据 + 模拟执行），自动结算
- 提供 Dashboard 统一查看所有代理的交易洞察

**适合人群：** 量化交易研究者、AI Agent 开发者、金融科技爱好者

> Star: 17,567 | Fork: 2,698 | 语言: Python | 本周涨幅: +2,475

---

### 10. [financial-services](https://github.com/anthropics/financial-services) — 金融服务 AI 解决方案

**项目简介：** Anthropic 推出的面向金融服务行业的 AI 应用方案集。涵盖合规审查、风险评估、客户服务、文档处理等金融核心场景，提供可直接部署的 AI 工作流和最佳实践。

**核心亮点：**
- 3,290 个 Fork 说明社区在积极基于此项目构建金融应用
- 158 个 Open Issues 反映了金融场景的复杂性和持续迭代需求
- Apache-2.0 协议，适合企业级应用和商业化部署

**适合人群：** 金融科技从业者、银行/保险/证券行业技术团队、合规科技开发者

> Star: 23,830 | Fork: 3,290 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +6,935

---

## 三、前沿技术 & 创新应用

### 11. [RuView](https://github.com/ruvnet/RuView) — WiFi 信号变身空间传感器

**项目简介：** 将普通 WiFi 信号转化为实时空间智能的技术方案。不需要任何摄像头，仅通过分析 WiFi 信号的反射和衰减，就能实现人体姿态估计（类似 DensePose）、生命体征监测和存在检测。可部署在 ESP32 等低成本 MCU 上。

**核心亮点：**
- 零摄像头方案，完全通过 WiFi CSI（信道状态信息）实现空间感知
- 支持人体姿态估计、存在检测、生命体征监测三大能力
- 边缘部署友好，ESP32 等 MCU 即可运行，功耗极低

**应用场景：**
- 智能家居：老人跌倒检测、入侵检测（无隐私顾虑）
- 医疗健康：非接触式生命体征监测（呼吸、心率）
- 商业空间：客流统计、空间利用率分析

**适合人群：** IoT 开发者、智能家居方案商、空间计算研究者

> Star: 58,373 | Fork: 7,627 | 语言: Rust | 本周涨幅: +5,861

---

### 12. [CloakBrowser](https://github.com/CloakHQ/CloakBrowser) — 通过所有机器人检测的隐身浏览器

**项目简介：** 一个在源码级别修补浏览器指纹的隐身 Chromium。作为 Playwright 的直接替代品，30/30 项机器人检测测试全部通过。不是简单的参数伪装，而是从 Chromium 源码层面彻底消除了自动化痕迹。

**核心亮点：**
- 30/30 项机器人检测测试全部通过（Cloudflare、reCAPTCHA 等）
- Playwright 的直接替代品，现有代码无需修改即可迁移
- 源码级指纹修补：不是修改 navigator.webdriver 这种表面参数，而是彻底移除自动化特征

**快速上手：**
```bash
pip install cloakbrowser
# 替换 Playwright 的 browser launch 即可
```

**适合人群：** 数据采集工程师、自动化测试开发者、反爬虫研究人员

> Star: 12,673 | Fork: 978 | 语言: Python | 本周涨幅: +8,618

---

### 13. [supertonic](https://github.com/supertone-inc/supertonic) — 端上实时多语言语音合成

**项目简介：** 一个极速、完全本地运行的多语言文本转语音引擎。99M 参数的轻量级模型，通过 ONNX Runtime 实现 31 种语言的端上原生运行，无需云端，零隐私风险。输出 44.1kHz 高品质音频，支持笑声、呼吸等 10 种表情标签。

**核心亮点：**
- 31 种语言支持，含中日韩英法德等主流语种
- 端上实时合成，速度快到一秒内可将整页网页转为语音
- 支持 iOS、Android、Web（WebGPU）、Python、Rust、Java、C# 等 10+ 平台

**快速上手：**
```bash
pip install supertonic
# 或 npm install、cargo install
# 也提供 HuggingFace Spaces 在线 Demo
```

**适合人群：** 需要离线 TTS 的移动端开发者、嵌入式开发者、无障碍应用开发者

> Star: 6,920 | Fork: 711 | 协议: MIT | 语言: Swift | 日榜连续 3 天

---

## 四、开发工具 & 个人 AI

### 14. [openhuman](https://github.com/tinyhumansai/openhuman) — 本地 AI 个人超级智能

**项目简介：** 一个本地运行的个人 AI 超级智能系统。强调隐私优先，所有数据和计算都在本地完成。用 Rust 构建，性能出色，设计目标是理解你个人上下文的 AI 助手——不只是聊天，而是真正的「个人超级智能」。目前处于 Early Beta 阶段。

**核心亮点：**
- 全本地化运行，数据不上传云端，隐私安全有保障
- 基于 Rust 构建，性能出色，资源占用低
- 提供 DMG（macOS）和 EXE（Windows）安装包，开箱即用

**快速上手：**
```bash
# 下载安装包：https://tinyhumans.ai/openhuman
# 或查看文档：https://tinyhumans.gitbook.io/openhuman/
```

**适合人群：** 注重隐私的 AI 应用开发者、个人效率工具爱好者

> Star: 10,777 | Fork: 932 | 协议: GPL-3.0 | 语言: Rust | 日榜连续 3 天

---

### 15. [bun](https://github.com/oven-sh/bun) — 高性能 JavaScript 全合一运行时

**项目简介：** 集运行时、打包器、测试运行器和包管理器于一体的 JavaScript 工具链。用 Zig 和 Rust 编写，冷启动和热运行性能远超传统 Node.js 工具链。项目总 Star 已超 9 万，是本周持续热门的基础设施项目。

**核心亮点：**
- 四合一工具链：运行时 + 打包 + 测试 + 包管理
- 兼容 Node.js 生态，迁移成本极低
- 原生支持 TypeScript、JSX，无需额外配置

**快速上手：**
```bash
# 安装
curl -fsSL https://bun.sh/install | bash
# 创建项目
bun init my-app
# 运行
bun run dev
```

**适合人群：** 前端开发者、Node.js 用户、追求极致开发效率的工程师

> Star: 91,251 | Fork: 4,550 | 语言: Rust | 本周涨幅: +1,328

---

### 16. [supersplat](https://github.com/playcanvas/supersplat) — 3D 高斯溅射编辑器

**项目简介：** 基于 WebGL/WebGPU 的 3D 高斯溅射（Gaussian Splatting）编辑器。高斯溅射是近两年兴起的 3D 场景重建技术，相比传统 NeRF 速度更快、质量更高。这个编辑器提供了完整的可视化编辑能力。

**核心亮点：**
- 浏览器端运行，基于 WebGL/WebGPU，无需安装
- 支持高斯溅射数据的可视化和编辑操作
- PlayCanvas 引擎出品，技术成熟度高

**适合人群：** 3D 视觉研究者、AR/VR 开发者、计算机图形学爱好者

> Star: 8,169 | Fork: 882 | 协议: MIT | 语言: TypeScript | 本周涨幅: +2,108

---

## 本周总结

本周 GitHub Trending 呈现三大趋势：

1. **AI Agent 基础设施成型** — skills（技能）、agentmemory（记忆）、9router（路由）三大基础设施齐头并进，加上 react-doctor（质量检测）、academic-research-skills（科研流水线）等垂直技能，说明 AI Agent 的工具链正在从实验阶段走向工程化。一周内多个代理技能项目涨星破万，这在 GitHub 历史上是首次

2. **AI 向垂直领域渗透** — AiToEarn（内容营销）、AI-Trader（金融交易）、financial-services（金融服务）、UI-TARS（GUI 自动化）等项目的集中爆发，说明 AI 不再只是技术圈的玩具，正在快速渗透到商业、金融、内容创作等实体经济领域

3. **本地化和隐私成为共识** — openhuman（本地 AI 大脑）、supertonic（本地 TTS）、CloakBrowser（反检测浏览器）都强调「不依赖云端」或「数据不上传」。用户对隐私和性能的双重需求正在推动 AI 应用从云端回归端上

**本周最值得关注：** mattpocock/skills（AI 编程代理技能的标杆）和 RuView（WiFi 信号替代摄像头的空间感知创新）。

**数据说明：** 本文数据来自 GitHub Weekly Trending 页面和每日 Trending 本地记录交叉验证，排除了因 CDN 缓存导致的重复数据。周涨幅以 GitHub Weekly 页面数据为准，日榜信息作为持续性参考。
