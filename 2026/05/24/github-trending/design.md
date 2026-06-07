# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博
mood: 紧凑爆发

## 配色方向
color_direction:
  background: 深色暗调（接近纯黑 #0a0a1a）
  accent_cool: 霓虹青 #00D4FF（用于项目展示场景）
  accent_warm: 金橙色 #FF8C32（用于 hook/CTA 场景）
  text: 白色主 + 浅灰辅

## 配乐方向
music_mood: 科技/赛博/紧凑

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.3, 0.5, 0.8, 1.0, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "topic1, topic2"
    reveal: "topic3, topic4"
    climax: "topic5"
    settle: "topic6"
    summon: "cta"

## 选取项目（6 个）
projects:
  - rank: 1
    full_name: "multica-ai/andrej-karpathy-skills"
    contrarian_angle: "只用一个 CLAUDE.md 文件，就能让所有 AI 编程助手变强，不需要装任何插件"
    label: "Karpathy 秘籍"
    selling_points: "零配置·全平台兼容·立竿见影"
    commentary: "一天涨三千星，开发者用脚投票"

  - rank: 2
    full_name: "colbymchenry/codegraph"
    contrarian_angle: "不读代码就能理解整个项目——预索引知识图谱，本地运行不联网"
    label: "代码透视镜"
    selling_points: "预索引·本地运行·省Token"
    commentary: "涨星近两千五，效率工具真需求"

  - rank: 3
    full_name: "Lum1104/Understand-Anything"
    contrarian_angle: "把任何代码库变成可交互知识图谱，像用地图导航一样理解代码"
    label: "知识图谱生成器"
    selling_points: "可交互·多平台支持·实时问答"
    commentary: "两天累计两万星，速度惊人"

  - rank: 4
    full_name: "presenton/presenton"
    contrarian_angle: "一句话就能生成专业演示文稿，Gamma 的开源替代品"
    label: "AI 演示文稿"
    selling_points: "开源免费·API 可调用·一键生成"
    commentary: "新上榜就冲上来了"

  - rank: 5
    full_name: "NVlabs/LongLive"
    contrarian_angle: "NVIDIA 出品，用 NVFP4 量化做实时长视频生成，专业级压缩"
    label: "NVIDIA 长视频"
    selling_points: "实时生成·NVFP4量化·并行推理"
    commentary: "NVIDIA 出手就是不一样"

  - rank: 6
    full_name: "anthropics/claude-plugins-official"
    contrarian_angle: null
    label: "连续霸榜"
    selling_points: "官方出品·高质量插件·持续更新"
    commentary: "连续两天霸榜，又涨两千星"
