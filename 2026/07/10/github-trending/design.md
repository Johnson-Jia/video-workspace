# design.md — 视觉风格方向 + 故事板（GitHub Trending 2026-07-10）

## 风格
style: 暗色科技 + 多领域混搭（游戏绿/安全蓝/学习金三色信号灯）
mood: 信息紧凑带反转惊喜——开篇换口味钩子，中段三段利益分组（能玩/能学/能防）层层推进，结尾霸榜带过沉淀

## 导演 5 问
1. **Q1 情感内核**：反转好奇 + 实用收藏欲——"原来 GitHub 还有这种东西"的新鲜感（连续 3 期工具/效率后换口味的反差）+ "这些我能玩能学能防"的实用驱动
2. **Q2 视觉调性**：暗色科技底色 + 三色信号灯分区（游戏段绿系活力 / 学习段金系知识 / 安全段蓝系防御）——色码区分领域而非纯涨星排序，让信息分层更清晰
3. **Q3 字体气质**：几何简洁（Inter 900）—— 多领域盘点需要利落专业的标题，不煽情不柔软；数据用等宽极客强化"信息密度"
4. **Q4 节奏张力**：紧凑中速（每段 5-7s）—— 5 个全新项目 + 1 个霸榜带过 = 6 段，标准模式 30-40s，每段不超 8s 避冗长
5. **Q5 角色出场**：码力角色在 climax（pentagi AI 渗透段，最反直觉）出场做"AI 自己攻防"的表情，settle 段（ai-job-search 霸榜带过）做"它又来了"的表情

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑 + 深蓝深紫渐变底）
  accent_cool: 霓虹青/翠绿（用于游戏段 U3-SDK + AI 安全段 pentagi，冷色系活力+科技）
  accent_warm: 金色/琥珀（用于学习资源段 claude-cookbooks + awesome-design-md + hook/CTA，暖色知识感）
  accent_signal: 深蓝（用于安全指南段 How-To-Secure-A-Linux-Server，沉稳防御感）
  text: 白色主（约 60%）+ 浅灰辅（约 40%），禁纯白端点（OLED 过曝）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "多领域盘点需要利落专业的标题气质，Q1 反转好奇 + 实用驱动适配几何简洁（紧凑/专业/利落），不煽情"
    fallback: "'Inter','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 低调辅助 clean-corporate（GitHub 分类 bgm_style ✅ 首选，避开 bold-energetic 抢旁白）—— 多领域盘点快播报，配乐衬底不抢主角，靠画面色码分区做信息分层

## 素材预判
assets_needed:
  - 6 个 owner avatar（assets/avatars/ 已下载，ProjectFullCard 中部引用）
  - 各项目色码分区背景（绿/金/蓝三色信号灯，纯 CSS 渐变/光效实现）
  - 数据图表（星标增量条/总星大字，纯 CSS 实现）

## 故事板
storyboard:
  narrative_template: "contrast-arc"   # 平淡换口味 → 三段对比（玩/学/防）→ 霸榜带过沉淀 → CTA
  emotion_curve: [0.5, 0.6, 0.75, 0.9, 0.65, 0.45]  # 钩子中高（换口味反转）→ 三段递进到 climax（pentagi AI 攻防最反直觉）→ settle（霸榜带过）→ summon
  immersion_mode: "hyper-pace"          # 多项目盘点 + 快节奏分区，hyper-pace 适配
  humor_style: "dual-track"             # 旁白轻度幽默（游戏/学习段）+ 视觉色码分区趣味
  character_presence: true
  beat_mapping:
    grab: "hook（换口味钩子）"
    build: "U3-SDK 游戏开源（能玩）"
    reveal: "awesome-design-md + claude-cookbooks（能学双段）"
    climax: "pentagi AI 渗透 + How-To-Secure 加固（能防双段，climax 在 pentagi AI 自己攻防最反直觉）"
    settle: "ai-job-search 霸榜带过（连续霸榜第 1，沉淀）"
    summon: "CTA"

## 场景规划（6 场景，标准模式 30-40s）
1. **hook**（4-5s）：换口味钩子——「GitHub 今天换口味了，AI 不再是主角」+ 三色信号灯分区预览 + 数字锚定（5 个全新 1 个霸榜）
2. **U3-SDK**（5-6s，绿色系）：免费僵尸生存游戏全开源，能玩——反直觉：商业游戏源码通常闭源，这个反向开放
3. **awesome-design-md + claude-cookbooks**（5-6s，金色系学习双拼）：大厂设计规范 + 官方 AI 用法手册，能学——两段拼一场景或快速连续两个 ProjectFullCard
4. **How-To-Secure-A-Linux-Server**（5-6s，深蓝安全色）：服务器加固手册，能防——反直觉：运维私藏经验变 6 年开放手册
5. **pentagi**（5-6s，青绿 AI 安全色，climax）：AI 自己跑渗透测试，最反直觉——码力角色出场
6. **ai-job-search 霸榜带过 + CTA**（4-5s）：07/08 已讲，今天 +3728 连续霸榜第 1，带过 + 结尾提问

## 方向
orientation: portrait
orientation_source: default   # GitHub 分类默认竖屏，未指定横屏
