# design.md — FDE 番外篇 · cta 段（考核差异对照 + 收尾）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程类强制横屏（categories/tutorial.md orientation_hint=landscape）。4×3 考核对照表 + CTA 收尾区，横屏同屏 reveal 信息密度足，竖屏装不下。s6_assemble 横屏分支依赖此字段。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16 教程横屏范式：单 phase + 多 region + data-reveal（不是竖屏 phase 切换）。对照表逐行 reveal 同屏累积，CTA 收尾区随后 reveal。

## fields（gate 解析速览）

style: 清爽专业科技风·考核对照收尾（克制稳重，对照表信息密度为主，CTA 收束温暖）
mood: 稳重·收束（对照表理性铺陈 + 一句话点透 + 温暖 CTA 收尾，不煽动）
color_direction: 深蓝底 #0F172A + 金 #FBBF24（FDE 现场列金边强调 + CTA 暖收）+ 蓝 #3B82F6（甲方内部列）+ 蓝白 #E0E7FF + 中性 #94A3B8
storyboard: 收尾 4 场景（对照表引入+表头 / 逐行 reveal / 一句话收束+CTA / 互动提问卡），narrative_template+emotion_curve+immersion_mode 见下
emotion_curve: [0.55, 0.62, 0.70, 0.75, 0.62, 0.50]

## style

清爽专业科技风·考核对照收尾。稳重、克制——对照表逐行展开靠信息密度，一句话收束点透差异，CTA 温暖收尾。深蓝底 + fx-aura 静态光晕（CTA 区 fx-particle 漂浮粒子，禁划过类 fx）。教程重内容轻视觉。

## mood

稳重·收束——用考核对照表铺陈（同一角色两种考核），一句话点透（对系统负责 vs 对客户业务结果负责），结尾温暖 CTA + 中性互动提问。不煽动、不夸张。

## color_direction

深蓝底 + 双色分工（金=FDE 现场考核列 / 蓝=甲方内部考核列）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（沉稳，让对照表清晰） |
| FDE 现场列 | `#FBBF24` | FDE 现场考核列金边强调 + 箭头指向 + CTA 暖收 |
| 甲方内部列 | `#3B82F6` | 甲方内部考核列（对照基准） |
| 蓝白 | `#E0E7FF` | 表头 / 角色列 / 次要文字 |
| 中性 | `#94A3B8` | 注释 / 分隔 / 互动提问副文 |

> 强色控制：金/蓝严格分工——蓝=甲方内部（主教程基准），金=FDE 现场（乙方转变，金边强调）。箭头从甲方列指向 FDE 列表达「考核变了」。渐变文字禁白色端点，同色系高饱和（金 #FBBF24→#F59E0B→#FCD34D / 蓝 #60A5FA→#3B82F6→#93C5FD）。

## storyboard

### narrative_template

收尾段（考核对照 + 转岗决策 + CTA）：
1. hook：同一个角色，甲方乙方，考核竟然不一样（蓝金对照大字，冲突钩子）
2. 对照框架：最后用一张表收尾，讲入行后最不适应的事——考核标准从甲方内部到 FDE 现场变了（箭头条 + 框架）
3. 表格逐行 reveal：开发 / 测试 → 组长 / 产品，四行对照表收齐
4. 一句话点透：主教程对系统负责 vs FDE 对客户业务结果负责
5. 规律条：代码质量/覆盖率从考核项变成手段——客户签字和业务收益才是标尺（金边结论条）
6. 转岗决策二分卡：慎重（纯技术深度/稳定作息/自主权）↔ 适合（跟人打交道/真实业务/适应出差），稀缺性对适合的人实打实
7. CTA：合集标识 + 仓库指引（评论区，无 URL）
8. 互动提问卡 + 关注：技术执行那块 / 客户现场那块（两选项并列中性）+ 关注引导 + fx-particle 漂浮收束

### emotion_curve

[0.70, 0.60, 0.70, 0.78, 0.72, 0.68, 0.58, 0.48]

> 节奏：hook 冲突开场（0.70，竟然钩子）→ 框架建立回落（0.60）→ 表格逐行信息密度累积（0.70）→ 一句话点透高点（0.78）→ 规律条理性延伸（0.72）→ 转岗决策贴近个人（0.68）→ CTA 温暖回落（0.58）→ 互动提问中性收束（0.48，留思考给观众）。

### immersion_mode

教程横屏 reveal — 每场景单 phase + 多 region data-reveal 同屏累积。对照表逐行 reveal 后保持在场（不消失），规律条/二分卡依次推进，CTA 收尾区随后 reveal，最后互动提问卡定格收束。

## 视觉区域范式

### 场景 1：hook（~4s，冲突钩子）

- **对照大字区**（data-reveal=0）：「甲方（蓝）↔ 乙方（金）」对照 + 主句「考核竟然不一样」金色渐变大字 + eyebrow「同一个角色」
- **fx-aura**：蓝金双静态光晕（alpha ≤ 0.22）

### 场景 2：对照框架（~10s，箭头条）

- **箭头条**（data-reveal=0）：「甲方内部 · 主教程 → FDE 现场 · 乙方」+ 金 tag「考核变了」
- **副题**：「同一个角色 · 两套考核标准」+「入行后最容易不适应的事」

### 场景 3：表格 开发+测试行（~15s，信息累积 1）

- **表头**（data-reveal=0）：三列「角色 / 甲方内部考核 / FDE 现场考核」+ 开发行 reveal
- **测试行**（data-reveal≈8）：蓝 覆盖率·缺陷率 → 金 验收口径达成·责任边界书面划清
- **fx-blink**：行首锚点

### 场景 4：表格 四行收齐（~15s，信息累积 2）

- **四行全表**：开发/测试保持在场 + 组长行（data-reveal=0）+ 产品行（data-reveal≈5）reveal
- **fx-blink**：锚点平衡

### 场景 5：一句话点透（~7s）

- **一句话大字区**（data-reveal=0）：蓝「对自己的系统负责」｜ 金「对客户的业务结果负责」左右对照
- **fx-aura**：左蓝右金双光晕

### 场景 6：规律条 + 转岗决策二分卡（~26s，>15s 拆 2 phase）

- **规律条**（phase1，data-reveal=0）：对照表下方金边结论条「代码质量 · 覆盖率 → 从考核项变成手段」+ 标尺句「客户签字 · 业务收益才是标尺」
- **转岗决策二分卡**（phase2，data-reveal≈14）：左卡「要慎重（蓝）：纯技术深度 · 稳定作息 · 自主权」↔ 右卡「适合（金）：跟人打交道 · 真实业务 · 适应出差」+ 收束句「稀缺性对适合的人是实打实的」
- **fx-blink**：锚点

### 场景 7：CTA 收尾带（~10s）

- **合集标识 badge**（data-reveal=0）：「AI 转型实战 · 13 集 + 番外」
- **双卡**（data-reveal=3）：教程仓库（所有 demo 可下载即跑 · 地址在评论区）+ 合集（十三集 + 番外 · 点关注不走丢）
- **fx-particle**：金色漂浮粒子（alpha ≤ 0.22）

### 场景 8：互动提问卡（~9s，中性收束）

- **提问**（data-reveal=0）：「你缺哪块？」
- **两并列选项卡**（data-reveal=2.5）：「技术执行那块（蓝）｜客户现场那块（金）」中性并列
- **关注引导**（data-reveal=5.5）：「点关注不走丢」
- **fx-particle**：漂浮粒子收束氛围

## 动画策略

- **对照表行 reveal**：opacity 0→1 + translateY 12px→0，600ms ease-out，data-reveal 错时同屏累积
- **箭头条 reveal**：opacity 0→1，500ms，甲方列→FDE 列方向
- **一句话大字 fade-in**：opacity 0→1 + scale 1.04→1，600ms
- **CTA 带 / 提问卡 reveal**：opacity 0→1，500ms
- **fx-particle 静态漂浮**：粒子缓慢上浮呼吸（不划过不追线）
- **禁**：fx-scan/fx-stream/fx-beam 划过类、粒子过载、3D 翻转、强切换

## bg_component

按 R-R-010 相邻 bg 多样性轮换（全蓝/青冷静系，≥3 种、相邻互异）：
- s01 hook `clean_slate`｜ s02 框架 `contour_lines`｜ s03 表 `aurora_night`｜ s04 表 `clean_slate`｜ s05 一句话 `aurora_night`｜ s06 规律+二分 `contour_lines`｜ s07 CTA `clean_slate`｜ s08 提问 `aurora_night`

## visual_type 映射

- 场景 1：`contrast_hook`（甲方↔乙方 考核竟然不一样）
- 场景 2：`arrow_framework`（甲方内部→FDE 现场 框架）
- 场景 3：`table_rows_dev_qa`（开发+测试行）
- 场景 4：`table_rows_lead_pm`（组长+产品行，四行收齐）
- 场景 5：`one_liner_contrast`（一句话对照）
- 场景 6：`rule_then_decision`（规律条 + 转岗决策二分卡）
- 场景 7：`cta_band`（合集标识 + 仓库指引）
- 场景 8：`interaction_card`（中性互动提问卡 + 关注引导）
