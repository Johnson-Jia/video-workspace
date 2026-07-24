# design.md — 视觉风格方向 + 故事板

## 风格
style: 科技新闻深度解析        # 深色底科技风，数据可视化为主
mood: 紧凑理性 + 数据震撼      # 数据密集型，理性权威感

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/黑底）—— 科技新闻深度感
  accent_cool: 科技蓝 + 紫（Kimi 品牌色 / 性能数据 / 开源属性）
  accent_warm: 数据红（市场下跌：台积电-7%）+ 金色（开源价值 / 榜首）
  text: 白色主 + 浅灰辅 + 数据等宽体强调

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "紧凑专业利落"        # Q1 情感内核：理性数据震撼，科技新闻权威感
    family: "Inter"
    weight: 900
    rationale: "科技新闻深度解析需要紧凑专业的标题字体，传递权威与数据精度"
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
music_mood: 科技/悬疑/紧凑       # 数据密集 + 中美AI竞争张力

## 素材预判
assets_needed:
  - benchmark 数据卡片（SWE-bench 93.4% / Arena Frontend 榜首）
  - 价格对比条（$15 vs $50，1/3）
  - 中国开源模型时间线（DeepSeek → Qwen → Kimi K3）
  - 市场反应数据条（台积电 -7% / Nvidia 失最高市值）
  - 参数柱状图（2.8万亿开源 vs 闭源）

## 故事板
storyboard:
  narrative_template: "contrast-arc"     # 数据对比转折：开源vs闭源 / 中美AI分化
  emotion_curve: [0.7, 0.5, 0.8, 1.0, 0.9, 0.4]   # hook强冲击→分析→对比震撼→开源价值高潮→中美张力→CTA沉淀
  immersion_mode: "versus"               # 对比沉浸：开源vs闭源 / K3 vs Fable / 中美AI
  humor_style: "narration-only"          # 科技新闻严肃调，仅旁白偶尔带点（S7"翻车反而证明需求炸了"）
  character_presence: false              # 科技新闻无码力角色
  beat_mapping:
    grab: "hook（2.8万亿开源+硅谷焦虑）"
    build: "K3是什么（项目身份+发布事件）"
    reveal: "性能对比（benchmark+14项对决）"
    climax: "开源价值 + 中美AI竞争（价格优势+地缘张力）"
    settle: "市场反应 + 火爆证明（数据收尾）"
    summon: "CTA（格局变了）"

## 方向
orientation: portrait
orientation_source: default
