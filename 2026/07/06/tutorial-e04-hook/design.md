# design.md — E04 hook（工具选错差一个量级）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。钩子：工具选错差一个量级（效率翻倍 vs 原地踏步）+ 本集主题（全员赋能）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 3 region**（标题 + 对比卡 + 本集主题），按 narration 锚点 reveal 同屏累积。

## style

工具选错量级差。顶部标题醒目，中部双卡对比（效率翻倍 绿 / 原地踏步 红），底部本集主题卡收束。

## color_direction

深蓝底 + 对比双色（绿=效率翻倍 / 红=原地踏步）+ 金色本集主题：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | scan_grid | 深蓝网格 |
| 效率翻倍 | `#6EE7B7` | 绿色（正面） |
| 原地踏步 | `#F87171` | 红色（负面） |
| 本集主题 | `#FCD34D` | 金色（收束） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+对比卡+主题）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 对比卡 left / 主题 top）。

## 视觉区域范式（1 场景，~22s TTS）

### 单场景：工具选错 + 本集主题（3 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「工具选错」+ 副标「差一个量级」
- **region2 对比卡**（data-reveal=7，dir=left）：左卡「效率翻倍」绿 + 右卡「原地踏步」红 + 中间「差别在工具 不在人」
- **region3 本集主题**（data-reveal=17，dir=top）：金色主题卡「全员赋能」（选对工具 + 装好 Claude Code + 规范资产化）

## 动画策略

- region fade-in + 方向偏移，500ms
- 对比卡左右对称布局
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`scan_grid`（深蓝网格）

## visual_type

`tutorial_hook`（钩子对比 + 本集主题）
