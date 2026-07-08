# design.md — E06 段7 TDD + 子代理分工

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。四代理卡片（Explore/实现/规格审/质量审）+ TDD 循环图（RED→GREEN→REFACTOR 三圆环）+ 一条铁律卡。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 / 四代理卡片 / TDD 循环 / 铁律卡）。

## color_direction

深蓝 dark_cipher 底 + 四代理分色（蓝/绿/紫/金）+ TDD 三色（红/绿/蓝）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵 |
| 标题 | `#FCD34D` | 金色 |
| Explore 代理 | `#60A5FA` | 蓝（搜索只读）|
| 实现代理 | `#6EE7B7` | 绿（改代码）|
| 规格审代理 | `#A78BFA` | 紫（对照 spec）|
| 质量审代理 | `#FBBF24` | 金（风格安全）|
| RED 测试失败 | `#FCA5A5` | 红 |
| GREEN 测试过 | `#6EE7B7` | 绿 |
| REFACTOR 重构 | `#60A5FA` | 蓝 |
| 铁律 | `#FCA5A5` | 红（警示）|

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「TDD 加子代理分工」+ 副标「阶段四 · RED GREEN REFACTOR」
- **region2 四代理卡片**（reveal 4，left）：四卡（Explore 只搜索只读 / 实现按 plan 改代码 / 规格审对照 spec / 质量审查风格安全命名）+ 各司其职标签
- **region3 TDD 循环**（reveal 18，fade）：三圆环（RED 先写测试看它失败 → GREEN 写最少代码让测试过 → REFACTOR 重构）+ 循环箭头
- **region4 铁律卡**（reveal 32，fade）：红边警示卡「不要让 Claude 同时写代码和测试 · 它会写出验证错误逻辑的测试 · 全绿但全错」+ 测试先行独立验证

## bg_component

`dark_cipher`
