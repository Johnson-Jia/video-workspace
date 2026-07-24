# E13 arch 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 55s
category: tutorial
segment: arch

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，架构总览底色）
- 强调色：冷蓝 #60A5FA/#93C5FD（架构文件名 / 树状连接线）+ 翠绿 #34D399/#6EE7B7（每文件一句话作用）+ 紫色 #A78BFA/#C4B5FD（五核心思想收尾）
- 字体：Inter（大字标题 / 文件计数）/ Noto Sans SC（文件名 / 中文说明）/ JetBrains Mono（代码文件名 .py）
- 整体调性：8 文件架构树全景 + 每文件一句话作用 + 五核心思想收尾

## 情绪曲线 emotion_curve（5 点）
- 0.35（架构总览开篇）
- 0.55（registry / assertions 两文件展开）
- 0.68（base_page / runner / handlers 三文件展开）
- 0.80（main / data / site 三文件展开）
- 0.72（收尾：八文件对应五核心思想）

## 沉浸模式 immersion_mode
phase 切换：8 文件架构树分三批展开（纯 GSAP phase 切换，禁 data-reveal）

## 叙事模板 narrative_template
架构总览（panorama → tree-batch-1 → tree-batch-2 → tree-batch-3 → ideas-finale）
- Step 1（0-7s）：架构总览 hero + 8 文件计数
- Step 2（7-21s）：registry / assertions / base_page 三文件（注册中心 + 软断言 + 基类）
- Step 3（21-37s）：runner / handlers / main 三文件（调度器 + 处理器 + 入口）
- Step 4（37-49s）：data / site 两文件 + 八文件架构树完整呈现
- Step 5（49-55s）：八文件对应五核心思想收尾

## 场景规划（visual_phases）—— phase 切换（纯 GSAP，禁 data-reveal）

### Phase 1（0-7s）：架构总览 hero
- 8 文件计数大字 + 标题「框架八个文件全景」
- 架构树根节点（ai-test-frame/）

### Phase 2（7-21s）：核心机制三文件
- registry / assertions / base_page 三文件卡片
- 每文件一句话作用（注册中心 / 软断言 / 基类）

### Phase 3（21-37s）：业务流程三文件
- runner / handlers / main 三文件卡片
- 每文件一句话作用（调度器 / 处理器 / 入口）

### Phase 4（37-49s）：数据被测两文件 + 树完整
- data / site 两文件卡片
- 八文件架构树完整呈现

### Phase 5（49-55s）：五核心思想收尾
- 八文件对应五核心思想（AI 只生成 / 数据代码解耦 / 注册中心 / 软断言 / 变量传递）

## music_mood
低调科技衬底，pastel-soft 系列（plan 已分配 pastel-soft-1.mp3）

## bg_component
hex_grid
