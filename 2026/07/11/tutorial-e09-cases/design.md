# E09 cases 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 50s
category: tutorial
segment: cases

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，承接 E09 commonalities 六大共性）
- 强调色：暖金 #FBBF24/#FCD34D（数据卡大字对比 + 录制+生成提效强调）+ 冷蓝 #60A5FA/#93C5FD（工具型/编排型卡）+ 翠绿 #34D399/#6EE7B7（避坑资产 + 提效箭头）+ 紫 #A78BFA/#C4B5FD（避坑资产卡）
- 字体：Inter（大字标题/数据大字）/ Noto Sans SC（正文）/ JetBrains Mono（编号/标签/Skill 名）
- 整体调性：沉稳科技 + 数据冲击（4-8h→10-30min 大字对比）+ 4 类资产卡清晰

## 情绪曲线 emotion_curve（5 点）
- 0.50（点题「沉淀复用的真实效果」）
- 0.62（工具型/编排型，务实复用）
- 0.72（避坑资产，不再重犯）
- 0.88（录制+生成提效大字对比，4-8h→10-30min 冲击高潮）
- 0.70（收尾「个体的会用变成组织的默认能力」）

## 沉浸模式 immersion_mode
data_reveal：数据卡 + 4 类资产卡 reveal stagger

## 叙事模板 narrative_template
沉淀复用案例（intro → 4 类资产卡 → 数据卡提效高潮 → 收尾升华）
- Phase 1（0-5s）：标题「沉淀复用的真实效果」+ 副标「个体→组织」
- Phase 2（5-40s）：4 类资产卡 reveal stagger：工具型（sql-query/crud-gen）/ 编排型（devflow）/ 避坑资产（静默吞异常）/ 录制+生成
- Phase 3（40-50s）：数据卡高潮（4-8h→10-30min 大字对比）+ 收尾「个体的会用变成组织的默认能力」

## bg_component
hex_grid

## 文字安全
- 渐变文字两端亮色（#FCD34D/#FBBF24/#60A5FA/#93C5FD/#34D399/#6EE7B7）
- text-shadow alpha ≤0.32
- 文字溢出防御：word-break / overflow-wrap / flex min-width:0
- 多音字：转→转型 / 藏→隐藏 / 9→九（本段用「四到八/十到三十」中文数字）
- 禁"第一"用"其一/首"（本段无）
- 创作指令禁泄露
