# design.md — 视觉风格方向 + 故事板

## 风格
style: 科技赛博
mood: 紧凑悬疑

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变作基底）
  accent_cool: 霓虹青/翠绿（用于 AI 安全/扫描类场景，体现「审视/检测」冷峻感）
  accent_warm: 金色/琥珀（用于 hook/数字锚定/CTA 场景，强调涨星数据冲击）
  text: 白色主 + 浅灰辅（高对比，前 3 秒视觉最强）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核「理性/精准/极客」——AI 审 AI 的冷峻数字反差需要几何无衬线的精准力量感，配数字锚定钩子最有冲击力"
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
music_mood: 科技/赛博（紧凑悬疑底色，开篇冲击 + 中段节奏推进 + 结尾沉淀）

## 素材预判（可选）
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.45, 0.55, 0.75, 0.9, 0.65, 0.4]
  immersion_mode: "mystery-box"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "skillspector, aisuite"
    reveal: "kronos, swc"
    climax: "chatwoot"
    settle: "music-assistant"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default

## 设计推导说明

### 情绪提炼
- **主题**：今日 GitHub Trending 6 个跨领域项目，以「AI 自己扫描自己的安全」（SkillSpector）为核心反直觉钩子，辐射到多模型统一接口、时序基础模型、Rust Web 工具链、开源客服 SaaS、音乐 IoT 六方向
- **情绪基调**：紧凑悬疑 + 理性极客。开篇用数字冲击（+962 涨星）+ 认知反差（AI 审 AI）建立悬念，中段逐个揭示项目非直觉角度，结尾沉淀到开源生活化场景
- **情绪弧线**：好奇（数字锚定）→ 期待（AI 安全悖论）→ 惊喜（时序当语言/Rust 重写 Web）→ 激动（开源替代年费 SaaS）→ 思考（音乐聚合到树莓派）→ 行动（CTA）
- **节奏感**：紧凑。标准 6 场景 45-55s，hook 4s + 5 项目各 7-8s + CTA 4s
- **文化调性**：现代科技。深色暗调 + 霓虹冷暖双色光晕，体现「AI 时代的开源观察者」定位

### 风格推导依据
- **科技赛博**：6 项目全部为开发者/技术向（AI 安全/多模型/时序/Web 工具/客服 SaaS/音乐 IoT），内容天然适配科技调性
- **深色做底亮色做刀**：深蓝/深紫渐变让霓虹青（冷峻审视）和金色（数字冲击）的强调色跳出，是短视频黄金法则
- **统一但不单调**：6 项目配色按类别分配——AI 安全/扫描类用霓虹青冷调，涨星数据/CTA 用金色暖调，非 AI 项目（swc/chatwoot/music-assistant）用紫/琥珀过渡色保持多样

### 沉浸模式选择依据
- **mystery-box**：「AI 自己扫描自己的安全」天然是悬念揭示型故事。开篇抛出认知反差（AI 反过来审 AI），逐个揭示每个项目的「非直觉角度」（时序当语言/苹果不在此列改用 Rust 重写 Web/年费客服的开源替代/树莓派做音乐中枢），符合 mystery-box 「好奇→线索→揭示→惊喜」情感弧
- **避开近期 hyper-pace**：近 5 期连续 hyper-pace 盘点是 6 月崩盘主因。本期叙事改 contrast-arc（对比弧：平淡数字开场 → 反差揭示 → 震撼 → 高潮 → 沉淀），视觉改 mystery-box 渐进揭示，主动差异化

### 角色出场规划
- 码力角色 climax 段（chatwoot 开源替代年费 SaaS）必出 explode 表情（大厂收费 vs 开源免费的强对比）
- reveal 段（kronos/swc 揭示非直觉角度）出 cool/think 表情
- settle 段（music-assistant 树莓派做音乐中枢）出 tease 表情（开发者生活化幽默）
