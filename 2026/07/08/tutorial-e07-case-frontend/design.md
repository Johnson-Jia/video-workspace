# design.md — E07 段7 案例 前端陪练（复杂集成案例卡）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。前端 AI 陪练对话生成案例卡（8 人日 / 5289 行 / React×Vue / SSE 拦截器）+ 复杂集成示意 + 第四案例一带而过。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 / 案例数据卡 / 复杂集成示意 / 第四案例+启示）。

## color_direction

深蓝 hex_grid 底（与 case-rewrite 一致，同集案例段）+ 数据金 + 集成蓝 + 启示绿：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格 |
| 标题 | `#FCD34D` | 金色 |
| 数据大字 | `#FBBF24` | 金（醒目）|
| 集成标签 | `#60A5FA` | 蓝（技术栈）|
| 启示 | `#6EE7B7` | 绿（落地证明）|
| 第四案例 | `#A78BFA` | 紫（一带而过）|

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「前端陪练」+ 副标「AI 生成对话交互模块 · 复杂集成」
- **region2 案例数据卡**（reveal 2，left）：4 格数据卡（八人日 / 五千二百八十九行 / React×Vue / SSE 拦截器）
- **region3 复杂集成示意**（reveal 10，left）：技术栈集成链（React ↔ Vue Monkey Patch + SSE 拦截器）
- **region4 启示+第四案例**（reveal 22，fade）：绿边启示卡（给足上下文+分步验证）+ 紫边第四案例一带而过

## bg_component

`hex_grid`
