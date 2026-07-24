# GitHub Trending 内容分析 — 2026-07-24

## 数据
- 采集 15 项目（gh 15/15 验证，代理），活跃 13/15（87%），与 07-23 重叠 9 + 新 6
- 对齐诊断 P0：trending 快报

## 选题（6 个，跨 6 圈 + A 档 4/6 + 全新项目最大化 freshness）

| # | 项目 | 涨幅 | 受众 | 方向 | 处理 |
|---|------|------|------|------|------|
| 1 | block/buzz | +2460 | A | 人+AI 协作工作空间 | 新展开（涨幅王·Block 出品·gh 已核实） |
| 2 | Automattic/harper | +590 | A | 离线语法检查器 | 新展开，跨圈写作工具 |
| 3 | Pumpkin-MC/Pumpkin | +563 | A | Rust Minecraft 服务器 | 新展开，跨圈游戏 |
| 4 | likec4/likec4 | +475 | B | 实时架构图 | 新展开，跨圈开发者 |
| 5 | earthtojake/text-to-cad | +293 | B | 文字转 CAD | 新展开，跨圈设计 |
| 6 | jellyfin/jellyfin | +66 | A | 免费媒体系统 | 新展开，跨圈影音 |

**配比**：A 档 4（buzz/harper/Pumpkin/jellyfin）+ B 档 2（likec4/text-to-cad）；跨 6 圈（协作/写作/游戏/架构图/3D设计/影音）；AI 类 2（buzz 人机协作 / text-to-cad agent 技能）控制。

## 避重复（连续上榜老项目，今日主动避开以拉高 freshness）
- worldmonitor (+3196)：07-22 展开 + 07-23 一带过，连续 3 天已充分曝光
- OmniRoute (+1925)：07-23 展开
- Apollo-11 (+599)：07-22 展开

> 注：今日涨幅王实际是 worldmonitor (+3196)，但因其连续 3 天已报，本期换新涨幅王 block/buzz (+2460) 作主推，避免观众疲劳 + template_sim 拉低 freshness

## 排除
- 一个 WiFi 信号感知项目（历史核实不可实现，永久排除·不入选；今日涨幅 +1726 仍排除）
- 两个 last push >30 天的项目（金融基础模型 Kronos / claude-skills 清单，active=false，不入选）

## 真实性核实
- **block/buzz**：gh API 已核实 README——Block 公司（原 Square）出品的自托管人+AI agent 共享工作空间，基于 Nostr relay，功能详尽（开 repo/发 patch/审代码/跑工作流/语音 huddle）。非杜撰，可信
- 其余 5 项描述清晰、gh 15/15 验证 active

## 合规
- **buzz**：README 自嘲「又是一个 AI 邻接工具」，旁白聚焦「人与 AI 在同一房间协作」概念，泛化不堆砌品牌；Nostr 是去中心化协议名（中性技术术语）可提
- **harper**：Automattic 用「开源公司 Automattic（WordPress 背后团队）」背景描述，非竞品攻击
- **Pumpkin**：Minecraft 为游戏产品名（用途描述，gate 允许产品名；非字节系 app 名）
- 无 app 名（剪映/CapCut 等）、无违禁词、无搜索引导
