# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风（GitHub 风）
mood: 紧凑利落，跨圈扫榜

## 配色方向
color_direction:
  background: 深蓝紫渐变（接近纯黑底 #0a0e1a / #14182b）
  accent_cool: 霓虹青/翠绿（用于 solution/features 场景，跨圈工具冷色沉稳）
  accent_warm: 橙金（用于 hook/CTA 场景，强钩子数据锚点）
  text: 白色主 + 浅灰辅
  note: 冷色主调贯穿 4 个跨圈场景（部署/SEO/语音/学习），暖色仅用于 hook/CTA/霸榜数据；视觉色不进旁白

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter 900"
    weight: 900
    rationale: "快节奏跨圈扫榜，几何无衬线呼应 GitHub 风的利落专业"
    fallback: "'Inter','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: clean-corporate / warm-editorial（低调衬底，跨圈扫榜节奏）

## 素材预判
assets_needed: []
note: 6 项目卡片走 ProjectFullCard 单卡布局；不依赖外部图表素材，纯 CSS+卡片

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.35, 0.5, 0.7, 0.85, 0.55, 0.4]
  immersion_mode: "contrast-arc"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "openship（部署跨圈）/ open-seo（SEO 跨圈）"
    reveal: "voicebox（AI 语音工作室）/ Ontology（微软官方）"
    climax: "jcode（编程智能体）"
    settle: "code-review-graph（霸榜一带过）"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default
