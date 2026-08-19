# 8月18日 GitHub 热门项目（daily 综合榜 · 本地优先专题）

> 数据源：raw_trending.json（github_trending.py 新闻页 11 项 + 语言日榜扩池 1 项，2026-08-18 采集）+ gh api repos 实时核验。
> 叙事主线：**本地优先（local-first）**——不用账号、不上云、自己的数据自己的机器自己管。五个项目覆盖照片管理、外设设置、下载工具、模型适配、安全自查，方向零重叠。

## 入选项目（5 个，AI 2/5 上限内，非 AI 3 个）

### 1. immich — 把照片从云相册搬回自己家
- GitHub: immich-app/immich | TypeScript | 11.1万★ (+175 单日)
- 原始描述：High performance self-hosted photo and video management solution.
- 中文：高性能自托管的照片和视频管理方案——自己一台机器，替代云相册，手机 App 自动备份，照片永远在自己手里
- 钩子：云相册要会员、要压缩、要看广告，11 万人选择把照片搬回自己家
- 受众：B 半可用（需一台常开设备部署，手机端装好即用）

### 2. OpenLogi — 罗技外设设置，不用登录账号
- GitHub: AprilNEA/OpenLogi | Rust | 8.6K★ (+115 单日)
- 原始描述：⚡️A native, local-first alternative to Logitech Options+, written in Rust 🦀 — remap buttons, DPI, and SmartShift over HID++. No account, no telemetry.
- 中文：本地优先的罗技 Options+ 替代品，Rust 编写——改键、调 DPI、SmartShift 滚轮全支持，免账号、零遥测
- 钩子：调个鼠标按键凭什么要注册账号、常驻后台？这个 3 个月的新项目用原生应用把这事变简单了
- 受众：A 普通可用（下载即用，罗技 MX Master 用户直击痛点）

### 3. Motrix — 装了就用的全能下载器
- GitHub: agalwood/Motrix | TypeScript | 5.3万★ (+344 单日)
- 原始描述：A full-featured download manager.
- 中文：全功能的下载管理器——界面干净，HTTP/BT/磁力全支持，全平台桌面端
- 钩子：7 年常青，5.3 万人收藏的老牌工具，今天还在单日涨 344 星（合规提醒：只讲工具本身的工程能力，不引导下载版权内容）
- 受众：A 普通可用

### 4. llmfit — 下载模型之前，先测你的机器跑得动什么
- GitHub: AlexsJones/llmfit | Rust | 3.2万★ (+198 单日)
- 原始描述：Hundreds of models &amp; providers. One command to find what runs on your hardware.
- 中文：几百个模型和提供商，一条命令找出你的硬件能跑什么——本地跑模型前的第一步
- 钩子：别再下了 20G 模型才发现显卡带不动，一条命令直接告诉你答案（收藏向实用信息）
- 受众：B 半可用（命令行工具，想本地跑模型的人群）

### 5. strix — AI 帮你查自己应用的漏洞
- GitHub: usestrix/strix | Python | 5.4万★ (+598 单日)
- 原始描述：Open-source AI penetration testing tool to find and fix your app’s vulnerabilities.
- 中文：开源 AI 安全测试工具，帮你找出并修复自己应用的漏洞（中性化表述：开发者自查角度，讲"给自己应用做体检"，不渲染攻击话术）
- 钩子：上线前不知道自己的应用哪里有洞？让 AI 先替你把体检做一遍
- 受众：C 开发者向

## 落选说明（泛化，不录全名）

- 一个 AI 短视频生成工具今日登顶（+1189）：昨日刚讲过，按近 2 天不重复规则跳过
- 一个前端元框架（+957）：昨日刚讲过，跳过
- 一个免费 API 清单、一个命令行下载内核、一个时序预测模型：均为昨日已讲项目，跳过
- 一个 Rust 原生交易引擎：topics 带 AI 标签按口径计入 AI 名额，为守住 AI ≤2 让位
- 一个开源视频剪辑器：3 天前刚做过主角，观众视角重复，主动避开
- 其余 AI 工具类（agent 记忆、求职自动化、推理服务器、网安技能库）：AI 名额已满 2，留待 ai-wind 专项

## 数字锚点

| 项目 | 锚点 |
|------|------|
| immich | 11.1万★ +175 |
| OpenLogi | 8.6K★ +115（3 个月新项目） |
| Motrix | 5.3万★ +344 |
| llmfit | 3.2万★ +198 |
| strix | 5.4万★ +598 |
