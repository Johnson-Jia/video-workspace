# design.md — 视觉风格方向 + 故事板

## 风格
style: 时间轴编年史（科技史诗）
mood: 史诗 · 震撼 · 推进感（收尾转骄傲）

> **核心视觉概念：贯穿全片的「垂直时间轴」。** 竖屏 1080×1920 的垂直纵深是最大资产——一条从画面顶部向底部流动的时间主轴，每个里程碑节点是轴上的一个发光锚点。时间轴随进化「向下生长」，观众视觉跟随时间推进。年份用等宽大数字（节拍器），参数跃迁用数字翻牌/上升曲线。这是本期视频区别于其他视频的视觉灵魂，Stage 6 每个场景都围绕「时间轴上的一个节点」构图。

> **配色弧线（色温叙事）：** 颜色随时间线推进演变，不是全片一种色调——
> - 第一阶段 2017-2019 奠基：**冷蓝/青**（实验室科技感，理性、庄重，硅谷起点）
> - 第二-三阶段 2020-2022 产业化：**蓝→紫**（规模扩张、ChatGPT 全民爆发的震撼）
> - 第四阶段 2023 开源民主化：**青绿**（开放、普惠、技术民主）
> - 第五-六阶段 2024-2026 推理+国产：**渐变到金/琥珀**（推理革命、国产突围，价值与骄傲）
> - **盘古金句高潮场景：中国红+金**（全片最强暖色冲击，辛德勒名单式焦点）
> 配色弧线本身即叙事工具——冷暖交替让观众感受「从硅谷主导到国产高潮」的情绪转换。

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑的科技深空底，营造史诗纵深感）
  accent_cool: 冷蓝/青/紫（奠基-产业化-全民AI 段；理性、深邃、硅谷主导）
  accent_warm: 金/琥珀/中国红（开源-推理-国产高潮 段；价值、骄傲、民族自豪）
  text: 白色主 + 浅灰辅（信息层级：年份/参数 > 模型名 > 描述）
  climax: 中国红 + 金（盘古金句场景专属，全片唯一最强暖焦点）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "理性/精准/极客"
    family: "JetBrains Mono"
    weight: 800
    rationale: "九年进化史的核心是『时间+参数数字』的精准推进，等宽体像节拍器般精准可信，承载年份/模型名/参数数据。Q1 情感内核『史诗+震撼』通过配色弧线与大字号释放，字体保持精准冷峻的科技节拍器气质"
    fallback: "'JetBrains Mono','Consolas','PingFang SC','Microsoft YaHei',monospace"
  climax_font:
    voice: "毛笔力量"
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "盘古金句『先有华为后有天，盘古从此降人间』是全片唯一破格高潮点，毛笔力量体呼应盘古的中国古典意象，释放民族自豪情感。仅此一处特例，不破坏全片字体统一"
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
music_mood: 史诗科技 / 电影预告感（从克制推进到宏大爆发，有「时间推进」的鼓点节奏感，收尾可渐弱过渡到拼接素材的原声）

## 素材预判
assets_needed: []   # 时间轴可视化、配色光晕、数字翻牌全部用纯 CSS/HTML 实现，无需外部素材；模型 Logo 不使用（无素材源，用文字+参数+时间轴节点表达）

## 故事板
storyboard:
  narrative_template: "contrast-arc"    # 平淡奠基→对比震撼→开源民主化对比→盘古高潮→沉淀过渡
  emotion_curve: [0.5, 0.5, 0.75, 1.0, 0.5, 0.4]
  # grab=震撼数字开场 / build=奠基庄重 / reveal=产业化+全民AI震撼 / climax=开源+推理+盘古金句最高点 / settle=金句收束 / summon=过渡拼接片呼吸
  immersion_mode: "hyper-pace"          # 快节奏密集串讲 20+ 节点（完整版 90-120s）
  humor_style: "narration-only"         # 科技史诗内容，不注入幽默/角色，保持庄重史诗感
  character_presence: false             # 无码力角色，纯知识科普编年史
  beat_mapping:
    grab: "hook（9年进化 + 参数跃迁震撼数字锚点开场）"
    build: "2017-2019 Transformer / GPT-1 / BERT / GPT-2 奠基期（冷蓝，庄重留白）"
    reveal: "2020-2022 GPT-3 / ChatGPT / 盘古 产业爆发与全民 AI（蓝→紫，信息密集）"
    climax: "2023-2026 LLaMA 开源 / o1 推理 / DeepSeek-R1 / 盘古系列国产突围 → 盘古金句最高潮（青绿→金红→中国红）"
    settle: "『先有华为后有天，盘古从此降人间』金句收束（毛笔体 + 中国红金，全片视觉最强点）"
    summon: "自然过渡到华为开源实拍片（旁白结束，画面交棒给拼接素材）"

## 方向
orientation: portrait
orientation_source: default   # 抖音竖屏频道默认竖屏；拼接素材横屏→竖屏转换在交付后单独处理

## 场景规划建议（供 Stage 3 参考）
完整版 90-120s 覆盖 20+ 节点，建议按「时间轴节点」组织场景，相关节点可合并到同一场景的多个 phase：
- hook 场景（强钩子，~6-8s）：9 年进化总览 + 参数跃迁震撼数字
- 奠基段（2017-2019，~12-15s）：Transformer → GPT/BERT 双路线 → GPT-2
- 产业化段（2020-2022，~20s）：GPT-3 规模定律 → ChatGPT 全民 AI（重点）→ 盘古气象/InstructGPT
- 开源+多模态段（2023，~15s）：LLaMA 民主化 → GPT-4 → 百模大战 → PanGu-Σ
- 推理革命段（2024，~18s）：Gemini1.5 长上下文 → GPT-4o → o1 推理 → DeepSeek-V3
- 国产高潮段（2025-2026，~20s）：DeepSeek-R1/开源周 → Qwen3/Claude4 → 盘古5.5 → openPangu1.0 → ★openPangu2.0+金句
- 过渡（~2-3s）：旁白收束，画面交棒给拼接素材

> 金句场景必须是全片视觉最强点（黄金 3 秒法则的最高潮版）：字号最大、对比最强、毛笔体、中国红+金配色、单焦点。
