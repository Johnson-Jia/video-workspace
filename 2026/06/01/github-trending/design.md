# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 信息密度高、节奏紧凑（涨星数据驱动的兴奋感）

## 方向
orientation: portrait
orientation_source: duration
width: 1080
height: 1920

## 配色方向
color_direction:
  background: 深邃暗蓝（#0a0e1a 级别，开发者暗色调）
  accent_primary: 橙金色（涨星数据、排名数字——数据冲击力）
  accent_secondary: 青蓝色（项目名、技术标签——科技感）
  accent_highlight: 翠绿（核心卖点词——行动感）
  text: 白色主 + 浅灰辅
  code: 语法高亮色系

## 配乐方向
music_mood: 科技/电子 — 节奏紧凑的信息流配乐，有推进感但不抢旁白
bgm_candidates:
  - "tech-electronic 系列（快速信息流节奏）"
  - "upbeat-corporate 系列（专业+节奏感）"

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "listicle"
  emotion_curve: [0.8, 0.7, 0.7, 0.65, 0.6, 0.65, 0.6, 0.5]
  immersion_mode: "rapid-fire"
  humor_style: "none"
  character_presence: false
  beat_mapping:
    grab: "hook（涨星总览 + 最高数据锚定）"
    items: "6个项目逐一展示（每人独占一屏）"
    summon: "CTA（关注我，下期见）"

## 场景规划（8 场景，竖屏标准模式）
scenes:
  - id: hook
    beat: grab
    focus: "6月1日涨星总览：单日最高近三千星"
    visual_concept: "大号数字冲击 + 涨星数据流动画，金色高亮"

  - id: p1-markitdown
    beat: items
    focus: "microsoft/markitdown — 微软出品，2759★/天，134K★，万物皆可 Markdown"
    visual_concept: "文件格式图标堆叠 → 全部转为 Markdown 的流光效果"

  - id: p2-moneyprinter
    beat: items
    focus: "MoneyPrinterTurbo — 74K★，AI 视频生成，文字变视频"
    visual_concept: "文字输入框 → 视频播放器的转化动画"

  - id: p3-voxcpm
    beat: items
    focus: "VoxCPM — 无分词器 TTS，端到端语音合成，声音克隆"
    visual_concept: "声波图形 + 跳过分词器的架构对比"

  - id: p4-train-llm
    beat: items
    focus: "train-llm-from-scratch — 从零训练大模型教程"
    visual_concept: "代码流 + Notebook 界面风格 + 神经网络拓扑"

  - id: p5-nomad
    beat: items
    focus: "project-nomad — 断网也能用的离线 AI 生存电脑"
    visual_concept: "断网图标 + 本地工具箱展开，赛博朋克离线感"

  - id: p6-compound
    beat: items
    focus: "compound-engineering-plugin — Claude Code/Cursor 工程插件"
    visual_concept: "多工具 logo 汇聚 + 插件连接线"

  - id: cta
    beat: summon
    focus: "关注我，下期见"
    visual_concept: "频道品牌收束 + 简洁 CTA"
