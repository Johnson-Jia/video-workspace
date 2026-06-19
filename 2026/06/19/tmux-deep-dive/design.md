---
# design.md — 视觉风格方向 + 故事板（tmux 深度解析）

## 风格
style: 终端暗色科技        # 暗色做底 + 终端经典色（琥珀/终端绿）做刀，呼应 tmux 终端复用器身份
mood: 沉静深度·理性克制     # 开源基建项目气质，非营销话术，工程师视角

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，终端背景感）
  accent_cool: 终端绿 / 青色（用于架构图、client-server 拓扑、功能速览——技术理性）
  accent_warm: 琥珀色 / 金色（用于 hook 痛点、CTA、关键数字锚点——情绪锚）
  text: 白色主 + 浅灰辅 + 终端绿点缀（命令/路径/技术术语）
  visual_note: "终端美学——等宽体命令行、网格/扫描线背景、ASCII 拓扑图风格的架构可视化"

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "等宽极客"
    family: "JetBrains Mono"
    weight: 800
    rationale: "tmux 是终端工具，理性/精准/极客的情感内核最适合等宽体，呼应命令行美学"
    fallback: "'JetBrains Mono','Consolas','Courier New',monospace"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/暗色氛围·克制电子（lo-fi / ambient electronic，非高能 EDM——基建项目需要沉静感而非爆点）

## 素材预判（架构图场景必须可视化）
assets_needed:
  - "client-server 进程拓扑图（用户终端 → tmux client → Unix socket → tmux server daemon）—— scene5 必做"
  - "渲染三层架构图（grid → screen → tty）—— scene5 必做"
  - "断线/会话存活对比图（client 断开 vs server session 保留）—— scene1 hook + scene4 解耦"

## 故事板
storyboard:
  narrative_template: "mystery-box"       # 好奇（SSH 断线痛点）→ 线索（client-server 自孵化）→ 揭示（会话终端解耦=持久化根基）→ 惊喜（架构图+渲染分层）→ 结论（适用场景+诚实边界）
  emotion_curve: [0.6, 0.45, 0.7, 0.85, 0.55, 0.4]   # hook 高(痛点) → what 平(定位) → 哲学爬升 → 架构图高潮 → 边界沉淀(诚实) → CTA 收
  immersion_mode: "hidden-gem"            # 隐藏宝石：单项目深度解析，非盘点 hyper-pace；脉冲光晕 + 终端网格
  humor_style: "narration-only"           # 旁白单线克制幽默（基建项目，不夸张）
  character_presence: false               # 无码力角色（开源架构深度，严肃理性）
  beat_mapping:
    grab: "hook（SSH 断线痛点）"
    build: "what（tmux 是什么）+ 哲学①（client-server 自孵化）"
    reveal: "哲学②（会话终端解耦）+ 架构图（拓扑+渲染分层）"
    climax: "架构图三层揭示"
    settle: "功能速览 + 软硬件限制 + 性能边界（诚实）"
    summon: "适用场景 + 推荐 + CTA"

## 方向
orientation: portrait        # 竖屏（抖音默认）
orientation_source: default  # 用户指定竖屏 portrait

## 架构图场景视觉规划（scene5 必做，深度解析核心）
architecture_diagram_plan:
  scene: "architecture"
  visual_phases:
    - phase: 1
      focus: "进程拓扑：用户终端 → tmux client → Unix socket/imsg → tmux server daemon（libevent 事件循环）"
      visual_type: "timeline"
      key_data: ["用户终端", "tmux client", "Unix socket", "imsg 协议", "tmux server", "libevent"]
    - phase: 2
      focus: "对象模型：session → window(winlink) → window_pane → pty(forkpty)，红黑树+队列管理"
      visual_type: "list"
      key_data: ["session", "window(winlink)", "window_pane", "pty(forkpty)", "红黑树+队列"]
    - phase: 3
      focus: "渲染分层（性能关键）：grid（字符存储·懒分配+紧凑压缩）→ screen（显示状态/重绘）→ tty（终端能力 terminfo）"
      visual_type: "timeline"
      key_data: ["grid 字符存储", "懒分配+紧凑cell压缩", "screen 显示/重绘", "tty 终端能力 terminfo"]
  visual_note: "用终端绿/青色绘制 ASCII 风格拓扑节点 + 箭头连线，server daemon 节点用琥珀色高亮（核心锚点），呼应 client-server 自孵化哲学"
