# E13 aigenonly 段 · 设计文档（AI 只生成不执行·最关键思想）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 55s
category: tutorial
segment: aigenonly

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：
  - 编码期流程蓝 #60A5FA/#93C5FD（录制 → AI 转换 → 人审）
  - handler 产出金 #FBBF24/#FCD34D（编码期成果 handler）
  - 运行期确定性绿 #34D399/#6EE7B7（运行期零 AI 确定性执行）
  - 虚假通过警示红 #FCA5A5/#EF4444（幻觉风险红叉）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码片段 handler / 录制）
- 整体调性：3 phase 纯切换（禁 data-reveal，多 phase 用 GSAP timeline 顺序切换，避 phase-2/3 不显示）—— phase-1 最关键思想总览（AI 只生成不执行 + 虚假通过红叉警示）→ phase-2 编码期三步产出 handler（录制 → AI 转换 → 人审）→ phase-3 运行期零 AI 确定性执行 + 根治虚假通过收尾

## 情绪曲线 emotion_curve（3 点）
- 0.55（这是整套框架最关键的思想 + 虚假通过红叉警示 抛出核心）
- 0.68（编码期三步产出 handler 录制 → AI 转换 → 人审）
- 0.82（运行期零 AI 确定性执行 根治虚假通过 收尾）

## 沉浸模式 immersion_mode
phase 切换（3 phase，纯 GSAP timeline，禁 data-reveal）：核心思想 → 编码期三步 → 运行期确定性

## 叙事模板 narrative_template
方法论 + 流程（key-idea-overview → coding-time-three-steps → runtime-deterministic）
- Step 1（0-10s）：这是整套框架最关键的思想——AI 只生成不执行 + 虚假通过红叉警示（AI 以为验证了实际没有）
- Step 2（10-20s）：编码期三步产出 handler——录制 → AI 转换 → 人审（handler 在编码期产出）
- Step 3（20-30s）：运行期零 AI 确定性数据驱动调度——AI 只生成代码 人审通过后 运行期全确定性执行 根治虚假通过

## 组件
- bg：diamond_lattice（深蓝底菱形网格，与 E13 hook/intro/arch/registry/datadriven 同款，跨段视觉连贯）
- fx：fx-aura 静态光晕（蓝编码+金handler+绿运行+红警示，冷色优先 alpha≤0.22 暖色）+ fx-particle + fx-blink（禁划过类 scan/stream/beam，教程铁律）

## fonts
title: Inter
body: Noto Sans SC
data: JetBrains Mono
