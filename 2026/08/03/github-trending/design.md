# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 紧凑利落、知识增量感

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于 Agent 基建类项目：Agent-Reach / TencentDB / reverse-skill 场景，传递"AI 感知/记忆/技能"的科技冷感）
  accent_warm: 橙色/金色（用于 hook / CTA / 涨星数据强调，形成冷暖对比）
  text: 白色主 + 浅灰辅（清晰对比，禁发光 text-shadow，用极淡 drop）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=知识增量/紧凑专业，GitHub 快速播报需要利落的标题气质，Inter 900 几何感强、信息密度高"
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
music_mood: 科技/低调辅助（clean-corporate 首选，衬底不抢旁白，符合 GitHub 快速播报 BGM 定位）

## 素材预判
assets_needed:
  - 6 个 owner avatar（已在 assets/avatars/，ProjectFullCard 中部引用）
  - 涨星数据用 CSS 数字计数动画（无需外部素材）
  - AI Agent 三件套（眼睛/记忆/技能）可用 CSS 图标/光效隐喻

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.35, 0.55, 0.75, 0.95, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（6个项目杀入，有个让AI长眼睛）"
    build: "Agent-Reach（AI 看全网）"
    reveal: "reverse-skill（AI 安全技能）+ TencentDB（AI 共享记忆）"
    climax: "build-your-own-x（535K★ 从零造技术）"
    settle: "AI-For-Beginners + kaneo（连续霸榜带过增量）"
    summon: "CTA（中性二选一互动）"

## 方向
orientation: portrait
orientation_source: default
