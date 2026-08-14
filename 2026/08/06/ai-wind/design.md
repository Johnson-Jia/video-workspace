# design.md — 视觉风格方向 + 故事板（ai-wind 电紫）

## 风格
style: 电紫赛博
mood: 神秘激昂

## 配色方向（描述性）
color_direction:
  background: 深紫暗调（近黑紫，#1a0a2e 系）
  accent_warm: 霓虹品红/紫（#d946ef 系，ai-wind 主色，hook/CTA/排名）
  accent_cool: 电紫蓝/青紫（#a78bfa 系，项目卡/数据）
  text: 白色主 + 浅紫灰辅

## 字体（三层 + voice）
fonts:
  title:
    voice: "几何简洁（紧凑/专业/利落）"
    family: "Inter"
    weight: 900
    rationale: "ai-wind 沿用 AI 专项的 Inter 紧凑利落，匹配电紫 hyper-pace 节奏"
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
music_mood: 电紫/赛博/神秘激昂

## 素材预判
assets_needed:
  - "5 项目 ProjectFullCard（avatar 已下载 assets/avatars/）"
  - "涨星进度条（stars_today 相对当日最大 TencentDB 1892）"

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.65, 0.7, 0.72, 0.68, 0.7, 0.65, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "s1-hook（AI agent 炸场，九个集体进化）"
    build: "s2-superpowers（267K技能框架）"
    reveal: "s3-DeepSeek-Reasonix（终端编程）"
    climax: "s4-agent-skills（编程技能）"
    settle: "s5-loopx（agent循环）+ s6-supervision（CV）"
    summon: "s7-CTA"

## 方向
orientation: portrait
orientation_source: default
