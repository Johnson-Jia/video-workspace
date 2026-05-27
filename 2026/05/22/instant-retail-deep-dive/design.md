# design.md — 视觉风格方向 + 故事板

## 风格
style: 现代商务科技
mood: 深度专业、节奏稳健

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（深蓝灰接近黑）
  accent_cool: 科技青/蓝绿（用于数据、市场场景）
  accent_warm: 金色/琥珀（用于商机、结论场景）
  accent_danger: 暗红色（用于风险警示场景）
  text: 白色主 + 浅灰辅

## 配乐方向
music_mood: 商业纪录片风格 — 稳重、现代、有推动感
bgm_keywords: "corporate documentary, modern business, inspiring tech"

## 素材预判
assets_needed: []
# 纯数据/概念展示，CSS渐变+光效背景即可

## 故事板（长篇深度解读模式 — 15场景）

narrative_template: "contrast-arc"
emotion_curve: [0.7, 0.5, 0.6, 0.8, 0.7, 0.4]
immersion_mode: "mega-update"
humor_style: "narration-only"
character_presence: false

beat_mapping:
  grab: "S1-hook"
  build: "S2-background, S3-pain-points, S4-market-size"
  reveal: "S5-landscape, S6-2025-changes, S7-keywords"
  climax: "S8-lower-tier, S9-tech-stack"
  settle: "S10-paths-1, S11-paths-2, S12-risks, S13-future"
  summon: "S14-conclusion, S15-cta"

scenes:
  - id: S1
    type: hook
    title: "万亿赛道"
    desc: "钩子：1万亿市场规模的震撼数据"
    duration_target: 35s

  - id: S2
    type: background
    title: "什么是即时零售"
    desc: "定义即时零售，从消费者需求演变讲起"
    duration_target: 40s

  - id: S3
    type: pain-points
    title: "谁在痛苦"
    desc: "消费者端的'不想等' + 商家端的数字化鸿沟"
    duration_target: 45s

  - id: S4
    type: data
    title: "万亿数据"
    desc: "市场规模数据：7810亿→9714亿→1万亿→2万亿"
    duration_target: 40s

  - id: S5
    type: landscape
    title: "四强格局"
    desc: "美团、阿里、京东、抖音四大玩家定位"
    duration_target: 50s

  - id: S6
    type: showdown
    title: "2025外卖大战"
    desc: "京东入局，三足鼎立新格局"
    duration_target: 45s

  - id: S7
    type: keywords
    title: "快爽值"
    desc: "三大消费关键词解析"
    duration_target: 35s

  - id: S8
    type: opportunity
    title: "下沉蓝海"
    desc: "县域市场渗透率<10%的机会"
    duration_target: 40s

  - id: S9
    type: tech
    title: "开源武器"
    desc: "Spree Commerce、Nearby Shops、Localsearch技术栈"
    duration_target: 50s

  - id: S10
    type: business
    title: "路径一：垂直品类"
    desc: "宠物即时医疗、老人陪诊等缝隙市场"
    duration_target: 40s

  - id: S11
    type: business
    title: "路径二：下沉市场"
    desc: "县域即时零售的MVP方案"
    duration_target: 40s

  - id: S12
    type: risk
    title: "风险预警"
    desc: "正面竞争必败、利润率极低、物流成本极高"
    duration_target: 45s

  - id: S13
    type: future
    title: "未来展望"
    desc: "2030年2万亿、质量跃升、AI+即时零售"
    duration_target: 40s

  - id: S14
    type: conclusion
    title: "核心结论"
    desc: "避开巨头、找垂直缝隙、做深做透"
    duration_target: 30s

  - id: S15
    type: cta
    title: "关注获取"
    desc: "CTA引导"
    duration_target: 25s

total_duration_target: 600s  # ~10分钟
