orientation: landscape
resolution: 1920x1080
# E09 essence 段 · 设计文档

## 元数据
duration: 30s
category: tutorial
segment: essence

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，承接 E09 cases 收尾"个体变组织"）
- 强调色：暖金 #FBBF24/#FCD34D（金句大字「人 + AI，人是根本」+ 个体经验→组织资产 流向金色箭头）+ 冷蓝 #60A5FA/#93C5FD（"AI"渐变 + 地基）+ 翠绿 #34D399/#6EE7B7（持续进化 / 经验不走 收尾点缀）
- 字体：Inter（金句大字）/ Noto Sans SC（正文）/ JetBrains Mono（"人 + AI" 数学式 + 阶段标签）
- 整体调性：克制精美（少元素大留白，金句居中）+ 升华感（不堆砌，每个元素呼吸）

## 情绪曲线 emotion_curve（5 点）
- 0.55（点题「转型不是一次性项目，是持续进化的能力」）
- 0.72（人加 AI，人是根本——金句大字 reveal 高潮）
- 0.78（工具方法论会迭代，但思想/原理/拥抱 AI 是地基）
- 0.85（个体经验→组织资产 流向金色箭头 reveal）
- 0.80（收尾「让人走经验不走」绿色点缀）

## 沉浸模式 immersion_mode
quote_reveal：金句大字居中 reveal + 流向箭头 stagger

## 叙事模板 narrative_template
组织资产本质（金句点题 → 人+AI 人是根本 → 三大地基 → 个体→组织 流向 → 收尾）
- Phase 1（0-4s）：点题「转型 = 持续进化的能力」
- Phase 2（4-12s）：金句大字「人 + AI，人是根本」reveal 居中
- Phase 3（12-20s）：三大地基（转变思想 / 懂原理 / 拥抱 AI）stagger + 工具方法论迭代注脚
- Phase 4（20-30s）：流向金色箭头「个体经验 → 组织资产」+ 收尾「让人走经验不走」

## bg_component
hex_grid

## 文字安全
- 渐变文字两端亮色（#FCD34D/#FBBF24/#60A5FA/#93C5FD/#34D399/#6EE7B7）
- text-shadow alpha ≤0.32
- 文字溢出防御：word-break / overflow-wrap / flex min-width:0
- 多音字：转→转型（非转动）
- 禁"第一"用"其一/首"（本段无）
- 创作指令禁泄露
