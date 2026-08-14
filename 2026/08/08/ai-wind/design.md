# design.md — 视觉风格方向 + 故事板（ai-wind 电紫）

## 风格
style: 电紫赛博
mood: 神秘激昂

## 配色方向（描述性，电紫主题）
color_direction:
  background: 深紫暗调（近黑紫，#0a0a14 → #1a0a2e 渐变）
  accent_warm: 电紫/品红（#A855F7 主色 → #d946ef 高光，hook/CTA/排名/数字锚）
  accent_cool: 青紫/电青（#00D4FF → #a78bfa，项目卡/数据/辅光）
  text: 白色主 + 浅紫灰辅

## 字体（三层 + voice）
fonts:
  title:
    voice: "几何简洁（紧凑/专业/利落）"
    family: "Inter"
    weight: 900
    rationale: "ai-wind 沿用 AI 专项的 Inter 紧凑利落，匹配电紫 hyper-pace 快剪节奏"
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
  - "4 项目 ProjectFullCard（avatar 已下载 assets/avatars/）"
  - "单日涨星进度条（stars_today 相对当日最大 prime-agent 2293）"

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.8, 0.7, 0.75, 0.85, 0.65, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "s1-hook（单日三千星，AI 不再单干）"
    build: "s2-prime-agent（能给自己打补丁的自迭代 agent，+2293）"
    reveal: "s3-google-skills（Google 官方下场做 agent 技能）"
    climax: "s4-semantica（图原生可追溯基建，专治黑盒胡编）"
    settle: "s5-swarm-forge（资深从业者轻量协调多 AI 协作）"
    summon: "s6-CTA（最看好哪个方向）"

## 方向
orientation: portrait
orientation_source: default
