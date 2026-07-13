# E09 selfimprove 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 60s
category: tutorial
segment: selfimprove

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，承接 E09 pitfall 案例卡）
- 强调色：暖金 #FBBF24/#FCD34D（循环图节点高亮 + CLAUDE.md 更新动作）+ 冷蓝 #60A5FA/#93C5FD（AI 犯错/下次避开节点）+ 翠绿 #34D399/#6EE7B7（团队规范进化升华）+ 紫 #A78BFA/#C4B5FD（人指出节点）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（编号/标签/CLAUDE.md）
- 整体调性：沉稳科技 + 循环图清晰流转（圆形节点逐个亮起 + 循环箭头）+ 金色升华

## 情绪曲线 emotion_curve（5 点）
- 0.50（点题「自我改进循环是精华」）
- 0.62（流程开始：AI 犯错 → 人指出）
- 0.72（AI 更新 CLAUDE.md，规则防类似情况）
- 0.85（下次自动避开 + 循环箭头闭合，团队规范进化升华）
- 0.70（收尾金句「规则越用越厚」）

## 沉浸模式 immersion_mode
data_reveal：自我改进循环图（4 圆形节点逐个亮起 + 循环箭头流转 + 金边升华）

## 叙事模板 narrative_template
自我改进循环（intro → 4 节点循环 → 升华金句）
- Phase 1（0-5s）：标题「自我改进循环」+ 副标「方法论的精华」
- Phase 2（5-50s）：循环图 reveal stagger：AI 犯错（蓝）→ 人指出（紫）→ AI 更新 CLAUDE.md（金，强调）→ 下次自动避开（绿）→ 循环箭头闭合
- Phase 3（50-60s）：升华金句「AI 边用边学，规则越用越厚，团队越来越强」

## bg_component
hex_grid

## 文字安全
- 渐变文字两端亮色（#FCD34D/#FBBF24/#60A5FA/#93C5FD/#34D399/#6EE7B7）
- text-shadow alpha ≤0.32
- 文字溢出防御：word-break / overflow-wrap / flex min-width:0
- 多音字：转→进化（避开"转动"歧义，用"进化"）/ 9→九（本段无）
- 禁"第一"用"其一/首"（本段无）
- 创作指令禁泄露
