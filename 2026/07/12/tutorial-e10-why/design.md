# E10 why 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 50s
category: tutorial
segment: why

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，度量/数据主题）
- 强调色：暖金 #FBBF24/#FCD34D（Co-authored-by 真实）+ 警示红 #F87171/#FCA5A5（虚高/误标）+ 翠绿 #34D399/#6EE7B7（三层识别真实收尾）+ 冷蓝 #60A5FA/#93C5FD（commit trailer 代码块）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码/数字/commit trailer）
- 整体调性：双卡对比（✗ 只数虚高 vs ✓ 三层真实）+ Copilot 自动加 trailer 机制揭示

## 情绪曲线 emotion_curve（5 点，对应 0% / 25% / 50% / 75% / 100%）
- 0.42（开场：为什么度量难）
- 0.58（Co-authored-by 是什么：commit 署名行）
- 0.82（大坑爆点：Copilot 自动加 trailer，手写被算 AI）
- 0.78（占比虚高警示）
- 0.62（解决方向：识别真 AI vs 误标，更准的算法收尾）

## 沉浸模式 immersion_mode
data_reveal：Co-authored-by 定义 → Copilot 自动加 trailer 大坑 → 双卡对比（虚高 vs 真实）→ 更准的算法收尾

## 叙事模板 narrative_template
问题剖析（提问 → 定义 → 大坑 → 后果 → 解决方向）
- Step 1（0-12s）：为什么度量难 + Co-authored-by 是 commit message 署名行定义
- Step 2（12-28s）：只数它不行 + Copilot 自动加 trailer 机制 + 手写代码被算成 AI
- Step 3（28-40s）：占比虚高警示 + 双卡对比（✗ 虚高 / ✓ 三层识别真实）
- Step 4（40-50s）：必须识别真 AI vs 误标 → 需要更准的算法收尾

## 场景规划（visual_phases）—— 单 phase + data-reveal stagger（绕过 s6_assemble 多 phase 重叠 bug）

### Phase 1（0-50s）：单 phase 内多 region data-reveal 累积
- region-1（data-reveal=0）：阶段标签「E10 · 度量实操 · 为什么度量难」
- region-2（data-reveal=0）：大字提问「为什么度量难」+ Co-authored-by 定义卡（commit message 署名行）
- region-3（data-reveal=2）：Copilot 自动加 trailer 大坑示意（commit trailer 代码块 + 手写代码标签 + 自动加 trailer 箭头）
- region-4（data-reveal=8）：双卡对比（✗ 只数 Co-authored-by 虚高 / ✓ 三层识别真实）
- region-5（data-reveal=14）：必须识别真 AI vs 误标 → 更准的算法收尾带

## 布局规则（tutorial.md）
- 单 .phase phase-1 tut-scene，多 tut-region data-reveal stagger（紧凑 0/2/8/14）
- center→space-between（撑满 1920×1080）
- 标题 flex-start 左对齐
- padding-top ≥ 60
- 卡片 flex:1

## 配色规范
- 渐变文字：同色系亮端（暖金 #FBBF24 → 浅金 #FCD34D / 翠绿 #34D399 → #6EE7B7），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32，禁发光 0 0 Xpx）
- fx 冷色优先（蓝/紫/绿），暖色 alpha ≤ 0.22

## bg 组件
diamond_lattice（45° 金色菱形网格 + 对角漂移 + 中心金辉 + 菱形节点，匹配「度量精确性/真伪辨别」主题，与 hook 的 scan_grid 和 intro 的 hex_grid 区分）— 保留 `<!-- bg-component: diamond_lattice -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline + data-reveal）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
- 禁「数提交」（用「统计」避多音字 shǔ 误读）
- 禁「校验」（用「检查」避多音字 jiào 误读）
