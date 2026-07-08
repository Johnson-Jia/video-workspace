# design.md — E04 intro（全员赋能三件事）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏导引：全员赋能三件事 + 本集结构（前半/后半）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。3 region（标题 + 三件事列表 + 本集结构）。

## color_direction

深蓝 scan_grid 底 + 三件事三色（蓝=选工具 / 绿=培训 / 金=规范）+ 结构分隔：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | scan_grid | 深蓝网格 |
| ① 选对工具 | `#93C5FD` | 蓝色（工具） |
| ② 全员培训 | `#6EE7B7` | 绿色（人） |
| ③ 规范资产化 | `#FCD34D` | 金色（资产） |

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「全员赋能 · 三件事」
- **region2 三件事**（reveal 5，left）：3 卡片横排（① 选对工具 按角色 / ② 全员培训 全覆盖 / ③ 规范资产化）
- **region3 本集结构**（reveal 16，top）：分隔条「前半段 工具选型+安装 ｜ 后半段 规范资产化」

## bg_component

`scan_grid`

## visual_type

`tutorial_intro`
