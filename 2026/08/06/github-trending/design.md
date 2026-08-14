# design.md — 视觉风格方向 + 故事板

## 风格
style: 科技赛博（暖金）
mood: 紧凑激昂

## 配色方向（描述性）
color_direction:
  background: 深邃近黑（科技暗调）
  accent_warm: 琥珀金/橙（hook/CTA/排名强调）
  accent_cool: 青绿/钢蓝（项目卡/语言标签/数据）
  text: 白色主 + 浅灰辅

## 字体（三层 + voice）
fonts:
  title:
    voice: "几何简洁（紧凑/专业/利落）"
    family: "Inter"
    weight: 900
    rationale: "GitHub 项目盘点沿用分类标准 Inter，紧凑利落匹配 hyper-pace 快闪节奏"
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
music_mood: 科技/赛博/紧凑推进

## 素材预判
assets_needed:
  - "4 项目 ProjectFullCard（owner avatar 已下载 assets/avatars/）"
  - "涨星进度条（stars_today 相对当日最大值）"

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.6, 0.7, 0.75, 0.7, 0.6, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "s1-hook（给AI配电脑，榜单炸场）"
    build: "s2-cloudflare/computer（钩子项目详）"
    reveal: "s3-TencentDB（今日最热）"
    climax: "s4-pdf-inspector（Rust利器）"
    settle: "s5-next.js（常青基建）"
    summon: "s6-CTA"

## 方向
orientation: portrait
orientation_source: default
