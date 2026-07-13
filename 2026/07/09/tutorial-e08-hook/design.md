# E08 hook 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 35s
category: tutorial
segment: hook

## 视觉风格
- 主色：深蓝底 #0B1F3A（夜空科技感）
- 强调色：青蓝 #38BDF8（数据冷色）+ 暖金 #F5C26B（76.6% 反差强调）
- 字体：Ma Shan Zheng（大字标题）/ 思源黑体（正文）/ JetBrains Mono（代码 trailer）
- 整体调性：沉稳科技 + 反差冲击

## 情绪曲线 emotion_curve（6 点，对应 0% / 20% / 40% / 60% / 80% / 100%）
- 0.30（开场承接，平稳）
- 0.55（抛出 76.6% 反差问题）
- 0.70（揭示 Copilot 误标陷阱，悬念上升）
- 0.85（虚高占比的危机感峰值）
- 0.65（预告三层识别，转向解决）
- 0.50（收尾定调，引出本集）

## 沉浸模式 immersion_mode
data_reveal：关键数字（76.6%）+ trailer 文本逐字浮现 + 误标动画分层揭示

## 叙事模板 narrative_template
反常识开篇（problem → misconception → reveal → resolution preview）
- Step 1（0-6s）：承接上集 + 抛出反差数字「76.6% 怎么算」
- Step 2（6-15s）：常见误解——光数 Co-authored-by trailer
- Step 3（15-25s）：揭示陷阱——VS Code Copilot 误标手写代码
- Step 4（25-35s）：预告三层识别算法，算真实占比

## 场景规划（visual_phases）

### Phase 1（0-6s）：承接 + 反差数字
- 视觉：深蓝底渐入，大字「76.6% 怎么算」金边渐变浮现
- fx：fx-aura 静态光晕（蓝紫，alpha 0.18）
- 文字特效：渐变（暖金→深金，同色系禁白端点）+ text-shadow 深蓝 rgba(30,41,59,0.6)

### Phase 2（6-15s）：Co-authored-by trailer 浮现
- 视觉：右侧终端窗口（深底 #0a0a0a + 红黄绿圆点）浮现 commit message
- Co-authored-by trailer 金色高亮逐字打字
- 左侧文字「光数 trailer 够吗？」疑问句

### Phase 3（15-25s）：VS Code Copilot 误标动画
- 视觉：手写代码行被自动打上 Co-authored-by trailer（红色警示标记）
- 「误标」红框警示 + 占比虚高柱状条扭曲上升
- fx：fx-pulse-ring 脉冲（冷色蓝，alpha 0.20）

### Phase 4（25-35s）：三层识别预告
- 视觉：三段胶囊横排「首层 Co-authored-by / 第二层 风格学 / 第三层 注册表」
- 底部「算真实 AI 代码占比」收尾
- data-reveal stagger 入场

## 布局规则（tutorial.md）
- center→space-between（撑满 1920×1080）
- 标题 flex-start 左对齐
- padding-top ≥ 60
- 卡片 flex:1

## 配色规范
- 渐变文字：同色系（暖金 #F5C26B → 深金 #B8842B），禁白端点
- text-shadow：深蓝 rgba(30,41,59,0.6)（非黑，禁发光 0 0 Xpx）
- fx 冷色优先（蓝/紫/绿），alpha ≤ 0.22

## bg 组件
hex_grid（深蓝底 + 同色系蓝玻璃光晕，已修白端点）— 保留 `<!-- bg-component: hex_grid -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「首层」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline）
