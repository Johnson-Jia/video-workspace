# E10 hook 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 30s
category: tutorial
segment: hook

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，度量/数据主题）
- 强调色：暖金 #FBBF24/#FCD34D（占比强调）+ 冷蓝 #60A5FA/#93C5FD（三层识别）+ 警示红 #F87171/#FCA5A5（误标 AI）+ 翠绿 #34D399/#6EE7B7（真实度量收尾）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码/数字/commit trailer）
- 整体调性：沉稳科技 + 反常识冲击（Co-authored-by 虚高误标 vs 三层识别真实）

## 情绪曲线 emotion_curve（5 点，对应 0% / 25% / 50% / 75% / 100%）
- 0.32（开场提问：AI 占比怎么算）
- 0.70（揭示「只数 Co-authored-by」本能）
- 0.85（大坑爆点：Copilot 自动加 trailer，手写被误标 AI）
- 0.62（解决预告：三层识别 + 风格学反伪造）
- 0.50（收尾定调：把 AI 占比真实算出来）

## 沉浸模式 immersion_mode
data_reveal：大字「Co-authored-by 不够」+ Copilot 误标动画（手写代码 trailer 红✗）+ 三层识别预告 stagger

## 叙事模板 narrative_template
反常识开篇（question → misconception → pitfall → resolution preview）
- Step 1（0-7s）：提问「AI 代码占比怎么算」+ 大字「Co-authored-by 不够」浮现
- Step 2（7-15s）：本能解法「数 Co-authored-by」+ Copilot 自动加 trailer 动画揭示
- Step 3（15-23s）：大坑爆点：手写代码被误标成 AI 红✗，占比虚高警示
- Step 4（23-30s）：三层识别算法 + 风格学反伪造预告收尾

## 场景规划（visual_phases）—— 单 phase + data-reveal stagger（绕过 s6_assemble 多 phase 重叠 bug）

### Phase 1（0-30s）：单 phase 内多 region data-reveal 累积
- region-1（data-reveal=0）：阶段标签「E10 · 度量实操」
- region-2（data-reveal=0）：大字提问「AI 代码占比怎么算」
- region-3（data-reveal=2）：大字答案「Co-authored-by 不够」（暖金渐变，同色系亮端）
- region-4（data-reveal=6）：Copilot 自动加 trailer 动画（commit trailer 代码块 + 手写代码标签 + 红✗ 误标警示）
- region-5（data-reveal=12）：占比虚高警示带（虚高箭头 + 红色警示）
- region-6（data-reveal=18）：三层识别算法 + 风格学反伪造 三段胶囊预告收尾

## 布局规则（tutorial.md）
- 单 .phase phase-1 tut-scene，多 tut-region data-reveal stagger（紧凑 0/2/6/12/18）
- center→space-between（撑满 1920×1080）
- 标题 flex-start 左对齐
- padding-top ≥ 60
- 卡片 flex:1

## 配色规范
- 渐变文字：同色系亮端（暖金 #FBBF24 → 浅金 #FCD34D），禁白端点 / 禁暗端（#B8842B/#1E6FB8/#DC2626）
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32，禁发光 0 0 Xpx）
- fx 冷色优先（蓝/紫/绿），alpha ≤ 0.22

## bg 组件
scan_grid（扫描网格 + 双扫描线 + 节点闪烁 + HUD 监控角标，匹配「度量/数据监控」主题）— 保留 `<!-- bg-component: scan_grid -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）—— scan_grid 自带扫描线属 bg 层动画（不属 fx 层）
- 禁「第一」（用「其一/首/反应」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline + data-reveal）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
- 禁「数提交」（用「统计」避多音字 shǔ 误读）
- 禁「第一」（用「反应/其一」避 no_forbidden_speech 子串误报）
