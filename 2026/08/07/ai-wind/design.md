# design.md — 视觉风格方向 + 故事板（ai-wind 电紫）

## 风格
style: 电紫赛博
mood: 神秘激昂

## 配色方向（描述性，电紫主题）
color_direction:
  background: 深紫暗调（近黑紫，#0a0a14 → #1a0a2e 渐变）
  accent_warm: 电紫/品红（#A855F7 主色 → #d946ef 高光，hook/CTA/排名）
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
  - "单日涨星进度条（stars_today 相对当日最大 computer 2802）"

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.7, 0.72, 0.75, 0.78, 0.7, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "s1-hook（单日涨六千星，AI 居然自己干活）"
    build: "s2-computer（cloudflare 给 AI 配电脑操作实体）"
    reveal: "s3-tencentdb（腾讯给 AI 团队装共享脑）"
    climax: "s4-skills（mattpocock 207K 星工程技能包）"
    settle: "s5-autogpt（186K 星自主 agent 老前辈）"
    summon: "s6-CTA（最想让谁替你干活）"

## 方向
orientation: portrait
orientation_source: default
