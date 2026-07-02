# design.md — 视觉风格方向 + 故事板（goldminer 创业淘金者 · Xiaoming Bike）

## 风格
style: 淘金暖金风（残骸淘金 = 宝藏意象）      # goldminer IP 视觉，区别主轨冷色科技风
mood: 警醒痛心（Bonfire 烧钱教训）              # 情绪档位：警醒

## 配色方向（描述性，深色底 + 暖金/琥珀火光）
color_direction:
  background: 深棕黑底（接近 #0A0805，残骸/墓地夜色感）
  accent_gold: 暖金/沙金（#FFB800 / #D4A017，宝藏/残骸里淘到的金子）
  accent_amber: 琥珀火光（#FF6B00，烧钱的"火" + 火光强调）
  accent_warn: 暗红警示（#8B2500，补贴战/死亡警示，节制使用）
  text: 米白主（#F5E6C8）+ 浅金辅（#D4A017）
  card_bg: 深棕不透明（rgba(26,16,8,0.88)）— 卡片背景 alpha≥0.7 挡 fx 光晕透字
  rule: 渐变禁纯白端点（director_gate 查）；glow blur≤30px

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "毛笔力量"          # Q1 情感内核 = 震撼/警醒（1500万 vs 22亿美金的悬殊死法）
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "创业失败的震撼警醒内核需要毛笔力量感标题，淘金者人设的厚重感"
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
music_mood: 暖金励志 / 史诗警醒（loot 段给希望，why_fail 段克制悲壮）— BGM 暖金/励志方向，区别主轨科技冷感

## 素材预判
assets_needed:
  - 共享单车残骸/墓地意象（CSS 实现：单车剪影 + 暖金光晕）
  - 数字对比（1500万 vs 22亿 vs 9亿，纯 CSS 大字 + 数据条）
  - FleetOS SaaS 卖铲子图示（CSS：铲子图标 + 平台分层）

## 故事板（5 段失败复盘 + showdown 悬殊对决）
storyboard:
  narrative_template: "showdown"              # 1500万 vs 22亿美金的悬殊对决
  emotion_curve: [0.5, 0.4, 0.7, 0.9, 0.6, 0.5]   # grab(钩子震撼)→build(是什么铺陈)→reveal(死因反直觉)→climax(数学残酷顶点)→settle(教训沉淀)→summon(可偷点子+CTA)
  immersion_mode: "contrast-arc"              # 对比复盘 + 暖金 #FFB800（警醒档映射）
  humor_style: "narration-only"               # 失败复盘不宜视觉幽默，旁白带淘金者态度
  character_presence: true                    # 码力角色承载淘金者人设（惋惜=moved/警醒=think）
  scenes:                                     # 5 段失败复盘结构
    - hook:     "「淘金！开淘！」+ 1500万 vs 22亿美金的数据钩子（不报名）"
    - what:     "Xiaoming Bike 是什么 + 融资1500万 + 共享单车行业（报项目名大字）"
    - why_fail: "死因：超本地密度战 + 数学残酷（6万辆 vs 1000万辆）"
    - loot:     "教训：资本密集赢家通吃 + 可偷点子：FleetOS 卖铲子"
    - compare:  "对比 Gobee.bike 同行业 + Magic Ears 跨行业（双减）+ 讨论 CTA"
  beat_mapping:
    grab: "hook"
    build: "what"
    reveal: "why_fail"
    climax: "why_fail(数学残酷顶点)"
    settle: "loot(教训沉淀)"
    summon: "loot(可偷点子) + compare(CTA)"

## 方向
orientation: portrait
orientation_source: default
