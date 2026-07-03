# design.md — 视觉风格方向 + 故事板

> 日期：2026-07-03 | 分类：github | 模式：标准（6 项目）| 画布：portrait 竖屏

## §1 导演 5 问（Q1-Q5 全片层）

- **Q1 情感内核**：「好奇 + 紧迫」——AI 正在替人干脏活累活的现实感，安全/剪辑/求职/健身都被 AI 接管，节奏紧凑带紧迫感
- **Q2 节拍情感**：grab=AI 替你干活的悬念 → build=各项目能力揭示 → reveal=反直觉应用 → climax=24万星 Agent 框架高潮 → settle=实用工具落地 → summon=选择行动
- **Q3 视觉放大**：暗色赛博底 + 冷色（青/紫）做技术理性 + 暖色（橙/琥珀）做价值锚点（排名/星标/数据），冷暖交替制造张力
- **Q4 相邻反差**：hook 暖橙冲击 → 安全项目冷青理性 → Agent 框架紫调神秘 → 数据集暖金活力 → 剪视频冷蓝流动 → ECC 橙红爆发 → 求职青绿稳重 → CTA 暖橙召唤。每相邻场景至少触发一个色温反转
- **Q5 视线焦点**：每场景单一焦点——排名数字/项目名/核心数据，用字号+光晕+强调色三重锚定

## §2 风格

style: 暗色赛博（深空底 + 冷暖双色锚）
mood: 紧凑利落、好奇紧迫

## §3 配色方向（描述性）

color_direction:
  background: 深空黑底（接近纯黑 #06080F），40px 网格纹理 opacity 0.04
  accent_cool: 霓虹青/电光紫（#4DA8DA / #7C3AED，用于安全/技术/Agent 类场景）
  accent_warm: 琥珀橙/金（#FF8C32 / #FFB627，用于 hook/排名/星标/CTA 场景）
  text: 白色主（#FFFFFF）+ 浅灰辅（#B8C0CC）+ 深灰氛围（#5A6478）

## §4 字体（三层 + voice 链接 Q1）

fonts:
  title:
    voice: "几何简洁"          # 链接 Q1「好奇 + 紧迫」——紧凑专业的工具感
    family: "Inter"
    weight: 900
    rationale: "工具/效率题材需要利落理性气质，几何无衬线强化'AI 在干活'的专业感"
    fallback: "'Inter','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## §5 配乐方向

music_mood: 科技/赛博（紧凑电子，中快节奏，2-3 分钟长度适配 6 项目盘点）

## §6 素材预判

assets_needed:
  - 6 个项目 avatar（已在 assets/avatars/，ProjectFullCard 用）
  - CSS 渐变光晕背景（每场景双色光球）
  - 数据计数动画（星标/动作数/模式数，纯 CSS+JS）

## §7 故事板

storyboard:
  narrative_template: "contrast-arc"      # 平淡 → 对比 → 震撼 → 高潮 → 沉淀（6 项目对比递进）
  emotion_curve: [0.35, 0.5, 0.65, 0.85, 0.6, 0.4]
  immersion_mode: "contrast-arc"          # 冷暖交替锚定单点价值，6 项目混合（安全+工具+框架）适合对比叙事
  humor_style: "narration-only"           # 仅旁白轻调剂，画面保持紧凑专业
  character_presence: false               # 不启用码力角色（紧凑盘点节奏）
  beat_mapping:
    grab: "hook（AI 替你干活悬念）"
    build: "strix（AI 白帽，安全反直觉）"
    reveal: "superpowers（24万星 Agent 框架）"
    climax: "exercises-dataset + video-use（实用高潮，能力落地）"
    settle: "ECC（AI 助手增强，沉淀）"
    summon: "career-ops + CTA（求职系统 + 选择行动）"

## §8 画布方向

orientation: portrait
orientation_source: default    # github 分类默认竖屏

## §9 各场景 visual_type 规划

| 场景 | 项目 | emotion | visual_type | 视觉焦点 |
|------|------|---------|-------------|---------|
| S0 hook | — | grab | hero | "AI 替你干活" 大字 + 6 个能力光点 |
| S1 | usestrix/strix | build | hero | AI 白帽主题 + 项目卡片（安全冷青） |
| S2 | obra/superpowers | reveal | hero | 24万星数据震撼（紫色神秘） |
| S3 | hasaneyldrm/exercises-dataset | climax | data | 433 动作数据计数（暖金活力） |
| S4 | browser-use/video-use | climax | hero | AI 剪视频能力（冷蓝流动） |
| S5 | affaan-m/ECC | settle | hero | 三件套增强（橙红沉淀） |
| S6 | santifer/career-ops | summon | hero | 14 模式求职（青绿稳重） |
| S7 CTA | — | summon | highlight | "想用哪个" 互动收尾（暖橙） |

## 约束声明

> 本阶段结构化约束（HARD/SOFT + Guard Red Flags）由引擎注入提供。执行前已运行 inject.py，已读取 shared/director-toolkit + shared/shared-rules。
