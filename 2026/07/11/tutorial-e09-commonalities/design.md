# E09 commonalities 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 50s
category: tutorial
segment: commonalities

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，承接 E09 selfimprove 循环图）
- 强调色：暖金 #FBBF24/#FCD34D（资产化卡）+ 冷蓝 #60A5FA/#93C5FD（Skill/OpenSpec 卡）+ 翠绿 #34D399/#6EE7B7（录制/多Agent 卡）+ 紫 #A78BFA/#C4B5FD（RAG 卡）+ 暖橙 #FB923C/#FDBA74（OpenSpec 规范驱动强调）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（编号/标签）
- 整体调性：沉稳科技 + 六卡共性清晰（六卡片网格 + 每卡一句话核心）

## 情绪曲线 emotion_curve（5 点）
- 0.50（点题「六大共性方法论」）
- 0.60（资产化/Skill，务实沉淀）
- 0.68（OpenSpec+Superpowers，规范驱动）
- 0.75（录制+多Agent，规模化复制）
- 0.65（RAG 调研收尾）

## 沉浸模式 immersion_mode
data_reveal：6 卡片网格 reveal stagger

## 叙事模板 narrative_template
六大共性（intro → 6 卡片 reveal → 收尾）
- Phase 1（0-5s）：标题「六大共性方法论」+ 副标「十三组实战提炼」
- Phase 2（5-45s）：6 卡片网格 reveal stagger（3+3 两行）：资产化/Skill/OpenSpec（顶行）+ 录制/多Agent/RAG（底行）逐卡亮起
- Phase 3（45-50s）：收尾「十三组实战 · 六大共性」总结

## bg_component
hex_grid

## 文字安全
- 渐变文字两端亮色（#FCD34D/#FBBF24/#60A5FA/#93C5FD/#34D399/#6EE7B7）
- text-shadow alpha ≤0.32
- 文字溢出防御：word-break / overflow-wrap / flex min-width:0
- 多音字：转→转型 / 藏→隐藏 / 9→九（本段无）
- 禁"第一"用"其一/首"（narration 已用"其一"）
- 创作指令禁泄露
