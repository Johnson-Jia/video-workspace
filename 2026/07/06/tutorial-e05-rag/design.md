# design.md — E05 段2（业务知识 RAG：开卷考试 + 两阶段检索）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。业务知识 RAG：左侧原理流程卡（知识库→向量化→检索→模型回答），右侧代码块（两阶段检索伪代码 + 多租户隔离 expr）。E04 claudemd 段的代码窗口范式延续。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。**1 场景 6 region**（scenes=1，避开 R-R-010 相邻同质误报）。标题 + RAG 原理卡 + 代码窗口（注释→流程→expr 逐段 reveal）+ 金句，按 narration 锚点 reveal 同屏累积。

## style

企业级 RAG 讲解风。左侧原理卡（蓝色主调，流程图逐步点亮：知识库→向量→检索→模型），右侧代码窗口（深底 #0a0a0a + 等宽字 JetBrains Mono + 语法高亮：注释灰/关键字蓝/字符串绿，伪代码逐行 reveal）。底部金句收束。

## color_direction

深蓝 hex_grid 底 + 蓝（RAG原理）+ 金（金句/警示）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格（基础设施结构感） |
| 代码窗 | `#0a0a0a` | 终端深底 |
| RAG 主色 | `#3B82F6` | 蓝（向量化/检索） |
| 召回绿 | `#34D399` | 第一阶段召回 |
| 重排金 | `#FBBF24` | 第二阶段 CrossEncoder |
| 多租户紫 | `#A78BFA` | 租户隔离 |
| 金句 | `#FBBF24` | 金（业务记忆） |
| 蓝白 | `#E0E7FF` | 标题/次要 |

## immersion_mode

教程横屏 reveal — 1 场景 + 多 region（标题+RAG原理卡+代码窗+金句）。region 按 data-reveal 时间点淡入 + 方向（标题 fade / 原理卡 left / 代码窗 top / 代码行 fade / 金句 top）。

## 视觉区域范式（1 场景，~80s TTS）

### 单场景：业务 RAG 讲解（6 region 同屏累积）

- **region1 标题**（data-reveal=0，dir=fade）：标题「业务知识 RAG」+ 副「让 AI 开卷考试 · 给它装上业务记忆」
- **region2 RAG 原理卡**（data-reveal=9，dir=left）：左侧原理流程卡——知识库 → 向量化 → 检索 → 模型回答（4 步竖排，逐步点亮）
- **region3 代码窗头部**（data-reveal=22，dir=top）：代码窗口 reveal + 注释行 `# 两阶段检索：召回优先 → 重排提精度` 打字
- **region4 代码流程行**（data-reveal=30，dir=fade）：代码块流程行 reveal「三路并发召回 → 按原文去重 → CrossEncoder 重排 → 过滤低分」分四段点亮
- **region5 代码 expr 行**（data-reveal=46，dir=fade）：代码注释「# 多租户隔离」+ expr 行 `expr = 'corp_code in ["租户A", "default"]'` 打字（字符串绿色高亮）
- **region6 金句**（data-reveal=62，dir=top）：金句「幻觉大幅下降 · 给 AI 装上业务记忆」

## 动画策略

- 代码注释行逐字打字（GSAP timeline + textContent snap，每字 50ms）
- 代码流程行分段 fade-in（data-reveal 触发，500ms，4 段 stagger 200ms）
- expr 行字符串部分绿色高亮闪烁
- region fade-in + 方向偏移（left 从 x:-40 / top 从 y:-40 / fade 纯 opacity），500ms
- fx-pulse + fx-blink 静态点缀（禁划过类）

## bg_component

`hex_grid`（六边网格，基础设施结构感；E05 全集统一 bg）

## visual_type

`tutorial_rag_code`（原理流程卡 + 代码窗口 + 两阶段检索伪代码布局）
