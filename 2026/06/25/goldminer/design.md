# design.md — 视觉风格方向 + 故事板

## 风格
style: 淘金暖金风·警醒复盘（残骸里淘金，深色底+暖金宝藏意象）
mood: 警醒痛心+理性剖析（监管套利=定时炸弹的复盘语气，不是吃瓜嘲讽）

## 配色方向（描述性，goldminer 暖金视觉 IP）
color_direction:
  background: 深色底（接近纯黑 #0A0805，烘托暖金光感）
  accent_warm_primary: 暖金/沙金（#FFB800/#D4A017，残骸淘金主色，hook/CTA/数据高亮）
  accent_warm_fire: 琥珀火光（#FF6B00，警示/监管重锤/庞氏崩塌强调）
  text: 白色主 + 浅灰辅（数据/英文配暖金高亮）
  rationale: 暖金=残骸里淘到的宝藏意象；琥珀火光=警示与崩塌的张力；深色底让暖色更突出（短视频黄金法则）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "毛笔力量"          # Q1 警醒痛心的情感内核需要力量感的标题字体（敲击感=监管重锤）
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "金融覆灭的警醒感+淘金开场签名，毛笔力量既能承载'淘金！开淘！'的干脆，也能承载'5000清零'的重量"
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
music_mood: 警醒复盘/低沉紧张带暖意（淘金者开场+金融崩塌剖析，开头暖金上升感，why_fail 段落转向低沉警示，loot 段回暖）
music_keywords: "cinematic tension, reflective, gold rush ambient, dark strings, cautionary"

## 素材预判（CSS/HTML 即可实现，无需外部素材）
assets_needed:
  - "5000→0 行业清零数字计数动画（why_fail 段）"
  - "庞氏死亡螺旋循环示意图（why_fail 段，新钱还旧钱的环形箭头）"
  - "$7.6B e租宝 引爆点（数据卡片）"
  - "CreditOS 卖铲子架构图（loot 段：银行←API→风控）"
  - "微贷网 vs 千和 双栏对比（compare 段）"

## 故事板
storyboard:
  narrative_template: "contrast-arc"    # 平淡(是什么) → 对比(为什么死/庞氏反直觉) → 震撼(5000清零) → 高潮(CreditOS 淘金) → 沉淀(对比+讨论)
  emotion_curve: [0.4, 0.5, 0.85, 1.0, 0.6, 0.45]   # hook 好奇→what 铺陈→why_fail 震撼反差→loot 淘金高潮→compare 沉淀→CTA 行动
  immersion_mode: "contrast-arc"        # goldminer.md 警醒档位映射：对比复盘+暖金
  humor_style: "narration-only"         # 失败复盘偏严肃，仅旁白偶尔反差吐槽（不视觉化幽默）
  character_presence: true              # 码力角色承载淘金者人设
  character_code: "think"               # 警醒档位 → think（剖析思考）表情为主
  beat_mapping:
    grab: "hook"                        # 淘金签名 + 5000清零反差钩子
    build: "what"                       # 微贷网是什么 + P2P 规模铺陈
    reveal: "why_fail"                  # 监管清退+庞氏死亡螺旋（反直觉核心揭示）
    climax: "loot"                      # CreditOS 卖铲子淘金点子（淘金高潮）
    settle: "compare"                   # 千和对比衬托（同卵双生死法）
    summon: "compare"                   # 讨论 CTA（卖铲子能不能成）

## 方向
orientation: portrait
orientation_source: user_explicit       # 项目参数明确指定 portrait（竖屏抖音）

## 角色人设备注（goldminer 淘金者第一人称）
- 全程"我"视角："我扒了微贷网""我淘到一个教训""我觉得这个点子能成"
- 态度：惋惜（曾经金融创新标杆）+ 警醒（监管套利是定时炸弹）+ 淘金（CreditOS 卖铲子思路值得偷）
- hook 签名「淘金！开淘！」固定开场（听觉识别符）
