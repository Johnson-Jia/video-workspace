# E09 hook 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 30s
category: tutorial
segment: hook

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感）
- 强调色：暖金 #FBBF24/#FCD34D（9 个月反差强调，同色系亮端）+ 冷蓝 #60A5FA/#93C5FD（SFTP 任务绿）+ 警示红 #F87171/#FCA5A5（挂掉反差）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码/数字）
- 整体调性：沉稳科技 + 反差冲击（绿成功 vs 红挂掉）

## 情绪曲线 emotion_curve（5 点，对应 0% / 25% / 50% / 75% / 100%）
- 0.30（开场承接）
- 0.65（抛出「静默九个月」反差钩子）
- 0.80（揭示「自报成功」陷阱）
- 0.60（转向「永远不再发生」解决）
- 0.50（预告本集，收尾定调）

## 沉浸模式 immersion_mode
data_reveal：大字「静默 9 个月」+ SFTP 报绿/挂红反差揭示 + 三段胶囊预告

## 叙事模板 narrative_template
反常识开篇（problem → trap → resolution preview）
- Step 1（0-7s）：大字「静默 9 个月」+ 反差钩子
- Step 2（7-15s）：SFTP 任务报绿但实际挂掉揭示
- Step 3（15-23s）：「自报成功」陷阱
- Step 4（23-30s）：预告七种 Skill 范式 + 自我改进循环

## 场景规划（visual_phases）

### Phase 1（0-7s）：大字「静默 9 个月」反差
- 视觉：深蓝底渐入，大字「静默 9 个月」暖金渐变浮现（同色系亮端，禁白端点 / 禁暗端 #B8842B）
- fx：fx-aura 静态光晕（冷色蓝紫，alpha 0.18-0.22）
- 文字特效：渐变（暖金→深金，同色系亮端）+ text-shadow 深蓝 rgba(30,41,59,0.32)（非黑，禁发光 0 0 Xpx）

### Phase 2（7-15s）：SFTP 任务报绿/挂红反差
- 视觉：SFTP 任务卡（绿色✓成功图标）但右侧挂红色警示框（实际挂掉）
- 任务状态条：绿色 100% 成功 vs 红色「实际未推送」反差
- fx：fx-blink 锚点脉冲（冷色蓝）

### Phase 3（15-23s）：自报成功陷阱
- 视觉：catch 吞异常代码 trailer + 无条件 handleSuccess 调用
- 红框警示「任务自报成功」
- fx：fx-aura 静态光晕（红，alpha 0.18）

### Phase 4（23-30s）：本集预告
- 视觉：三段胶囊横排「七种 Skill 范式 / 自我改进循环 / 团队规范自动进化」
- 底部「让 AI 犯过的错自动变成团队规范」收尾
- data-reveal stagger 入场

## 布局规则（tutorial.md）
- 单 .phase phase-1 tut-scene，多 tut-region data-reveal stagger
- center→space-between（撑满 1920×1080）
- 标题 flex-start 左对齐
- padding-top ≥ 60
- 卡片 flex:1

## 配色规范
- 渐变文字：同色系亮端（暖金 #FBBF24 → 浅金 #FCD34D），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32，禁发光 0 0 Xpx）
- fx 冷色优先（蓝/紫/绿），alpha ≤ 0.22

## bg 组件
hex_grid（深蓝底 + 同色系蓝玻璃光晕，已修白端点）— 保留 `<!-- bg-component: hex_grid -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
