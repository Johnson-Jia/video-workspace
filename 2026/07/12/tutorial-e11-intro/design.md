# E11 intro 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 30s
category: tutorial
segment: intro

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：暖金 #FBBF24/#FCD34D（skill 分工）+ 冷蓝 #60A5FA/#93C5FD（三件套结构）+ 翠绿 #34D399/#6EE7B7（怎么装收尾）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（目录/路径）
- 整体调性：承上启下 + 三件套预告（SKILL.md / reference / rules）

## 情绪曲线 emotion_curve（5 点）
- 0.32（承上：前集度量 → 这集沉淀复用）
- 0.70（揭示：skill 做成 / rule 做成 统一放 .claude）
- 0.85（预告：skill + rule 分工）
- 0.70（预告：三件套 + 四核心 + 十三条）
- 0.50（收尾：怎么装到你的项目）

## 沉浸模式 immersion_mode
data_reveal：三件套预告（SKILL.md / reference / rules）stagger

## 叙事模板 narrative_template
方法论预告（recap → topic → preview-five-things → install-teaser）
- Step 1（0-8s）：承上「前集度量实操 → 这集沉淀复用」+ 大字「Skill 仓库实操」
- Step 2（8-16s）：skill 做成 / rule 做成 统一放 .claude 目录 揭示
- Step 3（16-24s）：五件事预告 stagger（skill vs rule / 三件套 / 四核心 / 十三条 / 怎么装）
- Step 4（24-30s）：怎么装到你的项目 收尾

## 场景规划（visual_phases）—— 多 phase

### Phase 1（0-8s）：承上 + 大字主题
- region-1：阶段标签「E11 · Skill 仓库实操 · intro」
- region-2：承上「前集度量实操 · 这集沉淀复用」
- region-3：大字「Skill 仓库实操」（暖金渐变）

### Phase 2（8-30s）：五件事预告 stagger + 怎么装收尾
- region-1：阶段标签
- region-2：「这集你能学到 五件事」标题
- region-3：五卡 stagger（① skill vs rule 分工 / ② 三件套结构 / ③ 四核心 skill / ④ 十三条规范分层 / ⑤ 怎么装到你的项目）
- region-4：收尾带「全部放在 .claude 目录 · AI 自动加载」

## 布局规则
- 多 .phase intro-scene（每 phase 完整状态）
- center→space-between（撑满 1920×1080）
- padding 64px 110px 80px

## 配色规范
- 渐变文字：同色系亮端（金 #FBBF24→#FCD34D / 蓝 #60A5FA→#93C5FD / 绿 #34D399→#6EE7B7），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)，alpha ≤ 0.32
- fx 冷色优先（蓝/金/绿），alpha ≤ 0.22

## bg 组件
hex_grid（六边形蜂窝 + 翡翠辉光 + 全息菱形 + 高亮节点，匹配「方法论/结构」主题）— 保留 `<!-- bg-component: hex_grid -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性
- 禁 opacity 入场
- 禁暗端渐变
- 禁创作指令泄露
- 禁「9」（用「九」）
