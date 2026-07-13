# design.md — E07 段5（案例 form 编辑器：时间线 + 方案演进）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。案例时间线（需求→2 Explore→2 次纠方向→3 方案→最终 2 文件 10 行）+ 方案演进卡（v1/v2/v3 对比，v3 金边）。E07 真实案例——form 编辑器数据丢失修复。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 6 region（避开 R-R-010）。标题 + 时间线（横向节点依次出现）+ 方案演进卡（v1/v2/v3 对比）+ 启示金句，按 narration 锚点 reveal 同屏累积。

## style

案例时间线风。上方横向时间线（需求→Explore→纠方向→方案→最终，节点依次出现）+ 下方方案演进卡（v1/v2/v3 三栏对比，v3 金边强调）+ 启示金句。

## color_direction

深底 + 三色方案（红=v1 覆盖不全 / 黄=v2 改动大 / 金=v3 最优）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（scan_grid 网格叠层） |
| 时间线节点 | `#3B82F6` | 蓝色（流程节点） |
| v1 | `#F87171` | 红色（覆盖不全，差） |
| v2 | `#FBBF24` | 黄色（改动大，中） |
| v3 | `#34D399` | 绿色（最优，金边强调） |
| 最终数据 | `#FBBF24` | 金色（2 文件 10 行） |
| 启示 | `#A78BFA` | 蓝紫（用户引导是核心） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+时间线+方案卡+金句）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 时间线 top / 节点 stagger / 方案卡 left / 金句 top）。

## 视觉区域范式（1 场景，~40s TTS）

### 单场景：form 编辑器案例（6 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「案例一 · form 编辑器数据丢失」+ 副「2 次纠方向 · 3 方案演进」
- **region2 时间线-前半**（data-reveal=4，dir=top）：时间线 reveal 需求节点 + 两个 Explore 节点 + 两次纠方向节点（横向依次）
- **region3 时间线-后半**（data-reveal=12，dir=fade）：时间线 reveal 三方案节点 + 最终节点（2 文件 10 行，金色）
- **region4 方案卡-v1**（data-reveal=18，dir=fade）：v1 卡 reveal（prop 开关 · 2 文件 · 覆盖不全 · 红✗）
- **region5 方案卡-v2/v3**（data-reveal=24，dir=fade）：v2 卡 reveal（prop 开关 · 25 文件 · 改动大 · 黄△）+ v3 卡 reveal（provide/inject · 2 文件 · 自动覆盖 · 绿✓ 金边）
- **region6 启示金句**（data-reveal=32，dir=top）：金句「用户引导是核心 · AI 是执行者」

## 动画策略

- 时间线节点逐个 reveal（scale 0→1，stagger 1.5s）
- 方案卡逐个 reveal（v1→v2→v3，stagger 3s，v3 金边脉冲）
- region fade-in + 方向偏移，500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`scan_grid`（深蓝扫描网格，与 E04/deny/tdd 同款保持合集一致）

## visual_type

`tutorial_case_timeline`（横向时间线 + 方案演进卡 + 启示金句布局）
