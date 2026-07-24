# GitHub Trending 内容分析 — 2026-07-23

## 数据
- 采集 19 项目（gh 19/19 验证，代理），活跃 17/19（89%），与 07-22 重叠 11 + 新 8
- 对齐诊断 P0：trending 快报

## 选题（6 个，跨 6 圈 + A 档 3/6 + 避近 9 期重复）

| # | 项目 | 涨幅 | 受众 | 方向 | 处理 |
|---|------|------|------|------|------|
| 1 | koala73/worldmonitor | +4131 | A | 全球情报仪表板 | **一带而过**（昨日展开过，今日涨幅翻四倍再报热度）|
| 2 | diegosouzapw/OmniRoute | +1648 | A | AI 统一网关 | 新展开，跨圈 AI 网关 |
| 3 | DioxusLabs/dioxus | +411 | B | Rust 全栈框架 | 新展开，跨圈框架 |
| 4 | dottxt-ai/outlines | +362 | C | LLM 结构化输出 | 新展开，跨圈 AI 工具（标开发者向）|
| 5 | hyprwm/Hyprland | +353 | B | Wayland 桌面 | 新展开，跨圈桌面 |
| 6 | dreamhunter2333/cloudflare_temp_email | +60 | A | Cloudflare 临时邮箱 | 新展开，跨圈实用工具 |

**配比**：A 档 3（worldmonitor/OmniRoute/cloudflare）+ B 档 2（dioxus/Hyprland）+ C 1（outlines 标开发者向）；跨 6 圈（情报/AI网关/框架/AI工具/桌面/邮箱）；AI 类 2（OmniRoute/outlines）控制。

## 避重复（近 9 期已展开，今日跳过）
- i-have-adhd (+1682)、schollz-croc (+737)、Apollo-11 (+766)：07-22 刚做过
- openship (+1304)、voicebox (+565)：07-21 做过
- ai-engineering-from-scratch (+688)：07-19 做过
- code-review-graph (+872)：07-18/19/21/22 多次做过
- worldmonitor 昨日展开，今日涨幅暴涨（1167→4131），仅一带而过报热度，不重复展开

## 排除
- 一个 WiFi 信号感知项目（历史核实不可实现，永久排除·不入选）
- 两个 last push >30 天的项目（金融基础模型 / claude-skills 清单，active=false，不入选）

## 合规
- **worldmonitor**：原文 "geopolitical monitoring" → 旁白用「全球情报」（中性，避地缘政治敏感）
- **OmniRoute**：原文描述含多个大模型品牌名（Kimi/Claude/GPT 等）+ &amp; 实体。保真锚点完整保留原文（含 &amp;），旁白泛化「268 家服务商、500+ 模型」不逐一点品牌（避免竞品堆砌观感 + 冗长）。无 app 名问题
- **cloudflare_temp_email**：原文已是中文，保真锚点直接用
- 无 app 名（剪映等）、无违禁词、无搜索引导

## design
github 暗色科技风（冷色主 + 暖强调），世界地图/网格/数据流元素配合情报与网关主题
