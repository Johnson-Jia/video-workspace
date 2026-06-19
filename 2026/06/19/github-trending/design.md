# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 紧凑利落，理性中带悬念

## 配色方向
color_direction:
  background: 深色暗调（深蓝/深紫渐变底，接近纯黑）
  accent_cool: 霓虹青/电光蓝（用于 AI/数据/翻译场景）
  accent_warm: 橙金（#FF8C32 系，用于 hook/涨星数字/CTA 场景）
  text: 白色主 + 浅灰辅

## 字体
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "工具/效率题材的紧凑专业感，搭配反直觉钩子的干脆利落"
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
music_mood: 科技/紧凑（暗色电子，中等节奏，不抢旁白）

## 素材预判
assets_needed: []
（纯 CSS/光效/卡片即可，avatars 已下载用于 ProjectFullCard）

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.4, 0.5, 0.7, 0.9, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "codebase-memory-mcp, Universal-Debloater"
    reveal: "LibreTranslate, insomnia"
    climax: "GLM-5"
    settle: "timesfm"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default
