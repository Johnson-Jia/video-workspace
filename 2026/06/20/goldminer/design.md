# design.md — 视觉风格方向 + 故事板

## 风格
style: 淘金暖金风（残骸淘金=宝藏意象）
mood: 警醒痛心（失败复盘调性，非吃瓜嘲讽）

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑 #0A0805，衬托暖金宝藏意象）
  accent_warm: 暖金/沙金 #FFB800/#D4A017（残骸里淘到的宝藏，淘金者主色）
  accent_fire: 琥珀火光 #FF6B00（烧钱档警示，Bonfire 视觉锚）
  text: 白色主 + 浅灰辅 + 暖金强调

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "毛笔力量"
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "警醒痛心的情感内核需要力量感的标题字体，22 亿烧光的冲击力"
    fallback: "'Ma Shan Zheng','PingFang SC','Microsoft YaHei',cursive"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 暖金警醒（失败复盘的克制悲壮，非悲情煽情）

## 素材预判
assets_needed:
  - ofo 钩子数据可视化（$2.2B 烧钱 + 250 城 + 20-30% 利用率）
  - 单位经济对比图（日收 $0.5-1 vs 日成本 $2-3）
  - doom loop 流程图（扩张→闲置→vandalism→rebalancing 成本）
  - 摩拜/小鸣/Gobee 对比双栏（第5段 CompareSplit）
  - B2B 校园微出行点子图（淘金核心，geofenced 闭环）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.6, 0.85, 0.95, 0.7, 0.5]
  immersion_mode: "contrast-arc"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（淘金！开淘！+$2.2B 钩子）"
    build: "what（ofo 共享单车/250 城/融资规模）"
    reveal: "why_fail（负单位经济+运营混乱+增长幻觉，多 phase 拆解）"
    climax: "loot（教训+可偷点子=B2B 校园微出行，淘金核心）"
    settle: "compare（摩拜/小鸣/Gobee 衬托）"
    summon: "CTA（讨论：这个点子你觉得能成吗）"

## 方向
orientation: portrait
orientation_source: default
