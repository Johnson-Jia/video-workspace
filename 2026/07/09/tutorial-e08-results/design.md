# design.md — E08 段7 量化效果（数据卡核心段）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。量化效果数据卡：五项大字数据（+104% / -16.4pp / 76.6% / 5-10倍 / -40%）+ 转型前后趋势对比条 + 客观口径收尾。数据卡 width:100% 撑满画布。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景多 region。标题（左对齐）+ 五项数据卡（grid 撑满）+ 转型前后趋势对比条 + 客观口径收尾条。布局 space-between 撑满画布，数据卡 flex:1。

## style

数据卡技术风。标题左对齐 + 五项数据卡大字（人均产出 +104% / Bug 占比 -16.4pp / AI 代码占比 76.6% / 测试用例 5-10倍 / 词元 -40%）+ 转型前后趋势对比条（Before→After 可视化）+ 客观口径收尾（不夸大，承认需求加人员变动）。冷色优先（青/蓝/绿），数据大字渐变同色系禁白端点。

## color_direction

深底 + 三色（青=数据主色 / 绿=正向改善（含 Bug 降） / 金=AI 占比锚点）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 数据主色 | `#22D3EE` | 青色（人均产出 +104% / 测试 5-10倍） |
| 正向改善 | `#34D399` | 绿色（Bug -16.4pp / 词元 -40%，降是好） |
| AI 锚点 | `#FBBF24` | 金色（AI 代码占比 76.6%） |
| 主背景 | `#0F172A` | 深蓝主底（scan_grid 扫描网格叠层） |
| 客观口径 | `#E0E7FF` | 蓝白（收尾条文字） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+五数据卡+趋势对比+客观口径）。region 按 data-reveal 时间点淡入。数据卡大字渐变 reveal（GSAP scale+opacity）。

## bg_component

`scan_grid`（深蓝扫描网格，数据度量感 + 与相邻段异质：coauthored contour_lines / stylometry diamond_lattice / multiagent diamond_lattice / why hex_grid / results scan_grid；visual_types 含 scan/grid/glow/gradient，符合 R-R-009 要求非 {gradient,glow,grid} 单一组件）

## fx_strategy

冷色优先（青/蓝/绿），fx-aura 静态光晕衬底（禁划过类 scan/stream/beam），≥3 元素/场。数据卡边缘冷色光晕呼应度量氛围。fx-blink 锚点点缀数据卡角（青/绿）。
