# design.md — 视觉风格方向 + 故事板（goldminer 创业淘金者）

## 风格
style: 淘金暖金风（警醒+理性档）
mood: 警醒 + 理性（单位经济庞氏的痛心警示 + 双死商业逻辑剖析）

## 配色方向（goldminer IP 识别符：暖金宝藏 + 深色残骸底）
color_direction:
  background: 深色残骸底（接近纯黑 #0A0805，衬托暖金宝藏感）
  accent_warm: 暖金/沙金主色（#FFB800 / #D4A017）——残骸里淘到的宝藏意象，用于 hook/CTA/数据高光
  accent_fire: 琥珀火光（#FF6B00）——警示与冲突强调，用于单位经济崩塌段/双减补刀
  text: 白色主 + 浅金/浅灰辅
  rationale: 暖金=淘金底色（区别主轨冷色科技风）；警醒档用暖金+琥珀火光烘托"越扩越亏的庞氏"的灼烧感与"钱烧光"的警示

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "毛笔力量"
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "hook 的 $188M 震撼数据 +「淘金！开淘！」签名需要力量感；警醒中带理性，毛笔厚重烘托『越扩越亏烧光 188M』的分量与痛心"
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
music_mood: 警醒/理性/电影感暖色（搜索关键词：tense, reflective, cinematic, dramatic, warm）
bg_pool_hint: radial_beams / vignette_glow / gradient_mesh / contour_lines / wave_ripple（暖金组件，相邻场景类型不同，全片 ≥3 种）

## 素材预判
assets_needed: []
（纯 CSS/HTML 实现：$188M 大字计数、CAC vs ARPU 单位经济对比柱、双减补刀时间线、Qkids vs Changingedu 双栏、AI 原生 loot 卡）

## 故事板（5 段失败复盘 → contrast-arc）
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.6, 0.6, 0.85, 1.0, 0.6, 0.5]
  immersion_mode: "contrast-arc"
  humor_style: "narration-only"
  character_presence: true
  character_expression_plan: "hook=think（警醒）/ what=cool（介绍）/ why_fail=think（剖析双死）/ loot=cool（淘金点子）/ compare=moved（沉淀）"
  beat_mapping:
    grab: "hook（淘金签名 + 越扩越亏反直觉钩子）"
    build: "what（Changingedu 做什么 + 融资 + 砸钱抢市明星）"
    reveal: "why_fail（双刀死：单位经济早崩 + 双减补刀，反直觉：没监管也撑不到盈利）"
    climax: "loot（淘金：小规模跑通教训 + 大模型主讲可偷点子）"
    settle: "compare（Qkids 同双减死 + 行业 $100B+ 蒸发衬托行业性）"
    summon: "compare 尾（淘金签名 + 讨论 CTA）"

## 方向
orientation: portrait
orientation_source: default
