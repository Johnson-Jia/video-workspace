# E11 skillvrule 段 · 设计文档（段1 Skill vs Rule）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 50s
category: tutorial
segment: skillvrule

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：暖金 #FBBF24/#FCD34D（skill 按需）+ 冷蓝 #60A5FA/#93C5FD（rule 始终）+ 翠绿 #34D399/#6EE7B7（配合收尾）
- 字体：Inter（大字）/ Noto Sans SC（正文）/ JetBrains Mono（例子 skill/rule 名）
- 整体调性：对比卡 + 双机制（按需 ⚡ vs 始终 🛡）+ 真实例子

## 情绪曲线 emotion_curve（5 点）
- 0.40（开篇：skill 和 rule 区别）
- 0.65（skill 按需调用 ⚡ 机制）
- 0.85（rule 始终生效 🛡 机制）
- 0.80（真实例子：sql-query skill / database rule）
- 0.60（收尾：两者配合 既会干活又守规矩）

## 沉浸模式 immersion_mode
data_reveal：双卡对比（skill ⚡ / rule 🛡）+ 例子 stagger

## 叙事模板 narrative_template
概念对比（definition → mechanism-a → mechanism-b → example → synthesis）
- Step 1（0-10s）：定义 skill（按需）vs rule（始终）
- Step 2（10-25s）：skill 按需调用机制 ⚡ + rule 始终生效机制 🛡 双卡
- Step 3（25-40s）：真实例子（sql-query 是 skill / database 规范是 rule）
- Step 4（40-50s）：两者配合 既会干活又守规矩 收尾

## 场景规划（visual_phases）—— 多 phase

### Phase 1（0-10s）：定义对比
- 阶段标签「E11 · Skill vs Rule」
- 大字「skill 按需 / rule 始终」对比

### Phase 2（10-25s）：双卡机制
- skill 卡 ⚡（按需调用：让它做时才加载）
- rule 卡 🛡（始终生效：不提也每次遵守）

### Phase 3（25-50s）：真实例子 + 配合收尾
- 例子：sql-query skill（你让它查数据时调用）
- 例子：database rule（每次写 SQL 自动按规范）
- 配合收尾：既会干活又守规矩

## 布局规则
- 多 .phase svr-scene
- center→space-between
- padding 64px 110px 80px

## 配色规范
- 渐变文字：同色系亮端（金/蓝/绿），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)，alpha ≤ 0.32
- fx 冷色优先（蓝/金/绿），alpha ≤ 0.22

## bg 组件
diamond_lattice（45° 金色菱形网格 + 中心金辉 + 粒子漂浮，匹配「对比/分工/精致」主题）— 保留 `<!-- bg-component: diamond_lattice -->`

## 禁忌
- 禁划过类 fx
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性
- 禁 opacity 入场
- 禁暗端渐变
- 禁创作指令泄露
- 禁「9」（用「九」）
