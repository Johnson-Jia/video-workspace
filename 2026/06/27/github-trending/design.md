# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技工具风（深蓝紫底 + 橙金强调）
mood: 紧凑利落、工具感、节奏明快

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑的深蓝紫渐变，让亮色工具卡片浮起来）
  accent_cool: 霓虹青/电光蓝（用于 AI 类项目场景：design.md / Agent-Reach / MinerU）
  accent_warm: 金橙/琥珀（用于 hook/CTA/老牌项目：CasaOS / simplex-chat 收尾）
  text: 白色主 + 浅灰辅（项目名白色突出，描述浅灰退后）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "本期是工具盘点，情感内核是『紧凑/专业/利落』——几何简洁的标题字体最贴合工具感，每张卡片的项目名和排名数字都要利落有力"
    fallback: "'Inter','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/利落节奏（轻电子，节奏明快不抢旁白，工具感）

## 素材预判
assets_needed: []
# 头像已就位（assets/avatars/），ProjectFullCard 用；纯 CSS/HTML 实现排名数字、星标增量、卖点卡片，无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"    # 6 项目多样对比，从平淡榜单到 simplex-chat 反直觉收尾
  emotion_curve: [0.35, 0.5, 0.7, 0.85, 0.6, 0.45]  # hook 抓眼→项目递进→design.md/Agent-Reach 高潮→CasaOS 沉淀→simplex 收尾召唤
  immersion_mode: "contrast-arc"        # 默认对比弧，6 项目独占场景做视觉对比（按 github.md immersion_mapping，工具类无单一标签主导时用默认 contrast-arc）
  humor_style: "narration-only"         # 旁白层幽默（开发者文化梗/生活类比），视觉层保持工具感的精致利落
  character_presence: true              # 启用码力角色，工具盘点视频角色增强记忆点
  beat_mapping:
    grab: "hook"                        # 黄金 3 秒纯钩子：数字 + 工具利益
    build: "design.md"                  # 第一项目：建立「工具盘点」基调
    reveal: "Agent-Reach"               # AI 联网能力揭示
    climax: "TREK + MinerU"             # 高潮：自托管工具 + 文档转 AI（最实用）
    settle: "CasaOS"                    # 老牌快速带过沉淀
    summon: "simplex-chat + CTA"        # 反直觉收尾 + 二选一提问

## 方向
orientation: portrait
orientation_source: default
