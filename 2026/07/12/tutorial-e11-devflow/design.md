# E11 devflow 段 · 设计文档（段4 devflow 编排型，核心段）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 60s
category: tutorial
segment: devflow

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：金 #FBBF24/#FCD34D（编排型主线 + 断点续传）+ 蓝 #60A5FA/#93C5FD（OpenSpec/Superpowers 调用）+ 翠绿 #34D399/#6EE7B7（规则覆盖）+ 紫 #A78BFA/#C4B5FD（归档/收尾）
- 字体：Inter（大字）/ Noto Sans SC（正文）/ JetBrains Mono（阶段名/skill 名）
- 整体调性：六阶段横向流水线 + SVG 连线 + 每阶段调用 skill + 断点续传/规则覆盖标签

## 情绪曲线 emotion_curve（5 点）
- 0.45（开篇：devflow 编排型 自己不实现）
- 0.65（探索+规范：调 OpenSpec）
- 0.80（计划+TDD：调 Superpowers）
- 0.78（验证+归档：规则覆盖）
- 0.62（收尾：规范驱动开发变成默认工作流）

## 沉浸模式 immersion_mode
data_reveal：六阶段流水线 stagger（探索 → 规范 → 计划 → TDD → 验证 → 归档）

## 叙事模板 narrative_template
流程展开（overview → phases-1-2 → phases-3-4 → phases-5-6 → synthesis）
- Step 1（0-10s）：devflow 编排型定位 + 六阶段流水线总览
- Step 2（10-25s）：探索 + 规范（调 OpenSpec）+ 计划 + TDD（调 Superpowers）
- Step 3（25-40s）：验证 + 归档 + 断点续传 + 规则覆盖
- Step 4（40-60s）：规范驱动开发变成默认工作流 收尾

## 场景规划（visual_phases）—— 多 phase

### Phase 1（0-10s）：devflow 定位 + 六阶段总览
- 阶段标签「E11 · devflow 编排型 · 核心段」
- 大字「devflow 六阶段流水线」
- 六节点缩略横向连线

### Phase 2（10-25s）：探索 + 规范 + 计划 + TDD（前四阶段）
- 四阶段卡 + 每阶段调用 skill
- 规范阶段调 OpenSpec / 计划阶段调 Superpowers

### Phase 3（25-40s）：验证 + 归档 + 断点续传 + 规则覆盖
- 验证归档卡 + 断点续传标签 + 规则覆盖标签

### Phase 4（40-60s）：规范驱动开发变成默认工作流 收尾
- 大字收尾「规范驱动开发 从口号变成 默认工作流」

## 布局规则
- 多 .phase devflow-scene
- center→space-between
- padding 64px 110px 80px

## 配色规范
- 渐变文字：同色系亮端（金/蓝/绿/紫），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)，alpha ≤ 0.32
- fx 低 alpha 冷暖搭配，alpha ≤ 0.22

## bg 组件
scan_grid（深蓝底 + 扫描网格 + 数据流节点，匹配「流水线/编排/数据流」主题）— 保留 `<!-- bg-component: scan_grid -->`
注：scan_grid 自带扫描网格属 bg 层；fx 层禁划过类

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性
- 禁 opacity 入场
- 禁暗端渐变（#6D28D9/#B8842B/#1E6FB8/#DC2626）
- 禁创作指令泄露
- 禁「9」（用「九」）
