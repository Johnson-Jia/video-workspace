# design.md — 视觉风格方向 + 故事板（合集标准开场段）

## 风格
style: 清爽专业科技风
mood: 邀请讲解（专业 + 温和邀请，非强冲击）

## 方向（HARD）
orientation: landscape
orientation_source: category_hint

## 教程横屏范式（HARD）
tutorial_reveal_mode: true
tutorial_reveal_note: 一屏多区域 + data-reveal 依次淡入（不切 phase，同屏累积），见 stage6 §6.16

## 语速覆盖（开场段专属）
rate_override: "+20%"
segment_rate_purpose: "开场背景介绍，快节奏（约 6 字/秒 → ~18s），让观众快速进入正片；区别主体段 +0%"

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深蓝主底（接近 #0F172A，干净专业）
  accent_cool: 蓝（主色 #1E3A8A / 亮蓝 #3B82F6，用于标题/分区线/邀请行动）
  accent_warm: 金（#FBBF24，仅用于"方法论"等关键概念强调，克制点缀）
  text: 白主 + 浅蓝灰辅（#E0E7FF 辅助色）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "教程类邀请讲解调性需要专业利落的标题气质，几何简洁贴合企业级方法论"
    fallback: "'Inter','Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: clean-corporate / 低调衬底（教程类 BGM 不能抢旁白；本段为过场，BGM 极弱或无）

## 素材预判
assets_needed: []   # 纯 CSS 多区域布局 + reveal，无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.4, 0.5, 0.7, 0.8, 0.6, 0.5]
  immersion_mode: "tutorial-reveal"
  humor_style: "narration-only"
  character_presence: false
  beat_mapping:
    grab: "合集定位区（一屏多区域 reveal 起手）"
    build: "方法论 vs 工具测评（性质对比）"
    reveal: "demo + 真实数据承诺"
    climax: "受众兜底（团队 Leader + 个人都拿真东西）"
    settle: "邀请学习"
    summon: "跟着拆透"

## 场景规划
- 1 个场景（合集介绍一屏多区域：标题区 + 定位区 + 性质区 + 受众区 + 邀请区，data-reveal 依次淡入）
- 总时长约 18s（110 字 / 6 字每秒，+20% 语速）
- visual_phases 记 reveal 步骤（每步对应一个区域 reveal 时间点），单 phase div + 多 region

## 合规备注
- 话术已用"转型"（非单字"转"），多音字合规
- 无夸大用语（最强/必装/神器/第一/绝对均不出现）
- 无 URL / 搜索引导 / 项目名（背景介绍段不展开项目）
