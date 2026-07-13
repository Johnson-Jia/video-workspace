# design.md — E08 cta（收尾：E09 预告 + 关注 CTA + 互动问）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。收尾段：合集标识 + E09 预告卡（金边强调下一集）+ 关注 CTA（合集还有五集）+ 互动问大字收尾（中性，禁站队）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。合集标识（左对齐 tag）+ 本集总结数据底座 + E09 预告卡（金边）+ 关注 CTA + 互动问大字。region 按 data-reveal 时间点淡入 + 方向。

## style

收尾预告风。合集标识 tag（左对齐）+ 本集总结数据底座卡（蓝绿渐变）+ E09 预告卡（金边强调下一集 Skill 范式整合）+ 关注 CTA（合集还有五集 + 教程仓库评论区）+ 互动问大字（中性问句收尾）。

## color_direction

深底 + 三色（蓝=本集数据底座 / 金=E09 预告关键 / 绿=关注 CTA）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（hex_grid 网格叠层） |
| 数据底座（本集） | `#3B82F6` | 蓝色（本集总结） |
| E09 预告（关键） | `#FBBF24` | 金色（下一集 Skill 范式整合金边强调） |
| 关注 CTA | `#10B981` | 绿色（合集还有五集 + 点关注） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（合集标识+本集总结 / E09 预告 / 关注 CTA / 互动问）。region 按 data-reveal 时间点淡入 + 方向。

## bg_component

`hex_grid`（深蓝六边网格，与相邻 essence dark_cipher 异质做差异）

## visual_type

`tutorial_cta`（收尾：合集标识 + 本集总结 + E09 预告 + 关注 CTA + 互动问布局）

## 字数核算

旁白约 100 字（中文 +0% 实际约 5.3 字/秒）。目标时长 ~30s。100 字 ÷ 5.3 ≈ 19s，偏短——补合集标识 + E09 预告卡 + 互动问 reveal 等待补足到 ~30s 视觉时长。实际按 narration 时长定 phase 时长。

## visual_phasing（data-reveal stagger）

1. 合集标识 + 本集总结数据底座 fade-in（合集 tag + 一句话总结）
2. E09 预告卡（金边强调下一集 Skill 范式整合）reveal 左滑入
3. 关注 CTA（合集还有五集 + 点关注 + 教程仓库评论区）reveal 底部上滑
4. 互动问大字（中性：你的团队 AI 写了多少代码，能量出来吗？）reveal 顶部下推

## 旁白句拆（narration_anchor）

- 句0：「AI 代码占比是转型的数据底座——三层识别防伪造，事前估算配事后统计。」
- 句1：「下集讲 Skill 范式整合，怎么把个体经验变成组织资产。」
- 句2：「合集还有五集，点关注不走丢，教程仓库在评论区。」
- 句3：「最后问你：你的团队，AI 写了多少代码，能量出来吗？」
