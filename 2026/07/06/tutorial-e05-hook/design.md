# design.md — E05 hook（给 AI 装上眼睛和记忆 + 反常识钩子）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。钩子：AI 上手三个痛点（瞎编/看不见/留不住）+ 反常识收束「这集可以跳过」。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region（标题 + 三痛点 + 反常识收束），按 narration 锚点 reveal 同屏累积。

## style

三痛点文字依次浮现，最后大字反差钩子。顶部标题「基础设施」，中部三痛点（瞎编/看不见/留不住），底部金色反常识卡「这集可以跳过？」。

## color_direction

深蓝 hex_grid 底 + 三痛点蓝/紫/红 + 金色反常识：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格（基础设施结构感） |
| 标题 | `#E0E7FF` | 蓝白（主标） |
| 痛点1 瞎编 | `#FCA5A5` | 浅红（幻觉） |
| 痛点2 看不见 | `#C4B5FD` | 紫色（盲读） |
| 痛点3 留不住 | `#93C5FD` | 蓝色（流失） |
| 反常识 | `#FCD34D` | 金色（钩子） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 痛点 left / 反常识 top）。

## 视觉区域范式（1 场景，~28s TTS）

### 单场景：三痛点 + 反常识钩子（4 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「给 AI 装上眼睛和记忆」+ 副标「基础设施」
- **region2 三痛点**（data-reveal=4，dir=left）：三痛点横排（瞎编/看不见/留不住），各列一句话
- **region3 反常识钩子**（data-reveal=18，dir=top）：金色大字「这集可以跳过？」反差收束

## 动画策略

- region fade-in + 方向偏移，500ms
- 三痛点横排对称布局
- fx-aura 静态光晕（禁划过类）

## bg_component

`scan_grid`（六边网格，基础设施结构感）

## visual_type

`tutorial_hook`（三痛点 + 反常识钩子）
