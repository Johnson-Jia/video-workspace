# design.md — FDE 番外篇 · hook 段（数据钩子：两年四十二倍的新岗位）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程类强制横屏（categories/tutorial.md orientation_hint=landscape）。三组数据卡 + FDE 大字收尾，多区域同屏 reveal，竖屏装不下。s6_assemble 横屏分支依赖此字段。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16 教程横屏范式：单 phase + 多 region + data-reveal（不是竖屏 phase 切换）。三组数据卡依次 reveal 同屏累积，不换屏。每场景一个 phase，场景内 region 用 data-reveal 错时。

## fields（gate 解析速览）

style: 清爽专业科技风·数据钩子（冷静克制，靠数字冲击不靠花哨动画）
mood: 沉稳·好奇（数据悬念开场 + 口径严谨 + FDE 大字收束，不煽动）
color_direction: 深蓝底 #0F172A + 金 #FBBF24（数据冲击）+ 蓝 #3B82F6（定义对照）+ 蓝白 #E0E7FF + 中性 #94A3B8
storyboard: 数据钩子 4 场景（42倍数字 / 40-60配比 / FDE 大字揭晓 / ≠AI Engineer 对照），narrative_template+emotion_curve+immersion_mode（教程横屏 reveal）见下
emotion_curve: [0.90, 0.55, 0.50, 0.65, 0.80, 0.95]

## style

清爽专业科技风·数据钩子。冷静、克制——三组数据依次弹出，靠数字本身冲击，不靠花哨动画。深蓝底 + fx-aura 静态光晕脉冲（禁划过类 fx）。教程重内容轻视觉。

## mood

沉稳·好奇——用数据悬念开场（什么岗位涨四十二倍？），层层给口径标注（严谨感），结尾 FDE 大字收束。不煽动、不夸张。

## color_direction

深蓝底 + 双色分工（金=数据冲击 / 蓝=定义与对照）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（沉稳，让数据跳出来） |
| 数据冲击 | `#FBBF24` | 「42 倍↑」「40% / 60%」金色数据大字 |
| 定义与对照 | `#3B82F6` | 「FDE · 前线部署工程师」大字、≠ 对照卡边框 |
| 蓝白 | `#E0E7FF` | 口径标注 / 次要文字 |
| 中性 | `#94A3B8` | 注释 / 分隔 |

> 强色控制：金/蓝严格分工——金=数据冲击（钩子数字），蓝=岗位定义与对照（理性）。口径标注一律蓝白小字（严谨感）。渐变文字禁白色端点，同色系高饱和（金 #FBBF24→#F59E0B→#FCD34D / 蓝 #60A5FA→#3B82F6→#93C5FD）。

## storyboard

### narrative_template

数据钩子（单段 hook）：
1. 悬念开场：一个岗位两年涨四十二倍（数字冲击 + 口径标注严谨感）
2. 精力配比：40% 写代码 + 60% 面向客户（经验刻画）
3. 岗位揭晓：FDE · 前线部署工程师（大字定格）
4. 差异对照：≠ AI Engineer（偏客户现场 + 业务落地，相对稀缺）

### emotion_curve

[0.90, 0.55, 0.50, 0.65, 0.80, 0.95]

> 节奏：开场数字冲击高（0.90）→ 口径标注回落求严谨（0.55/0.50）→ 配比数据回稳（0.65）→ FDE 揭晓爬升（0.80）→ 差异对照收束在高位（0.95，稀缺感留悬念给 intro 段）。

### immersion_mode

教程横屏 reveal — 每场景单 phase + 多 region data-reveal 同屏累积。数据卡 reveal 后保持在场（不消失），四场景依次推进。

## 视觉区域范式

### 场景 1：数字钩子（~5s，「42 倍」大字）

- **数据大字区**（data-reveal=0）：金色渐变大字「42 倍↑」（200px 级）+ 蓝白小字「一个岗位 · 两年招聘增长」
- **fx-aura**：大字后方金色静态光晕脉冲呼吸（alpha 0.18 ≤ 0.22，禁划过类）

### 场景 2：口径 + 精力配比（~13s，严谨感）

- **口径标注区**（data-reveal=0）：蓝白小字胶囊「媒体转引 · 置信度中等」「经验刻画 · 非精确统计」
- **配比双卡区**（data-reveal=2 依次）：金色数据卡「40% 写代码」「60% 面向客户」左右并排 reveal
- **fx-blink**：角落锚点点缀

### 场景 3：岗位揭晓（~5s，FDE 大字）

- **FDE 大字区**（data-reveal=0）：蓝色渐变大字「FDE · 前线部署工程师」+ 蓝白小字「Forward Deployed Engineer」
- **fx-aura**：蓝色静态光晕

### 场景 4：差异对照（~10s，≠ AI Engineer）

- **对照大字区**（data-reveal=0）：蓝色「≠ AI Engineer」+ 副题「偏客户现场 · 偏业务落地 · 相对稀缺」
- **对照小卡区**（data-reveal=4）：两张并列小卡「AI 工程师｜偏纯技术」「FDE｜偏客户现场」reveal
- **fx-blink**：锚点平衡构图

## 动画策略

- **数据大字 fade-in**：opacity 0→1 + scale 1.04→1，600ms ease-out（克制）
- **口径胶囊 reveal**：opacity 0→1，500ms
- **数据卡依次 reveal**：data-reveal 错时 2s，同屏累积
- **fx-aura 静态光晕**：脉冲呼吸（opacity 0.4→0.6 循环），不划过不追线
- **禁**：fx-scan/fx-stream/fx-beam 划过类、粒子过载、3D 翻转、强切换

## bg_component

`clean_slate`（数据钩子收敛简洁底，四场景共用）

## visual_type 映射

- 场景 1：`data_burst`（42 倍数字冲击开场）
- 场景 2：`dual_stats`（40/60 配比双卡 + 口径标注）
- 场景 3：`title_reveal`（FDE 岗位大字揭晓）
- 场景 4：`contrast_cards`（≠ AI Engineer 对照）
