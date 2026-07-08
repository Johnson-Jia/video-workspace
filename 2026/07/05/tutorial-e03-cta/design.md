# design.md — E03 CTA 收尾（E04 全员赋能预告 + 合集引导 + 互动老板三问）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。E03 收尾：E04 全员赋能预告 + 12 集合集引导 + 互动（中性提问禁站队）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 3 region**（scenes=1，避开 R-R-010）。E04 预告 + 合集引导 + 互动，按 narration 锚点 reveal 同屏累积。

## style

教程收尾预告风。深色底 + 金色预告卡（E04·全员赋能）+ 合集引导条 + 蓝色互动提问。布局：E04 预告卡居中大块 → 合集引导横条 → 互动提问底部强调。

## color_direction

深蓝底 + 金/绿/蓝三色（金=预告高亮 / 绿=合集正向 / 蓝=互动理性）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| E04 预告（高亮） | `#FBBF24` | 金色（合集固定色） |
| 合集引导（正向） | `#10B981` | 绿色（行动号召） |
| 互动提问（理性） | `#3B82F6` | 蓝色（中性提问） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 3 region（E04 预告 + 合集 + 互动）。region 按 data-reveal 时间点淡入（预告 fade / 合集 top / 互动 fade）。

## 视觉区域范式（1 场景，~30s）

### 单场景：CTA 收尾（3 region 同屏累积）

- **region1 E04 预告卡**（data-reveal=0，dir=fade）：「下集 · 全员赋能」+ 三模块（工具怎么选 / 培训怎么做 / 规范怎么资产化）+ 「预算批了不落地 · 钱白花」
- **region2 合集引导**（data-reveal=12，dir=top）：「12 集深度解析 · 点关注不走丢」+ 教程仓库在评论区
- **region3 互动**（data-reveal=20，dir=fade）：「你的转型方案，能答出老板三问吗？」+ 评论区聊（中性提问，禁站队）

## 动画策略

- region fade-in + 方向偏移（fade 纯 opacity / top 从 y:-40），500ms
- E04 预告卡居中大块（金边框 + 三模块胶囊）
- fx-pulse 多色静态光晕 + fx-blink 锚点（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_cta`（E04 预告 + 合集引导 + 互动）
