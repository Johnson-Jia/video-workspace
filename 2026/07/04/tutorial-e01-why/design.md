# design.md — E01 段1（为什么必须转型）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程类强制横屏（categories/tutorial.md orientation_hint=landscape）。B 站横屏播放，观众要读对比双栏/数据卡/金句同屏，竖屏装不下。s6_assemble 横屏分支依赖此字段。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16 教程横屏范式：一屏多区域 + reveal（**不是竖屏 phase 切换**）。每场景单 phase div + 多 region（标题/对比/数据/金句 grid 同屏）+ `data-reveal="N"` 按时间点依次淡入；区域 reveal 后保持同屏累积丰富。s6_assemble build_gsap 扫碎片 data-reveal 属性生成 reveal 动画。教程观众「读」画面消化，不被「切」着走。

## style

清爽专业科技风。教程类要**干净、可读 + 高信息密度**（一屏多区域，观众同时读标题+对比+数据+金句），不要花哨动画抢注意力。

## color_direction

深蓝底 + 主色蓝 + 强调色（按内容语义分配）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（沉稳专业） |
| 主色 | `#1E3A8A` / `#3B82F6` | 蓝色主调（标题/阶段条/数据卡边框） |
| 蓝白 | `#E0E7FF` | 浅蓝白（正文文字/次要说明） |
| 数据强调 | `#FBBF24` | 金（2 倍代码等数字高亮） |
| 对比强调 | `#10B981` | 绿（「正确姿态 / 拥抱验证」一栏） |
| 对比警示 | `#EF4444` | 红（「两个极端 / 抗拒 / 盲目」一栏） |
| 中性 | `#94A3B8` | 灰（次要文字 / 注释 / 相关性非因果） |

> 强色控制：金色仅数据高亮 / 绿仅「正确」栏 / 红仅「极端」栏。一屏多区域靠色块区分语义，不靠强切换。

## immersion_mode

教程横屏 reveal — 每场景单 phase div + 多 region grid 同屏，按 data-reveal 时间点淡入累积。三种区域范式按内容自然组合：

| 区域范式 | 用于 | 视觉手段 |
|---------|------|---------|
| 标题区（hero 大字）| 每场景顶部 | 主色蓝大字 + 蓝白副文字 + 蓝色下划线 width 0→100% |
| 对比双栏（极端/姿态）| 「两个极端」「正确姿态」场景 | 左红「抗拒」+ 中红「盲目」+ 右绿「拥抱+验证」对称卡片，图标+标题+说明三行 |
| 数据卡区 | 2 倍代码 / 估值承压 | 金色大字 + 「相关性非因果」灰色小字注释 |
| 金句区 | 人+AI 人是根本 | 金句条（金/蓝边框 + 白字）fade-in，长停留 |
| 承接条 | 段尾接思想转变 | 蓝白承接文字 + 向右箭头 |

## bg 组件池（≥3 种相邻不同）

- **clean_slate** — 干净深蓝底（用于标题区 hero 呼吸，让多区域不互相干扰）
- **scan_grid** — 细网格扫描线（用于对比双栏/数据卡，科技感衬底不抢文字）
- **gradient_mesh** — 蓝色径向渐变（用于金句区/收尾承接，柔和过渡）

> 教程类 bg 定位：**低调衬底，不抢多区域文字**。不用粒子/光晕过载（§6.16 教程横屏禁忌）。

## typography

- 中文标题（hero）：思源黑 / Inter 粗体，96-120px（横屏多区域，比竖屏 hero 小一档）
- 区域标题：思源黑 Bold，48-56px
- 中文正文/要点：思源黑 Medium，32-40px（横屏可读底线，多区域密度需控字号）
- 数字：等宽数字 / JetBrains Mono Bold，金色高亮 140-180px
- 注释/相关性说明：思源黑 Regular，22-26px，灰色
- 字间距：标题 0.02em，正文 0.01em

## motion

教程横屏 reveal 动画（§6.16 — data-reveal 时间点淡入，克制）：

- 标题区：场景开始即 fade-in（data-reveal="0"）+ 下划线 width 0→100%（600ms）
- 对比双栏：左右对称 fade-in + 微 translateY（300ms，错峰 150ms）
- 数据卡：金色数字从 0 滚动到目标值（500ms，ease-out）+ 「相关性非因果」注释同步淡入
- 金句区：金句条 fade-in + width 0→100%（800ms），长停留
- **区域 reveal 后保持**（不隐藏），同屏累积丰富（区别竖屏 phase 切换换屏）
- **禁**：粒子、过强光晕、闪烁、3D 翻转、3 秒强切换（§6.16 教程横屏最大误区）

## layout_principles

- 横屏 1920×1080 安全区：padding 80px（左右）/ 60px（上下）
- 一屏多区域 grid：标题区顶部（横跨）+ 中部主内容区（grid 2-3 列）+ 底部金句/承接条
- 对比双栏/三栏：左红 + 中红 + 右绿对称，中间 60px gap
- 数据卡：宽 600-800px 居中或右栏，数字 140px+ 配注释小字
- 文字层级：标题 > 数字 > 区域标题 > 正文 > 注释（5 级清晰，多区域不打架）
- reveal 节奏：每场景 4-5 个区域 reveal，间隔 3-4s（与 narration 句子锚点对齐）

## storyboard

narrative_template: "contrast-arc"
emotion_curve: [0.4, 0.6, 0.8, 0.7, 0.9, 0.5]
immersion_mode: "tutorial_reveal"
humor_style: "narration-only"
character_presence: false
beat_mapping:
  grab: "hook（不转型=相对落后的认知冲击）"
  build: "why1（生产关系重写 + 2 倍代码）"
  reveal: "why2（传统软件巨头承压 + 不转=落后）"
  climax: "extremes（两个极端三栏对比）"
  settle: "posture（拥抱+验证金句）"
  summon: "handoff（人是根本 + 承接思想转变）"

## music_mood

clean-corporate / warm-editorial 低调衬底（教程类 BGM 不抢旁白，观众要听清讲解）
