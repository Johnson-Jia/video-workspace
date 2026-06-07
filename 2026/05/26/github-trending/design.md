# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博
mood: 激烈紧凑 + 反差惊喜

> 今日主题：5个新项目集中冲榜 + 1个19万星巨头突然出现。"AI工具生态大爆发"——信息密度高，节奏快，但有taste-skill这样的反直觉角度制造惊喜转折。

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，微带深蓝）
  accent_warm: 金色/琥珀（用于 hook、Star 数据、排名数字、CTA）
  accent_cool: 霓虹青/翠绿（用于技术描述、功能列表、项目标签）
  accent_special: 电紫/靛紫（用于 AI Agent 类项目、ECC 巨头场景）
  text: 白色主 + 浅灰辅（描述/说明用灰，标题/数据用白）
  glow: 暖光左上 + 冷光右下（双光晕，每个场景都保持）

## 配乐方向
music_mood: 科技/赛博电子，中速偏快，有脉冲感但不压迫

## 素材预判
assets_needed: []  # 纯 CSS 渐变 + 光效即可，无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.7, 0.5, 0.8, 1.0, 0.5, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook — 19万星巨头冲上日榜，用金色大字+数据冲击"
    build: "ECC介绍 → taste-skill介绍（从冷色技术切到暖色反直觉）"
    reveal: "taste-skill反直觉角度（'给AI品味'）→ ai-engineering 学习热潮"
    climax: "gstack（YC总裁配置10万星）+ Understand-Anything今日涨星王"
    settle: "Anthropic-Cybersecurity-Skills 安全领域"
    summon: "CTA — 关注看明天"

## 场景规划（6场景，预计30-40秒）

### Scene 1: hook（3-4s）
- 情感：震撼（grab）
- 视觉焦点：巨大金色数字 "192K" + "今天冲上日榜"
- 配色：金色主导，暖光强化
- 内容：一个19万星的项目，今天突然冲上 GitHub 日榜

### Scene 2: ECC + taste-skill（7-8s）
- 情感：好奇 → 惊喜（build → reveal）
- 子场景 A（ECC，4s）：紫色光晕 + 192K星标 + Agent优化系统简介
- 子场景 B（taste-skill，4s）：暖色转折 + "让AI有好品味" + 反直觉钩子
- 反差：紫色（巨头/工具）→ 暖金（品味/人文感）

### Scene 3: ai-engineering-from-scratch（5-6s）
- 情感：期待（build）
- 视觉：青色功能列表 + 从零到全栈的学习路径
- 重点：今日+3167，Fork≈Star增长说明真有人在学

### Scene 4: gstack（5-6s）
- 情感：激动（climax）
- 视觉：金色 + "YC总裁的配置" + 10万星
- 重点：人物背书 + 23个工具角色

### Scene 5: Understand-Anything + Cybersecurity（6-7s）
- 情感：思考（settle）
- 子场景 A（Understand-Anything，3s）：快速带过，"上次说的知识图谱，今天又涨了五千多星"
- 子场景 B（Cybersecurity，4s）：红色/暗色调 + 754个安全技能 + 26个安全域
- 反差：从暖色快速提及 → 冷色安全主题

### Scene 6: CTA（2-3s）
- 情感：行动意愿（summon）
- 视觉：频道名 + 关注引导
- 配色：金色强调

## 导演笔记
- 今日6个项目，5个是新上榜，信息密度高 → 场景切换节奏要快（平均5-6s/场景）
- hook不能用"炸了/霸榜"（昨天用过），改用"19万星项目突然冲上日榜"的数据锚定角度
- ECC是视觉重点：192K星+突然冲榜的反直觉 → 用紫色+金色双光晕制造"巨头降临"感
- taste-skill是叙事转折点："给AI好品味"打破科技冷感 → 用暖色转折制造惊喜
- Understand-Anything连续霸榜，只给3秒快速带过，不重复介绍
