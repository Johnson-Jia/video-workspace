# E11 fourskill 段 · 设计文档（段3 4 核心 skill，核心段）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 70s
category: tutorial
segment: fourskill

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：金 #FBBF24/#FCD34D（编排型 devflow）+ 蓝 #60A5FA/#93C5FD（工具型 sql-query）+ 翠绿 #34D399/#6EE7B7（工具型 crud-gen）+ 紫 #A78BFA/#C4B5FD（编排型 code-review）
- 字体：Inter（大字）/ Noto Sans SC（正文）/ JetBrains Mono（skill 名/类型）
- 整体调性：四卡片网格 + 每卡类型标签 + 一句话定位

## 情绪曲线 emotion_curve（5 点）
- 0.45（开篇：七个挑四个核心）
- 0.70（devflow 编排型：六阶段流水线）
- 0.80（sql-query 工具型：只读查询+安全护栏）
- 0.78（crud-gen 工具型：自动生成 CRUD）
- 0.62（code-review 编排型 + 三类覆盖收尾）

## 沉浸模式 immersion_mode
data_reveal：四卡片网格 stagger（devflow → sql-query → crud-gen → code-review）

## 叙事模板 narrative_template
核心枚举（overview → skill-1 → skill-2 → skill-3 → skill-4 → synthesis）
- Step 1（0-10s）：仓库七个 skill 挑四个核心 + 概览
- Step 2（10-25s）：devflow 编排型（六阶段流水线）
- Step 3（25-40s）：sql-query 工具型（PostgreSQL 只读+三模式+护栏）
- Step 4（40-55s）：crud-gen 工具型（读表→分层生成）
- Step 5（55-70s）：code-review 编排型（三级分级）+ 三类覆盖收尾

## 场景规划（visual_phases）—— 多 phase

### Phase 1（0-10s）：概览 + 七挑四
- 阶段标签「E11 · 4 核心 skill · 核心段」
- 大字「七个 skill 挑四个核心」
- 四卡缩略

### Phase 2（10-25s）：devflow 编排型
- 卡 1（金）：devflow / 编排型
- 一句话：需求到交付串成六阶段流水线

### Phase 3（25-40s）：sql-query 工具型
- 卡 2（蓝）：sql-query / 工具型
- 一句话：PostgreSQL 只读查询 三模式加安全护栏

### Phase 4（40-55s）：crud-gen 工具型
- 卡 3（翠绿）：crud-gen / 工具型
- 一句话：读表结构自动生成增删改查代码

### Phase 5（55-70s）：code-review 编排型 + 收尾
- 卡 4（紫）：code-review / 编排型
- 一句话：AI 代码审查加三级分级
- 收尾：编排 工具 审查 三类覆盖

## 布局规则
- 多 .phase fourskill-scene
- center→space-between
- padding 64px 110px 80px

## 配色规范
- 渐变文字：同色系亮端（金/蓝/绿/紫），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)，alpha ≤ 0.32
- fx 低 alpha 冷暖搭配，alpha ≤ 0.22

## bg 组件
hex_grid（深蓝底 + 蜂巢网格 + 玻璃光斑，匹配「网格/枚举/覆盖」主题）— 保留 `<!-- bg-component: hex_grid -->`
注：hex_grid 自带蜂巢网格属 bg 层；fx 层禁划过类

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性
- 禁 opacity 入场
- 禁暗端渐变（#6D28D9/#B8842B/#1E6FB8/#DC2626）
- 禁创作指令泄露
- 禁「9」（用「九」）
