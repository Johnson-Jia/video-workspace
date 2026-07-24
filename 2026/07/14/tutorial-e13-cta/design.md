# E13 cta 段 · 设计文档（合集收官·13 集完结）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 25s
category: tutorial
segment: cta

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：
  - 合集标识蓝 #60A5FA/#93C5FD（合集标识 + 思想→实操收束）
  - 13 集完结徽章金 #FBBF24/#FCD34D（收官暖金点缀，徽章主体可用，fx 暖色 alpha≤0.22）
  - 关注 CTA 绿 #34D399/#6EE7B7（点关注 CTA 引导）
  - 提问互动白 rgba(255,255,255,0.90)（中性互动提问文案）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（数字 13 + 标签）
- 整体调性：3 phase 纯切换（禁 data-reveal，多 phase 用 GSAP timeline 顺序切换，避 phase-2/3 不显示）—— phase-1 核心思想收束（AI 只生成·确定性执行·挡幻觉于运行期之外）→ phase-2 合集收官（13 集完结徽章 + 思想转变→落地实操 一条龙）→ phase-3 关注 CTA + 中性互动提问（点关注 / 教程仓库评论区 / 你的项目测试现在怎么跑的）

## 情绪曲线 emotion_curve（3 点）
- 0.62（核心思想收束——AI 只生成·确定性执行·挡幻觉于运行期之外）
- 0.78（十三集合集完结——从思想转变到落地实操一条龙走完 + 徽章）
- 0.88（关注 CTA + 中性互动提问——点关注 / 教程仓库评论区 / 你的项目测试现在怎么跑的）

## 沉浸模式 immersion_mode
phase 切换（3 phase，纯 GSAP timeline，禁 data-reveal）：核心收束 → 合集收官 → 关注 CTA

## 叙事模板 narrative_template
收束 + 收官 + CTA（core-recap → series-finale → follow-cta）
- Step 1（0-8s）：核心思想收束——AI 只生成·确定性执行·把幻觉挡在运行期之外（ai-test-frame 开箱跑通·换你系统四步改造）
- Step 2（8-16s）：十三集合集完结——从思想转变到落地实操一条龙走完（13 集完结徽章）
- Step 3（16-25s）：关注 CTA + 中性互动提问——点关注 / 教程仓库在评论区 / 你的项目测试现在是怎么跑的（中性互动，禁站队对抗）

## 组件
- bg：diamond_lattice（深蓝底菱形网格，与 E13 hook/intro/arch/registry/datadriven/softassert/aigenonly/rundemo/customize 同款，跨段视觉连贯）
- fx：fx-aura 静态光晕（蓝合集标识 + 金完结徽章 + 绿关注 CTA，冷色优先 alpha≤0.22 暖金）+ fx-particle + fx-blink（禁划过类 scan/stream/beam，教程铁律）

## fonts
title: Inter
body: Noto Sans SC
data: JetBrains Mono
