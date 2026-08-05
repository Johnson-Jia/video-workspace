# design.md — 视觉风格方向 + 故事板（AI 风向标 / 电紫主题）

## 风格
style: 暗色科技 AI 电紫
mood: 紧凑科技 自主跃迁

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深紫暗调（接近纯黑 #0a0a14 → 深紫 #1a0a2e 渐变）
  accent_cool: 电紫主色（#A855F7 主，渐变端点紫 #A855F7→#C084FC→#E9D5FF，禁白色端点）
  accent_secondary: 辅青（#00D4FF 主，渐变端点青 #00D4FF→#60A5FA→#93C5FD，禁白色端点）
  accent_warm: 暖点缀橙（#FF6B35，仅用于数据强调/排名编号，少量）
  text: 白色主 + 浅紫灰辅

## text-shadow 规则
极淡 drop text-shadow: 0 2px 6px rgba(30,41,59,0.08)，禁发光 0 0 Xpx

## 渐变文字配色（background-clip:text）
紫色系: #A855F7 → #C084FC → #E9D5FF（同色系高饱和，禁白色端点）
青色系: #00D4FF → #60A5FA → #93C5FD（同色系高饱和，禁白色端点）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Noto Sans SC"
    weight: 900
    rationale: "AI 科技紧凑内核需要几何力量感的标题字体，电紫主题配粗体无衬线"
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/电音/紧凑（暗色电紫匹配，hyper-pace 快节奏）

## 素材预判
assets_needed: []  # 纯 CSS/HTML 光晕 + 粒子实现电紫科技感，无需外部素材；avatars 已在 assets/avatars/

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.3, 0.5, 0.8, 1.0, 0.7, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（AI 不健忘 + 团队共用脑 反直觉钩子）"
    build: "topic1 TencentDB（建立 AI 自主性主题：记忆中枢）"
    reveal: "topic2 Agent-Reach（65K 总星揭示 AI 自主调研），topic3 livekit（实时语音新方向揭示）"
    climax: "topic4 airllm（27K + 本地大模型数据震撼，连续爆火项高潮）"
    settle: "topic5 voicebox（回归普通人可用的 AI 语音工作室，沉淀）"
    summon: "CTA（中性二选一互动）"

## 方向
orientation: portrait
orientation_source: default
