# design.md — E06 CTA 收尾（合集标识+E07预告+关注+中性提问）

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏·收尾段。合集标识 + E07 预告卡（防偷改测试 + 真实案例）+「关注不走丢」+ 中性提问「你的团队 AI 写代码能跑通端到端闭环吗」。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（合集标识+E07预告 / 关注引导 / 中性提问 / 教程仓库）。

## color_direction

深蓝 dark_cipher 底 + 合集金 + E07 预告蓝紫 + 关注红 + 提问金：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | dark_cipher | 代码矩阵 |
| 合集标识 | `#FBBF24` | 金 |
| E07 预告 | `#A78BFA` | 紫（测试主题）|
| 关注 CTA | `#FCA5A5` | 浅红（关注转化）|
| 中性提问 | `#FCD34D` | 金（互动）|
| 教程仓库 | `#60A5FA` | 蓝 |

## 视觉区域范式（1 场景）

- **region1 合集标识 + E07 预告**（reveal 0，fade）：合集标识「AI 转型实战 · E06」+ E07 预告卡（防偷改测试 + 4 真实案例 · 单点修复→大规模迁移）
- **region2 关注引导**（reveal 6，fade）：「关注不走丢」+ 合集还有七集
- **region3 中性提问**（reveal 12，fade）：大字提问「你的团队，AI 写代码能跑通端到端闭环吗？」
- **region4 教程仓库**（reveal 18，fade）：教程仓库在评论区 + Johnson-Jia/ai-landing-tutorial

## bg_component

`dark_cipher`
