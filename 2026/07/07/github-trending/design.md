# design.md — GitHub Trending 2026-07-07 视觉风格方向 + 故事板

## 导演 5 问（推导依据）

- **Q1 情感内核**：理性掌控 + 反套路惊喜。6 项目表面是工具盘点，主线是"AI 时代把控制权攥自己手里"——会议记录不上云（meetily）、给 AI 装审美防套路（taste-skill）、菜单栏自己看用量（CodexBar）、自托管书签（karakeep）。观众感受应是"原来还能这样把数据/规则握在自己手里"
- **Q2 节拍情感**：grab 好奇（会议记录还能不上云？）→ build 期待（AI 写垃圾？有人治它）→ reveal 惊喜（提示词合集公开整理）→ climax 激动（菜单栏秒看用量 / 阿里极速向量库）→ settle 思考（自己搭书签 AI 自动分类）→ summon 行动（最想尝试哪个）
- **Q3 视觉手段**：冷色深底做"理性/隐私/本地"基调，暖色橙金做星标数字和反直觉点高光，冷暖交替强化"反套路"张力；等宽字体强化"极客/精准/数据"质感
- **Q4 相邻反差**：hook（暖光橙金 + 大数字 2494）→ meetily（冷光深蓝 + 隐私锁概念）形成色温反转；taste-skill（紫色 + "垃圾/审美"对比）→ system_prompts_leaks（青色 + 网格列表）形成密度反转；CodexBar（菜单栏模拟暖光）→ zvec（极速能量条冷光）形成节奏反转；karakeep（自托管书签网格）→ CTA（暖光收束）
- **Q5 视线焦点**：每个场景单一焦点——hook 是 2494 数字，meetily 是项目名 + "本地不上云"，taste-skill 是 "AI 审美"对比，system_prompts_leaks 是提示词网格，CodexBar 是菜单栏模拟，zvec 是极速能量条，karakeep 是书签收纳网格

## 风格
style: 科技暗调·冷色理性
mood: 紧凑利落·反套路惊喜

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，带轻微蓝紫底色做"本地/隐私/极客"基调）
  accent_cool: 深蓝 / 靛紫 / 青色（用于功能描述、技术说明、向量库、提示词网格等理性场景）
  accent_warm: 橙金 / 琥珀（仅用于 hook 数字 2494、星标、CTA 等高光锚点，强化"反套路惊喜"）
  text: 白色主 + 浅灰辅（高对比保证可读）
  contrast_strategy: 冷暖交替——hook 暖、正文冷、 climax 暖、settle 冷、summon 暖，用色温反转制造场景间视觉反差

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "等宽极客"
    family: "JetBrains Mono"
    weight: 800
    rationale: "Q1 情感内核是'理性掌控 + 极客数据主权'，等宽体的精准节拍感强化'把数据攥手里/给 AI 立规则'的主题；与近 5 期教程类衬线/毛笔风格形成差异化"
    fallback: "'JetBrains Mono','Consolas','PingFang SC','Microsoft YaHei',monospace"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/电子（clean-corporate 偏向，节奏稳不抢旁白；避免 bold-energetic 激进电子——本期是工具盘点不是燃向）
music_keywords: ["clean electronic", "tech corporate", "minimal synth", "data pulse"]

## 素材预判（可选）
assets_needed:
  - "avatars（6 项目 owner avatar 已下载，用于 ProjectFullCard）"
  - "纯 CSS/HTML 实现的星标数字、菜单栏模拟、向量能量条、书签网格（无需外部图片）"

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.85, 0.55, 0.65, 0.90, 0.50, 0.45]
  # 6 拍：grab(0.85 反直觉钩子强冲击) → build(0.55 taste-skill 铺垫) → reveal(0.65 提示词公开整理) → climax(0.90 CodexBar+zvec 双项目高潮) → settle(0.50 karakeep 思考) → summon(0.45 CTA 温和)
  # 拒绝均匀填充：hook 和 climax 双高点，settle 落到中位形成"快-思考-收"节奏
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: false  # github 工具盘点无角色，纯项目卡片 + 数据
  beat_mapping:
    grab: "hook（2494 涨星 + 反直觉：会议记录不上云）"
    build: "meetily + taste-skill（本地会议 + 给 AI 装审美，铺垫'数据/规则主权'主线）"
    reveal: "system_prompts_leaks（提示词公开整理，反直觉'各家底牌'）"
    climax: "CodexBar + zvec（菜单栏秒看用量 + 阿里极速向量库，性能/工具双高点）"
    settle: "karakeep（自托管书签 AI 自动分类，连接观众'自己搭'的现实）"
    summon: "CTA（最想尝试哪个，中性二选一）"

## 方向
orientation: portrait
orientation_source: default  # github 分类默认竖屏抖音

## 场景规划（供 stage3 参考，5-6 段）
# 段1 (hook + meetily): 反直觉开篇——"开会记录不上云，2494 颗星撑它"
# 段2 (taste-skill): 给 AI 装审美，治套路化输出
# 段3 (system_prompts_leaks): 各家 AI 提示词公开整理（用'公开整理'不渲染猎奇）
# 段4 (CodexBar + zvec 合段): macOS 菜单栏看用量 + 阿里极速向量库（性能/工具双高点）
# 段5 (karakeep + CTA): 自托管书签 AI 自动分类 + 结尾中性提问
# 共 5 段，单段 8-12s，总时长约 35-45s（标准模式）

## 合规锚点（stage3 必须遵守）
- 禁用词字面：翻墙/盗版/破解/最强/第一/绝对/必备/神器（包括"禁用说明"语境也不写）
- system_prompts_leaks 措辞：用"公开整理"，不渲染"泄露"猎奇
- 项目名必报 owner/repo（如 Zackriya-Solutions/meetily），禁全程用"它"
- 禁搜索引导（搜一下/评论区搜/去 GitHub 搜）
- 结尾仅 1 个中性二选一（最想尝试哪个/会用哪个），禁站队对抗式
