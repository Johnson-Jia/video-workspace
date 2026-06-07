# design.md — 视觉风格方向 + 故事板

## 风格
style: 科技匠心
mood: 从理性到激情（渐进升温）

## 方向
orientation: landscape
orientation_source: duration
width: 1920
height: 1080

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深邃黑蓝（开发者编辑器风格的暗色调）
  accent_primary: 霓虹青/蓝（管线架构、技术栈场景——代码感）
  accent_secondary: 琥珀金/橙（核心洞察、成果展示——温度感）
  accent_highlight: 翠绿（关键数据、CTA——行动感）
  text: 白色主 + 浅灰辅
  code: 语法高亮色系（关键字蓝、字符串绿、注释灰）

## 配乐方向
music_mood: 科技/灵感 — 从沉稳到昂扬的电子配乐，有递进感但不喧闹。适合讲解型长视频的背景音乐，需要有节奏但不能抢旁白
bgm_candidates:
  - "clean-corporate 系列"（沉稳专业）
  - "neon-electric 系列"（科技感强）
  - "inspiring-motivational 系列"（有递进感）

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "origin-story"
  emotion_curve: [0.3, 0.4, 0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9, 0.85, 0.8, 0.7, 0.6]
  immersion_mode: "explanatory-pace"
  humor_style: "none"
  character_presence: false
  beat_mapping:
    grab: "hook（AI 自制视频的震撼可能性）"
    tension: "痛点（手动做视频的折磨）"
    spark: "灵感（开发者自动化直觉）"
    build: "哲学 → 管线 → 规则引擎（逐步深入技术架构）"
    reveal: "三层视觉系统 + 设计洞察（核心创新）"
    climax: "双闭环进化系统（自我进化能力）"
    settle: "实际成果（数据说话）"
    summon: "CTA（开源邀请）"

## 场景规划（13 场景，横屏深度讲解）
scenes:
  - id: hook
    beat: grab
    focus: "AI 自制视频的可能性——如果 AI 能从一行文字做出一个完整的短视频？"
    visual_concept: "大字冲击 + 数据流特效，画面从代码流渐变到视频画面"

  - id: pain
    beat: tension
    focus: "手动做视频的痛苦：选题→文案→配音→配乐→画面→剪辑→封面→发布，至少 4 小时"
    visual_concept: "流程步骤卡片逐个堆叠，越来越沉重"

  - id: spark
    beat: spark
    focus: "开发者的直觉：重复劳动→自动化流水线。让 AI 驱动每个环节"
    visual_concept: "混乱的步骤被收束为一条清晰的管线"

  - id: philosophy
    beat: build
    focus: "三条设计铁律：Schema 即真相、状态即文件、委托不重写"
    visual_concept: "三条铁律作为三个并列的规则卡片，金色高亮"

  - id: pipeline
    beat: build
    focus: "9 阶段 DAG 管线：内容→设计→旁白→音频→素材→视频→交付→评分→清理"
    visual_concept: "管线流程图，节点逐步亮起"

  - id: rule-engine
    beat: build
    focus: "规则引擎四原子：Intent/Boundary/Gate/Trace——如何控住 AI 不失控"
    visual_concept: "四个原子的关系图，注入→执行→门禁循环"

  - id: inject-gate
    beat: build
    focus: "执行流程：注入正向规则→AI 自由创作→门禁自动检验→轨迹全程记录"
    visual_concept: "执行时序图，从注入到门禁的闭环"

  - id: visual-layers
    beat: reveal
    focus: "三层视觉架构：bg 氛围层 + fx 特效层 + content 内容层，30+ 组件库"
    visual_concept: "三层分离透视效果，每层独立展示后合并"

  - id: design-insight
    beat: reveal
    focus: "最核心的洞察：流程零自由度·内容最大自由度。LETTER 管流程，SPIRIT 管内容"
    visual_concept: "对比分割：左半 LETTER（严谨框架），右半 SPIRIT（自由创作）"

  - id: code
    beat: build
    focus: "技术栈全景：Python 规则引擎 + YAML 声明 + HTML/GSAP + Edge-TTS + HyperFrames"
    visual_concept: "技术栈层级图，每层展示关键技术"

  - id: evolution
    beat: climax
    focus: "双闭环进化：即时门禁拦截问题 + 延迟播放数据校准。30+ 规则，每条来自真实事故"
    visual_concept: "双闭环示意图，门禁闭环和数据闭环交叉"

  - id: results
    beat: settle
    focus: "实际成果：标准 45s / 深度 60s / 长视频 3-5min，支持分类和全自动化"
    visual_concept: "三种视频模式的卡片展示，配数据"

  - id: cta
    beat: summon
    focus: "ClipForge 开源。AI 驱动的视频锻造炉，让创作者专注创意"
    visual_concept: "CTA 收束，GitHub 地址 + 核心理念总结"
