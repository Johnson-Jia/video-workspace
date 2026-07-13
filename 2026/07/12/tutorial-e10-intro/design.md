# E10 intro 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 30s
category: tutorial
segment: intro

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，度量/数据主题）
- 强调色：暖金 #FBBF24/#FCD34D（AI 占比强调）+ 冷蓝 #60A5FA/#93C5FD（提效同比）+ 翠绿 #34D399/#6EE7B7（HTML 报告收尾）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码/数字/数据高亮）
- 整体调性：方法论预告 + 度量三步清晰可读

## 情绪曲线 emotion_curve（5 点，对应 0% / 25% / 50% / 75% / 100%）
- 0.40（开场承上：前集讲推广度量，数据证明有效）
- 0.62（钩起疑问：那个数据怎么来的）
- 0.78（这集讲什么：手把手跑 ai-metrics）
- 0.85（三步预告高潮：挡误标 / 反伪造 / 一条命令出占比）
- 0.55（收尾：换成你自己的数据）

## 沉浸模式 immersion_mode
data_reveal：度量三步预告（AI 占比 / 提效同比 / HTML 报告）stagger 累积显现

## 叙事模板 narrative_template
方法论预告（承上 → 这集讲什么 → 三步预告 → 换数据收尾）
- Step 1（0-7s）：承上 + 钩起疑问「数据怎么来的」
- Step 2（7-15s）：这集讲度量实操，手把手跑 ai-metrics
- Step 3（15-23s）：度量三步预告 stagger（挡误标 / 反伪造 / 一条命令出占比）
- Step 4（23-30s）：换成你自己的数据收尾

## 场景规划（visual_phases）—— 单 phase + data-reveal stagger（绕过 s6_assemble 多 phase 重叠 bug）

### Phase 1（0-30s）：单 phase 内多 region data-reveal 累积
- region-1（data-reveal=0）：阶段标签「E10 · 度量实操 · intro」
- region-2（data-reveal=0）：承上钩起「数据怎么来的」+ 大字「这集讲度量实操」
- region-3（data-reveal=2）：手把手跑 ai-metrics 副标题
- region-4（data-reveal=6）：度量三步预告三卡（① AI 占比 / ② 提效同比 / ③ HTML 报告）
- region-5（data-reveal=12）：一条命令跑出 + 换成你自己的数据收尾带

## 布局规则（tutorial.md）
- 单 .phase phase-1 tut-scene，多 tut-region data-reveal stagger（紧凑 0/2/6/12）
- center→space-between（撑满 1920×1080）
- 标题 flex-start 左对齐
- padding-top ≥ 60
- 卡片 flex:1

## 配色规范
- 渐变文字：同色系亮端（暖金 #FBBF24 → 浅金 #FCD34D / 冷蓝 #60A5FA → #93C5FD / 翠绿 #34D399 → #6EE7B7），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32，禁发光 0 0 Xpx）
- fx 冷色优先（蓝/紫/绿），alpha ≤ 0.22

## bg 组件
hex_grid（六边形网格 + 节点连线 + 微光流动，匹配「数据度量/网格化指标」主题，与 hook 的 scan_grid 区分）— 保留 `<!-- bg-component: hex_grid -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首/前集」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline + data-reveal）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
- 禁「数提交」（用「统计」避多音字 shǔ 误读）
- 禁「校验」（用「检查」避多音字 jiào 误读）
