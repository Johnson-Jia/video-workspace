# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风（冷色主+暖强调）
mood: 紧凑专业·带反差冲击

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑/深蓝/深紫渐变基底）
  accent_cool: 深蓝/翠青（用于 AI/推理/学习类场景，理性沉稳）
  accent_warm: 橙色/金色（用于 hook/CTA/星标/反差强调）
  text: 白色主 + 浅灰辅
  text_shadow: 极淡 drop（rgba(30,41,59,0.08)），禁发光
  gradient_rule: 渐变文字禁白色端点，用同色系高饱和（橙 #FF8C32→#FB923C→#FDBA74 / 蓝 #4DA8DA→#60A5FA→#93C5FD / 金 #FBBF24→#F59E0B→#FCD34D）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"            # Q1: 紧凑专业利落（标准 GitHub 暗色科技风）
    family: "Inter"
    weight: 900
    rationale: "科技盘点调性需要紧凑专业的几何标题字体，避免装饰字体分散数字注意力"
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
music_mood: 科技/低调电子（clean-corporate 首选，衬底不抢旁白；禁 bold-energetic/epic-trailer 抢人声）

## 素材预判
assets_needed: []
# 项目 avatar 已预下载到 assets/avatars/，无需额外素材
# 数据卡/星标全 CSS 渐变实现，无外部图

## 故事板
storyboard:
  narrative_template: "contrast-arc"   # 反差钩子 → 项目展开 → 反差收束
  emotion_curve: [0.4, 0.5, 0.7, 0.85, 0.6, 0.4]  # hook 反差低开 → 项目展开渐升 → build-your-own-x 一带而过（不冲高潮）→ CTA 沉淀
  immersion_mode: "hyper-pace"          # 多项目快速播报，AI 类占一半
  humor_style: "narration-only"         # 旁白类比/吐槽点缀，视觉保持科技沉稳
  character_presence: true              # 启用码力角色
  beat_mapping:
    grab: "hook（airllm 反差钩子）"
    build: "airllm 展开"
    reveal: "lingbot-map 3D 反差 + ui-skills 跨圈"
    climax: "ai-engineering 学习资源 + ossie apache 背书"
    settle: "build-your-own-x 一带而过（增量）"
    summon: "CTA 中性二选一"

## 方向
orientation: portrait
orientation_source: category_hint   # github 分类默认竖屏（抖音）
