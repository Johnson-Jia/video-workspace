# 多 Agent 并行（段2）

## 主题
AI 转型推广期，多 Agent 并行把单点提效放大成规模——三种玩法 + Windows 起步坑。

## 旁白要点（对应脚本段2）
- 放大靠多 Agent 并行，三种玩法
- agent-teams：六步流程 + 四种策略 + 项目注册表跨项目复用
- psmux：一个终端驱动多个 Agent 并行开发不同端
- code-review 多 Agent：Haiku 资格审查 + 五个 Sonnet 并行专项审查 + 独立 Haiku 打置信度分 + 八十分才发评论
- 坑：Windows 同时跑五个 Agent 容易 fork 失败（内存不足）
- 建议：两到三个起步

## 视觉设计
- 三卡纵排（agent-teams / psmux / code-review）
- Windows 警示条（5 个 fork 失败 / 建议 2-3 个）
- 布局 space-between 撑满画布
- bg 换 scan_grid 或 diamond_lattice（与 hook/intro/why 异质）
- fx 冷色（蓝/紫/绿）alpha≤0.22，≥3 元素/场
