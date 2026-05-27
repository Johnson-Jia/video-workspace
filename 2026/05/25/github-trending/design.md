# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博
mood: 紧凑有力

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝紫渐变）
  accent_cool: 霓虹青/翠绿（用于项目场景、技术标签）
  accent_warm: 金橙/琥珀（用于涨星数据、排名数字、hook）
  text: 白色主 + 浅灰辅

## 配乐方向
music_mood: 科技/赛博/紧凑

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.4, 0.6, 0.8, 1.0, 0.7, 0.5, 0.3, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "topic1"
    reveal: "topic2, topic3"
    climax: "topic4, topic5"
    settle: "topic6"
    summon: "cta"

## 选项目列表（6 个项目，4 新上榜 + 2 连续霸榜）
projects:
  - rank: 1
    full_name: Lum1104/Understand-Anything
    repo: Understand-Anything
    owner: Lum1104
    language: TypeScript
    stars_today: 3999
    stars_total: 27471
    forks: 2337
    description: "把代码变成可交互知识图谱，支持搜索和问答"
    status: 连续霸榜（快速带过）
    category_tag: "代码透视镜"
    selling_points: "代码可视化·交互探索·兼容多平台"
    contrarian_angle: "代码文件不再是死文字，而是可以对话的知识网络"
    commentary: "一天涨近四千星，连续霸榜"

  - rank: 2
    full_name: colbymchenry/codegraph
    repo: codegraph
    owner: colbymchenry
    language: TypeScript
    stars_today: 3003
    stars_total: 23058
    forks: 1269
    description: "预构建的代码知识图谱，100% 本地运行，更少 token 消耗"
    status: 连续霸榜（快速带过）
    category_tag: "代码图谱"
    selling_points: "预构建索引·本地运行·省 token"
    contrarian_angle: "不需要联网就能理解整个代码库的结构"
    commentary: "三千星日增，势不可挡"

  - rank: 3
    full_name: manaflow-ai/cmux
    repo: cmux
    owner: manaflow-ai
    language: Swift
    stars_today: 696
    stars_total: 19145
    forks: 1453
    description: "基于 Ghostty 的 AI 编码终端，带垂直标签和通知系统"
    status: 新上榜
    category_tag: "AI 专属终端"
    selling_points: "AI编码专用·垂直标签·实时通知"
    contrarian_angle: "一个终端窗口就能管理所有 AI 编码代理"
    commentary: "新上榜直接六百星"

  - rank: 4
    full_name: shiyu-coder/Kronos
    repo: Kronos
    owner: shiyu-coder
    language: Python
    stars_today: 106
    stars_total: 25855
    forks: 4499
    description: "金融市场的基础语言模型，理解市场语言"
    status: 新上榜
    category_tag: "金融语言模型"
    selling_points: "市场语言理解·金融专用·基础模型"
    contrarian_angle: "用理解自然语言的方式理解金融市场"
    commentary: "让 AI 听懂市场的声音"

  - rank: 5
    full_name: 666ghj/MiroFish
    repo: MiroFish
    owner: 666ghj
    language: Python
    stars_today: 197
    stars_total: 62296
    forks: 9741
    description: "简洁通用的群体智能引擎，预测万物"
    status: 新上榜
    category_tag: "群体智能"
    selling_points: "群体智能·通用预测·简洁易用"
    contrarian_angle: "不是单个 AI 做决策，而是让一群 AI 像鱼群一样协作预测"
    commentary: "六万星的项目还在涨"

  - rank: 6
    full_name: anthropics/knowledge-work-plugins
    repo: knowledge-work-plugins
    owner: anthropics
    language: Python
    stars_today: 550
    stars_total: 14299
    forks: 1764
    description: "Anthropic 官方开源的知识工作者插件集"
    status: 新上榜
    category_tag: "官方插件库"
    selling_points: "官方出品·知识工作者·开源免费"
    contrarian_angle: "做大模型的公司亲自下场做插件，给知识工作者量身定制"
    commentary: "官方出手，品质有保障"
