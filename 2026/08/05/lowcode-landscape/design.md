# design.md — 视觉风格方向 + 故事板

## 风格
style: 商业深度解析（科技智库感）
mood: 冷静理性 + 反转张力

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深邃墨蓝/近黑（商业周刊封面质感，专业沉稳）
  accent_cool: 钢蓝/科技青（用于"通用低代码困境"侧——70/30、认知墙、复杂度悬崖、AI 冲击，传达冷峻/警示）
  accent_warm: 琥珀金/暖橙（用于"垂直低代码出路"侧——行业母语、80/20、护城河、CTA，传达希望/价值）
  text: 白色主 + 浅灰辅 + 数据用等宽体高亮
  contrast_logic: 冷暖对比 = 通用 vs 垂直的叙事可视化（前半冷色讲困境，后半暖色讲出路，反转点在 AI 变量）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "衬线庄重（知识/文化/深度）"
    family: "Noto Serif SC"
    weight: 900
    rationale: "低代码赛道解读的情感内核是商业洞察与深度思辨，衬线庄重传递《财经》《哈佛商业评论》式的智库权威感，区别于快闪盘点的几何简洁"
    fallback: "'Noto Serif SC','Source Han Serif SC','PingFang SC','Microsoft YaHei',serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 商业科技/沉稳推进（带轻度悬念张力，反转处有情绪起伏）

## 素材预判
assets_needed:
  - "70/30 数据可视化（纯 CSS 环形/条形对比图）"
  - "80/20 分割线图（三段式：平台预置/领域专家配置/开发者兜底）"
  - "通用 vs 垂直对比表（冷色左 vs 暖色右）"
  - "护城河三层结构图（金字塔/同心圆：行业本体/真实集成/合规沉淀）"
  - "无需外部素材，全部 HTML/CSS 实现"

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.55, 0.45, 0.7, 0.9, 0.6, 0.5]
  immersion_mode: "cinematic"
  humor_style: "narration-only"
  character_presence: false
  beat_mapping:
    grab: "s1-hook（差点全盘否定的反转）"
    build: "s2-70/30 + s3-认知墙（拆解通用低代码的真实困境，冷色铺垫）"
    reveal: "s4-复杂度悬崖 + s5-AI变量（通用低代码被从核心抽砖，反转点）"
    climax: "s6-垂直低代码活路 + s7-80/20分割线（暖色出路，全片高潮）"
    settle: "s8-护城河三层（AI 打不动的地方，沉淀思考）"
    summon: "s9-结论四问 + CTA（中性互动收尾）"

## 方向
orientation: portrait
orientation_source: default

## 场景规划（供 stage3 参考，约 9 场景，75-95s）
scenes_plan:
  - s1_hook: 反转钩子（差点全盘否定→对了一半错了一半）— 全片视觉最强，暖冷对撞
  - s2_70_30: 70/30 定律（开源为什么不够）— 冷色数据可视化
  - s3_cognition_wall: 认知墙（人人都是开发者是营销）— 真实用户画像数据
  - s4_complexity_cliff: 复杂度悬崖（边界处比写代码更痛苦）— 悬崖/下滑视觉隐喻
  - s5_ai_variable: AI 致命变量（2026 通用低代码被抽砖）— 反转点，冷暖切换
  - s6_vertical_life: 唯一活路·垂直低代码（行业母语）— 暖色，对比通用
  - s7_80_20_splitline: 80/20 分割线铁律（三段式谁来做）— 结构化分块
  - s8_moat: 护城河（AI 打不动的三样资产）— 金字塔/同心圆
  - s9_conclusion: 结论 + 四问 CTA（做窄做深）— 收尾沉淀
