# design.md — GLM vs Qwen 大模型实战对比

## 风格
style: 竞技对决风（红蓝对抗）
mood: 紧张激烈 + 数据理性

## 导演必答

### Q1: 情感内核
**不服**。号称全球前三的大模型，实测编码能力被"老选手"碾压——这种反差本身就是最大的钩子。

### Q2: 观众情绪节拍
- grab: "真假的？国产第一竟然翻车？"（悬念冲击）
- build: "百人团队三个月实战，这不是纸面测试"（建立可信度）
- reveal: "装个插件都装不对 vs 秒懂"（具象对比，释放笑点）
- climax: "32分 vs 21分，碾压式差距"（数据高潮）
- settle: "选模型看实战，不看营销"（冷静收束）
- summon: "评论区说说你的选择"（行动召唤）

### Q3: 视觉手段
**左右分屏对抗**是核心视觉手段。GLM 用蓝/青色系代表冷静强者，Qwen 用橙/红色系代表高调挑战者。每次对比都是左右对决，数据条形图直接可视化差距。

### Q4: 场景间反差
- hook → 背景：hook 纯文字大冲击，背景暗调 → 切到背景叙述用暖色微光
- 案例 → 数据：具象故事用卡片布局，数据对比用条形图布局（密度反转）
- 数据 → 结论：密集数据切到大字金句留白（节奏反转）

### Q5: 视线引导
每个场景一个焦点。hook 聚焦"翻车"二字，案例聚焦对比结果，数据聚焦最大分差（视觉5分 vs 2分），结论聚焦金句。

## 配色方向
color_direction:
  background: 深黑底（#0a0e1a 级别）
  glm_side: 霓虹青/电光蓝（冷静、专业、强者）
  qwen_side: 琥珀橙/警示红（高调、挑战、翻车）
  text: 白色主 + 浅灰辅
  accent_data: 翠绿（用于"胜出"标记）

## 配乐方向
music_mood: 科技竞技/紧张节奏，偏电子鼓点

## 素材预判
assets_needed: []  # 纯数据对比内容，CSS 条形图/卡片即可

## 故事板
storyboard:
  narrative_template: "showdown"
  emotion_curve: [0.9, 0.4, 0.7, 1.0, 0.5, 0.3]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: false
  scenes:
    - id: hook
      beat: grab
      purpose: 悬念开场——"国产大模型全球前三"的翻车现场
      visual: 大字"翻车"居中，下方小字"全球前三？实测结果让你意外"
      duration_target: 4s

    - id: background
      beat: build
      purpose: 建立可信度——百人团队三个月实战
      visual: 时间线卡片：3月→全员接入GLM→提效→全员驾驭
      duration_target: 6s

    - id: trigger
      beat: build
      purpose: 切换契机——80亿tokens的诱惑
      visual: 对话气泡风格，"80亿免费tokens"突出显示
      duration_target: 5s

    - id: case1
      beat: reveal
      purpose: 实测案例1——Superpowers安装翻车
      visual: 左右分屏对比，GLM蓝方✓ vs Qwen红方✗
      duration_target: 7s

    - id: case2-data
      beat: climax
      purpose: 4组对照数据总览——32分碾压21分
      visual: 横向条形图，GLM最高32分满格绿色，Qwen最低21分
      duration_target: 8s

    - id: breakdown
      beat: climax
      purpose: 关键维度拆解——视觉5分vs2分
      visual: 雷达图或分维度条形，突出视觉/动画差距
      duration_target: 7s

    - id: conclusion
      beat: settle
      purpose: 核心结论——选模型看实战
      visual: 大字金句居中留白
      duration_target: 5s

    - id: cta
      beat: summon
      purpose: 行动召唤
      visual: "评论区说说你用哪个" + 频道信息
      duration_target: 4s
