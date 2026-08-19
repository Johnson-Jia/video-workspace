# design.md — FDE 番外篇 · intro 段（视角声明：从甲方内部到乙方 FDE）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程类强制横屏（categories/tutorial.md orientation_hint=landscape）。左右分栏对照 + 定义卡 + 全流程链，横屏多 region 同屏 reveal，竖屏装不下。s6_assemble 横屏分支依赖此字段。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16 教程横屏范式：单 phase + 多 region + data-reveal（不是竖屏 phase 切换）。分栏两卡、定义链节点依次 reveal 同屏累积，不换屏。每场景一个 phase，场景内 region 用 data-reveal 错时。

## fields（gate 解析速览）

style: 清爽专业科技风·视角声明（左右分栏对照 + 定义卡，靠结构对比不靠花哨动画）
mood: 沉稳·切换（视角宣告 → 对照展开 → 定义收拢，不煽动）
color_direction: 深蓝底 #0F172A + 蓝 #3B82F6（甲方内部/定义主体）+ 金 #FBBF24（乙方 FDE/切换落点）+ 蓝白 #E0E7FF + 中性 #94A3B8
storyboard: 视角声明 4 场景（切换宣告 / 甲方乙方分栏对照 / FDE 定义卡 / 本集定位），narrative_template+emotion_curve+immersion_mode（教程横屏 reveal）见下
emotion_curve: [0.60, 0.68, 0.78, 0.62, 0.72, 0.80]

## style

清爽专业科技风·视角声明。左右分栏结构对比（甲方内部 vs 乙方 FDE），中间竖线 + 切换箭头做视觉轴。深蓝底 + 静态/脉冲 fx（禁划过类）。教程重内容轻视觉。

## mood

沉稳·切换——先宣告视角切换（本集立场变了），再左右展开两套视角对照（有重叠但立场不同），落到 FDE 定义卡（Palantir 起源 + 全流程负责），收在一句定位（成长地图 + 实战方法论）。理性克制，像开场白不像广告。

## color_direction

深蓝底 + 双色分工（蓝=甲方内部·定义主体 / 金=乙方 FDE·切换落点）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（沉稳，让结构对比跳出来） |
| 甲方内部 / 定义主体 | `#3B82F6` | 左栏卡边框、FDE 大字、全流程链节点 |
| 乙方 FDE / 切换落点 | `#FBBF24` | 右栏卡边框、切换箭头、定位句高亮 |
| 蓝白 | `#E0E7FF` | eyebrow / 次要说明文字 |
| 中性 | `#94A3B8` | 注释 / 分隔线 / 竖线 |

> 强色控制：蓝/金严格分工——蓝=甲方侧与 FDE 定义主体（理性），金=乙方侧与切换落点（现场感）。渐变文字禁白色端点，同色系高饱和（金 #FBBF24→#F59E0B→#FCD34D / 蓝 #60A5FA→#3B82F6→#93C5FD）。fx 暖色 alpha ≤ 0.22。

## storyboard

### narrative_template

视角声明（单段 intro）：
1. 切换宣告：先说一个重要的视角切换（本集立场变了）
2. 视角对照：甲方内部（带自己的团队）↔ 乙方 FDE（进客户现场），两套肌肉有重叠但立场不同
3. FDE 定义：Forward Deployed Engineer，Palantir 起源，带 AI 产品进客户现场，需求探索→生产上线全流程负责
4. 本集定位：FDE 成长地图 + 客户现场实战方法论（武器库 → 现场怎么用）

### emotion_curve

[0.60, 0.68, 0.78, 0.62, 0.72, 0.80]

> 节奏：切换宣告中高起（0.60，宣告立场变化）→ 分栏对照展开爬升（0.68/0.78，左右对撞是本段视觉高点）→ 重叠带回落求稳（0.62，理性说明两套肌肉关系）→ 定义卡沉稳推进（0.72）→ 定位句收在高位（0.80，把期待递给正文第 1 章）。

### immersion_mode

教程横屏 reveal — 每场景单 phase + 多 region data-reveal 同屏累积。分栏两卡先左后右 reveal，定义链节点依次点亮，reveal 后保持在场。

## 视觉区域范式

### 场景 1：切换宣告（~5s，「视角切换」大字）

- **切换大字区**（data-reveal=0）：金色渐变大字「视角切换」（160px 级）+ 蓝白 eyebrow「FDE 番外 · 立场变了」
- **fx-pulse-ring**：大字后方蓝金双环静态脉冲锚点（冷色为主，暖色 alpha ≤ 0.22）

### 场景 2：甲方乙方分栏对照（~20s，左右分栏）

- **分栏对照区**（data-reveal=0/2 先左后右）：左卡「甲方内部｜带自己的研发团队」蓝边框 / 右卡「乙方 FDE｜进客户业务现场」金边框，中间竖线 + 切换箭头「→」（视觉轴）
- **重叠带**（data-reveal=12）：底部横条「都用 AI · 都要证明价值 · 立场不同」reveal
- **fx-blink**：两栏角落锚点平衡构图

### 场景 3：FDE 定义卡（~28s，Palantir 起源 + 全流程）

- **定义头区**（data-reveal=0）：蓝色渐变大字「FDE · 前线部署工程师」+ 蓝白小字「Forward Deployed Engineer」+ 起源胶囊「概念起源 · Palantir」
- **定义句区**（data-reveal=4）：定义文字「把 AI 产品带进客户业务现场 · 按需求设计实现 · 落地扎根」
- **全流程链区**（data-reveal=10）：四节点链「需求探索 → 设计实现 → 落地扎根 → 生产上线」+ 尾标「全流程负责」，节点依次点亮
- **fx-aura**：冷蓝静态光晕脉冲

### 场景 4：本集定位（~18s，成长地图 + 实战方法论）

- **定位大字区**（data-reveal=0）：双色大字「成长地图 + 实战方法论」（蓝「成长地图」+ 金「实战方法论」）+ 蓝白小字「一句话定位这集」
- **对照小卡区**（data-reveal=6）：两卡「前面十三集｜技术武器库」「这一集｜武器在客户现场怎么用」reveal
- **fx-pulse-ring**：定位大字锚点环

## 动画策略

- **切换大字 fade-in**：opacity 0→1 + scale 1.04→1，600ms ease-out（克制）
- **分栏卡 reveal**：左卡 data-reveal=0，右卡 data-reveal=2，箭头随右卡点亮
- **链节点依次点亮**：data-reveal 每节点错 2s，点亮后保持
- **fx-pulse-ring 静态脉冲**：环呼吸扩散（不划过不追线），冷色为主
- **禁**：fx-scan/fx-stream/fx-beam 划过类、粒子过载、3D 翻转、强切换

## bg_component

`clean_slate`（s01/s03，宣告与定义收敛底）+ `hex_grid`（s02 分栏结构底）+ `scan_grid`（s04 定位收束底）

## visual_type 映射

- 场景 1：`title_reveal`（视角切换大字宣告）
- 场景 2：`contrast_cards`（甲方乙方左右分栏对照）
- 场景 3：`definition_card`（FDE 定义卡 + 全流程链）
- 场景 4：`positioning_statement`（一句话定位 + 武器库对照）
