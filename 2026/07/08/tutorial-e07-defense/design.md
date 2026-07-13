# design.md — E07 defense（三层防护：权限层金边强调 + deny 代码块 + 三层叠加）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。三层防护详解：提示词（弱化）+ 权限 deny（金边强调 关键）+ Git 兜底 + settings.json deny 代码块 + 三层叠加总结。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。标题（左对齐）+ 三层防护横排（02 权限金边强调）+ deny 代码块 + 三层叠加总结条。

## style

三层防护详解风。标题左对齐 + 三层防护横排卡（02 权限 deny 金边强调 + 关键 badge + 锁图标）+ settings.json deny 代码块（高亮）+ 三层叠加总结条。

## color_direction

深底 + 三色（蓝=提示词 / 金=权限关键 / 绿=Git 兜底）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（dark_cipher 网格叠层） |
| 提示词 | `#3B82F6` | 蓝色（01 靠自觉会被绕过） |
| 权限 deny | `#FBBF24` | 金色（02 关键 硬拦截） |
| Git 兜底 | `#10B981` | 绿色（03 最后核查） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（标题+三层防护+deny 代码+三层叠加）。region 按 data-reveal 时间点淡入 + 方向。

## bg_component

`dark_cipher`（深蓝密码网格，与 E07 hook/intro/motive/defense 统一）

## visual_type

`tutorial_explain`（三层防护：横排卡 + deny 代码块 + 叠加总结布局）

## container_text 注意

deny 代码块 `"deny": ["Write(test/**)", "Edit(test/**)", "Write(**/*.test.ts)"]` 字号 34px JetBrains Mono，代码块宽够容纳。
