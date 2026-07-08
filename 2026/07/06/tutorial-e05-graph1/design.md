# design.md — E05 段3（代码知识图谱原理：节点图可视化，重头戏）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。代码知识图谱原理：核心新组件——知识图谱节点图（圆形节点 + SVG 连线 + Community 染色），选中节点 ring 发光 + 调用链边点亮，底部六阶段索引流水线。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 6 region**（scenes=1）。标题 + 节点图（节点 stagger 出现 → 选中高亮 → 边点亮）+ 三个好处 + 分层共存 + 六阶段流水线，按 narration 锚点 reveal 同屏累积。

## style

代码知识图谱可视化风。主视觉：节点图（认证域蓝色节点 / 支付域绿色节点 + SVG CALLS 边 + 选中节点 ring 发光 + 调用链边流光）。右上浮「三个好处」卡，下方分层共存条，底部六阶段索引流水线（横向圆点依次点亮）。

## color_direction

深蓝 hex_grid 底 + 双 Community 染色（认证蓝/支付绿，同色系禁白端点）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格（基础设施结构感） |
| 认证域节点 | `#3B82F6` | 蓝（validateToken/checkSession） |
| 支付域节点 | `#10B981` | 绿（processPay/PaymentService） |
| 选中节点 ring | `#60A5FA` | 浅蓝光晕（同色系） |
| CALLS 边（active） | `#60A5FA` | 浅蓝流光（确定调用关系） |
| IMPORTS 边 | `rgba(148,163,184,0.4)` | 灰虚线（依赖关系） |
| 三个好处 | 蓝/绿/金 | 可靠/省token/解放小模型 |
| 分层共存 | 蓝 + 绿 | 图查询/向量搜索 |
| 蓝白 | `#E0E7FF` | 标题/节点标签 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region。region 按 data-reveal 时间点淡入/缩放出现（标题 fade / 节点 scale stagger / 边 stroke-opacity / 三个好处 left / 流水线 bottom）。

## 视觉区域范式（1 场景，~70s TTS）

### 单场景：知识图谱节点图（6 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「代码知识图谱 · 重头戏」+ 副「索引期算关系 · 一次拿全调用链」
- **region2 节点图骨架**（data-reveal=5，dir=fade）：节点（validateToken/checkSession/AuthController 蓝色认证域 + processPay/PaymentService/checkout 绿色支付域）scale 0→1 stagger 出现，SVG CALLS/IMPORTS 边连线（初始低 opacity）
- **region3 选中高亮 + 调用链点亮**（data-reveal=16，dir=fade）：processPay 节点 ring 发光 + 其 CALLS 链边 stroke-opacity 0→1 流光（展示「一次查询拿全调用链」）
- **region4 三个好处卡**（data-reveal=28，dir=left）：右侧浮现三个好处（可靠：漏不掉上下文 / 省 token：不查十次 / 解放小模型：降顶级依赖）
- **region5 分层共存条**（data-reveal=40，dir=top）：图查询（确定） ↔ 向量搜索（语义）各管一摊
- **region6 六阶段流水线**（data-reveal=46，dir=top）：底部横向 6 圆点（扫描→解析→传播→社区→执行流→概念）依次点亮 + 连线渐进绘制

## 动画策略

- 节点 scale 0→1 stagger 出现（GSAP fromTo，每个节点 delay 0.15s，共 6 节点）
- 选中节点 ring 发光（box-shadow 同色系 pulse，非 0 0 发光 text-shadow）
- 调用链边流光（SVG stroke-dashoffset 动画 + stroke-opacity 0→1，CSS animation 循环态可，禁入场）
- 流水线圆点依次点亮（fill 颜色变化，data-reveal stagger）
- region fade-in + 方向偏移，500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`hex_grid`（六边网格，基础设施结构感；E05 全集统一 bg）

## visual_type

`tutorial_graph_viz`（知识图谱节点图 + 六阶段索引流水线布局）
