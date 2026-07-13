# design.md — E08 段9 度量的本质（金句升华核心段）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。度量的本质金句段：三阶梯递进金句大字（量化→管理→方向，金色渐变文字递进放大）+ 左右对比「拍脑门蒙一次 vs 量化对齐一百次」+ 收尾「度量不是为了证明 AI 有用，是为了让下一组决策有根」。深蓝底 + 金色渐变文字（同色系深金→暖金，禁白端点）。思想升华段，视觉比其他段更克制精致——少元素、大留白、金句居中。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。三阶梯金句递进（量化→管理→方向）+ 左右对比 + 收尾金句。region 按 data-reveal 时间点淡入。金句居中大留白，每阶梯文字递进放大（72px → 96px → 120px）。

## style

思想升华克制风。深蓝主底（#0F172A）+ 金色渐变文字三阶梯递进（深金 #B8860B → 暖金 #FBBF24，同色系禁白端点）+ text-shadow 深蓝 rgba(30,41,59,0.6) 禁发光 + fx-aura 静态低 alpha（≤0.18）冷金衬底。少元素、大留白、金句居中。三阶梯用「→」连接递进关系。

## color_direction

深蓝底 + 金色同色系渐变（禁白端点）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 主背景 | `#0F172A` | 深蓝主底（思想沉稳） |
| 金句文字-深端 | `#B8860B` | 深金（DarkGoldenrod，渐变深端，禁白） |
| 金句文字-暖端 | `#FBBF24` | 暖金（amber-400，渐变亮端） |
| 文字阴影 | `rgba(30,41,59,0.6)` | 深蓝阴影（禁发光） |
| 对比-拍脑门（弱） | `#64748B` | slate-500（灰，弱化「蒙一次」） |
| 对比-量化（强） | `#FBBF24` | 暖金（强化「对齐一百次」） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（阶梯1量化+阶梯2管理+阶梯3方向 → 左右对比 → 收尾金句）。region 按 data-reveal 时间点淡入 + 方向。三阶梯递进放大（72→96→120px），金色渐变文字。

## bg_component

`scan_grid`（扫描网格纹理，冷色科技感衬底；与相邻 gradual（hex_ladder 阶梯）/ cta（不同组件）做 bg 差异；scan_grid visual_types 含 scan/gradient/glow，符合 R-R-009 要求非 {gradient,glow,grid} 单一组件）
