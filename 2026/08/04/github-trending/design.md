# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风（GitHub Dark 调）
mood: 紧凑干练，反差震撼（4G vs 700亿参数的数字冲击）

## 情绪提炼
- 主题：8月4日 GitHub 日榜，本地大模型推理成最大看点，辅以语音/文档/编程/项目管理工具
- 情绪基调：反直觉震撼（4G显存跑700亿参数）+ 极客理性（开源工具盘点）
- 情绪弧线：好奇（4G能跑700亿？）→ 求证（逐个项目展开）→ 高潮（A档GUI能力/涨幅数据）→ 沉淀（霸榜带过）→ 行动
- 节奏感：紧凑（标准模式日榜快播报）
- 文化调性：现代科技 + 开源极客

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，GitHub Dark 系深蓝/深紫渐变底）
  accent_cool: 霓虹青/翠绿（用于项目展开、技术栈、能力展示场景）
  accent_warm: 橙色/金色（用于 hook 的反差数字、CTA、涨幅数据）
  text: 白色主 + 浅灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "反差数字钩子（4G vs 700亿）需要现代、利落、有力量感的几何粗体，传达科技工具的紧凑专业"
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
music_mood: 科技/低调辅助（GitHub 快速播报衬底，clean-corporate/warm-editorial/monospace 首选，不抢旁白）

## 素材预判
assets_needed: []  # 纯 CSS/数据即可，avatar 已在 assets/avatars/，无外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.55, 0.65, 0.75, 0.85, 0.5, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（4G vs 700亿反差钩子）"
    build: "airllm（钩子延伸：分层流式加载原理）"
    reveal: "ds4（antirez 推理引擎三平台）"
    climax: "voicebox（A档GUI语音工作室）+ pdf-inspector（涨幅第二）"
    settle: "DeepSeek-Reasonix + kaneo（带过/霸榜增量）"
    summon: "CTA（中性二选一提问）"

## 方向
orientation: portrait
orientation_source: default
