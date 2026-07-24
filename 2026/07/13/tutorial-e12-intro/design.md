# E12 intro 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 30s
category: tutorial
segment: intro

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，方法论预告主题）
- 强调色：暖金 #FBBF24/#FCD34D（这集讲什么 大字）+ 冷蓝 #60A5FA/#93C5FD（五件事预告）+ 翠绿 #34D399/#6EE7B7（原生可编辑）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（数据）
- 整体调性：承上启下 + 五件事预告 stagger

## 情绪曲线 emotion_curve（5 点）
- 0.32（承上：前集 Skill 仓库 → 这集汇报材料）
- 0.62（大字「汇报材料实操」）
- 0.78（五件事预告 stagger）
- 0.85（五类模板 + 战略 PPT 两版本核心预告）
- 0.50（收尾：原生可编辑 PPT）

## 沉浸模式 immersion_mode
phase 切换：承上大字「汇报材料实操」+ 五件事预告 stagger

## 叙事模板 narrative_template
方法论预告（recap → title → five-things-preview）
- Step 1（0-11s）：承上「前集 Skill 仓库 → 这集汇报材料」+ 大字「汇报材料实操」
- Step 2（11-30s）：五件事预告 stagger（四步工作流 / 五类模板 / 战略 PPT 两版本 / 五分钟最小可走通 / ppt-master 原生 PPT）+ 原生可编辑收尾

## 场景规划（visual_phases）—— phase 切换

### Phase 1（0-11s）：承上 + 大字
- 承上「前集 Skill 仓库 → 这集汇报材料」
- 大字「汇报材料实操」+ 五个 prompt 包加 ppt-master

### Phase 2（11-30s）：五件事预告 stagger
- 五张卡片（四步工作流 / 五类模板 / 战略 PPT 两版本 / 五分钟最小可走通 / ppt-master 原生 PPT）
- 收尾：原生可编辑 PPT

## 布局规则
- 单场景类 intro-scene，phase-1/phase-2 切换
- center→space-between
- scene align-items: center（禁 stretch）
- mech-row/preview-row justify-content: center

## 配色规范
- 渐变文字同色系亮端（禁白端点 / 禁暗端）
- text-shadow rgba(30,41,59,0.32)
- fx 冷色优先 alpha ≤ 0.22

## bg 组件
hex_grid（六边形网格 + 节点闪烁 + 科技结构感，匹配「方法论预告/结构化」主题）— 保留 `<!-- bg-component: hex_grid -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性 / 禁 opacity 入场
- 禁暗端渐变
- 禁创作指令泄露
- 禁「一定」（「不一定」→「未必」）
