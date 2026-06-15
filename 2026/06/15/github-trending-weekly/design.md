# design.md — 视觉风格方向 + 故事板（第24周 GitHub Weekly）

## 风格
style: 暗色科技·四组色谱分区
mood: 紧凑信息流 + 现象级趋势的震撼感

## 配色方向（4 组色谱分区，整体暗色科技底）
color_direction:
  background: 深色暗调（接近纯黑 #0A0E1A），统一基底让 4 组色谱可清晰区分
  group1_ai_skills: 冷青色谱（青蓝 #00D4FF → 深青 #0EA5B7）—— 本周主线 6 个 skills 项目，科技冷感呼应"AI 编程工具技能化"趋势
  group2_agent_vision: 紫色谱（电紫 #A855F7 → 深紫 #6D28D9）—— AI Agent 视觉组，神秘智能感
  group3_ai_tool: 蓝色谱（宝石蓝 #3B82F6 → 深蓝 #1E40AF）—— markitdown 单项目，沉稳工具感
  group4_non_ai: 暖橙金色谱（琥珀 #F59E0B → 暖金 #FBBF24）—— 非 AI 跨域，与前三组冷色形成温度反差，平衡本周 AI 占 10/13 的同质感
  accent_warm: 金色（#FBBF24）用于 hook/CTA 周次强调和跨组通用指标（星数）
  text: 白色主 + 浅灰辅（#E5E7EB / #9CA3AF）

> 4 组色谱逻辑：前 3 组 AI 系（冷青/紫/蓝）冷色递进，组四非 AI（暖橙金）温度反转——视觉上让观众直观感受"本周 AI 主场，但也有非 AI 跨域值得关注"，呼应同质化平衡的选题意图。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "毛笔力量"
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "现象级趋势（6 个 skills 集体上榜）+ 周汇总的分量感，需要力量感的中文字体撑住 hook 和组标题"
    fallback: "'Ma Shan Zheng','PingFang SC','Microsoft YaHei',cursive"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/赛博紧凑（与 hyper-pace 沉浸模式匹配，节奏明快支撑 4 组快速切换）

## 素材预判
assets_needed: []
> 本期为项目盘点，纯 CSS/HTML 渐变 + 光晕 + 数据卡片即可，无需外部素材。

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  rationale: "周汇总 4 组对比结构（AI skills 主线 → Agent 视觉 → AI 工具 → 非 AI 跨域反转），用对比弧突出'本周 AI 主场但非 AI 跨域亦有亮点'的张力，避开近期高频的 hyper-pace 线性盘点"
  emotion_curve: [0.4, 0.6, 0.75, 0.85, 0.7, 0.5]
  immersion_mode: "hyper-pace"
  rationale_immersion: "AI 类项目 >50%（10/13），按 categories immersion_mapping 规则用 hyper-pace；但通过 4 组色彩分区 + contrast-arc 叙事结构避免与近期纯盘点雷同"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（第24周 + 6 个 skills 集体上榜现象）"
    build: "组一 AI Skills 生态（本周主线，3-4 个 skills 聚合）"
    reveal: "组一续 + 组二 AI Agent 视觉（taste/pm skills + goose/roboflow）"
    climax: "组三 AI 工具 markitdown（15 万星本周最高总星）"
    settle: "组四非 AI 跨域（apple container/PowerToys/mattermost/music-assistant 暖色反转）"
    summon: "CTA（第24周周榜收尾）"

## 方向
orientation: portrait
orientation_source: default
> 默认竖屏，抖音主战场。

## 黄金 3 秒视觉要求
hook 场景是全片视觉最具冲击力的画面：周次大标题"第24周" + "AI 集体进化出技能"现象陈述 + 金色光晕（accent_warm）+ 冷青主色谱（group1）背景渐变。前 3 秒画面元素 ≤3 个，主标题字号 ≥100px。
