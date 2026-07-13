# E10 algorithm 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 80s
category: tutorial
segment: algorithm

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，度量/算法分析主题）
- 强调色：暖金 #FBBF24/#FCD34D（① Co-authored-by 初筛）+ 冷蓝 #60A5FA/#93C5FD（② 风格学复核）+ 翠绿 #34D399/#6EE7B7（③ 注册表组合 + 确认 AI 收尾）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码/数字/置信度数值/commit trailer）
- 整体调性：三卡片横排 + 置信度流向 + 一句话核心 + 收口逻辑

## 情绪曲线 emotion_curve（5 点，对应 0% / 25% / 50% / 75% / 100%）
- 0.42（开场：ai-metrics 用三层识别算法）
- 0.65（① Co-authored-by 初筛，置信度一点零）
- 0.78（② 风格学复核，余弦相似度，反伪造核心）
- 0.82（③ 检测器注册表，组合收口）
- 0.60（收尾：粗筛 + 反伪造 + 收口）

## 沉浸模式 immersion_mode
data_reveal：三层算法总标题 → 三卡片横排（① 初筛 / ② 复核 / ③ 注册表）+ 置信度流向 → 收口逻辑带

## 叙事模板 narrative_template
算法分层解析（总览 → ① 初筛 → ② 复核 → ③ 注册表 → 收口）
- Step 1（0-12s）：ai-metrics 用三层识别算法总标题 + 三卡片预告
- Step 2（12-30s）：① Co-authored-by 初筛卡（commit message 含 AI 工具名 → 判 AI，置信度一点零）
- Step 3（30-50s）：② 风格计量学复核卡（余弦相似度 + 像本人降置信度 + 不像确认 AI）
- Step 4（50-65s）：③ 检测器注册表卡（组合前两层 → 最终判定）
- Step 5（65-80s）：三层逻辑收口带（粗筛 + 反伪造 + 收口）

## 场景规划（visual_phases）—— 单 phase + data-reveal stagger（绕过 s6_assemble 多 phase 重叠 bug）

### Phase 1（0-80s）：单 phase 内多 region data-reveal 累积
- region-1（data-reveal=0）：阶段标签「E10 · 度量实操 · 三层识别算法」
- region-2（data-reveal=0）：总标题「ai-metrics 用三层识别算法」+ 三卡片预告横排
- region-3（data-reveal=3）：① Co-authored-by 初筛卡详展（图标 + 一句话 + 置信度一点零 + commit trailer 示例）
- region-4（data-reveal=10）：② 风格学复核卡详展（图标 + 一句话 + 余弦相似度公式 + 像本人/不像对比）
- region-5（data-reveal=18）：③ 注册表组合卡详展（图标 + 一句话 + 组合流向）
- region-6（data-reveal=26）：三层收口逻辑带（粗筛 + 反伪造 + 收口）

## 布局规则（tutorial.md）
- 单 .phase phase-1 tut-scene，多 tut-region data-reveal stagger（紧凑 0/3/10/18/26）
- center→space-between（撑满 1920×1080）
- 标题 flex-start 左对齐
- padding-top ≥ 60
- 卡片 flex:1

## 配色规范
- 渐变文字：同色系亮端（暖金 #FBBF24 → 浅金 #FCD34D / 冷蓝 #60A5FA → #93C5FD / 翠绿 #34D399 → #6EE7B7），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32，禁发光 0 0 Xpx）
- fx 冷色优先（蓝/紫/绿），暖色 alpha ≤ 0.22

## bg 组件
scan_grid（扫描网格 + 双扫描线 + 网格节点闪烁 + HUD 监控角标，匹配「三层算法分析/置信度监控」核心段主题）— 保留 `<!-- bg-component: scan_grid -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）—— scan_grid 自带扫描线属 bg 层动画（不属 fx 层）
- 禁「第一」（用「其一/首/前一层」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline + data-reveal）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
- 禁「数提交」（用「统计」避多音字 shǔ 误读）
- 禁「校验」（用「检查」避多音字 jiào 误读）
