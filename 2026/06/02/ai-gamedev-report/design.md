# design.md — AI × 游戏开发生态深度分析

## 风格
style: 科技前沿
mood: 紧凑专业、信息密度高

## 配色方向
color_direction:
  background: 深色暗调（接近纯黑，带微妙蓝紫渐变）
  accent_cool: 霓虹青/电子蓝（用于数据展示、项目卡片）
  accent_warm: 琥珀金/暖橙（用于 hook、CTA、关键数字）
  accent_highlight: 品红/洋红（用于技术架构、对比亮点）
  text: 白色主 + 浅灰辅

## 配乐方向
music_mood: 电子/科技氛围，节奏紧凑但不抢旁白

## 素材预判
assets_needed: []  # 纯 CSS 渐变/光效即可，无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.6, 0.85, 0.95, 0.65, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: false
  beat_mapping:
    grab: "S1-hook"
    build: "S2-background, S3-six-routes"
    reveal: "S4-autonomix, S5-mcp, S6-claude-studios"
    climax: "S7-business-analysis, S8-future"
    settle: "S9-practical-guide"
    summon: "S10-cta"

## 场景规划（10 场景，~300s）
scenes:
  - id: s1
    name: hook
    duration: 5
    beat: grab
    content: "AI正在重写游戏开发规则，40+开源项目同时爆发"
  - id: s2
    name: background
    duration: 35
    beat: build
    content: "三重驱动力：MCP标准 + 编辑器Agent + 本地模型"
  - id: s3
    name: six-routes
    duration: 35
    beat: build
    content: "六大技术路线全景，75%项目2025年新建"
  - id: s4
    name: autonomix
    duration: 50
    beat: reveal
    content: "明星项目Autonomix：85工具、T3D注入、VLM视觉、PIE自动测试"
  - id: s5
    name: mcp-ecosystem
    duration: 40
    beat: reveal
    content: "MCP协议生态：8个项目竞争，88工具居首"
  - id: s6
    name: claude-studios
    duration: 35
    beat: reveal
    content: "49 Agent虚拟工作室，73 Skills，三引擎通用"
  - id: s7
    name: business-analysis
    duration: 40
    beat: climax
    content: "成熟度评级A到C，风险矩阵，选型决策"
  - id: s8
    name: future
    duration: 35
    beat: climax
    content: "12个月预测：MCP官方支持、本地模型突破、自动化测试标配"
  - id: s9
    name: practical-guide
    duration: 45
    beat: settle
    content: "四件套技术栈：Autonomix+Game-Studios+MCP+Ollama"
  - id: s10
    name: cta
    duration: 10
    beat: summon
    content: "关注我，追踪AI工具链最前沿"

## 方向
orientation: portrait
orientation_source: default
