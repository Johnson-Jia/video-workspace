# design.md — E06 hook（需求到交付一条命令 + 纠错左移反常识）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。钩子：一条命令跑完需求到交付 + 反常识收束「真正的发动机是纠错左移」。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 3 region（标题 + 一条命令 + 反常识），按 narration 锚点 reveal 同屏累积。

## style

反常识钩子结构。顶部标题「需求→交付 一条命令」，中部左移对比（改代码红 vs 改 Markdown 绿 + 左移箭头），底部金色反常识卡「发动机不是写更多代码 是纠错左移」。

## color_direction

深蓝 dark_cipher 代码矩阵底 + 左移对比红/绿 + 金色反常识：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵（规范驱动结构感） |
| 标题 | `#E0E7FF` | 蓝白（主标） |
| 改代码（损失） | `#FCA5A5` | 浅红（质量损失） |
| 改 Markdown（可控） | `#6EE7B7` | 浅绿（质量可控） |
| 反常识 | `#FCD34D` | 金色（钩子） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 对比 left / 反常识 top）。

## 视觉区域范式（1 场景，~32s TTS）

### 单场景：一条命令 + 左移对比 + 反常识（3 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「需求 → 交付 一条命令」+ 副标「OpenSpec + Superpowers」
- **region2 左移对比**（data-reveal=8，dir=left）：左红「改代码 质量损失」→ 右绿「改 Markdown 质量可控」+ 左移箭头，标注「偏差从改代码 → 改 Markdown」
- **region3 反常识钩子**（data-reveal=20，dir=top）：金色大字「发动机不是写更多代码 是纠错左移」反差收束

## 动画策略

- region fade-in + 方向偏移，500ms
- 左移对比横排，箭头从右指向左（改代码→改 Markdown 是左移方向）
- fx-aura 静态光晕（金反常识 / 红/绿对比；呼吸脉冲，禁划过类）

## bg_component

`dark_cipher`（代码矩阵，规范驱动结构感；换掉 E05 的 hex_grid/diamond_lattice 做合集内差异）

## visual_type

`tutorial_hook`（一条命令 + 左移对比 + 反常识钩子）
