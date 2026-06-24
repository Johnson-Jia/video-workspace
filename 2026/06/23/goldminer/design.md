# design.md — 视觉风格方向 + 故事板

## 风格
style: 淘金暖金风（残骸淘金=宝藏意象）
mood: 惋惜共鸣（好生意败给监管一刀切，双减全民记忆，非吃瓜嘲讽）

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑 #0A0805，衬托暖金宝藏意象）
  accent_warm: 暖金/沙金 #FFB800/#D4A017（残骸里淘到的宝藏，淘金者主色）
  accent_fire: 琥珀火光 #FF6B00（双减一刀切的警示锚，Outlaw 视觉锚）
  text: 白色主 + 浅灰辅 + 暖金强调

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "毛笔力量"
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "惋惜共鸣的情感内核需要力量感的标题字体，一纸文件归零的冲击力"
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
music_mood: 暖金惋惜（失败复盘的克制悲壮，非悲情煽情）

## 素材预判
assets_needed:
  - 魔力耳朵钩子数据可视化（$50M 烧光 + 双减一刀切 + 100% 客户归零）
  - 单位经济对比图（CAC $500-800/学生 vs 毛利 20-30%）
  - 双减政策时间线（2021年7月 overnight elimination）
  - VIPKid/沪江/猿辅导对比双栏（第5段 CompareSplit）
  - AI 出海语言学习点子图（淘金核心，印度1.25亿用户 $5/月）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.6, 0.85, 0.95, 0.7, 0.5]
  immersion_mode: "contrast-arc"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（淘金！开淘！+$50M 监管清零钩子）"
    build: "what（魔力耳朵在线少儿英语/$50M/北美外教）"
    reveal: "why_fail（双减一刀切+单位经济崩坏，多 phase 拆解）"
    climax: "loot（教训=监管风险生存级 + 可偷点子=AI出海语言学习，淘金核心）"
    settle: "compare（VIPKid/沪江/猿辅导衬托）"
    summon: "CTA（讨论：AI出海教英语的点子你觉得能成吗）"

## 方向
orientation: portrait
orientation_source: default
