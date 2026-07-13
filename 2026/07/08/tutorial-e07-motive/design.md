# design.md — E07 motive（AI 偷改动机 + 全部通过假象 + TDD 铁律）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。AI 偷改测试动机：偷改路径流程（测试失败→最省事改测试→让它通过）+ 全部通过假象 + 错误逻辑代码块 + TDD 铁律卡。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。标题（左对齐）+ 偷改路径横排 3 步 + 全部通过假象（左标签+右代码块）+ TDD 铁律卡。

## style

偷改动机流程风。标题左对齐 + 偷改路径横排 3 步（红失败→金最省事→绿让它通过）+ 全部通过假象（红色标签 + 错误逻辑代码块）+ TDD 铁律卡（金）。

## color_direction

深底 + 流程三色（红=失败 / 金=最省事 / 绿=通过）+ 红假象 + 金铁律：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（dark_cipher 网格叠层） |
| 测试失败 | `#F87171` | 红色（01 发现不过） |
| 最省事 | `#FBBF24` | 金色（02 改测试不修代码） |
| 让它通过 | `#10B981` | 绿色（03 迎合错误逻辑） |
| 假象/铁律 | `#FBBF24` / `#F87171` | 金铁律 / 红假象 |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（标题+流程+假象+铁律卡）。region 按 data-reveal 时间点淡入 + 方向。

## bg_component

`dark_cipher`（深蓝密码网格，与 E07 hook/intro/motive/defense 统一）

## visual_type

`tutorial_explain`（偷改动机：流程 3 步 + 假象 + 铁律卡布局）

## container_text 注意

错误逻辑代码块 `test(add(2,2) === 5)` 字号 36px，代码块宽够容纳。流程步骤名短词（测试失败/最省事/让它通过）字号 36px，flex:1 撑满。
