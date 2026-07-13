# E11 hook 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 30s
category: tutorial
segment: hook

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，Skill 仓库/资产沉淀主题）
- 强调色：暖金 #FBBF24/#FCD34D（4 skill 数字锚点）+ 冷蓝 #60A5FA/#93C5FD（13 规范）+ 翠绿 #34D399/#6EE7B7（复制即用）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（目录树/路径）
- 整体调性：沉稳科技 + 资产即用冲击（4 skill + 13 rule 复制到 .claude 就跑）

## 情绪曲线 emotion_curve（5 点，对应 0% / 25% / 50% / 75% / 100%）
- 0.32（开场：4 skill + 13 规范 概念抛出）
- 0.70（skill 按需 / rule 始终 分工揭示）
- 0.85（核心爆点：复制到自己项目就能跑）
- 0.62（落地预告：七种范式 → 一组拿来即用资产）
- 0.50（收尾定调：整个仓库开源）

## 沉浸模式 immersion_mode
data_reveal：大字「4 skill + 13 规范」+ 「复制即用」+ .claude/ 目录树生长

## 叙事模板 narrative_template
资产即用开篇（asset → mechanism → copy-run → open-source preview）
- Step 1（0-7s）：大字「4 skill + 13 规范」浮现 + 复制即用 标签
- Step 2（7-15s）：skill 按需调用 ⚡ / rule 始终生效 🛡 双卡机制揭示
- Step 3（15-23s）：复制到 .claude 目录树生长 + 「就能跑」收尾
- Step 4（23-30s）：E09 七种范式 → 一组资产 + 整个仓库开源 预告

## 场景规划（visual_phases）—— 单 phase + data-reveal stagger（绕过 s6_assemble 多 phase 重叠 bug）

### Phase 1（0-30s）：单 phase 内多 region data-reveal 累积
- region-1（data-reveal=0）：阶段标签「E11 · Skill 仓库实操」
- region-2（data-reveal=0）：大字「4 skill + 13 规范」（暖金渐变 4 + 冷蓝渐变 13）
- region-3（data-reveal=2）：「复制即用」翠绿胶囊
- region-4（data-reveal=6）：双卡机制（skill 按需调用 ⚡ / rule 始终生效 🛡）
- region-5（data-reveal=12）：.claude/ 目录树生长（skills/ + rules/）
- region-6（data-reveal=18）：E09 七种范式 → 一组资产 + 「整个仓库开源」收尾

## 布局规则（tutorial.md）
- 单 .phase phase-1 tut-scene，多 tut-region data-reveal stagger（紧凑 0/2/6/12/18）
- center→space-between（撑满 1920×1080）
- .phase.tut-scene flex-start（内容从顶排列，padding-top 188）
- .region flex-shrink:0（不压缩）

## 配色规范
- 渐变文字：同色系亮端（暖金 #FBBF24 → 浅金 #FCD34D / 冷蓝 #60A5FA → #93C5FD / 翠绿 #34D399 → #6EE7B7），禁白端点 / 禁暗端（#B8842B/#1E6FB8/#DC2626）
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32，禁发光 0 0 Xpx）
- fx 冷色优先（蓝/金/绿），alpha ≤ 0.22

## bg 组件
scan_grid（扫描网格 + 双扫描线 + 节点闪烁 + HUD 监控角标，匹配「Skill 仓库/资产盘点」主题）— 保留 `<!-- bg-component: scan_grid -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）—— scan_grid 自带扫描线属 bg 层动画（不属 fx 层）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline + data-reveal）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
- 禁「9」（用「九」避多音字误读）
