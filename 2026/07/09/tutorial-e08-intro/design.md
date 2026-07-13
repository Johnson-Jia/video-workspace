# design.md — E08 intro（方法论：推广度量 + 多 Agent 并行 + 三层识别 AI 代码占比）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。方法论预告：两件事横排（多 Agent 放大 + 度量证伪）+ 三层识别预告（初筛/复核/组合）+ 学习目标三栏。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。标题（左对齐）+ 两件事横排（02 度量证伪金边强调）+ 三层识别横排（03 注册表组合金边强调）+ 学习目标三栏。region 按 data-reveal 时间点淡入 + 方向。

## style

方法论预告风。标题左对齐 + 两件事横排卡（02 度量证伪金边强调）+ 三层识别横排卡（03 注册表组合金边强调）+ 学习目标三栏（绿色 ✓）。

## color_direction

深底 + 三色（蓝=多 Agent 放大 / 金=度量证伪关键 / 绿=三层识别）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（dark_cipher 网格叠层） |
| 多 Agent 放大 | `#3B82F6` | 蓝色（01 规模化） |
| 度量证伪 | `#FBBF24` | 金色（02 关键 数据证明真提效） |
| 三层识别 | `#10B981` | 绿色（核心反伪造） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（标题+两件事+三层识别+学习目标）。region 按 data-reveal 时间点淡入 + 方向。

## bg_component

`dark_cipher`（深蓝密码网格，与 E08 hook/intro 系列统一）

## visual_type

`tutorial_intro`（方法论预告：两件事横排 + 三层识别 + 学习目标布局）

## 字数核算

旁白约 100 字（中文 +0% 实际约 5.3 字/秒）。目标时长 ~35s。100 字 ÷ 5.3 ≈ 19s，偏短——补数据卡 + 标语补足到 ~35s 视觉时长（旁白停顿 + reveal 等待）。实际按 narration 时长定 phase 时长。

## visual_phasing（data-reveal stagger）

1. 标题「推广度量 · 两件事 + 三层识别」fade-in
2. 两件事横排（多 Agent 放大 / 度量证伪）reveal 左滑入
3. 三层识别横排（初筛 / 复核 / 组合）reveal 底部上滑
4. 学习目标三栏 reveal

## 旁白句拆（narration_anchor）

- 句0：「这集讲推广度量。」
- 句1：「两件事：多 Agent 并行把单点提效放大成规模，加 AI 代码占比度量用数据证明真提效。」
- 句2：「核心是三层识别：Co-authored-by 初筛，风格学复核，注册表组合。」
- 句3：「你能学到：多 Agent 怎么并行不炸，AI 代码占比怎么算才不被骗，事前估算和事后统计怎么配合。」
