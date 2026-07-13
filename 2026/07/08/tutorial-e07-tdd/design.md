# design.md — E07 段4（TDD 铁律：RED/GREEN/REFACTOR 循环图）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。TDD 循环图（RED/GREEN/REFACTOR 三圆，圆内仅短词，长词移外）+ 铁律卡（不同时写代码和测试）。E07 防偷改测试——TDD 铁律。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 6 region（避开 R-R-010）。标题 + TDD 循环图（三圆逐个 reveal + 箭头流转）+ 铁律卡 + 金句，按 narration 锚点 reveal 同屏累积。

## style

TDD 循环图风。左侧 TDD 三圆循环（RED 红/GREEN 绿/REFACTOR 蓝紫，圆内仅 3-4 字母短词，长词 RED/GREEN/REFACTOR 全称移圆外下方）+ 流转箭头，右侧铁律卡（不同时写代码和测试 + 错误逻辑测试示例）。底部金句。

## color_direction

深底 + 三色循环（红=RED 失败 / 绿=GREEN 通过 / 蓝紫=REFACTOR 重构）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（scan_grid 网格叠层） |
| 圆-RED | `#F87171` | 红色（先写测试看它失败） |
| 圆-GREEN | `#34D399` | 绿色（写最少代码让测试过） |
| 圆-REFACTOR | `#A78BFA` | 蓝紫（重构） |
| 铁律 | `#FBBF24` | 金色（不同时写代码和测试） |
| 金句 | `#FBBF24` | 金色（测试先行） |
| 错误逻辑 | `#F87171` | 红色（验证错误逻辑的测试） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+循环图+铁律卡+金句）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 循环图 top / 三圆 stagger / 箭头 draw / 铁律卡 left / 金句 top）。

## 视觉区域范式（1 场景，~70s TTS）

### 单场景：TDD 铁律循环（6 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「TDD 铁律 · 测试先行」+ 副「不同时写代码和测试」
- **region2 循环图-RED 圆**（data-reveal=6，dir=top）：RED 圆 reveal（圆内「RED」3 字母短词 + 圆外下方「先写测试看它失败」长词）+ 红色脉冲
- **region3 循环图-GREEN 圆 + 箭头**（data-reveal=16，dir=fade）：GREEN 圆 reveal（圆内「GREEN」5 字母 + 圆外「写最少代码让测试过」）+ RED→GREEN 箭头
- **region4 循环图-REFACTOR 圆 + 箭头**（data-reveal=28，dir=fade）：REFACTOR 圆 reveal（圆内「REF」3 字母短词 + 圆外「REFACTOR 重构」长词）+ GREEN→REFACTOR 箭头 + REFACTOR→RED 回环箭头
- **region5 铁律卡**（data-reveal=42，dir=left）：右侧卡「不同时写代码和测试」+ 错误逻辑测试示例（AI 写验证错误逻辑的测试 → 全部通过但业务逻辑全错）+ 正确做法（测试先行 + 独立验证）
- **region6 金句**（data-reveal=56，dir=top）：金句「测试先行 · 独立验证」

## 动画策略

- 三圆逐个 reveal（scale 0→1 + 脉冲呼吸，stagger 10s）
- 流转箭头 draw（stroke-dasharray 动画，500ms）
- region fade-in + 方向偏移，500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`scan_grid`（深蓝扫描网格，与 E04 claudemd / E07 deny 同款保持合集一致）

## visual_type

`tutorial_tdd_cycle`（TDD 三圆循环图 + 铁律卡 + 金句布局）

## container_text 注意

圆内仅短词（RED/GREEN/REF），长词（REFACTOR 全称、先写测试看它失败等）移圆外下方。圆内径约 240px，字号 48px，字符×字号 < 内径×0.7（168px）。"GREEN" 5 字符 × 48px = 240px > 168px，故 GREEN 圆内用 "GRN" 缩写或字号缩到 32px（5×32=160<168 OK）。"REF" 3 字符 × 48px = 144px < 168px OK。"RED" 3 字符 × 48px = 144px < 168px OK。
