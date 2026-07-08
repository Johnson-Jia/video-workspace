# design.md — E04 段1 工具选型（Claude Code / Codex / GLM）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。三工具卡片（按角色）：Claude Code 开发 / Codex 非开发 / GLM 国内 + 杠杆结论。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。5 region（标题 + 3 卡 + 结论）。

## color_direction

深蓝 scan_grid 底 + 三卡三色（蓝=Claude Code / 紫=Codex / 绿=GLM）+ 金结论：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | scan_grid | 深蓝网格 |
| Claude Code | `#93C5FD` | 蓝色（开发/终端） |
| OpenAI Codex | `#C4B5FD` | 紫色（产品/云端） |
| GLM | `#6EE7B7` | 绿色（国内/性价比） |
| 结论 | `#FCD34D` | 金色（杠杆） |

## 视觉区域范式（1 场景，~35s TTS）

- **region1 标题**（reveal 0，fade）：标题「工具选型」+ 副标「按角色 不一刀切」
- **region2 卡① Claude Code**（reveal 5，left）：蓝卡 · 开发者/工程师 · 终端原生/自主执行/生态最完整/上下文最强
- **region3 卡② Codex**（reveal 22，left）：紫卡 · 产品/非开发 · 云端委托+ChatGPT 集成/不碰终端/做原型
- **region4 卡③ GLM**（reveal 40，left）：绿卡 · 国内团队 · 性价比高/国产模型/国内直连
- **region5 结论**（reveal 58，top）：金色「选对工具是杠杆 · 选错再努力也补不回来」

## bg_component

`scan_grid`

## visual_type

`tutorial_tools`
