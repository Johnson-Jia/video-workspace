# design.md — 视觉风格方向 + 故事板

## 风格
style: 淘金暖金风（残骸淘金=宝藏意象）        # goldminer 分类 IP，区别主轨冷色科技风
mood: 共鸣惋惜 + 警醒剖析                       # 双减监管一刀切的「共鸣」档位，配惋惜内核

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深暗暖底（接近纯黑带暖调，#0A0805 方向，衬托暖金发光）
  accent_warm: 暖金/沙金主色（#FFB800/#D4A017 方向，残骸里的宝藏意象，全片主视觉）
  accent_fire: 琥珀火光强调色（#FF6B00 方向，用于双减公文封禁/裁员 80%/死因警告高亮）
  accent_contrast: 冷绿点缀（仅用于 loot 段「可偷点子」AI pivot 卡片，区分教训 vs 收获）
  text: 暖白主 + 浅沙金辅（暖底上不用纯白，用暖白避免冷感）
  # 渐变同色系（金/琥珀），禁白端点；text-shadow 极淡 alpha≤0.6

## 字体（三层 + voice 链接情感内核）
fonts:
  title:
    voice: "残骸筛金的力量感"        # 链接情感内核：5.93亿烧光的震撼 + 双减一刀切的惋惜
    family: "Ma Shan Zheng"           # 毛笔体，承载「淘金！开淘！」签名的力量
    weight: 400
    rationale: "双减监管典型失败复盘的惋惜警示 + 淘金者人设需要毛笔力量的标题字体，与暖金风 IP 一致"
    fallback: "'Ma Shan Zheng','PingFang SC','Microsoft YaHei',cursive"
  body:
    voice: "客观复盘的清晰"
    family: "Noto Sans SC"
    weight: 400
    rationale: "双减政策剖析/数据陈述需高可读性中性字体，与毛笔标题形成对比"
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    voice: "数字锚定的厚重"
    family: "JetBrains Mono"
    weight: 700
    rationale: "$593M / 5.93亿美元 / 裁员80%+ 等数字锚点需等宽厚重字体强化冲击"
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 影视化暖金悬疑 + 警示节奏（非主轨电子激昂；loot 段转沉稳希望感）
# 暖金风的失败复盘：hook 用低沉悬疑+定音鼓（警醒），why_fail 用紧张弦乐堆叠（双减三重禁令递进），loot 段转温暖木管+轻颗粒感（淘到宝的收获感），compare 段用余韵收尾

## 素材预判（可选）
assets_needed: []       # goldminer 是数据驱动复盘，无需外部素材，全靠组件库+数据可视化

## 故事板
storyboard:
  narrative_template: "contrast-arc"   # 暗调（双减政策）→ 金转折（教训与可偷点子淘金）的对比弧线
  emotion_curve: [0.85, 0.55, 0.8, 0.95, 0.5]   # 5 元素：hook警醒强→what客观平稳→why_fail紧张攀升→loot淘金高光→compare余韵惋惜
  immersion_mode: "contrast-arc"        # goldminer 共鸣档位对应 contrast-arc（暗→金转折复盘）
  humor_style: "narration-only"         # 失败复盘庄重，仅旁白承载态度，不加视觉幽默
  character_presence: true              # 码力角色承载淘金者人设：警醒=think 姿态，惋惜=moved 姿态
  beat_mapping:                         # 节拍 → 场景映射（5 段失败复盘，5 元素 emotion_curve）
    grab: "hook"                        # 「淘金！开淘！5.93亿几周归零」签名+数字粉碎
    build: "what"                       # 火花思维做什么 + 融资 $593M + 规模铺垫
    reveal: "why_fail"                  # 双减政策三重禁令剖析（禁营利/禁外资/禁周末）
    climax: "loot"                      # 三教训 + AI 协作数学平台 pivot 点子（淘金核心）
    settle: "compare_CTA"               # 同行转型对比 + 签名收尾

## 五段场景情绪规划（goldminer 失败复盘五段）
scenes_emotion:
  - scene: "hook"
    emotion: "警醒共鸣"
    color_focus: "琥珀火光强调（#FF6B00 方向）爆闪 + 暖金大字"
    visual_signature: "「淘金！开淘！」签名 + 「5.93亿」数字粉碎/钱袋破裂特效"
  - scene: "what"
    emotion: "客观陈述"
    color_focus: "暖金主色稳定铺底"
    visual_signature: "火花思维公司名片卡 + K9数学小班直播场景 + $593M 融资阶梯"
  - scene: "why_fail"
    emotion: "紧张剖析（双减三重禁令）"
    color_focus: "琥珀火光渐强 + 冷绿警示点缀（裁员 80% 数据）"
    visual_signature: "双减公文印章+三重禁令堆叠 → 裁员80%+ 业务停止大字"
  - scene: "loot"
    emotion: "淘到宝的收获感"
    color_focus: "暖金回暖 + 冷绿希望色（AI pivot 点子）"
    visual_signature: "三教训金条逐条亮 + AI协作数学平台 pivot 卡（金币堆+75%毛利）"
  - scene: "compare_CTA"
    emotion: "余韵惋惜 + 签名收束"
    color_focus: "暖金收束"
    visual_signature: "CompareSplit 双栏（火花❌卡死K9 vs 学而思/猿辅导✓转型活下来）+「淘金！开淘！」签名章"

## 方向
orientation: portrait   # 抖音竖屏，goldminer 默认
orientation_source: category_hint   # goldminer 分类默认竖屏（与主轨一致）
