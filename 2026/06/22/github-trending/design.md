# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博
mood: 紧凑利落 + 大厂开源反差感

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑 + 深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于 deer-flow/cognee/English 等 AI/记忆/学习场景，呼应"AI 能力扩展"主线）
  accent_warm: 金色/琥珀（用于 hook/CTA 场景 + 数字锚点 72K★/754/5.4万★，形成双光晕暖冷对比）
  text: 白色主 + 浅灰辅（项目描述/感性评语）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核 = 紧凑/专业/利落（大厂开源自主 agent 的工程感），几何无衬线最贴 AI 工程调性"
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
music_mood: 科技/赛博（紧凑电子，配合大厂开源反差 + 自主 agent 跑活的节奏感）

## 素材预判（可选）
assets_needed: []  # 6 项目 avatar 已预下载到 assets/avatars/，无需外部素材；ProjectFullCard + 数字计数动画即可

## 故事板
storyboard:
  narrative_template: "contrast-arc"   # 平淡（钩子）→ 对比（大厂开源反差）→ 震撼（能力扩展拼图）→ 高潮（754 安全技能/全球情报）→ 沉淀（连续霸榜 + 英语学习）→ 召唤（CTA）
  emotion_curve: [0.4, 0.6, 0.75, 0.9, 0.65, 0.45]  # hook 中高起步 → build 上扬 → reveal 拼图展开 → climax 754 安全技能爆发 → settle 霸榜+英语回落 → summon CTA
  immersion_mode: "hyper-pace"          # AI/Agent/LLM 项目 >50%（deer-flow/cognee/cybersecurity-skills 3/6），匹配 AI 类用 hyper-pace 快速剪辑 + 密集粒子 + 霓虹 #00D4FF
  humor_style: "dual-track"             # 双线幽默：旁白类比 + 视觉调剂
  character_presence: true              # GitHub 分类启用码力角色
  beat_mapping:
    grab: "hook（7.2 万星 SuperAgent 大厂开源反差）"
    build: "deer-flow 自主跑活"
    reveal: "worldmonitor 全球情报一屏看 + cybersecurity 754 安全技能"
    climax: "cognee AI 长记性 + palmier-pro 连续霸榜一带过"
    settle: "English-level-up-tips 5.4 万星现象级"
    summon: "CTA（这 6 个你最想尝试哪个 + 关注我下期见）"

## 方向
orientation: portrait
orientation_source: default   # 标准竖屏，GitHub 系列默认 portrait
