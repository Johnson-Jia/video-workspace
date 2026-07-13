# design.md — E07 CTA（合集标识+E08预告+中性提问+关注CTA）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏收尾段。合集标识 + E08 预告卡（AI 代码占比度量）+ 中性提问（AI 写的测试你敢直接信任吗）+ 关注 CTA。收尾段居中合理。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（合集标识+E08预告 / 中性提问 / 关注CTA / 教程仓库）。

## color_direction

深蓝 hex_grid 底 + 合集金 + E08预告蓝 + 提问金 + CTA绿：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格 |
| 合集标识 | `#FBBF24` | 金（合集识别）|
| E08 预告 | `#60A5FA` | 蓝（下集预告）|
| 中性提问 | `#FCD34D` | 金（提问强调）|
| 关注 CTA | `#6EE7B7` | 绿（行动引导）|

## 视觉区域范式（1 场景）

- **region1 合集标识+E08预告**（reveal 0，fade）：合集标识「AI 转型实战 · E07」+ E08 预告卡（AI 代码占比度量 · 三层识别防伪造）
- **region2 中性提问**（reveal 8，fade）：大字提问「AI 写的测试你敢直接信任吗」（中性，禁站队）
- **region3 关注CTA**（reveal 16，fade）：绿边 CTA 卡（点关注不走丢 · 合集还有六集）
- **region4 教程仓库**（reveal 22，fade）：评论区引导（教程仓库在评论区）

## bg_component

`hex_grid`
