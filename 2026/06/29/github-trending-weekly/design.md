# design.md — 第27周 GitHub Trending 周榜视频

## 风格
style: 周榜暗色科技风
mood: 紧凑信息密集（周榜盘点，14项目高密度输出）

## Q1 情感内核（导演 5 问）
紧凑专业的「信息盘点感」+ 周次身份锚定带来的「系列感」+ 数字震撼（一周涨近1.9万星）。观众听完后应该感觉："这一周 GitHub 圈发生了这么多大事，我必须跟上"。

## 配色方向（描述性，5领域色彩区分是本期核心记忆点）
color_direction:
  background: 深蓝/深紫渐变基底（接近纯黑，#0A0E27 → #1A0B2E），周汇总主调，营造"一周合集"的厚重感
  accent_cool: 霓虹青蓝 #4DA8DA（AI Agent 领域主色，承载数据/技术含量感）
  accent_warm: 暖橙 #FF8C32（视频媒体创作领域主色 + hook/CTA 强调双光晕的暖端）
  domain_palette:
    ai_agent: 冷蓝 #4DA8DA        # 4项目，AI编程/记忆
    video_media: 暖橙 #FF8C32     # 3项目，AI视频/语音
    ai_tools: 紫 #9B6BFF          # 3项目，开发工具
    data_finance: 金 #F9A825      # 2项目，情报看板
    security_privacy: 绿 #3CC68A  # 2项目，安全隐私
  accent_dual_glow: 橙金双光晕（#FF8C32 + #F9A825），用于 hook/CTA/最高涨幅项目 OpenMontage 的视觉爆破
  text: 白色主（#FFFFFF）+ 浅灰辅（#B8C5D6），领域标题用对应领域色

> 5领域色彩是本期最强的视觉记忆锚点：每个领域分组场景用对应领域色作为标题/边框/光晕，观众一眼分辨"现在讲到哪个领域了"。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "紧凑专业"
    family: "Inter"
    weight: 900
    rationale: "周榜信息密度高，紧凑利落的几何简洁体能承载密集数据而不显拥挤，比毛笔/衬线更适合盘点类"
    fallback: "'Inter','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 500
    rationale: "正文可读性优先，中文项目名/利益描述"
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 800
    rationale: "周涨幅数字（+18703/+8926）和数据用等宽体，对齐感和极客气质"
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 暗色科技/紧凑电子（cinematic electronic / tech pulse / dark synthwave）。周榜盘点需要持续推进的脉冲感，AI 项目占多数（>50%）适配霓虹蓝紫主调。BPM 偏快但留旁白呼吸空间，避免抢旁白。

## 素材预判
assets_needed: []   # 纯 CSS/HTML 实现领域色彩分组、光晕、数据计数动画，无需外部素材

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.5, 0.6, 0.8, 1.0, 0.7, 0.4]
  immersion_mode: "hyper-pace"
  immersion_rationale: "AI 项目 >50%（4 AI Agent + 3 AI工具 + 视频媒体多含AI = 10/14），周榜盘点高信息密度，霓虹蓝紫为主调符合 hyper-pace 适用场景"
  humor_style: "dual-track"
  character_presence: true
  character_appearance: "climax 节拍（OpenMontage 最高涨幅爆破）必出 explode 表情；settle 节拍（安全领域）可出 tease/moved"
  beat_mapping:
    grab: "hook（周次+数字锚定）"
    build: "ai_agent 分组（最高涨幅领域，引出周榜主体）"
    reveal: "video_media + ai_tools 分组（揭示更多AI创作工具）"
    climax: "data_finance 分组（最高涨幅的金融情报项目冲击）"
    settle: "security_privacy 分组（隐私安全冷却思考）"
    summon: "CTA（第27周周榜收尾，下周见）"

## 场景规划（7场景：hook + 5领域分组 + CTA）
scenes_plan:
  - id: hook
    duration: 4s
    type: hook
    beat: grab
    note: "周次+数字锚定（'第27周，6月22到29日，最高一周涨了近1.9万星'），前5秒零废话，橙金双光晕爆破"
  - id: ai_agent
    duration: 10s
    type: features
    beat: build
    domain_color: "#4DA8DA 冷蓝"
    projects: ["OpenMontage +18703", "codebase-memory-mcp +8926", "Agent-Reach +7692", "cognee +6064"]
    note: "4项目分组场景，时长10s → visual_phases ≥2（按规则10-20s≥2 phase）"
  - id: video_media
    duration: 8s
    type: features
    beat: reveal
    domain_color: "#FF8C32 暖橙"
    projects: ["palmier-pro +5034", "voicebox +3883", "design.md +6728"]
    note: "3项目分组场景，时长8s → visual_phases ≥2"
  - id: ai_tools
    duration: 7s
    type: features
    beat: reveal
    domain_color: "#9B6BFF 紫"
    projects: ["orca +2769", "page-agent +1778", "agent-native +1540"]
    note: "3项目分组场景，时长7s → visual_phases ≥2"
  - id: data_finance
    duration: 7s
    type: capabilities
    beat: climax
    domain_color: "#F9A825 金"
    projects: ["daily_stock_analysis +7045", "worldmonitor +2845"]
    note: "2项目分组场景，climax节拍最高视觉浓度，时长7s → visual_phases ≥2"
  - id: security_privacy
    duration: 6s
    type: features
    beat: settle
    domain_color: "#3CC68A 绿"
    projects: ["Anthropic-Cybersecurity-Skills +5212", "simplex-chat +3218"]
    note: "2项目分组场景，settle冷却，时长6s → visual_phases ≥2"
  - id: cta
    duration: 5s
    type: cta
    beat: summon
    note: "'第27周周榜就到这，关注GitHub星探，下周见' + 中性互动'想试试哪个'"

## 方向
orientation: portrait
orientation_source: default
orientation_rationale: "GitHub 分类无 landscape hint，默认竖屏（抖音主战场）。5领域垂直分组天然适配竖屏纵深，每个领域场景纵向信息层叠"
