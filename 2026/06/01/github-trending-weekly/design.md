# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 信息密度高、周榜节奏紧凑、分组切换有辨识度

## 方向
orientation: portrait
orientation_source: duration
width: 1080
height: 1920

## 配色方向
color_direction:
  background: 深邃暗蓝（#0a0e1a，开发者暗色调）
  accent_primary: 橙金色（涨星数据、排名数字——数据冲击力）
  accent_secondary: 青蓝色（项目名、技术标签——科技感）
  accent_highlight: 翠绿（核心卖点词——行动感）
  text: 白色主 + 浅灰辅
  code: 语法高亮色系

## 分组主题色
group_colors:
  g1-skills: 霓虹青蓝（#00d4ff）— AI Agent 技能生态
  g2-content: 琥珀金橙（#ff9500）— AI 内容与工具
  g3-infra: 翠绿（#00e676）— 开发者基建
  g4-learn: 紫色（#b388ff）— AI 学习与治理

## 配乐方向
music_mood: 科技/电子 — 节奏紧凑的信息流配乐，有推进感但不抢旁白
bgm_candidates:
  - "tech-electronic 系列（快速信息流节奏）"
  - "upbeat-corporate 系列（专业+节奏感）"

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "listicle-grouped"
  emotion_curve: [0.8, 0.75, 0.7, 0.65, 0.6, 0.5]
  immersion_mode: "rapid-fire"
  humor_style: "none"
  character_presence: false
  beat_mapping:
    grab: "hook（本周主题：AI Agent 技能生态大爆发）"
    items_g1: "第一组：AI Agent 技能生态（5 项目，青蓝主题色）"
    items_g2: "第二组：AI 内容与工具（3 项目，金橙主题色）"
    items_g3: "第三组：开发者基建（4 项目，翠绿主题色）"
    items_g4: "第四组：AI 学习与治理（2 项目，紫色主题色）"
    summon: "CTA（关注我，下期见）"

## 场景规划（6 场景，竖屏周榜汇总）
scenes:
  - id: hook
    beat: grab
    focus: "本周 GitHub 关键词：AI Agent 技能生态大爆发，20 万星项目领跑"
    visual_concept: "大字冲击 + 四组主题色色带预览，数字 200K 高亮"
    group_color: white

  - id: g1-skills
    beat: items_g1
    focus: "ECC 200K★ / Understand-Anything 47K★ / codegraph 35K★ / taste-skill 30K★ / Cybersecurity-Skills 13K★"
    visual_concept: "青蓝主题色背景渐变，5 个项目卡片快速切换，技能图标流动"
    group_color: "#00d4ff"
    target_duration: 12

  - id: g2-content
    beat: items_g2
    focus: "markitdown 135K★ / MoneyPrinterTurbo 74K★ / heretic 23K★"
    visual_concept: "金橙主题色背景渐变，3 个项目卡片，内容创作工具图标"
    group_color: "#ff9500"
    target_duration: 8

  - id: g3-infra
    beat: items_g3
    focus: "iii 17K★ / liteparse 8.3K★ / dograh 4K★ / herdr 3.4K★"
    visual_concept: "翠绿主题色背景渐变，4 个项目卡片，Rust/基建元素"
    group_color: "#00e676"
    target_duration: 8

  - id: g4-learn
    beat: items_g4
    focus: "ai-engineering-from-scratch 26K★ / agent-governance-toolkit 3.6K★"
    visual_concept: "紫色主题色背景渐变，2 个项目卡片，学习/治理图标"
    group_color: "#b388ff"
    target_duration: 5

  - id: cta
    beat: summon
    focus: "关注我，下期见"
    visual_concept: "频道品牌收束 + 简洁 CTA"
    group_color: white
