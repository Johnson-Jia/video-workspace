# E12 hook 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 30s
category: tutorial
segment: hook

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，汇报材料/向上汇报主题）
- 强调色：暖金 #FBBF24/#FCD34D（5 类汇报 prompt 数字锚点）+ 冷蓝 #60A5FA/#93C5FD（ppt-master 原生可编辑）+ 翠绿 #34D399/#6EE7B7（三十秒出活）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（PPTX/目录）
- 整体调性：沉稳汇报 + 三十秒出原生可编辑 PPT 冲击

## 情绪曲线 emotion_curve（5 点，对应 0% / 25% / 50% / 75% / 100%）
- 0.32（开场：5 类汇报 prompt + ppt-master 概念抛出）
- 0.70（原生可编辑机制揭示：每个文本框都能改）
- 0.85（核心爆点：三十秒出活）
- 0.62（落地：转型最大卖点是向上汇报要资源）
- 0.50（收尾定调：prompt 包加渲染工具）

## 沉浸模式 immersion_mode
phase 切换：大字「5 类汇报 prompt」+「ppt-master 原生 PPT」+ 三十秒出活 + 向上汇报要资源

## 叙事模板 narrative_template
汇报即用开篇（asset → editable → thirty-sec → report-up）
- Step 1（0-13s）：大字「5 类汇报 prompt」+ ppt-master 原生可编辑 PPT 标签 + 每个文本框都能改
- Step 2（13-30s）：三十秒出活胶囊 + 转型最大卖点向上汇报要资源 + prompt 包加渲染工具收尾

## 场景规划（visual_phases）—— phase 切换（单场景类，phase-1/phase-2 依次显示，绕过 s6_assemble 多 phase 重叠 bug）

### Phase 1（0-13s）：大字 + 原生可编辑机制
- 大字「5 类」+ 汇报 prompt 标签
- ppt-master 原生可编辑 PPT 胶囊（DrawingML，每个文本框都能改）

### Phase 2（13-30s）：三十秒出活 + 向上汇报要资源
- 三十秒出活翠绿胶囊
- 转型最大卖点：向上汇报要资源（你的成果得变成上级看得懂的 PPT 和报告）
- prompt 包加渲染工具 收尾

## 布局规则（tutorial.md）
- 单场景类 hook-scene，phase-1/phase-2 切换（一次显示一个 phase）
- center→space-between（撑满 1920×1080）
- .hook-scene flex-start（内容从顶排列，padding-top 188）
- .region flex-shrink:0（不压缩）

## 配色规范
- 渐变文字：同色系亮端（暖金 #FBBF24 → 浅金 #FCD34D / 冷蓝 #60A5FA → #93C5FD / 翠绿 #34D399 → #6EE7B7），禁白端点 / 禁暗端（#B8842B/#1E6FB8/#DC2626）
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32，禁发光 0 0 Xpx）
- fx 冷色优先（蓝/金/绿），alpha ≤ 0.22

## bg 组件
gradient_mesh（渐变网格 + 流动光斑 + 柔和氛围，匹配「汇报材料/战略叙事」主题）— 保留 `<!-- bg-component: gradient_mesh -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline + phase 切换）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
- 禁「一定」（「不一定」→「未必」）
