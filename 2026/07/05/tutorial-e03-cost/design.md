# design.md — E03 段2（预算 · 4 块成本：工具/培训/基础设施/推广）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。预算四块成本——工具/API / 培训 / 基础设施 / 推广运营。2×2 grid 同屏累积。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 5 region**（scenes=1，避开 R-R-010 相邻同质误报）。标题 + 4 成本卡（2×2 grid），按 narration 锚点 reveal 同屏累积。

## style

预算清单 grid 风。清晰、对称——2×2 成本卡矩阵，每卡含编号 + 成本项 + 估算方式。第三块（基础设施）标「小团队可跳过」角标做差异化。

## color_direction

深蓝底 + 四色语义（蓝=工具/技术 / 紫=培训/人 / 橙=基础设施/可选 / 绿=推广/轻量）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 工具/API（技术） | `#3B82F6` | 蓝色（核心工具） |
| 培训（人） | `#A78BFA` | 紫色（人力投资） |
| 基础设施（可选） | `#FB923C` | 橙色（大团队/可跳过） |
| 推广运营（轻量） | `#10B981` | 绿色（轻量收尾） |
| 金/黄 | `#FBBF24` | 总投入收束 / 角标 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+4 成本卡 grid）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 卡 left 交替 top）。2×2 grid 同屏累积，最后收束总投入。

## 视觉区域范式（1 场景，~30s TTS）

### 单场景：预算 4 块成本（5 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「预算 · 4 块成本」+ 引子「立项要算清要多少钱」
- **region2 成本卡①**（data-reveal=5，dir=left）：① 工具/API（蓝，人均月费 × 人数 × 月数 · Claude Code 订阅/模型调用）
- **region3 成本卡②**（data-reveal=11，dir=top）：② 培训（紫，2 天全员脱产 + 讲师 · 工时成本）
- **region4 成本卡③**（data-reveal=17，dir=left）：③ 基础设施（橙，RAG/知识图谱服务器 + 架构师 · 角标「小团队可跳过」）
- **region5 成本卡④**（data-reveal=24，dir=top）：④ 推广运营（绿，度量工具/试点激励/考核绑定 · 轻量）+ 收束「四块 = 总投入」

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- 2×2 grid 对称布局（左上工具 / 右上培训 / 左下基础设施 / 右下推广）
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_cost`（成本清单 grid 布局）
