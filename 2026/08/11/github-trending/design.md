# design.md — 视觉风格方向 + 故事板（2026-08-11 github-trending daily）

## 风格
style: 暗色科技（AI 基建向）
mood: 紧凑理性·带一点冷峻的未来感（不激昂，铺基建层而非炫能力）

## 配色方向（描述性，不指定具体色值；暗色做底亮色做刀）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于 semantica 图谱/记忆/可追溯场景——冷色衬"确定性/可审计"）
  accent_warm: 金色/琥珀（用于 hook 与 prime-agent 单日涨星数据 + CTA——暖色衬"涨星爆发/自我进化"）
  text: 白色主 + 浅灰辅
  contrast_principle: 双项目用暖冷分色——prime-agent 偏暖（金/橙，autonomy 自我进化），semantica 偏冷（青/翠，accountability 可追溯），形成同一暗底上的两条路

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=震撼+紧凑理性的科技感，AI 基建题材需利落几何而非毛笔/衬里；Inter 900 在暗底上最干净有力"
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
music_mood: 低调科技/赛博衬底（clean-corporate 或 monochrome 类，不抢旁白；避开 bold-energetic/epic 激昂系——AI 基建是铺底层不是爆点）

## 素材预判
assets_needed: []
（双项目均为概念性 AI 基建，纯 CSS/HTML 图谱节点 + 数据卡片即可，无需外部素材）

## 故事板
storyboard:
  narrative_template: "contrast-arc"      # 双项目对比弧：prime-agent(autonomy) vs semantica(accountability) 两条路
  emotion_curve: [0.35, 0.7, 0.9, 0.55, 0.4]   # grab→reveal→climax→settle→summon
  immersion_mode: "hyper-pace"            # AI 内容 >50%，快速剪辑 + 密集粒子 + 霓虹冷色（github immersion_mapping）
  humor_style: "narration-only"           # 基建题材偏理性，幽默仅旁白轻调剂（analogy 类），视觉保持克制
  character_presence: true                # github 系列启用码力角色（climax 段必出）
  beat_mapping:
    grab: "hook（单日涨星+AI自我进化反直觉）"
    build: "prime-agent 引入（自我进化编程 agent）"
    reveal: "prime-agent 反直觉展开 + semantica 引入"
    climax: "semantica 可追溯记忆图谱（决策不再黑盒）"
    settle: "两条路对比沉淀（autonomy vs accountability）"
    summon: "CTA（想尝试哪个 + 关注）"

## camera_move 预防（[[feedback-stage6-camera-move-scale]]）
camera_move_plan:
  scene_hook: "推（grab 节拍，增加冲击）"
  scene_prime_agent: "固定（ProjectFullCard 项目段全固定，避免 layer-content scale 致 PFC 顶带溢出）"
  scene_semantica: "固定（同上）"
  scene_insight: "固定（对比沉淀，稳定镜头）"
  scene_cta: "固定"
原则: 仅 hook 可"推"；凡含 ProjectFullCard 的项目段一律"固定"，从源头规避 camera_move='推' 引发的 scale 溢出事故。

## 方向
orientation: portrait
orientation_source: default   # 竖屏优先（github 抖音系默认竖屏）
