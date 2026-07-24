# design.md — 视觉风格方向 + 故事板（GitHub Trending 2026-07-17）

## 风格
style: 暗色科技风（跨圈盘点）
mood: 紧凑利落 + 反差张力

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/蓝（用于 hallmark/AI 反差场景，呼应"AI 味"的冷感）
  accent_warm: 橙色/金色 #FF8C32 系（用于 hook/CTA/星标数字，强利益点）
  text: 白色主 + 浅灰辅

> ⛔ text-shadow 极淡 rgba(30,41,59,0.08) drop 禁发光；渐变文字禁白端点用同色系高饱和（橙 #FF8C32→#FDBA74 / 蓝 #4DA8DA→#93C5FD / 金 #FBBF24→#FCD34D）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "紧凑/专业/利落"
    family: "Inter"
    weight: 900
    rationale: "GitHub 快速播报的紧凑调性，几何简洁标题字体放大反差张力"
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
- avatar 已预下载到 assets/avatars/（build-your-own-x avatar 缺失，省略头像位）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.7, 0.6, 0.8, 0.5, 0.4]
  immersion_mode: "contrast-arc"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（反直觉：用 AI 去 AI 味）"
    build: "OpenCut summary（霸榜带过）+ hallmark（反差展开）"
    reveal: "exercises-dataset brief（跨界）"
    climax: "DeepTutor（A 档普通人可用 AI 辅导）"
    settle: "build-your-own-x + ossu（收藏向，编程学习路径）"
    summon: "CTA 中性二选一"

## 方向
orientation: portrait
orientation_source: default

## 备注
- immersion_mode 用 contrast-arc（非 hyper-pace）：AI 类项目仅 2/6（hallmark/DeepTutor）未达 >50% 阈值；本期跨 6 圈盘点，contrast-arc 的"平淡→对比→震撼→高潮→沉淀"弧线更贴合
- hook 场景全片视觉最强：大字反差（"AI 味"vs"去除"）+ 橙金强调 + 冷蓝背景，字号最大对比最强
