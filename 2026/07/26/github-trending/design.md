# design.md — 视觉风格方向 + 故事板

> 选题：去中心化通信 + 离线隐私主轴（见 topic_plan.json）。核心反直觉：蓝牙 mesh 断网群聊。
> 风格沿用 github 分类 default_style（暗色科技风），叙事/沉浸主动差异化近期 hyper-pace 盘点。

## 风格
style: 暗色科技·去中心化
mood: 反常规揭秘·紧凑利落

## 情绪提炼
- 主题：不依赖云端和运营商、自己掌控通信与工具——断网、本地、去中心化
- 情绪基调：反直觉冲击开场 → 原理揭秘 → 大厂背书 → 掌控感沉淀
- 情绪弧线：好奇（断网也能聊？）→ 恍然（蓝牙 mesh 多跳）→ 信任（阿里/Automattic/block 大厂背书）→ 掌控（自己托管、数据不出本机）
- 节奏感：紧凑（标准模式 4-5 场景，20-45s）
- 文化调性：现代科技 + 轻微反叛/极客（去中心化、无服务器、IRC 老派味道）

## 配色方向（沿用 github default_style，描述性不指定具体色值）
color_direction:
  background: 深蓝/深紫渐变暗调（接近纯黑底，烘托"地下/去中心化"氛围）
  accent_warm: 橙色（#FF8C32 系，用于 hook 数字、CTA、核心反直觉强调）
  accent_cool: 蓝色（#4DA8DA 系，用于 features、技术细节、数据）
  text: 白色主 + 浅灰辅
  text_shadow_rule: 极淡 drop（0 2px 6px rgba(30,41,59,0.08)），禁发光 0 0 Xpx
  gradient_text_rule: 同色系高饱和端点（橙 #FF8C32→#FB923C→#FDBA74 / 蓝 #4DA8DA→#60A5FA→#93C5FD），禁白色端点

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核是反常规揭秘+紧凑利落，科技盘点配几何无衬线最直接；去中心化主题需要清晰利落的字形传递'极客/掌控'感"
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
music_mood: 低调科技辅助（clean-corporate / warm-editorial 系，衬底不抢旁白；禁 bold-energetic/epic 激昂）

## 素材预判
assets_needed:
  - 蓝牙 mesh 多跳中继示意（纯 CSS 节点连线动画，bitchat 揭秘段）
  - "云端 vs 本地"对照分屏（contrast-arc 核心视觉）
  - 数据徽章（今日涨星数，JetBrains Mono 等宽体）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.45, 0.65, 0.85, 1.0, 0.6, 0.4]
  immersion_mode: "hidden-gem"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（断网群聊反直觉冲击）"
    build: "bitchat 揭秘（蓝牙 mesh 多跳中继 + Nostr 双传输）"
    reveal: "palmier-pro + harper（本地创作 + 离线隐私，云端 vs 本地对照）"
    climax: "open-code-review（阿里大厂开源背书，确定性规则 + AI 双引擎）"
    settle: "buzz + Pumpkin 一带而过（Nostr 协同 + 自托管增量）"
    summon: "CTA（二选一中性互动 + 关注）"

## 6 拍情感节奏说明
- grab（好奇 0.45）：断网无 WiFi 无 SIM 卡，手机对手机还能群聊——反直觉悬念
- build（期待 0.65）：蓝牙 mesh 多跳中继原理揭秘，IRC 老派味道
- reveal（惊喜 0.85）：本地创作 + 离线隐私，数据不出本机的掌控感
- climax（激动 1.0）：阿里大规模实战检验的代码审查工具开源
- settle（思考 0.6）：Nostr 协议串联两个项目 + 自托管游戏服，去中心化生态
- summon（行动 0.4）：二选一中性互动收尾

## 方向
orientation: portrait
orientation_source: default
