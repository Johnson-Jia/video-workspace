# design.md — 二次元开源生态商业分析

## 风格
style: 赛博二次元          # 暗色科技底 + 动漫霓虹强调色
mood: 专业洞察              # 分析感而非花哨展示

## 配色方向（描述性）
color_direction:
  background: 深色暗调（近纯黑 #0a0a0f）
  accent_cool: 霓虹紫/赛博青（#9D4EDD / #00F5D4）— 用于数据、技术点
  accent_warm: 珊瑚粉/金色（#FF6B9D / #FFD700）— 用于 hook、CTA、关键数据
  text: 白色主 + 浅灰辅
  danger: 暗红（#FF3B3B）— 用于停更/死亡项目

## 配乐方向
music_mood: 电子/赛博朋克（节奏感强、不过于激昂，适合分析旁白）

## 素材预判
assets_needed: []    # 纯 CSS 渐变 + 光效 + 图表，无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"     # 崛起 vs 倒下
  emotion_curve: [0.7, 0.5, 0.6, 0.8, 0.9, 0.6, 0.8, 0.7, 0.5, 0.4]
  immersion_mode: "hyper-pace"           # 信息密集 + 快节奏
  humor_style: "dual-track"              # 旁白幽默 + 视觉配合
  character_presence: false              # 商业分析不需要码力角色
  beat_mapping:
    grab: "scene1-hook"                  # 好奇：洗牌悬念
    build: "scene2-background"           # 期待：背景铺垫
    reveal: "scene3-ai-art, scene4-tts"  # 惊喜：两大核心赛道
    climax: "scene5-vtuber, scene6-games" # 激动：VTuber+游戏
    settle: "scene7-business, scene8-trends"  # 思考：商业逻辑+趋势
    summon: "scene9-practice, scene10-cta"    # 行动：实操+关注

## 场景规划（10 场景 × ~18s/场景 = 180s）

scenes:
  - id: scene1-hook
    type: hook
    duration_target: 8s
    content: "二次元开源生态正在大洗牌"
    notes: "全片视觉最强画面，大字号冲击，数据对比（115K★ vs 停更）"

  - id: scene2-background
    type: context
    duration_target: 18s
    content: "AI + 二次元的交汇点，为什么现在爆发"
    notes: "背景+驱动力：AI平民化、开源许可证趋势、组织化升级"

  - id: scene3-ai-art
    type: sector-analysis
    duration_target: 25s
    content: "AI绘画赛道：ComfyUI 称王，旧王退场"
    notes: "ComfyUI 115K★ 每日更新 vs SD WebUI 163K★ 僵尸维护，对比布局"

  - id: scene4-tts
    type: sector-analysis
    duration_target: 25s
    content: "语音赛道：1分钟克隆角色声音"
    notes: "GPT-SoVITS 45K★ + Fish Speech 20K★ + Style-Bert-VITS2，四项目对比"

  - id: scene5-vtuber
    type: sector-analysis
    duration_target: 20s
    content: "VTuber赛道：从皮套到AI全自动"
    notes: "Open-LLM-VTuber 8K★，LLM+Live2D+语音+视觉感知"

  - id: scene6-games
    type: sector-analysis
    duration_target: 18s
    content: "游戏工具+追番漫画：社区最热+基础设施"
    notes: "BetterGI 13.7K★ 593条issue + Auto_Bangumi 8K★ + Bangumi数据中台"

  - id: scene7-business
    type: analysis
    duration_target: 22s
    content: "三层生态结构：数据层→工具层→应用层"
    notes: "核心商业逻辑可视化，层级关系图"

  - id: scene8-trends
    type: analysis
    duration_target: 18s
    content: "趋势判断：停更警示 + 未来方向"
    notes: "红色标记停更项目 + 箭头指向未来趋势"

  - id: scene9-practice
    type: guide
    duration_target: 18s
    content: "四级入门路径：零门槛→深度玩家"
    notes: "阶梯式布局，从易到难"

  - id: scene10-cta
    type: cta
    duration_target: 8s
    content: "关注+收藏，下期深入讲解"
    notes: "简洁CTA，配收藏引导"

## 方向
orientation: portrait
orientation_source: default
