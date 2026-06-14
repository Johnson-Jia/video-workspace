# design.md — 视觉风格方向 + 故事板

> 2026-06-14 GitHub 每日热门盘点（6 个项目，AI Agent 占一半）

## 导演分析（5 必答题，驱动下方所有字段）

- **Q1 情感内核**：极客震撼 — AI Agent 工具链（技能标准化 → 安全扫描 → 推理加速）正以惊人速度成熟，叠加 Apple 下场做容器、微软打磨 PowerToys，大厂把基础设施做得更易用
- **Q2 节拍任务**：grab=动作+数字钩子冲击 / build=铺垫悬念 / reveal=反直觉惊喜 / climax=LMCache 推理砍延迟（全片最高点）/ settle=PowerToys 冷却连接日常 / summon=行动召唤
- **Q3 视觉手段**：暗色赛博底 + 霓虹双光晕（暖冷交替）放大"技术突进"的极速感；项目名/涨星数等宽体打数据精确感
- **Q4 相邻反差**：AI 冷色场景（青/电光蓝）与 数据暖色场景（金/琥珀橙）色温交替，避免视觉同质
- **Q5 视线焦点**：竖屏，中上部黄金分割点放涨星数据锚点；每场景单一焦点（数据 / 项目名 / 反直觉结论）

## 风格
style: 暗色科技赛博
mood: 紧凑震撼

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/电光蓝（AI/Agent/技术能力场景，冷色叙事"理性/技术"）
  accent_warm: 金色/琥珀橙（涨星数据/hook/CTA 场景，暖色叙事"价值/紧迫"）
  text: 白色主 + 浅灰辅（描述用浅灰，项目名/数据用白色）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"          # 链接 Q1「极客震撼 → 紧凑/专业/利落」
    family: "Noto Sans SC"     # 中文标题，英文项目名配 Inter 900
    weight: 900
    rationale: "GitHub 趋势盘点节奏紧凑、数据密集，几何无衬线粗体强化专业利落感，与 github.md 暗色科技风一致"
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/赛博（快速电子，匹配 hyper-pace 快剪节奏）

## 素材预判
assets_needed: []   # 纯 CSS/HTML 实现（数据对比用 div 块、图标用 emoji/内联），无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"     # github 默认：平淡 → 对比 → 震撼 → 高潮 → 沉淀
  emotion_curve: [0.7, 0.5, 0.75, 1.0, 0.5, 0.65]   # grab 强起 / build 铺垫 / reveal 上升 / climax 最高(LMCache) / settle 冷却 / summon 回升
  immersion_mode: "hyper-pace"           # AI 类项目 >50%（6 个中 3 个 Agent 相关）
  humor_style: "dual-track"              # 旁白+视觉双轨，≥30% 段落含幽默（开发者文化梗）
  character_presence: true               # github 启用码力角色，climax 段必出
  beat_mapping:                          # 节拍 → 场景粗映射
    grab: "hook — 动作+数字模式（杀入/占一半/砍延迟），本次最强经验 P-hook-action_number"
    build: "项目1 agent-skills / 项目2 apple-container"
    reveal: "项目3 superpowers / 项目4 SkillSpector（Agent 安全，反直觉）"
    climax: "项目5 LMCache（推理砍延迟，全片最高点，码力角色出场）"
    settle: "项目6 PowerToys（大厂基础设施，冷却连接日常）"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default   # 用户未指定横屏，github 无 orientation_hint，默认竖屏
