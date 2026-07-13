# design.md — E08 段3 首层 Co-authored-by（终端演示核心段）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。首层 Co-authored-by 初筛：终端窗口（commit message + trailer 金色高亮）+ 六个 AI 工具名名单侧栏 + VS Code Copilot 误标缺陷红框警示。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。标题（左对齐）+ 终端窗口（commit message + Co-authored-by trailer 金色高亮，打字动画）+ 六个工具名名单侧栏（claude/copilot/cursor/chatgpt/codeium/gemini）+ 误标缺陷红框警示条。布局 space-between 撑满画布。

## style

终端演示技术风。标题左对齐 + 终端窗口（深底 #0a0a0a + 红黄绿圆点 + JetBrains Mono 等宽）+ commit message 打字动画 GSAP + Co-authored-by trailer 金色高亮 + 六工具名名单侧栏（绿色 ✓ 命中标记）+ 误标缺陷红框警示（VS Code Copilot 对手写代码加 trailer）。

## color_direction

深底 + 四色（青=终端/数据 / 金=trailer 信号锚点 / 绿=命中✓ / 红=误标缺陷警示）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 终端底 | `#0a0a0a` | 终端深底（红黄绿圆点） |
| 信号锚点 | `#FBBF24` | 金色（Co-authored-by trailer 高亮） |
| 命中标记 | `#10B981` | 绿色（✓ 工具名命中） |
| 误标缺陷 | `#F87171` | 红色（VS Code Copilot 误标警示） |
| 主背景 | `#0F172A` | 深蓝主底（contour_lines 等高线叠层） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（标题+终端窗口+工具名名单+误标缺陷）。region 按 data-reveal 时间点淡入 + 方向。终端 commit message 行打字动画（GSAP 逐字 reveal）。

## bg_component

`contour_lines`（青色等高线地形纹理，冷色科技感，与 E08 其他段做 bg 差异：why=hex_grid / coauthored=contour_lines；visual_types 含 contour/glow/gradient/particles，符合 R-R-009 要求非 {gradient,glow,grid} 单一组件）

## fx_strategy

冷色优先（青/蓝），fx-aura 静态光晕衬底（禁划过类 scan/stream/beam），≥3 元素/场。终端窗口边缘冷色光晕呼应技术氛围。
