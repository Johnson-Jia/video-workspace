# E09 why 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 50s
category: tutorial
segment: why

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感）
- 强调色：暖金 #FBBF24/#FCD34D（沉淀三路强调）+ 冷蓝 #60A5FA/#93C5FD（个体脑/团队仓库对比）+ 翠绿 #34D399/#6EE7B7（自我改进）
- 警示色：红 #F87171/#FCA5A5（人员流动能力流失）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（编号）
- 整体调性：沉稳科技 + 对比清晰（个人 vs 团队）

## 情绪曲线 emotion_curve（5 点，对应 0% / 25% / 50% / 75% / 100%）
- 0.40（点题「为什么沉淀」）
- 0.60（痛点「能力长在个体」）
- 0.75（危机「人员流动能力流失」）
- 0.65（转折「阶段六变团队资产」）
- 0.55（沉淀三路收尾）

## 沉浸模式 immersion_mode
data_reveal：双卡对比 + 沉淀三路图标横排

## 叙事模板 narrative_template
为什么沉淀（problem → pain → transition → three paths）
- Step 1（0-10s）：点题「为什么必须沉淀」+ 能力长在个体
- Step 2（10-22s）：痛点——人员流动能力流失
- Step 3（22-32s）：转折——阶段六核心把个人变团队
- Step 4（32-50s）：沉淀三路详解（Skill 复用 / 知识沉淀 / 自我改进）

## 场景规划（visual_phases）

### Phase 1（0-10s）：标题 + 双卡对比开篇
- 视觉：标题「为什么必须沉淀」+ 标签「E09 · 阶段六」
- 双卡对比开篇：左「个人脑」（单人）vs 右「团队仓库」（多人）
- 大字渐变（暖金同色系亮端）+ text-shadow 深蓝 rgba(30,41,59,0.32)

### Phase 2（10-22s）：人员流动能力流失警示
- 视觉：左卡「人走了」红箭头 + 右卡「经验也走了」红色警示
- 红框警示「能力流失」
- fx：fx-aura 静态光晕（红，alpha 0.18）

### Phase 3（22-32s）：阶段六转折
- 视觉：双卡中间出现金色箭头流向 + 「阶段六 · 个人→团队资产」金边胶囊
- 转折亮色（暖金渐变）

### Phase 4（32-50s）：沉淀三路图标横排
- 视觉：三段卡片横排「Skill 复用 / 知识沉淀 / 自我改进」
- 每卡图标 + 标题 + 一句话详解（高频操作做成共享技能 / 规范围避坑写成 AI 自动加载规则 / AI 犯错后自己更新规则）
- data-reveal stagger

## 布局规则（tutorial.md）
- 单 .phase phase-1 tut-scene，多 tut-region data-reveal stagger
- center→space-between（撑满 1920×1080）
- 标题 flex-start 左对齐
- padding-top ≥ 60
- 卡片 flex:1

## 配色规范
- 渐变文字：同色系亮端（暖金 #FBBF24 → #FCD34D / 蓝 #60A5FA → #93C5FD / 绿 #34D399 → #6EE7B7），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32）
- fx 冷色优先（蓝/紫/绿），红色仅警示用 alpha ≤ 0.22

## bg 组件
hex_grid（深蓝底 + 同色系蓝玻璃光晕，已修白端点）— 保留 `<!-- bg-component: hex_grid -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
