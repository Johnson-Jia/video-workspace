# design.md — FDE 番外篇 · ch3 段（技术武器库重映射：五卡速览）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程类强制横屏（categories/tutorial.md orientation_hint=landscape）。五张武器卡横排 grid 撑满 1920 宽 + RAG 三层改造 + 底部总结条，多区域同屏，竖屏装不下。s6_assemble 横屏分支只读 design.md 此字段。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16 教程横屏范式：单 phase + 多 region + data-reveal（不是竖屏 phase 切换）。每场景一个 phase，场景内 region 用 data-reveal 错时累积。五卡 grid 用 space-between 撑满宽度（禁为居中而居中）。

## fields（gate 解析速览）

style: 清爽专业科技风·武器库重映射（冷静清单，五卡横排撑满，信息密度高靠卡片层级不靠花哨动画）
mood: 沉稳·条理（弹药库定位 → 逐卡讲改造 → 沉淀收束，理性梳理不煽动）
color_direction: 深蓝底 #0F172A + 金 #FBBF24（RAG/重点改造）+ 蓝 #3B82F6（定义/对照）+ 蓝白 #E0E7FF + 中性 #94A3B8
storyboard: 八场景（hook 锚点 → 弹药库+五卡总览 → RAG 三层 → RAG 对比 → 多Agent → 测试 → 度量 → Skill+总结条）
emotion_curve: [0.80, 0.55, 0.70, 0.62, 0.65, 0.90]

## style

清爽专业科技风·武器库重映射。冷静、条理——五张武器卡横排撑满画布，每卡 demo 名 + 何时用 + FDE 改造要点一句话，靠卡片层级和金/蓝分工传达信息，不靠花哨动画。深蓝底 + fx-aura/fx-pulse-ring 静态脉冲（禁划过类 fx）。教程重内容轻视觉。

## mood

沉稳·条理——先定位弹药库（主教程给的 demo），逐卡讲现场改造要点（RAG 三层是重点），最后落在 Skill 沉淀与资深/初级分界。理性梳理，不煽动、不夸张。

## color_direction

深蓝底 + 双色分工（金=RAG 重点改造/数据冲击 / 蓝=定义与对照）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（沉稳，让卡片跳出来） |
| RAG/重点改造 | `#FBBF24` | RAG 卡边框、三层改造 chip、Skill 总结条金边 |
| 定义与对照 | `#3B82F6` | 何时用标签、对照卡（主教程 vs 现场）蓝边 |
| 蓝白 | `#E0E7FF` | 改造要点正文 / 次要文字 |
| 中性 | `#94A3B8` | 注释 / 分隔 / 总结条副标 |

> 强色控制：金/蓝严格分工——金=RAG 重点改造（三层 + Skill 沉淀结论），蓝=对照与定义。其余三卡（多Agent/测试/度量）用蓝白 + 中性克制，让 RAG 金边突出。渐变文字禁白色端点，同色系高饱和（金 #FBBF24→#F59E0B→#FCD34D / 蓝 #60A5FA→#3B82F6→#93C5FD）。fx 暖色（金）alpha ≤ 0.22。

## storyboard

### narrative_template

武器库重映射（ch3 单段）：
1. hook 锚点（seg0）：同一套 demo，到客户现场用法全变
2. 弹药库定位（seg1）：主教程 demo 是弹药库，本章讲现场用法
3. RAG 三层改造（seg2）：脱敏 / 隔离 / 回写 + 评估换答准率
4. RAG 对比（seg3，增补）：沙盒玩 vs 真实数据上跑
5. 多Agent（seg4）：按客户流程拆阶段，职责客户听得懂
6. 测试（seg5）：回归用真实场景，软断言阈值当面定
7. 度量（seg6）：客户在意省人省钱，基线必须前置
8. Skill 沉淀（seg7）：怎么搞定客户 + 底部总结条 + 资深/初级分界

### emotion_curve

[0.80, 0.55, 0.70, 0.62, 0.65, 0.90]

> 节奏：hook 锚点高（0.80）→ 弹药库定位回落铺垫（0.55）→ RAG 三层重点爬升（0.70）→ 三张克制卡平稳（0.62-0.65）→ Skill 沉淀收束在高位（0.90，沉淀/分界感收尾）。

### immersion_mode

教程横屏 reveal — 每场景单 phase + 多 region data-reveal 同屏累积。卡片/要点 reveal 后保持在场，八场景依次推进。

## 视觉区域范式

### 场景 1：hook 锚点（seg0，~4s，「同一套 demo · 现场用法全变」）

- **标题区**（data-reveal=0）：蓝色渐变大字「同一套 demo」+ 蓝白副标「到客户现场 · 用法竟然全变」+ 金色小标签「技术武器库 · 现场重映射」
- **fx-aura**：蓝色静态光晕脉冲（alpha 0.20，禁划过类）

### 场景 2：弹药库定位 + 五卡总览（seg1，~12s，五卡 grid）

- **定位条**（data-reveal=0）：蓝白胶囊「主教程 demo = 弹药库」+ 文案「本章只讲现场用法与改造」
- **五卡 grid 区**（data-reveal=2 起 stagger）：五张卡横排 space-between 撑满宽度，每卡只 demo 名 + 一句「何时用」短标（RAG/多Agent/测试/度量/Skill），card-1 RAG 卡金边高亮（重点预告）
- **fx-blink**：卡间锚点平衡构图

### 场景 3：RAG 三层改造（seg2，~16s，RAG 卡详 ≥2 phases）

- **RAG 卡放大区**（phase 1, data-reveal=0）：RAG 卡放大居中偏左，金边，「何时用：客户知识库 AI 查答」
- **三层改造 chip 区**（phase 2, data-reveal=4）：三个金色 chip 横排「数据脱敏」「权限隔离」「结果回写」+ 蓝白注「评估换成客户业务答准率」
- **fx-pulse-ring**：RAG 卡左金色脉冲环锚点

### 场景 4：RAG 对比（seg3，~18s，沙盒 vs 真实 ≥2 phases）

- **对照双卡区**（phase 1, data-reveal=0）：左蓝卡「主教程：示例数据 · 看重排分数」/ 右金卡「现场版：脱敏 · 隔离 · 回写 · 答准率」
- **结论条**（phase 2, data-reveal=6）：底部金色结论「一个在沙盒里玩 · 一个在客户真实数据上跑」
- **fx-aura**：右侧金卡静态光晕

### 场景 5：多Agent（seg4，~12s，单 phase）

- **多Agent 卡区**（data-reveal=0）：卡名「多 Agent 编排」+ 蓝白「何时用：一个智能体搞不定」+ 改造要点「按客户真实流程拆阶段 · 职责用客户听得懂的话命名」
- **fx-blink**：锚点

### 场景 6：测试框架（seg5，~15s，≥2 phases）

- **测试卡区**（phase 1, data-reveal=0）：卡名「测试框架」+「何时用：防 AI 改一处坏一片」
- **阈值双分卡区**（phase 2, data-reveal=6）：左「可接受误差」蓝 chip / 右「红线」金 chip + 蓝白「和客户当面定 · 写进验收标准 · 别上线后扯皮」
- **fx-pulse-ring**：红线 chip 脉冲

### 场景 7：度量工具（seg6，~15s，≥2 phases）

- **度量卡区**（phase 1, data-reveal=0）：卡名「度量工具」+「何时用：向客户证明回报」+ 金色「客户最在意：省了多少人 · 省了多少钱」
- **基线前置区**（phase 2, data-reveal=6）：金边警示条「基线必须前置 · 演示启动前就采」+ 蓝白注「上线后没有对比基准 · 回报算出来客户也不认」
- **fx-blink**：锚点

### 场景 8：Skill 沉淀 + 总结条（seg7，~21s，≥2 phases）

- **Skill 卡区**（phase 1, data-reveal=0）：卡名「Skill 沉淀」+「FDE 自己的工程肌肉」+ 改造要点「把每个客户现场的通用经验沉淀成 Skill · 下个客户直接复用」
- **总结条区**（phase 2, data-reveal=8）：金色大总结条「主教程沉淀怎么写代码 / FDE 沉淀怎么搞定这类客户」+ 蓝白例「行业工单分流标准口径 · 遗留系统对接踩坑」+ 收尾标「资深 FDE 与初级 FDE 的效率分界 · 就在这」
- **fx-aura**：金色静态光晕收束

## 动画策略

- **标题/卡片 fade-in**：opacity 0→1 + scale 1.03→1，500-600ms ease-out（克制）
- **五卡 grid stagger reveal**：data-reveal 错时 0.4s 依次，space-between 撑满
- **三层 chip 依次 reveal**：data-reveal 错时 1s，同屏累积
- **fx-aura/fx-pulse-ring 静态脉冲**：opacity 呼吸循环（0.4→0.6），fx-pulse-ring 锚点脉冲，不划过不追线
- **禁**：fx-scan/fx-stream/fx-beam 划过类、粒子过载、3D 翻转、强切换；CSS animation 入场（用 GSAP .from）

## bg_component

`clean_slate`（武器库卡片收敛简洁底，八场景共用，靠卡片层与 fx 分场景差异化）

> 相邻场景 bg 差异靠 fx 层（aura 位置/色、pulse-ring 锚点、blink 数量）与卡片金/蓝边切换，bg 底色一致满足 check_adjacent_bg_diversity（fx+卡片层差异）。

## visual_type 映射

- 场景 1：`title_reveal`（hook 锚点标题）
- 场景 2：`card_grid`（五卡横排总览）
- 场景 3：`card_detail`（RAG 三层改造）
- 场景 4：`contrast_cards`（RAG 沙盒 vs 真实）
- 场景 5：`card_detail`（多Agent）
- 场景 6：`dual_split`（测试 可接受/红线）
- 场景 7：`card_detail`（度量 基线前置）
- 场景 8：`card_summary`（Skill + 总结条）
