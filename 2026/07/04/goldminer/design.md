# design.md — 视觉风格方向 + 故事板

## 风格
style: 淘金暖金风·深科技理性复盘
mood: 痛心警醒+硬朗理性（深科技资金耐力的复杂账）

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深暗底（接近纯黑 #0A0805，残骸煤渣感）
  accent_warm: 暖金/沙金 #FFB800 / #D4A017（残骸里淘到的宝藏意象，金矿筛沙闪光）
  accent_fire: 琥珀火光 #FF6B00（硬朗理性强调色，烧光美金的火焰隐喻 + versus 数据对比硬朗）
  accent_warning: 暗红警示 #B33A3A（SPAC 陷阱/股价崩盘的红色信号）
  text: 白色主 + 浅金辅（关键数字暖金强调）
  rationale: 暖金=淘金宝藏，琥珀火光=烧光+硬朗理性双关，暗红=SPAC/股价崩盘警示

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "毛笔力量"          # Q1 震撼警醒的情感内核需要力量感标题
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "三亿美金烧光的痛心警醒，毛笔体放大教训的重量感"
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
music_mood: 警醒+悬念（紧张低音铺底 + 暖金间歇光晕，匹配理性复盘+痛心警醒调性，区别主轨冷色科技风）

## 素材预判（可选）
assets_needed:
  - 数据对比卡片（$317M 烧光 / $5.2B SPAC 峰估值 / $10→<$1 股价 / 99% 投资者亏损）
  - SPAC 陷阱 vs 私下融资 对比双栏（why_fail 段）
  - HaulOS 转采矿/工业场景示意图（loot 段，geofence 受限场景）
  - 深科技失败三连对比（compare 段，Embark/Plenty/K-Scale）

## 故事板
storyboard:
  narrative_template: "showdown"          # 失败 vs 教训交锋结构（深科技时间线 vs 投资者耐力线 vs SPAC 锁死炸弹）
  emotion_curve: [0.5, 0.6, 0.85, 0.95, 0.7, 0.5]  # hook 痛心 → what 引入 → why_fail 反直觉高潮 → loot 淘金价值 → compare 对比沉淀 → summon 讨论
  immersion_mode: "versus"                # 理性档位：数据对比+硬朗 #FF6B00（深科技复杂商业逻辑，资金耐力 vs 时间线 vs SPAC 三方对比）
  humor_style: "narration-only"           # 失败复盘不宜视觉幽默，仅旁白偶有淘金者吐槽
  character_presence: true                # 码力角色承载淘金者人设（警醒=think，痛心=moved）
  beat_mapping:
    grab: "hook"
    build: "what"
    reveal: "why_fail"
    climax: "loot"
    settle: "compare"
    summon: "CTA"

## 视觉识别符（goldminer 专栏签名）
visual_signature:
  开场动画: hook 场景引用 goldminer 暖金放大镜+筛沙闪光（"淘金！开淘！"签名）
  标志符号: 淘金者剪影/宝藏箱图标（角落小标）
  对比呈现: compare 段用双栏主角 vs related 深科技失败衬托

## 方向
orientation: portrait
orientation_source: category_hint   # goldminer 分类默认竖屏
