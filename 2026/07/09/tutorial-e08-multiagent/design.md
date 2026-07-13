orientation: landscape
resolution: 1920x1080
duration: 70

style: 沉稳科技 + 方法论卡片三纵列（深蓝底 + 冷色卡 + 强调色胶囊）
mood: 专注、专业、信息密度适中（推广期方法论展示）
color_direction: 深蓝底（#0a0e1a）+ 冷色强调（蓝 #60a5fa / 紫 #a78bfa / 绿 #34d399）+ 警示红 #f87171；同色系渐变禁白端点；文字 text-shadow 深蓝 rgba(30,41,59,0.6)
emotion_curve: [neutral, focus, focus, peak, peak, neutral]
storyboard:
- phase0 标题入场（多 Agent 并行 · 三种玩法）
- phase1 agent-teams 卡展开（六步 + 四策略 + 注册表）
- phase2 psmux 卡展开（一终端驱动多 Agent）
- phase3 code-review 卡展开（Haiku 资格 + 5 Sonnet 并行 + 阈值 80）
- phase4 Windows 警示条（5 个 fork 失败）
- phase5 建议 2-3 个起步 + 收尾

# 多 Agent 并行 · 视觉设计补充

## bg 组件
- 用 diamond_lattice（菱形网格冷蓝光斑）
- 与 hook（hex_grid）/ intro（dark_cipher）/ why（hex_grid）异质
- 组件路径：components/bg/diamond_lattice.html

## 布局（space-between 撑满画布）
- 顶部标题区（padding-top 80px）：「多 Agent 并行 · 三种玩法」
- 中部三卡纵排（flex:1 各占 1/3 高度，space-between 间距）
  - 卡1：agent-teams（六步流程 + 四策略 + 注册表）
  - 卡2：psmux（一个终端驱动多 Agent 并行）
  - 卡3：code-review 多 Agent（Haiku 资格 + 5 Sonnet 并行 + Haiku 打分阈值 80）
- 底部警示条（padding-bottom 80px）：Windows 5 个 fork 失败 → 建议 2-3 个

## 卡片结构（每张）
- 卡片标题（图标 + 项目名）
- 卡片要点（2-3 行短句）
- 强调色胶囊（关键数字/关键词）
- 卡片背景：rgba(13,9,5,0.88) 不透明深色（防 fx 光晕透白字，feedback-cm-card-transparent-bg）

## fx（冷色，静态/脉冲，≥3 元素）
- fx-aura 静态光晕 ×2（蓝 + 紫，alpha≤0.22）
- fx-pulse-ring ×1（绿色脉冲，calc(50%-100px) 居中）
- fx-particle ×1（冷色粒子）
- 禁划过类（scan/stream/beam）

## 字体
- 主标题：64px
- 卡片标题：36px
- 卡片正文：22px
- 警示条：24px
- 行高 1.4
