# design.md — 视觉风格方向 + 故事板（GitHub Trending 2026-07-18）

## 风格
style: 暗色科技风（跨圈新项目盘点）
mood: 紧凑利落 + 跨圈张力

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 深蓝/深紫（用于跨圈新项目场景 docuseal/PostHog/turbovec/code-review-graph）
  accent_warm: 橙色/金色 #FF8C32 系（用于 hook/霸榜星标/CTA，强利益点）
  text: 白色主 + 浅灰辅

> ⛔ text-shadow 极淡 rgba(30,41,59,0.08) drop 禁发光；渐变文字禁白端点用同色系高饱和（橙 #FF8C32→#FDBA74 / 蓝 #4DA8DA→#93C5FD / 金 #FBBF24→#FCD34D）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "紧凑/专业/利落"
    family: "Inter"
    weight: 900
    rationale: "GitHub 快速播报的紧凑调性，几何简洁标题字体放大跨圈数字冲击力"
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
music_mood: 科技/低调辅助（clean-corporate 优先，禁 bold-energetic 抢旁白）

## 素材预判
assets_needed: []
- 项目数据全 CSS/HTML 实现（星标数字、用途胶囊、卡片布局）
- avatar 已预下载到 assets/avatars/

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.6, 0.7, 0.8, 0.5, 0.6, 0.4]
  immersion_mode: "contrast-arc"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（动作+数字+跨圈利益：今日霸榜过万星 + 跨圈新秀冲上来）"
    build: "霸榜带过（hallmark/OpenCut 一带而过）+ docuseal（电子签名跨圈 A 档）"
    reveal: "PostHog（产品分析平台，B 档跨圈）"
    climax: "turbovec（Rust 向量基建，C 档开发者向极速）"
    settle: "code-review-graph（代码知识图谱，C 档）"
    summon: "CTA 中性二选一（想试哪个）"

## 方向
orientation: portrait
orientation_source: default

## 备注
- immersion_mode 用 contrast-arc（非 hyper-pace）：AI 类项目仅 1/6（hallmark）未达 >50% 阈值；本期跨 6 圈盘点，contrast-arc 的"平淡→对比→震撼→高潮→沉淀"弧线更贴合
- hook 场景全片视觉最强：大字数字冲击（"过万星"/"六个新项目冲上来"）+ 橙金强调 + 冷蓝背景，字号最大对比最强
- 与昨日（用 AI 去 AI 味）差异化：hook 改数字+跨圈利益方向；项目集主体改 4 个全新跨圈项目；霸榜 2 项一带而过
