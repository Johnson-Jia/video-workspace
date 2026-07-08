# design.md — E02 原理② token 预测（大模型本质）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏（categories/tutorial.md orientation_hint=landscape）。大模型本质 = 预测下一个 token，1 场景 4 region 同屏累积 reveal：原理编号 + 预测示意 + 幻觉警示 + 验证金句（含 count-up 0→100%）。s6_assemble 横屏分支依赖此字段。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 4 region**（scenes=1，避开 R-R-010 相邻同质）。标题 + token 预测示意 + 幻觉卡 + 验证金句，按 narration 锚点 reveal 同屏累积。

## style

原理揭示科技风。冷静、克制——一句话讲透大模型本质，token 预测示意大字 + 幻觉红框警示 + 验证金句 count-up。教程重结构清晰、逻辑递进。

## color_direction

深蓝底 + 三段语义色（蓝=原理理性 / 红=幻觉警示 / 绿=验证正向）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 原理编号/标题 | `#3B82F6` | 蓝色（理性原理） |
| token 输入 | `#94A3B8` | 灰色（已给定上文） |
| token 预测 | `#FBBF24` | 金色（模型生成的高概率续写） |
| 幻觉警示 | `#EF4444` | 红色（一本正经地胡说 = 危险） |
| 验证金句 | `#10B981` | 绿色（必须验证 = 正向收束） |
| 蓝白 | `#E0E7FF` | 次要文字 |

> 强色控制：蓝/红/绿严格分工——蓝=原理、红=幻觉（要避免）、绿=验证（要落地）。金=高概率 token（模型生成的"看起来对"）。

## immersion_mode

教程横屏 reveal — 1 场景 + tut-grid 四区垂直布局 + count-up 数据飞升。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 预测 left / 幻觉 top / 验证 fade + count-up 0→100%）。

## 视觉区域范式（1 场景，~85s）

### 单场景：token 预测全流程（4 region 同屏累积）

- **region1 标题**（data-reveal=0，fade）：「原理 ②」蓝色编号胶囊 + 标题「预测下一个 token」
- **region2 token 预测示意**（data-reveal=8，left）：大字「今天天气真 → 好」（输入灰色 + 金色箭头 + 预测金色大字 120px+）+ 注「根据上文预测下一个 token」
- **region3 幻觉揭示卡**（data-reveal=30，top）：红边框卡「一本正经地胡说」+ 副「看起来对 ≠ 验证过对」+ 注「生成的是最可能的，不是验证过的」
- **region4 验证金句**（data-reveal=50，fade）：绿色大字「必须验证」+ count-up 验证率 0→100%（data-count-to="100" data-count-at="52"）+ 副「信任但验证 · 根在这」

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40），500ms
- **count-up 验证率**：data-count-to="100" data-count-at="52"（reveal 时间 50 + 2s 后触发），GSAP textContent tween 0→100 snap 整数，0.9s power2.out
- fx-pulse + fx-blink 静态点缀（禁划过类 fx-scan/fx-beam）
- token 预测示意区：金色箭头静态指向"好"字（不追线、不划过）

## bg_component

`clean_slate`（原理揭示收敛简洁底）

## visual_type

`principle_token_prediction`（原理② token 预测示意）
