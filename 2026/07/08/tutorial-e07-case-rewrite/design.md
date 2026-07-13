# design.md — E07 段6 案例 12 Controller 重构（大规模迁移数据卡）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。大规模迁移数据卡（12 Controller / 211 API / 15000 行 / 110 任务）大字醒目 + 任务中断后自动恢复流程。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 / 规模数据卡 4 格 / 任务中断恢复流程 / 闭环撑住大规模标签）。

## color_direction

深蓝 hex_grid 底（与 E06 dark_cipher 差异）+ 数据金 + 恢复路径蓝 + 完成绿：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格 |
| 标题 | `#FCD34D` | 金色 |
| 数据大字 | `#FBBF24` | 金（醒目）|
| 数据标签 | `#93C5FD` | 浅蓝（单位说明）|
| 恢复路径 | `#60A5FA` | 蓝（中断→恢复）|
| 完成标记 | `#6EE7B7` | 绿（全部完成）|
| 闭环标签 | `#34D399` | 绿（撑住大规模）|

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「大规模迁移」+ 副标「个人中心前后端分离重构 · OpenSpec+Superpowers+tasks」
- **region2 规模数据卡 4 格**（reveal 6，left）：2×2 grid 大字数据卡（十二 Controller / 两百一十一 API / 一万五千行 / 一百一十任务），金边强调，width:100% 撑满
- **region3 任务中断恢复流程**（reveal 20，left）：流程链（跨周退出 → 重进 → 看 x 标记 → 接着干）+ 恢复路径蓝色箭头
- **region4 闭环标签**（reveal 32，fade）：绿边标签「闭环撑住大规模迁移 · 不只是小修小补」

## bg_component

`hex_grid`
