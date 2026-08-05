# design.md — 视觉风格方向 + 故事板

## 风格
style: 淘金暖金风（残骸淘金=宝藏意象）
mood: 唏嘘惋惜（好产品败给监管时机）

## 配色方向（描述性，暖金主色区别主轨冷色科技风）
color_direction:
  background: 深色底（接近纯黑 #0A0805，残骸夜色，衬托暖金火光）
  accent_warm: 暖金/沙金（#FFB800/#D4A017，淘金宝藏主色，what/loot 段）
  accent_fire: 琥珀火光（#FF6B00，hook 钩子与"烧成灰"意象强调）
  text: 白色主 + 浅金辅（#F5E6C8 数据高亮）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "毛笔力量"
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "惋惜的情感内核——好产品败给监管的唏嘘，需力量感与苍凉并存的标题，配合暖金火光有残骸感"
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
music_mood: 唏嘘/沉稳/暖色叙事（loot-drop 失败复盘调性，中慢板，带克制力量感）

## 素材预判
assets_needed: []   # 纯 CSS/数据可视化即可（融资数字、95%占比、90天时间线、对比双栏）

## 故事板
storyboard:
  narrative_template: "contrast-arc"      # 平淡→对比→震撼→高潮→沉淀（惋惜→剖析→淘金）
  emotion_curve: [0.5, 0.5, 0.75, 0.9, 0.55, 0.4]
  immersion_mode: "story-time"            # 惋惜/共鸣档位映射（柔和+暖色+插画感过渡）
  humor_style: "narration-only"           # 复盘调性偏沉稳，幽默仅旁白轻点（compare 段反差）
  character_presence: true                # 码力角色承载淘金者人设：惋惜=moved、淘金思考=think
  beat_mapping:
    grab: "hook"
    build: "what"
    reveal: "why_fail"
    climax: "loot"
    settle: "compare"
    summon: "compare"

## 五段视觉规划（goldminer 失败复盘结构）
# 1. hook（6s）：「淘金！开淘！」签名开场，引用 components/content/goldminer_intro.html；暖金火光+大字钩子（25亿/90天/烧成灰）；纯钩子不报名
# 2. what（25s）：编程猫登场，hero 公司名+定位 → list 图形化编程产品形态 → data 融资3.6亿美金规模
# 3. why_fail（27s）：timeline 双减时间线 → compare 应试vs素质教育（殃及池鱼）→ highlight 95%违法/90天归零/裁员七成
# 4. loot（26s）：list 三教训（监管集中/订阅死区/转型慢）→ data 订阅死区数字 → highlight 可偷点子CodeQuest（AI老师+出海）
# 5. compare（14s）：compare 双栏（新东方/好未来幸存 vs 编程猫死）+ 讨论CTA

## bg_pool（满足 stage6 R-R-009/010，全片 ≥3 种，相邻场景类型不同）
# radial_beams（hook 暖金光束）/ vignette_glow（what 聚焦）/ gradient_mesh（why_fail 沉重过渡）/ contour_lines（loot 淘金地形）/ noise_field（compare 残骸质感）

## 方向
orientation: portrait
orientation_source: default
