# E11 triad 段 · 设计文档（段2 三件套结构，核心段）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 55s
category: tutorial
segment: triad

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：暖金 #FBBF24/#FCD34D（SKILL.md 入口）+ 冷蓝 #60A5FA/#93C5FD（reference/scripts 按需）+ 紫 #A78BFA/#C4B5FD（rules 覆盖）+ 翠绿 #34D399/#6EE7B7（收尾）
- 字体：Inter（大字）/ Noto Sans SC（正文）/ JetBrains Mono（文件名/目录）
- 整体调性：三层结构图（入口 → 按需 → 覆盖）+ 每层一句话

## 情绪曲线 emotion_curve（5 点）
- 0.40（开篇：三件套结构概览）
- 0.65（入口 SKILL.md：声明干什么/触发/调用）
- 0.85（按需 reference/scripts：省上下文）
- 0.80（rules 覆盖：改写默认行为）
- 0.60（收尾：自包含 可复用 不臃肿）

## 沉浸模式 immersion_mode
data_reveal：三层结构图 stagger（SKILL.md → reference/scripts → rules）

## 叙事模板 narrative_template
结构展开（overview → layer-1-entry → layer-2-on-demand → layer-3-override → synthesis）
- Step 1（0-8s）：三件套结构概览 + 入口 SKILL.md
- Step 2（8-25s）：入口 SKILL.md 详解（干什么/触发/调用）
- Step 3（25-40s）：第二层 reference/scripts 按需加载（省上下文）
- Step 4（40-50s）：第三层 rules 覆盖（改写默认行为）
- Step 5（50-55s）：自包含 可复用 不臃肿 收尾

## 场景规划（visual_phases）—— 多 phase

### Phase 1（0-8s）：结构概览 + 三件套总览
- 阶段标签「E11 · 三件套结构」
- 大字「一个 skill 的三件套」
- 三层缩略（SKILL.md / reference / rules）

### Phase 2（8-25s）：入口 SKILL.md 详解
- 第 1 层卡（金）：SKILL.md 入口
- 三个要点：干什么 / 怎么触发 / 调用什么

### Phase 3（25-40s）：第二层 reference/scripts 按需
- 第 2 层卡（蓝）：reference / scripts
- 按需加载 + 骨架 vs 细节 + 省上下文

### Phase 4（40-55s）：第三层 rules 覆盖 + 收尾
- 第 3 层卡（紫）：rules 覆盖
- 可选 + 改写默认行为 + 适配团队规矩
- 收尾：自包含 可复用 不臃肿

## 布局规则
- 多 .phase triad-scene
- center→space-between
- padding 64px 110px 80px

## 配色规范
- 渐变文字：同色系亮端（金/蓝/紫/绿），禁白端点 / 禁暗端
- 紫色用亮端 #A78BFA/#C4B5FD（非暗端 #6D28D9）
- text-shadow：深蓝 rgba(30,41,59,0.32)，alpha ≤ 0.32
- fx 冷色优先（蓝/紫/金/绿），alpha ≤ 0.22

## bg 组件
dark_cipher（深靛紫底 + 监控扫描 + 心跳脉冲 + 粒子，匹配「结构/层次/解构」主题）— 保留 `<!-- bg-component: dark_cipher -->`
注：dark_cipher 自带红裂缝/扫描线属 bg 层，不属 fx 层；fx 层禁划过类

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首/入口」）
- 禁 CSS class 切换可见性
- 禁 opacity 入场
- 禁暗端渐变（#6D28D9/#B8842B/#1E6FB8/#DC2626）
- 禁创作指令泄露
- 禁「9」（用「九」）
