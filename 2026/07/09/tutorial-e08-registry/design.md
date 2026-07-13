# design.md — E08 段5 第三层 注册表 + 双口径（registry）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。注册表组合卡（首层 + 第二层 → 第三层 → 最终判定）+ 双口径对比（提交占比 vs 行数占比，行数占比金边强调）+ 下钻三 chip。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region：
> - R1 标题（左对齐）"第三层 注册表 + 双口径"
> - R2 注册表组合卡（首层 Co-authored-by + 第二层 风格学 → 第三层 注册表 → 最终判定）
> - R3 双口径对比（提交占比 vs 行数占比，行数占比金边强调 + 500 行 vs 5 行案例）
> - R4 下钻三 chip（按作者 / 按模块 / 按周）
>
> region 按 data-reveal 时间点淡入 + 方向。

## style

注册表组合判定卡 + 双口径对比卡。深蓝主底 + hex_grid 蜂巢底（与 stylometry diamond_lattice / hook dark_cipher / why contour_lines / coauthored scan_grid 异质）。金边强调行数占比口径。

## color_direction

深底 + 五色（蓝主调，金强调，绿/红分支判定结果）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（hex_grid 蜂巢叠层） |
| 首层节点 | `#3B82F6` | 蓝色（Co-authored-by 初筛） |
| 第二层节点 | `#8B5CF6` | 紫色（风格学复核） |
| 第三层 / 最终判定 | `#FBBF24` | 金色（注册表组合 → 最终判定） |
| 行数占比强调 | `#FBBF24` | 金色金边（行数占比口径更真实） |
| 提交占比口径 | `#60A5FA` | 浅蓝（提交占比，辅助口径） |
| 下钻 chip | `#10B981` | 绿色（按作者/模块/周，趋势分析） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region。region 按 data-reveal 时间点淡入 + 方向。

## bg_component

`hex_grid`（深蓝蜂巢网格，注册表条目感 + 与相邻段异质：hook dark_cipher / stylometry diamond_lattice / coauthored scan_grid）

## 容器文字处理（container_text 规则）

注册表组合卡三层节点胶囊内**仅短词**：
- 首层胶囊内：`Co-authored-by`（外标"初筛"）
- 第二层胶囊内：`风格学`（外标"复核"）
- 第三层胶囊内：`注册表`（外标"组合判定"）
- 最终判定胶囊内：`最终判定`（外标"AI 占比"）

双口径卡内短词：
- 提交占比卡：`提交占比`（外"数 commit 数"）
- 行数占比卡（金边）：`行数占比`（外"数改动行数 更真实"）

下钻三 chip 内短词：`作者` / `模块` / `周`（无需外标，技术术语清晰）。

长描述移容器外，确保字符×字号 < 容器内径×0.7。

## 渐变文字处理

- 渐变同色系禁白端点：行数占比金边卡用 `#FBBF24 → #F59E0B`（深金→暖金），不用白端点
- text-shadow 深蓝 `rgba(30,41,59,0.6)`（禁发光 0 0 Xpx，避 R-S6-023 + 不泛光）

## fx 层

冷色静态/脉冲（蓝/紫/金），alpha ≤ 0.22：
- fx-aura（静态光晕，3 处，左上蓝 + 右上紫 + 底部金）
- fx-pulse-ring（脉冲圆环，2 处，行数占比卡金边呼吸）
- fx-particle（粒子，1 处，底部冷蓝散点）
- ≥3 元素，禁划过类（scan/stream/beam）
