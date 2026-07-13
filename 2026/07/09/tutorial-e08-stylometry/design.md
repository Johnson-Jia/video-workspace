# design.md — E08 段4 第二层 风格学（stylometry，算法流程核心段）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。算法四步流程横向铺满（n-gram → TF → 余弦 → 置信度）+ 两分支（相似度高/低）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。标题（左对齐）+ 算法四步横向流程卡（每步金边胶囊短词 + 外部描述）+ 两分支判定（高→误标降 / 低→确认 AI）+ 防误标场景（VS Code Copilot trailer）。region 按 data-reveal 时间点淡入 + 方向。

## style

算法流程图风。标题左对齐 + 四步横向流程（每步圆/胶囊内短词 + 外部长描述，container_text 规则）+ 两分支横排（高/低相似度 → 误标降/确认 AI）+ 防误标场景卡（VS Code Copilot trailer 命中率）。

## color_direction

深底 + 四色（按算法步骤渐变蓝→金，分支用绿/红）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（diamond_lattice 菱形网格叠层） |
| 算法步骤 | `#3B82F6` | 蓝色（n-gram / TF / 余弦 / 置信度 流程节点） |
| 关键步骤强调 | `#FBBF24` | 金色（置信度 = 1 − sim 公式金边） |
| 相似度高分支 | `#10B981` | 绿色（误标→降置信度，安全） |
| 相似度低分支 | `#EF4444` | 红色（确认 AI，标记） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（标题+算法四步+两分支+防误标场景）。region 按 data-reveal 时间点淡入 + 方向。

## bg_component

`diamond_lattice`（深蓝菱形网格，算法几何感 + 与 E08 hook/intro/why 的 dark_cipher/hex_grid/contour_lines 异质，避免视觉重复）

## 容器文字处理（container_text 规则）

四步流程节点圆/胶囊内**仅短词**：
- 步骤1 圆内：`n-gram`（外标"字符级切分"）
- 步骤2 圆内：`TF`（外标"词频归一化"）
- 步骤3 圆内：`余弦`（外标"相似度计算"）
- 步骤4 胶囊内：`置信度`（外标"= 1 − 相似度"）

两分支胶囊内短词：`高 → 降`（外"像本人 / 误标"）、`低 → AI`（外"不像本人 / 确认"）。长描述移容器外（圆下方/胶囊下方文字），确保字符×字号 < 容器内径×0.7。
