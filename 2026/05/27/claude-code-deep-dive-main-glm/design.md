# design.md — 视觉风格方向 + 故事板

## 风格
style: 科技暗域
mood: 紧张揭秘

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深空黑（接近纯黑，带微蓝调）
  accent_cool: 霓虹青（用于数据展示/工具体系场景）
  accent_warm: 琥珀金（用于 hook/核心发现/CTA 场景）
  accent_alert: 警示红（用于泄露事件/安全警告场景）
  text: 白色主 + 浅灰辅

## 配乐方向
music_mood: 科技/悬疑 — 紧凑节拍的电子配乐，带神秘感和递进张力

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.4, 0.6, 0.85, 1.0, 0.7, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: false
  beat_mapping:
    grab: "hook（泄露事件引爆）"
    build: "规模震撼 + 工具体系"
    reveal: "隐藏功能揭秘"
    climax: "三层门控体系 + 内外差异"
    settle: "竞争格局与护城河"
    summon: "CTA（行业启示）"

## 场景规划（8 场景深度解析）
scenes:
  - id: hook
    beat: grab
    focus: "源码泄露事件 — npm 包 source map 泄露 51 万行代码"
    visual_concept: "数据洪流涌出效果，大字冲击"
  - id: what
    beat: build
    focus: "Claude Code 是什么 — 终端原生 AI 代理，不是补全工具"
    visual_concept: "核心数据卡片：1987 文件 / 53 工具 / 87 命令"
  - id: architecture
    beat: build
    focus: "技术架构 — TypeScript + React Ink + MCP，51 万行工程"
    visual_concept: "技术栈层级可视化"
  - id: tools
    beat: reveal
    focus: "53 个工具体系 — 文件/命令/Agent编排/网络/MCP 六大类"
    visual_concept: "工具分类卡片矩阵"
  - id: hidden
    beat: reveal
    focus: "7 大隐藏功能 — BUDDY 宠物/KAIROS 持久助手/ULTRAPLAN 云端规划"
    visual_concept: "秘密功能逐个揭开，霓虹光效"
  - id: gating
    beat: climax
    focus: "三层功能门控 — 编译开关/用户类型/远程A/B测试，外部版是精简版"
    visual_concept: "三层门禁可视化，内外对比"
  - id: moat
    beat: settle
    focus: "真正的护城河是 harness — 编排层的工程复杂度才是壁垒"
    visual_concept: "模型 vs harness 对比图"
  - id: cta
    beat: summon
    focus: "行业启示 — MCP 成标准、多端覆盖成标配、竞争从模型转向工程"
    visual_concept: "总结收束，CTA 引导"
