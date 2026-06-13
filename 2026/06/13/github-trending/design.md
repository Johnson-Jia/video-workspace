# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 紧凑利落

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深蓝暗调（接近纯黑，带微蓝纹理）
  accent_cool: 冰蓝/青色（用于技术/安全/医疗场景）
  accent_warm: 金色/琥珀（用于 hook/CTA/数据高亮场景）
  text: 白色主 + 浅灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=紧凑/专业/利落（6 方向科技工具盘点），几何简洁体传递工具理性和盘点节奏感，与内容气质匹配"
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
music_mood: 科技/电子

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.35, 0.55, 0.75, 0.95, 0.6, 0.4]
  immersion_mode: "contrast-arc"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "apple/container"
    reveal: "openmed, MasterDnsVPN"
    climax: "superpowers, mattermost"
    settle: "iptv"
    summon: "cta"

## 方向
orientation: portrait
orientation_source: default
