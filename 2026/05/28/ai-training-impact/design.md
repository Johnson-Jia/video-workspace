# design.md — AI 对企业培训行业冲击深度解析

## 风格
style: 商业数据科技
mood: 权威分析 + 数据冲击

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深邃暗色（深蓝黑底，带微弱网格纹理）
  accent_primary: 科技青/翠绿（用于数据增长、正面指标）
  accent_secondary: 琥珀/金色（用于关键数字、警示数据）
  accent_alert: 渐变紫红（用于冲击光谱、颠覆性结论）
  text: 白色主 + 浅灰辅 + 深灰弱化

## 配乐方向
music_mood: 科技商业/数据驱动力，中速节奏，长视频需要情绪层次变化
bgm_notes: 需要能支撑 10 分钟的内容节奏，避免过于激昂导致疲劳

## 素材预判
assets_needed: []  # 全部用 CSS/HTML 组件实现，无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.6, 0.85, 1.0, 0.7, 0.8]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: false

  beat_mapping:
    grab: "S1-hook"
    build: "S2-S4（背景：市场数据、AI爆发、核心矛盾）"
    reveal: "S5-S11（现状：五个重构维度逐一展开）"
    climax: "S12-S13（冲击光谱 + 谁在被淘汰）"
    settle: "S14-S16（展望：L&D转型、中国市场、不拥抱的风险）"
    summon: "S17-S19（实操框架 + 行动号召）"

## 场景规划（19 场景，约 10 分钟）

### 第一部分：背景知识（~2 分钟，4 场景）
- S1-hook: "AI 正在杀死企业培训行业？"— 钩子，抛出争议问题
- S2-market: 全球培训市场 $4,175 亿→$5,413 亿，蛋糕在做大 — 市场规模数据
- S3-ai-boom: AI 培训细分 CAGR 21.7%，增速是传统 4 倍 — 爆发数据
- S4-paradox: 仅 25% 员工认为培训有效 — 核心矛盾揭示

### 第二部分：目前现状（~4 分钟，7 场景）
- S5-overview: 五个重构维度总览 — 框架建立
- S6-content: 内容生产革命 — 500% 效率提升、30% 由 AI 创建
- S7-learning: 学习模式转变 — 从推送到好奇驱动
- S8-compare: ChatGPT 10 亿用户 vs 传统 LMS — 对比冲击
- S9-personal: 个性化学习 — 保留率 +30%、78% 偏好 AI 路径
- S10-coach: AI 教练与模拟 — 80% 自动应答、北森六大 Agent
- S11-data: 数据驱动评估 — ROI +65%、预测准确率 85%

### 第三部分：未来展望（~2.5 分钟，4 场景）
- S12-spectrum: 冲击光谱 — 30%→55%→75%→95% 四层级渐变
- S13-disrupted: 谁在被冲击 — 42% 替换 LMS、标准课程被绕过
- S14-ld-shift: L&D 职能重塑 — 从课程交付到战略能力构建
- S15-china: 中国战场 — 北森/云学堂/知学云全面 AI 化

### 第四部分：实操落地（~1.5 分钟，4 场景）
- S16-risks: 不拥抱 AI 的 5 大风险
- S17-framework: 企业行动框架 — 评估→试点→规模化
- S18-action: 关键数据驱动行动 — 70% 整合 AI、48% 增加预算
- S19-cta: 终极结论 + 关注获取更多行业分析

## 组件预分配（场景→组件映射）
- S1-hook: HeroCard（大标题 + 副标题钩子）
- S2-market: MarketBars（市场规模条形图）
- S3-ai-boom: NumGrid（CAGR 对比数字）
- S4-paradox: HeroCard + 大数字强调
- S5-overview: BulletList（五维度清单）
- S6-content: NumGrid（效率提升数据）
- S7-learning: ContrastSplit（推送 vs 好奇驱动）
- S8-compare: ScoreCompare（ChatGPT vs LMS）
- S9-personal: DataViz（保留率和偏好数据）
- S10-coach: BulletList（AI 教练能力）
- S11-data: NumGrid（ROI 和准确率）
- S12-spectrum: Spectrum（冲击光谱色带+条形图）
- S13-disrupted: RecStrip（三档受冲击程度）
- S14-ld-shift: VerdictBox（角色重塑结论）
- S15-china: BulletList（中国厂商）
- S16-risks: NumGrid（5 大风险数字）
- S17-framework: BulletList（行动三步）
- S18-action: MarketBars（关键行动数据）
- S19-cta: HeroCard（终极结论 + CTA）
