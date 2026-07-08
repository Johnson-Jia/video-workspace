# design.md — E02 cta 段（收尾：E03 预告 + 合集引导 + 互动）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。三区域：E03 预告卡 + 合集引导 + 互动问题（中性）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 3 region**（scenes=1，避开 R-R-010）。

## style

教程科技风。预告卡（金/蓝）+ 合集引导（蓝）+ 互动问题（绿/蓝白收束）。

## color_direction

深蓝底 + 金（预告）+ 蓝（合集）+ 绿（互动收束）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| E03 预告 | `#FBBF24` / `#3B82F6` | 金/蓝（重点预告） |
| 合集引导 | `#3B82F6` | 蓝（合集品牌） |
| 互动问题 | `#10B981` / `#E0E7FF` | 绿/蓝白（中性收束） |

## immersion_mode

教程横屏 reveal — 1 场景。E03 预告 → 合集引导 → 互动问题，按 narration 锚点 reveal 同屏累积。

## 视觉区域范式（1 场景，~30s）

### 单场景：CTA 收尾（3 region 同屏累积）

- **region1 E03 预告卡**（data-reveal=0）：「下集 · 战略启动：向老板要预算」+ ROI/老板三问
- **region2 合集引导**（data-reveal=10，dir=top）：「12 集深度解析 · 点关注不走丢」+ 评论区引导
- **region3 互动问题**（data-reveal=18，dir=fade）：「你团队里，谁还在抗拒 AI？谁已经在用？」（中性提问，禁站队）

## 动画策略

- region fade-in + 方向偏移，500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`

## visual_type

`tutorial_cta`
