# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 紧凑利落·反差带感

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（深蓝/深紫渐变基底，接近纯黑）
  accent_cool: 霓虹青/科技蓝（用于 AI 记忆、免费功能、数据场景）
  accent_warm: 琥珀金（用于 hook、大厂跨界故事、CTA 场景）
  text: 白色主 + 浅灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核是跨界反差带来的好奇与利落——几何无衬线放大干脆的冲击力"
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
music_mood: 低调科技（clean-corporate 衬底，快节奏播报不抢人声）

## 素材预判（可选）
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.35, 0.55, 0.75, 0.95, 0.6, 0.45]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "omarchy"
    reveal: "ai-memory"
    climax: "OpenCut"
    settle: "ai-agent-book"
    summon: "public-apis 增量 + CTA"

## 方向
orientation: portrait
orientation_source: default
