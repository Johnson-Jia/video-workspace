# design.md — 视觉风格方向 + 故事板

## 风格
style: 淘金暖金风（残骸里淘到的宝藏意象）
mood: 警醒痛心（资本烧光教训 + 双向平台反中介警醒）

## 配色方向（暖金 #FFB800/#D4A017 主 + 琥珀火光 #FF6B00 强调，深色底 #0A0805 衬托）
color_direction:
  background: 深色暗调（接近纯黑 #0A0805，残骸/矿洞意象）
  accent_warm: 暖金/沙金 #FFB800/#D4A017（hook/loot/CTA 场景，宝藏/金块意象）
  accent_fire: 琥珀火光 #FF6B00（why_fail 场景强调，烧钱的火/警示）
  accent_cool: 浅沙金 #C9A961（数据/对比场景辅助，区别主轨纯冷色）
  text: 白色主 + 浅沙金辅

> 暖金为主（残骸里淘金），琥珀火光做强调（烧钱的火/警示），深色底衬托。禁止纯冷色（主轨科技风）。渐变禁纯白端点（用同色系高饱和，如 #FFB800→#D4A017 而非 #FFB800→#FFFFFF）。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "毛笔力量"
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "警醒痛心的情感内核（烧光1亿美金的教训）需要力量感的标题字体"
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
music_mood: 暖金励志（残骸淘金感，有起承转合，前段警醒低沉→中段剖析→后段淘金上扬）

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.7, 0.5, 0.85, 0.95, 0.6, 0.5]
  immersion_mode: "contrast-arc"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（淘金！开淘！+ 1亿美金烧光钩子）"
    build: "what（学吧100 是什么：K12 在线交易平台 + $100M 融资 + 规模）"
    reveal: "why_fail（死因反直觉：不是败给竞品，是败给自己老师把学生挖走）"
    climax: "loot（淘金核心：教训 7 条 + 可偷点子 Sensei AI 重建）"
    settle: "compare（对比 Magic Ears 双减一刀切 / Xiaoming Bike 烧钱补贴）"
    summon: "CTA（讨论：这个 AI 学习平台点子你觉得能成吗）"

## 方向
orientation: portrait
orientation_source: default
