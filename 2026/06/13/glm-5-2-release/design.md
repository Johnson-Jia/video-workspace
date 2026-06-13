# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗调科技·色温翻转
mood: 震撼·升华

## 导演 5 问（驱动风格推导）
- Q1 情感内核：理想主义的震撼——最强模型因国家安全下架，国产同日开源。力量感 + 希望感交织。
- Q2 观众感受：先倒吸一口凉气（这么强的模型说没就没），再心头一热（有人在开门）。
- Q3 视觉手段：色温翻转作为核心语言——前段冷色（墙/禁锢/封禁），后段暖光破入（路/开放/破晓）。
- Q4 相邻反差：关门场景钢蓝冷峻，开门场景琥珀暖光，同帧对照制造张力。
- Q5 视线焦点：数据锚点（5742 万、4 天、1M）+ 两张官方推文截图作为视觉证据。

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（近纯黑深蓝灰，营造封闭与厚重）
  accent_cool: 钢蓝/冷青（关门阶段：封闭、禁锢、冷峻，对应"墙"的意象）
  accent_warm: 琥珀金/暖橙（开门阶段：开放、破晓、希望，对应"路"的意象）
  text: 白色主 + 浅灰辅
  note: 全片以色温翻转为核心视觉语言——前段冷色（墙/禁锢），后段暖光破入（路/开放）；高潮场景冷暖同框对照。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "紧凑/专业/利落"
    family: "Inter"
    weight: 900
    rationale: "科技新闻的力量感与冷峻；几何简洁传递墙与路的对照冲击，比毛笔体更贴合现代 AI 议题"
    fallback: "'Inter','Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 史诗科技（前段紧张低沉鼓点 → 后段希望弦乐上扬，呼应色温翻转）

## 素材预判
assets_needed:
  - assets/anthropic-ban.png   # 关门证据（海外公司官方推文截图）
  - assets/glm52-open.png      # 开门证据（智谱官方推文截图）

## 故事板
storyboard:
  narrative_template: "contrast-arc"   # 平淡→对比→震撼→高潮→沉淀，天然匹配双线对照
  emotion_curve: [0.9, 0.6, 0.7, 1.0, 0.6, 0.8]   # grab最强→climax峰值→summon共鸣
  immersion_mode: "hyper-pace"          # 科技赛博暗调，支撑数据密集与快节奏对照
  humor_style: "narration-only"         # 严肃震撼向，纯旁白叙事，不注入视觉幽默
  character_presence: false             # 新闻评论质感，不启用吉祥物角色
  beat_mapping:
    grab: "钩子：最强模型 4 天下架"
    build: "关门：国家安全·立即禁用"
    reveal: "转折：同日有人开门"
    climax: "高潮：开源宣言·1M·属于所有人"
    settle: "沉淀：墙与路的对照"
    summon: "召唤：智能属于所有人 + CTA"

## 方向
orientation: portrait
orientation_source: default
