# E12 workflow 段 · 设计文档（4 步工作流）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 55s
category: tutorial
segment: workflow

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：暖金 #FBBF24/#FCD34D（步骤序号 01-04）+ 冷蓝 #60A5FA/#93C5FD（准备数据/复制 prompt）+ 翠绿 #34D399/#6EE7B7（发给 AI/渲染）+ 紫 #C4B5FD/#DDD6FE（ppt-master）
- 字体：Inter（大字/序号）/ Noto Sans SC（正文）/ JetBrains Mono（数据/prompt）
- 整体调性：四步横向流程图 + 每步图标 + 一句话

## 情绪曲线 emotion_curve（5 点）
- 0.32（四步总览抛出）
- 0.55（step 1 准备数据）
- 0.68（step 2 复制 prompt）
- 0.82（step 3 发给 AI + step 4 渲染）
- 0.85（收尾：一份完整汇报出炉）

## 沉浸模式 immersion_mode
phase 切换：四步总览 → 逐步展开 step1-2 → 逐步展开 step3-4 → 收尾出炉

## 叙事模板 narrative_template
四步工作流（overview → step1-2 → step3-4 → finale）
- Step 1（0-13s）：四步总览（准备数据→复制prompt→发AI→渲染）横向流水线
- Step 2（13-33s）：step1 准备数据 + step2 复制 prompt 双卡详情
- Step 3（33-48s）：step3 发给 AI（任意 AI）+ step4 渲染（ppt-master 原生 PPTX）双卡详情
- Step 4（48-55s）：四步走完 一份完整汇报出炉 收尾

## 场景规划（visual_phases）—— phase 切换（4 phase，每 phase 一个完整状态）

### Phase 1（0-13s）：四步总览横向流水线
- 大字「汇报材料生成四步」
- 四节点横向流程（01 准备数据 → 02 复制 prompt → 03 发给 AI → 04 渲染）

### Phase 2（13-33s）：step1 + step2 双卡详情
- step1 准备数据（产出 / AI 占比 / Bug / 进展）
- step2 复制 prompt（打开对应模板 + 填进数据）

### Phase 3（33-48s）：step3 + step4 双卡详情
- step3 发给 AI（任意 AI：Claude / ChatGPT / GLM → Markdown）
- step4 渲染（PPT 类用 ppt-master 原生 PPTX / 文档类导成 PDF）

### Phase 4（48-55s）：出炉收尾
- 四步走完 → 一份完整汇报出炉

## 布局规则
- 单场景类 workflow-scene，phase-1/2/3/4 切换
- 流程节点 justify-content: center + flex:1 撑满
- mech-row/双卡 justify-content: center
- scene align-items: center

## 配色规范
- 渐变文字同色系亮端（金/蓝/绿/紫，禁白端点/禁暗端）
- text-shadow rgba(30,41,59,0.32)
- fx 冷色优先 alpha ≤ 0.22

## bg 组件
diamond_lattice（菱形格 + 结构感 + 几何秩序，匹配「工作流/步骤化」主题）— 保留 `<!-- bg-component: diamond_lattice -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性 / 禁 opacity 入场
- 禁暗端渐变
- 禁创作指令泄露
- 禁「一定」（「不一定」→「未必」）
- 单字「转」（转型义）用「转型」；「转 PDF」用「导成 PDF」
