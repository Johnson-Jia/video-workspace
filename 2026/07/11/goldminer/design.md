# design.md — 视觉风格方向 + 故事板

## 风格
style: 淘金暖金风（残骸淘金=宝藏意象）        # goldminer 分类 IP，区别主轨冷色科技风
mood: 警醒痛心 + 惋惜剖析                       # 单位经济失败的「警醒」档位，配惋惜内核

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深暗暖底（接近纯黑带暖调，#0A0805 方向，衬托暖金发光）
  accent_warm: 暖金/沙金主色（#FFB800/#D4A017 方向，残骸里的宝藏意象，全片主视觉）
  accent_fire: 琥珀火光强调色（#FF6B00 方向，用于关键数据/死因/警告高亮）
  accent_contrast: 冷绿点缀（仅用于「可偷点子」loot 段，区分教训 vs 收获）
  text: 暖白主 + 浅沙金辅（暖底上不用纯白，用暖白避免冷感）

## 字体（三层 + voice 链接情感内核）
fonts:
  title:
    voice: "残骸筛金的力量感"        # 链接情感内核：1.9亿用户崩盘的震撼 + 淘金者第一人称
    family: "Ma Shan Zheng"           # 毛笔体，承载「淘金！开淘！」签名的力量
    weight: 400
    rationale: "失败复盘的痛心警示 + 淘金者人设需要毛笔力量的标题字体，与暖金风 IP 一致"
    fallback: "'Ma Shan Zheng','PingFang SC','Microsoft YaHei',cursive"
  body:
    voice: "客观复盘的清晰"
    family: "Noto Sans SC"
    weight: 400
    rationale: "死因剖析/数据陈述需高可读性中性字体，与毛笔标题形成对比"
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    voice: "数字锚定的厚重"
    family: "JetBrains Mono"
    weight: 700
    rationale: "$187M / 1.9亿用户 / 2-5%转化率等数字锚点需等宽厚重字体强化冲击"
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 影视化暖金悬疑 + 警示节奏（非主轨电子激昂；loot 段转沉稳希望感）
# 暖金风的失败复盘：hook 用低沉悬疑+定音鼓（警醒），why_fail 用紧张弦乐堆叠（三重失败递进），loot 段转温暖木管+轻颗粒感（淘到宝的收获感），compare 段用余韵收尾

## 素材预判（可选）
assets_needed: []       # goldminer 是数据驱动复盘，无需外部素材，全靠组件库+数据可视化

## 故事板
storyboard:
  narrative_template: "showdown"       # 失败 vs 教训的交锋结构（虚荣指标 vs 单位经济）
  emotion_curve: [0.5, 0.6, 0.85, 0.95, 0.55, 0.4]   # hook警醒→what平稳→why_fail紧张攀升→why_fail climax→loot缓和希望→compare余韵
  immersion_mode: "contrast-arc"        # goldminer 警醒档位对应 contrast-arc（对比复盘+暖金）
  humor_style: "narration-only"         # 失败复盘庄重，仅旁白承载态度，不加视觉幽默
  character_presence: true              # 码力角色承载淘金者人设：警醒=think 姿态，惋惜=moved 姿态
  beat_mapping:                         # 节拍 → 场景映射（5 段失败复盘）
    grab: "hook"                        # 「淘金！开淘！1.9亿用户怎么就死在这个数字上」
    build: "what"                       # 沪江做什么 + 融资 + 规模铺垫
    reveal: "why_fail"                  # 死因三重递进揭示（获客/毛利/漏斗）
    climax: "why_fail_peak"             # 2018 IPO 招股书暴露真相 = 死因高潮
    settle: "loot"                      # 教训 + 可偷点子（淘金核心，温暖转色）
    summon: "compare_CTA"               # 对比衬托 + 讨论问题

## 五段场景情绪规划（goldminer 失败复盘五段）
scenes_emotion:
  - scene: "hook"
    emotion: "警醒"
    color_focus: "琥珀火光强调（#FF6B00 方向）爆闪 + 暖金大字"
    visual_signature: "「淘金！开淘！」签名 + 1.9亿用户数字粉碎/裂解特效"
  - scene: "what"
    emotion: "客观陈述"
    color_focus: "暖金主色稳定铺底"
    visual_signature: "沪江公司信息卡 + 17年时间轴 + 融资阶梯"
  - scene: "why_fail"
    emotion: "紧张剖析（三重递进）"
    color_focus: "琥珀火光渐强 + 冷绿警示点缀（LTV/CAC倒挂数据）"
    visual_signature: "三重失败堆叠呈现：CAC$100-200 vs ARPU$50-80 对比柱 / 师生绕开抽佣流程图 / 2-5%漏斗"
  - scene: "loot"
    emotion: "淘到宝的收获感"
    color_focus: "暖金回暖 + 冷绿希望色（可偷点子）"
    visual_signature: "教训清单 + AI原生垂直培训平台点子卡（区别沪江横向的「垂直」视觉）"
  - scene: "compare_CTA"
    emotion: "余韵 + 互动"
    color_focus: "暖金收束"
    visual_signature: "CompareSplit 双栏（沪江 vs 魔力耳朵/Qkids/Changingedu，同行业不同死法）"

## 方向
orientation: portrait   # 抖音竖屏，goldminer 默认
orientation_source: category_hint   # goldminer 分类默认竖屏（与主轨一致）
