# design.md — E01 段3（5 个可运行 demo 速览）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程类强制横屏（categories/tutorial.md orientation_hint=landscape）。B 站横屏播放，观众要读 demo 名 + 三层算法表 + 5 类模板卡 + 4 份手册 + skill 清单同屏，竖屏装不下。s6_assemble 横屏分支依赖此字段（§6.12 横屏视觉增强）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16 教程横屏范式：一屏多区域 + reveal（**不是竖屏 phase 切换**）。每场景单 phase div + 多 region（标题/demo 名/作用说明/架构要点/数据卡 grid 同屏）+ `data-reveal="N"` 按时间点依次淡入；区域 reveal 后保持同屏累积丰富。s6_assemble build_gsap 扫碎片 data-reveal 属性生成 reveal 动画。教程观众「读」画面消化 demo 清单 + 三层算法结构，不被「切」着走。

## style

清爽专业科技风。教程类要**干净、可读 + 高信息密度**（一屏多区域：demo 名 + 作用 + 怎么跑 + 亮点同屏），不要花哨动画抢注意力。每个 demo 一场景，每场景一屏展示「demo 名 + 定位 + 架构/清单 + 运行命令」。

## color_direction

深蓝底 + 主色蓝 + 强调色（按 demo 语义分配，ai-metrics 三层算法用金色高亮「反伪造」）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | `#0F172A` | 深蓝主底（沉稳专业） |
| 主色 | `#1E3A8A` / `#3B82F6` | 蓝色主调（demo 名/编号胶囊/卡片边框） |
| 蓝白 | `#E0E7FF` | 浅蓝白（正文/要点说明） |
| 数据强调 | `#FBBF24` | 金（ai-metrics「反伪造」标签 / 「开箱即跑」徽章 / 5 类/4 份/4 个数字高亮） |
| 三层算法层级 | `#3B82F6` → `#10B981` → `#FBBF24` | 蓝（① 初筛）→ 绿（② 复核）→ 金（③ 兜底）渐次高亮，第三层金色最重 |
| 「不是空谈」对比 | `#10B981` | 绿（「开箱即跑」「自包含」「可 clone」一栏）|
| 「空谈」对比 | `#EF4444` | 红（「概念」「PPT 噱头」「装不了」一栏，仅总览场景对比用） |
| 中性 | `#94A3B8` | 灰（次要文字 / 注释 / 「相关性非因果」/ 运行命令等宽字体色） |

> 强色控制：金色仅「反伪造」「开箱即跑」「数字高亮」；绿仅「开箱即跑」对比；红仅总览「不是空谈」对比。一屏多区域靠色块区分语义，不靠强切换。

## immersion_mode

教程横屏 reveal — 每场景单 phase div + 多 region grid 同屏，按 data-reveal 时间点淡入累积。三种区域范式按 demo 内容自然组合：

| 区域范式 | 用于 | 视觉手段 |
|---------|------|---------|
| 标题区（hero 大字）| 每场景顶部 | demo 名主色蓝大字（等宽 JetBrains Mono）+ 蓝白定位副文字 + 蓝色下划线 width 0→100%（600ms） |
| 5 demo 总览条（横向）| 总览场景 | 5 个 demo 卡横向排列（ai-test-frame → ai-metrics → report-templates → role-handbooks → claude-skills），stagger 200ms 依次亮起，每卡含 demo 名 + 一句话定位 |
| 三层算法层级卡 | ai-metrics 场景 | 三卡纵向（① Co-authored-by 初筛 / ② 风格计量学复核 / ③ 注册表兜底），蓝→绿→金渐次高亮，第二层标「反伪造关键」金色胶囊 |
| 5 类/4 份/4 个清单卡 | report-templates / role-handbooks / claude-skills 场景 | 横向卡阵列（5 类模板 / 4 份手册 / 4 个 skill），每卡图标 + 名称 + 一句话用途，stagger 150ms |
| 运行命令区 | 每个 demo 场景底部 | 等宽字体命令（如 `python main.py`）+ 蓝色终端窗口框 + 「开箱即跑」金色徽章 |
| 「不是空谈」对比区 | 总览场景 | 双栏对比：左红「概念/PPT 噱头/装不了」vs 右绿「开箱即跑/自包含/可 clone」 |

## scene_plan

6 个场景，每场景单 phase div + 多 region + data-reveal（§6.16 教程横屏 reveal）：

| 场景 | 内容 | 区域结构 | reveal 步骤 |
|------|------|---------|------------|
| s1 总览 | 5 demo 一句话钩子 + 「不是空谈，每个开箱即跑」 | 标题（hero）+ 5 demo 横向总览条 + 「不是空谈」双栏对比 | 标题 r0 → 总览条 stagger r3 → 对比双栏 r9 |
| s2 ai-test-frame | 最小可运行 AI 自动化测试框架 | demo 名 + 定位 + 5 模块架构列表 + 运行命令 | 标题 r0 → 定位 r3 → 5 模块 stagger r6 → 命令 r12 |
| s3 ai-metrics（重头戏）| 三层识别算法 + 反伪造 | demo 名 + 定位 + 三层算法层级卡（蓝→绿→金）+ Excel 同比 | 标题 r0 → 定位 r3 → 三层卡 stagger r6（第二层「反伪造」金色高亮）→ Excel 同比 r15 |
| s4 report-templates | 5 类汇报 Prompt 包 | demo 名 + 定位 + 5 类模板横向卡 + ppt-master 渲染说明 | 标题 r0 → 定位 r3 → 5 类卡 stagger r6 → ppt-master 说明 r12 |
| s5 role-handbooks | 4 份角色手册 | demo 名 + 定位 + 4 份手册横向卡 + 「6 部分」结构说明 | 标题 r0 → 定位 r3 → 4 份卡 stagger r6 → 6 部分说明 r12 |
| s6 claude-skills + 承接 | 4 skill + 12 规范 + 承接下段 | demo 名 + 4 skill 卡 + 12 规范分层列表 + 「clone 即跑」金色徽章 + 承接语 | 标题 r0 → 4 skill 卡 stagger r3 → 12 规范 r9 → clone 徽章 r15 → 承接 r18 |

## tutorial_reveal_paradigm_note

- **每场景单 phase div**（不是竖屏多 phase 切换），内含多 region（grid/flex 同屏布局）
- **data-reveal="N"**：N = 相对场景开始的秒数，narration 讲到该区域时同步 reveal
- **区域 reveal 后保持**（不隐藏），同屏累积丰富（区别竖屏 phase 切换「换屏」）
- **动画克制**：reveal 淡入 0.5s > 粒子光晕过载，教程重内容轻视觉
- s6_assemble build_gsap 扫碎片 data-reveal 属性自动生成 reveal GSAP timeline

## compliance_notes

- demo 名（ai-test-frame 等）是教程自带 demo，非竞品，可点名（教程内容）
- 工具名（Claude Code / OpenSpec / Superpowers / Playwright / PowerPoint / Redisson）是教程技术工具，非品牌攻击
- ai-metrics 风格学「反伪造」是机制描述（降低误标置信度），不写「100% 准确」「彻底防伪造」
- 提效同比标「相关性非因果」（教程规范）
- 禁绝对化用语（最强/必装/神器/第一/必备）
- 无 URL/搜索引导（教程仓库 owner/repo 文本路径放评论区）
