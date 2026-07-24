# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风（航天档案感）
mood: 沉静厚重

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，带深蓝/深紫层次）
  accent_cool: 深蓝/青绿（用于世界仪表板/阿波罗等冷峻场景）
  accent_warm: 琥珀/金色（用于书/钩子/CTA 场景）
  text: 白色主 + 浅灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "沉静厚重搭配几何利落的标题气质，传递档案级可靠感"
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
music_mood: 低调辅助（clean-corporate，衬底不抢旁白）

## 素材预判（可选）
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.55, 0.7, 0.85, 0.6, 0.45]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（阿波罗钩子）"
    build: "ai-agent-book, i-have-adhd"
    reveal: "Apollo-11"
    climax: "worldmonitor"
    settle: "croc, code-review-graph"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default
