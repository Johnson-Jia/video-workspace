# E12 pptmaster 段 · 设计文档（ppt-master 原生 PPT）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 60s
category: tutorial
segment: pptmaster

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：原生蓝 #60A5FA/#93C5FD（DrawingML 可编辑元素）+ 红警示 #F87171（图片式不能改 ❌）+ 绿勾 #34D399/#6EE7B7（每元素可编辑 ✓）+ 金 #FBBF24/#FCD34D（一万六千星/二十多套 deck）
- 字体：Inter（大字）/ Noto Sans SC（正文）/ JetBrains Mono（DrawingML/Markdown/工作流）
- 整体调性：对比卡（图片式 ❌ vs DrawingML ✓）+ 工作流三步（Markdown → ppt-master skill → PPTX）

## 情绪曲线 emotion_curve（5 点）
- 0.35（PPT 类汇报用 ppt-master 生成原生 PPT 抛出）
- 0.55（关键是 原生 DrawingML 不是图片式）
- 0.72（每元素独立可编辑 PowerPoint 能改）
- 0.85（工作流 Markdown→ppt-master→PPTX）
- 0.78（一万六千星 二十多套 deck 收尾）

## 沉浸模式 immersion_mode
phase 切换：开场（PPT 类汇报用 ppt-master）→ 对比卡（图片式 ❌ vs DrawingML ✓）→ 工作流（Markdown→ppt-master→PPTX）→ 收尾（开源一万六千星/二十多套 deck）

## 叙事模板 narrative_template
对比 + 工作流（intro → compare-image-vs-drawingml → workflow-3steps → stats-finale）
- Step 1（0-9s）：PPT 类汇报用 ppt-master 生成原生可编辑 PPT 开场
- Step 2（9-30s）：对比卡 图片式 PPT 整张图不能改 ❌ / ppt-master DrawingML 每元素可编辑 ✓
- Step 3（30-46s）：工作流 AI 生成 Markdown → Claude Code ppt-master skill → 原生 PPTX
- Step 4（46-60s）：开源一万六千星 二十多套精美 deck 收尾

## 组件
- bg：diamond_lattice（深蓝底菱形网格）
- fx：fx-aura 静态光晕（蓝可编辑+红警示+绿勾）+ fx-particle + fx-blink（禁划过类 scan/stream/beam）
