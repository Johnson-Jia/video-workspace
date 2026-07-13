# design.md — E08 段6 事前估算 vs 事后统计（estimate，表格核心段）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。表格核心段——估算公式 + 场景表 4 行（CRUD/复杂/Bug/平均，AI 占比列柱状条）+ 实测 76.6% 落区间 + 金句收尾。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 phase（标题/公式/场景表/实测落点+金句）。phase 按 data-reveal 时间点淡入 + 方向。

## style

表格核心风。标题左对齐 + 估算公式卡（分子分母清晰，金边强调）+ 场景表四行（AI 占比列柱状条可视化，90% / 70% / 70% / 75%）+ 实测 76.6% 金边徽章落在估算区间内 + 金句收尾。

## color_direction

深底 + 蓝（场景行）+ 金（公式 + 实测落点 + 平均行强调）+ 绿（实测落在区间内 ✓）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（wave_ripple 同心波纹叠层） |
| 公式强调 | `#FBBF24` | 金色（估算公式金边 + 实测 76.6% 徽章） |
| 场景行/占比柱 | `#3B82F6` | 蓝色（CRUD / 复杂 / Bug 行，AI 占比柱状条） |
| 平均行强调 | `#60A5FA` | 浅蓝（平均 ~75% 行柱状条） |
| 实测落区间 | `#34D399` | 绿色（76.6% 落区间内 ✓ 标识） |
| 金句 | `#C4B5FD` | 紫色（估算给方向，统计给真相） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 phase（标题/公式/场景表/实测落点+金句）。phase 按 data-reveal 时间点淡入 + 方向。

## bg_component

`wave_ripple`（同心波纹扩散 + 玻璃折射，度量数据"扩散辐射"感 + 与 E08 已用 5 个 bg 异质：hook dark_cipher / intro dark_cipher / why hex_grid / multiagent diamond_lattice / coauthored contour_lines / stylometry diamond_lattice / registry hex_grid，避免视觉重复；visual_types 含 contour/glow/gradient/wave，符合 R-R-009 要求非 {gradient,glow,grid} 单一组件）

## 容器文字处理（container_text 规则）

公式分子/分母胶囊内仅短词或数字百分比（如 `AI 生成核心 + AI 辅助优化`、`总代码量`、`90%`），长描述移容器外。场景表单元格内文字字号≥28px，柱状条宽度按百分比可视化（90% → 90% 宽，70% → 70% 宽）。

## 容器结构（横屏 1920×1080）

1. **phase-1（0~8s）标题**：左对齐 eyebrow「E08 · 推广度量 · 段6 估算 vs 统计」+ 标题「事前估算 vs 事后统计」+ 副标题「占比有两种算法，要配合用」
2. **phase-2（8~20s）估算公式**：公式卡——分子「AI 生成核心 + AI 辅助优化」÷ 分母「总代码量」= 「AI 占比」（金边强调），旁注「事前估算 · 推广前按场景估目标占比 · 设预期定考核」
3. **phase-3（20~32s）场景表 4 行**：表头「开发场景 | AI 生成核心 | AI 辅助优化 | AI 占比目标」+ 四行（CRUD 80%+10%=90% / 复杂 50%+20%=70% / Bug 30%+40%=70% / 平均 53.3%+23.3%=~75%），AI 占比列柱状条可视化
4. **phase-4（32~40s）实测落点 + 金句**：实测 76.6% 金边徽章落在估算区间（70%~90%）内 + 绿色 ✓ 标识「落在区间内」+ 金句「估算给方向，统计给真相，两者独立」
