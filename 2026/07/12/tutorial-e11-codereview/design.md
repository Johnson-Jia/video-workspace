# E11 codereview 段 · 设计文档（段6 code-review，核心段）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 50s
category: tutorial
segment: codereview

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：红 #F87171/#FCA5A5（红色必须改）+ 黄 #FBBF24/#FCD34D（黄色建议改）+ 绿 #34D399/#6EE7B7（绿色通过）+ 紫 #A78BFA/#C4B5FD（编排型 code-review + 自动套规范）+ 蓝 #60A5FA/#93C5FD（database/error-handling rule）
- 字体：Inter（大字）/ Noto Sans SC（正文）/ JetBrains Mono（skill 名/rule 名/报告行）
- 整体调性：三级分级卡（红黄绿）+ rule 核对流向 + 报告示例

## 情绪曲线 emotion_curve（5 点）
- 0.45（开篇：编排型审查 skill）
- 0.70（三级分级：红必须改/黄建议改/绿通过）
- 0.82（自动核对 rule：database / error-handling）
- 0.78（不用人对照检查清单）
- 0.62（结构化报告 收尾）

## 沉浸模式 immersion_mode
data_reveal：三级分级卡 stagger（红 → 黄 → 绿）+ rule 核对流向

## 叙事模板 narrative_template
审查展开（overview → triage → rule-check → no-checklist → synthesis）
- Step 1（0-10s）：code-review 编排型审查 skill + 三级分级总览
- Step 2（10-25s）：三级分级卡（红必须改 / 黄建议改 / 绿通过）
- Step 3（25-38s）：自动核对 rule（database / error-handling）+ 不用人对照检查清单
- Step 4（38-50s）：结构化报告 哪行违反哪条 收尾

## 场景规划（visual_phases）—— 多 phase

### Phase 1（0-10s）：code-review 定位 + 三级总览
- 阶段标签「E11 · code-review 编排型 · 核心段」
- 大字「code-review 三级分级」
- 三圆点（红/黄/绿）

### Phase 2（10-25s）：三级分级卡
- 三卡（🔴 红 必须改 / 🟡 黄 建议改 / 🟢 绿 通过）

### Phase 3（25-38s）：rule 核对流向
- database rule + error-handling rule → 自动套规范
- 不用人对照检查清单

### Phase 4（38-50s）：结构化报告 哪行违反哪条 收尾

## 布局规则
- 多 .phase codereview-scene
- center→space-between
- padding 64px 110px 80px

## 配色规范
- 渐变文字：同色系亮端（红/黄/绿/紫/蓝），禁白端点 / 禁暗端
- 红用亮端 #F87171/#FCA5A5（非暗端 #DC2626）
- 黄用亮端 #FBBF24/#FCD34D（非暗端 #B8842B）
- text-shadow：深蓝 rgba(30,41,59,0.32)，alpha ≤ 0.32
- fx 低 alpha 冷暖搭配，alpha ≤ 0.22

## bg 组件
diamond_lattice（深蓝底 + 菱形格子 + 棱镜色散，匹配「分级/审核/棱镜」主题）— 保留 `<!-- bg-component: diamond_lattice -->`
注：diamond_lattice 自带菱形格属 bg 层；fx 层禁划过类

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性
- 禁 opacity 入场
- 禁暗端渐变（#DC2626/#B8842B/#6D28D9/#1E6FB8）
- 禁创作指令泄露
- 禁「9」（用「九」）
