# design.md — E07 hook（测试全绿但业务逻辑全错 + 权限层硬拦截）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。反常识钩子：测试全绿但业务逻辑全错 + AI 偷改测试 + 权限层硬拦截 + 四案例预告。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。标题（左对齐）+ 大字对比卡（测试全绿 vs 业务逻辑全错）+ 反常识条（AI 偷改测试迎合错误逻辑）+ 权限层硬拦截条。

## style

反常识钩子风。标题左对齐 + 大字对比卡（绿测试全绿 / 红业务逻辑全错）+ 反常识金条 + 权限层硬拦截金条 + 案例预告。

## color_direction

深底 + 对比双色（绿=测试通过 / 红=业务错）+ 金强调（反常识 / 权限层）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（dark_cipher 网格叠层） |
| 测试通过 | `#10B981` | 绿色（全部通过假象） |
| 业务错 | `#F87171` | 红色（业务逻辑全错） |
| 反常识/权限 | `#FBBF24` | 金色（关键强调） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（标题+对比卡+反常识条+权限层条）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 对比卡 left / 反常识 top / 权限层 top）。

## bg_component

`dark_cipher`（深蓝密码网格，与 E07 hook/intro/motive/defense 统一）

## visual_type

`tutorial_hook`（反常识钩子：大字对比 + 反常识条 + 权限层条布局）
