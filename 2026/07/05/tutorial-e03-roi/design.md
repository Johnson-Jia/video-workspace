# design.md — E03 段3（ROI 公式 + 老板三问 + 别承诺 +104%）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。ROI 公式 + 老板三问（要多少钱/多久回本/失败怎么办）+ 金色警告「别承诺 +104%」。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 6 region**（scenes=1，避开 R-R-010 相邻同质误报）。标题 + ROI 公式 + 三问卡 3 + 警告，按 narration 锚点 reveal 同屏累积。

## style

ROI 决策仪表盘风。顶部公式横幅醒目，中部三问卡 3 列横排（编号 ①②③ + 问句 + 答案），底部金色警告框收束。对称、信息密度高。

## color_direction

深蓝底 + 三问三色（蓝=问①钱 / 紫=问②回本 / 绿=问③失败兜底）+ 金色警告：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底 |
| 问① 要多少钱 | `#3B82F6` | 蓝色（钱/工具） |
| 问② 多久回本 | `#A78BFA` | 紫色（时间/公式） |
| 问③ 失败怎么办 | `#10B981` | 绿色（兜底/止损） |
| ROI 公式 | `#FBBF24` | 金色（核心公式醒目） |
| 警告（别承诺） | `#FBBF24` | 金色边框（警示） |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+公式+三问卡 3+警告）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 公式 top / 三问卡 left 交替 / 警告 top）。同屏累积，最后警告收束。

## 视觉区域范式（1 场景，~45s TTS）

### 单场景：ROI + 老板三问（6 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「ROI · 老板三问」+ 引子「算清成本，还要回答老板三问」
- **region2 ROI 公式**（data-reveal=4，dir=top）：ROI 公式大字横幅「回本月数 ≈ 总投入 ÷（人均月薪 × 提效等效人力）」
- **region3 三问卡①**（data-reveal=13，dir=left）：① 要多少钱？（蓝，四块成本表 · 一次性/持续标清）
- **region4 三问卡②**（data-reveal=22，dir=left）：② 多久回本？（紫，3-6 个月 · 先试点 3 月验证再全量）
- **region5 三问卡③**（data-reveal=32，dir=left）：③ 失败怎么办？（绿，试点可控/可止损/沉没成本低）
- **region6 警告**（data-reveal=42，dir=top）：金色警告框「别在立项承诺 +104% · 那是跑出来的结果 · 承诺目标值+试点路径更诚实」

## 动画策略

- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- 公式横幅顶部醒目（金底）
- 三问卡 3 列横排（编号 + 问句 + 答案，对称布局）
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`clean_slate`（单场景简洁底）

## visual_type

`tutorial_roi`（ROI 公式 + 三问卡 + 警告布局）
