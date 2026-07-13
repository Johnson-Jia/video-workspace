# design.md — E07 intro（方法论：三层防护 + 四案例预告 + 学习目标）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。方法论预告：三层防护（提示词/权限 deny/Git 兜底）+ 四案例预告 + 学习目标三栏。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。标题（左对齐）+ 三层防护横排（权限层金边强调）+ 四案例预告横排 + 学习目标三栏。

## style

方法论预告风。标题左对齐 + 三层防护横排卡（02 权限 deny 金边强调）+ 四案例预告胶囊横排 + 学习目标三栏（绿色 ✓）。

## color_direction

深底 + 三色（蓝=提示词 / 金=权限关键 / 绿=Git 兜底）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（dark_cipher 网格叠层） |
| 提示词 | `#3B82F6` | 蓝色（01 靠自觉） |
| 权限 deny | `#FBBF24` | 金色（02 关键 硬拦截） |
| Git 兜底 | `#10B981` | 绿色（03 diff 核查） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（标题+三层防护+四案例+学习目标）。region 按 data-reveal 时间点淡入 + 方向。

## bg_component

`dark_cipher`（深蓝密码网格，与 E07 hook/intro/motive/defense 统一）

## visual_type

`tutorial_intro`（方法论预告：三层防护横排 + 四案例 + 学习目标布局）
