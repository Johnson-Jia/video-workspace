# design.md — 视觉风格方向 + 故事板

## 风格
style: 科技商务          # 科技 + 商务混合风格
mood: 沉稳权威，节奏分明   # 长视频需要保持注意力但不喧哗

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（深蓝黑渐变，营造专业感）
  accent_cool: 科技青/翠绿（用于趋势/技术/数据场景）
  accent_warm: 琥珀金（用于商业/市场/金钱相关场景）
  accent_alert: 暗红色（用于风险/警告场景）
  text: 白色主 + 浅灰辅

## 配乐方向
music_mood: 科技/氛围电子（低调但有推进感，适合长视频）
music_notes: 不用激烈电子乐，用 Ambient/Downtempo 类型，BPM 90-110，不抢旁白

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"    # 旧 SaaS 模式 vs 新 Service-as-Software 模式的对比叙事
  emotion_curve: [0.5, 0.6, 0.8, 0.9, 0.7, 0.5]  # 长视频节奏：温和开场 → 逐步升温 → 高潮 → 沉淀收束
  immersion_mode: "mega-update"          # 大气专业感 + 暗色系 + 粒子/光效装饰
  humor_style: "narration-only"          # 长视频不需要视觉幽默，旁白可适当轻松
  character_presence: false              # 商业分析内容，不启用角色
  beat_mapping:
    grab: "s1-hook, s2-pain, s3-concept"
    build: "s4-market, s5-trends, s6-investment"
    reveal: "s7-competition, s8-bigcompany"
    climax: "s9-openaccountant, s10-taxhacker, s11-agenttax, s12-path1, s13-path2, s14-path3"
    settle: "s15-risk, s16-future"
    summon: "s17-action, s18-cta"

## 长视频特殊说明
long_form:
  target_duration: 600s    # 10 分钟
  scene_count: 18          # 18 个场景
  scene_duration_range: "25-45s"  # 每场景 25-45 秒
  narration_chars: "~2800"       # 目标旁白总字数（按 4.5 字/秒估算）
  bgm_style: "ambient_loop"      # 长视频需要循环型 BGM，不突兀
  visual_variety: true           # 18 个场景需要视觉变化防止审美疲劳
  data_scenes: ["s4-market", "s5-trends", "s7-competition"]  # 含数据对比的场景需图表
