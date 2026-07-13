orientation: landscape
resolution: 1920x1080
emotion_curve: [理性, 提醒, 递进, 警示, 收束, 落地]

# E08 段8 度量逐步建 — 视觉设计

style: 阶梯递进风标题居左 + 度量三阶段阶梯卡（业务模块覆盖 → bug 排查覆盖 → AI 代码占比，等宽 + 箭头连接 + 第三卡紫罗兰高亮）+ 琥珀警示条「别指望一上来 76.6%」+ 翠绿收尾金句。强调"逐级建立"的递进感。

## mood

mood: 沉稳、克制、提醒式。本段是"避坑提醒 + 阶梯方法"，节奏比 results 数据卡稍缓，避免兴奋调，保持理性引导。

## color_direction

color_direction: 深底 + 青（阶段卡 1/2）+ 紫（阶段卡 3 高亮，占比是最终目标）+ 琥珀（警示条）+ 翠绿（收尾金句 ✓）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（light_field 光场叠层） |
| 阶梯主色 | `#38BDF8` | 青蓝（阶段 1/2 卡边框 + 序号 + 箭头） |
| 阶段 3 强调 | `#A78BFA` | 紫罗兰（AI 占比卡高亮，最终目标） |
| 警示条 | `#F59E0B` | 琥珀（"别指望一上来 76.6%" ⚠） |
| 收尾金句 | `#34D399` | 翠绿（分阶段落地 ✓） |
| 正文白 | `#E2E8F0` | 主文字 |
| 副文灰 | `#94A3B8` | 副标题/说明 |

## storyboard

storyboard: 教程横屏 reveal — 1 场景 + 4 phase（标题 / 阶梯三卡 / 警示条 + 基础注脚 / 收尾金句）。phase 按 data-reveal 时间点淡入 + 方向。

## bg_component

`light_field`（冷蓝光场，2-3 个高斯模糊光球从中心缓慢漂移 + 星尘 + 棱镜色散呼吸；象征"度量体系从核心业务指标逐步铺开辐射"；与 E08 已用 bg 异质：hook dark_cipher / intro dark_cipher / why hex_grid / multiagent diamond_lattice / coauthored contour_lines / stylometry diamond_lattice / registry hex_grid / estimate wave_ripple / results scan_grid；visual_types 含 beams/glow/gradient/particles，符合 R-R-009 要求非 {gradient,glow,grid} 单一组件）

## 容器文字处理（container_text 规则）

阶梯卡内：序号（72px 大字）+ 阶段名（36px，短词如「业务模块覆盖」「bug 排查覆盖」「AI 代码占比」）+ 时序标签（先/中/后，胶囊）；长描述「能从告警追溯到代码行」移卡外注脚。警示条内仅短句「别指望一上来就跑出 76.6%」，不堆砌。

## 容器结构（横屏 1920×1080）

1. **phase-1（0~7s）标题**：左对齐 eyebrow「E08 · 推广度量 · 段8 度量逐步建」+ 标题「度量是逐步建的」（grad-text 青→紫渐变，text-shadow 深蓝 rgba(30,41,59,0.6)）+ 副标题「不是部署工具就出数据」
2. **phase-2（7~20s）阶梯三卡 reveal**：三卡等宽 flex:1 + 箭头连接 → 依次点亮。卡 1「业务模块覆盖率 · 先」（青蓝边）→ 卡 2「bug 排查覆盖率 · 中」（青蓝边）→ 卡 3「AI 代码占比 · 后」（紫罗兰高亮边 + 三层识别徽章）。卡下注脚「先盘点哪些模块接入 → 再追线上问题 → 最后算占比」
3. **phase-3（20~30s）警示 + 基础说明**：琥珀警示条 reveal「⚠ 别指望一上来就跑出 76.6%」+ 下方灰色注脚「前两层是基础 · 业务没铺开占比没分母 · 问题追不到占比是空中楼阁」
4. **phase-4（30~39s）收尾金句**：翠绿 ✓ + grad-text 渐变金句「先建可量化的业务指标，度量体系随转型成熟分阶段落地」

## fx 层（冷色 alpha≤0.22，≥3 元素，禁划过类）

1. fx-aura 静态光晕（青蓝 hsla(210,80%,55%,0.18)）置于阶梯卡组后方
2. fx-pulse-ring 脉冲环（紫 hsla(260,70%,65%,0.15)）围绕第三阶段卡（占比是目标，calc(50%-100px) 居中避 safe_area 误报）
3. fx-glow-dot 光点（翠绿 hsla(160,70%,55%,0.20)）散布于收尾金句区
4. 阶梯箭头粒子流（青蓝 alpha 0.18）随 phase-2 reveal 流动

## 文字特效

- 标题 + 收尾金句用 grad-text（background-image:linear-gradient，禁 background 简写；text-shadow 深蓝 rgba(30,41,59,0.6) 禁发光）
- 阶段序号大字 Ma Shan Zheng 毛笔体（72px，已注入 @font-face）
- 警示条文字纯琥珀色（非渐变，避免 clip:text 与背景冲突）

## 多音字

转→转型（zhuǎn）；行→代码行（háng）；铺→铺开（pū）。
