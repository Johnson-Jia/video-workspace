# E12 fivetemplates 段 · 设计文档（5 类模板）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 60s
category: tutorial
segment: fivetemplates

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：暖金 #FBBF24/#FCD34D（战略 PPT/序号）+ 冷蓝 #60A5FA/#93C5FD（计划书/周报）+ 翠绿 #34D399/#6EE7B7（总结/度量）+ 紫 #C4B5FD/#DDD6FE（PPTX 标签）
- 字体：Inter（序号/大字）/ Noto Sans SC（正文）/ JetBrains Mono（输出格式）
- 整体调性：五卡片网格 + 每卡用途 + 输出格式标签

## 情绪曲线 emotion_curve（5 点）
- 0.32（五类总览抛出）
- 0.55（卡 1 战略 PPT + 卡 2 计划书）
- 0.68（卡 3 周报 + 卡 4 总结）
- 0.85（卡 5 度量 + ai-metrics 实测）
- 0.62（收尾：从立项到结项 每一步都有模板）

## 沉浸模式 immersion_mode
phase 切换：五类总览 → 逐卡展开 1-2 → 逐卡展开 3-4 → 卡 5 度量 → 收尾

## 叙事模板 narrative_template
五卡片（overview → card1-2 → card3-4 → card5 → finale）
- Phase 1（0-11s）：五类总览 + 大字「五类汇报模板 覆盖转型全周期」
- Phase 2（11-26s）：卡 1 战略汇报 PPT（向上汇报争取资源 / PPTX）+ 卡 2 转型计划书（立项审批 / 文档）
- Phase 3（26-40s）：卡 3 周报（关键节点跟踪 / 文档）+ 卡 4 阶段总结报告（结项或晋升述职 / 文档）
- Phase 4（40-52s）：卡 5 效果度量报告（数据证明提效 + 接 ai-metrics 实测 / 文档）
- Phase 5（52-60s）：从立项到结项 每一步都有对应模板 收尾

## 场景规划（visual_phases）—— phase 切换（5 phase）

### Phase 1（0-11s）：五类总览
- 大字「五类汇报模板」+ 覆盖转型全周期
- 五卡缩略（序号 + 名称）

### Phase 2（11-26s）：卡 1 + 卡 2 双卡
- 01 战略汇报 PPT（向上汇报争取资源 / PPTX）
- 02 转型计划书（立项审批 / 文档）

### Phase 3（26-40s）：卡 3 + 卡 4 双卡
- 03 周报（关键节点跟踪 / 文档）
- 04 阶段总结报告（结项或晋升述职 / 文档）

### Phase 4（40-52s）：卡 5 度量
- 05 效果度量报告（数据证明提效 + 接 ai-metrics 实测 / 文档）

### Phase 5（52-60s）：收尾
- 从立项到结项 转型每一步都有对应模板

## 布局规则
- 单场景类 fivetemplates-scene，phase-1/2/3/4/5 切换
- 卡片 mech-row justify-content: center
- scene align-items: center

## 配色规范
- 渐变文字同色系亮端（金/蓝/绿/紫，禁白端点/禁暗端）
- text-shadow rgba(30,41,59,0.32)
- fx 冷色优先 alpha ≤ 0.22

## bg 组件
clean_slate（干净石板 + 极简氛围 + 柔和光晕，匹配「模板盘点/清单」主题）— 保留 `<!-- bg-component: clean_slate -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性 / 禁 opacity 入场
- 禁暗端渐变
- 禁创作指令泄露
- 禁「一定」（「不一定」→「未必」）
- 单字「转」（转型义）用「转型」
