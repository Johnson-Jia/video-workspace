# design.md — E02 instruct 段（原理⑥ 精准指令 + 人是根本）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。四区域：标题 + 差/好指令对比 + 金句（实习生）+ 收尾（人是根本）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 4 region**（scenes=1，避开 R-R-010）。

## style

教程科技风。差/好指令左右对比（红绿），金句+收尾向下累积。

## color_direction

深蓝底 + 红绿对比（差红 / 好绿）+ 收束金（金句）+ 蓝白（收尾）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 差指令 | `#EF4444` | 红（错误示范） |
| 好指令 | `#10B981` | 绿（正确示范） |
| 金句 | `#FBBF24` | 金（重点强调） |
| 收尾 | `#3B82F6` / `#E0E7FF` | 蓝/蓝白（人是根本） |

## immersion_mode

教程横屏 reveal — 1 场景。标题 → 差/好对比 → 金句 → 收尾，按 narration 锚点 reveal 同屏累积。

## 视觉区域范式（1 场景，~85s）

### 单场景：精准指令（4 region 同屏累积）

- **region1 标题**（data-reveal=0）：原理编号「原理 ⑥」+ 标题「精准下达指令」fade-in
- **region2 差vs好对比**（data-reveal=8，dir=left）：左红卡 ✗「帮我优化一下」/ 右绿卡 ✓「SQL 18秒→1秒内，先分析后改，EXPLAIN 验证」
- **region3 金句**（data-reveal=35，dir=top）：「像给聪明的实习生下指令」+ 四要素（给上下文/明目标/定流程/要验证）
- **region4 收尾**（data-reveal=55，dir=fade）：「人 + AI · 人是根本」+ 五原理缩略回显（①token②上下文③Agent④REACT⑤指令）

## 动画策略

- region fade-in + 方向偏移，500ms
- 差卡红边框 + 好卡绿边框（语义对比）
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`

## visual_type

`tutorial_instruct`
