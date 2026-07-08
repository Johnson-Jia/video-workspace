# design.md — E06 段9 工具演进：随能力做减法（阶梯图+金句卡）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏·升华段。三阶段阶梯图（入门 OpenSpec+Superpowers → 熟练 Superpowers → 精通 裸 Claude Code），逐级工具递减、能力递增。顶端金句卡「你就是最强的规范，你的话术就是专业的 prompt」，fx 用静态光晕强调。底部团队场景注脚。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 / 三阶段阶梯 / 金句卡 / 团队场景注脚）。

## color_direction

深蓝 dark_cipher 底 + 三阶段色（入门蓝 / 熟练紫 / 精通金）+ 金句卡金：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵 |
| 标题 | `#FCD34D` | 金色 |
| 入门（基础·框架兜底）| `#60A5FA` | 蓝 |
| 熟练（内化·执行交框架）| `#A78BFA` | 紫 |
| 精通（裸交互·个人上限）| `#FBBF24` | 金 |
| 金句卡 | `#FCD34D` | 金（顶端金句）|
| 团队注脚 | `#93C5FD` | 浅蓝（补充说明）|

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「随能力做减法」+ 副标「工具演进 · 三阶段」
- **region2 三阶段阶梯图**（reveal 4，left）：三阶梯节点（入门 OpenSpec+Superpowers / 熟练 Superpowers / 精通 裸 Claude Code）+ 每级工具数递减（2→1→0）+ 能力箭头递增
- **region3 金句卡**（reveal 18，fade）：顶端金句卡「你就是最强的规范 · 你的话术就是专业的 prompt」+ fx 静态光晕强调
- **region4 团队场景注脚**（reveal 28，fade）：底部注脚「团队协作/规范沉淀/新人上手 · 框架仍有价值 · 精通裸用是个人上限非团队标准」

## bg_component

`dark_cipher`
