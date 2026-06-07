# ClipForge 深度剖析 — 用 AI 管线锻造短视频

> 本报告由 ClipForge 自身使用，作为 VibeCoding 大赏参赛视频的内容源。视频将全面剖析 ClipForge 的设计哲学、技术架构、代码实现和演进历程。

---

## 一、起点：为什么需要 ClipForge

### 1.1 问题背景

短视频已成为信息传播的主流载体。2026 年，抖音日活用户超过 8 亿，其中知识类、科技类内容的需求量以每年 40% 的速度增长。但制作一条 45 秒的竖屏短视频，传统流程需要：写脚本、录制旁白、剪辑画面、配乐、做封面——平均耗时 2-4 小时。

对于内容创作者来说，核心瓶颈不是「不知道讲什么」，而是「讲出来了，但做不成视频」。

### 1.2 催化剂

ClipForge 的诞生源于一个具体需求：每天把 GitHub 上最火的开源项目，用 45 秒视频告诉所有人。听起来简单——抓数据、写文案、做视频、发出去。但真正做起来，每一步都是专业门槛：

- 脚本怎么写才能抓住前 3 秒？
- 配音用什么音色、什么语速？
- 画面怎么排才不会信息过载？
- 配乐怎么选才能和内容情绪匹配？
- 封面怎么设计才能让用户停下来？

一个人手工做，每天一条视频，光剪辑就要 2 小时。如果要做到「每天 7 点自动更新」，靠人是不可能的。

### 1.3 转折：发现 HyperFrames

HyperFrames 是一个开源项目，它提供了一个关键能力：**通过写 HTML 代码生成视频**。这意味着，只要你能在网页上画出来的东西，它都能变成视频帧。对于程序员来说，这把视频创作变成了代码问题。

但 HyperFrames 解决的是「渲染层」——它能把 HTML 变成视频，但不解决「写什么内容」「怎么排版」「配什么音乐」「旁白和画面怎么同步」这些上游问题。每个视频仍然需要手工编写 HTML、手工调试动画、手工处理音画同步。

### 1.4 ClipForge 的定位

ClipForge 不是又一个视频编辑器。它是**一套完整的自动化管线**——从原始内容到可发布的短视频，9 个阶段全链路自动化。它的核心假设是：**如果你能把「做视频」这件事拆解成足够清晰的步骤，每一步都可以交给 AI 来做。**

---

## 二、架构哲学：不教怎么做，只定边界

### 2.1 核心设计原则

ClipForge 的设计哲学可以浓缩为一句话：**流程零自由度，内容最大自由度。**

这是什么意思？

**流程层面（LETTER 模式）**：管线怎么走、每个阶段做什么、质量标准是什么——这些全部硬编码在配置文件中，AI 没有更改的自由。9 个阶段的执行顺序由 DAG（有向无环图）定义，质量门禁由规则引擎驱动，AI 只能遵守，不能绕过。

**内容层面（SPIRIT 模式）**：每个场景讲什么、画面怎么排、用什么颜色、选什么特效——这些全部由 AI 自主推导。系统不提供「照抄模板」，而是提供「推导约束」，让 AI 从内容本身出发，自主决定视觉表达。

这种分离的底层逻辑是：流程是工程的，需要确定性和可复现性；内容是创意的，需要自由度和惊喜感。

### 2.2 Schema 即真相

所有 artifact（产出物）的依赖关系、产出文件、完成状态，全部定义在一个 `schema.yaml` 文件中。这是整个系统的唯一真相源。

```
env-check → content → design → narration → audio → video → delivery → scoring → cleanup
```

每个 artifact 声明：
- `requires`：硬依赖（必须完成后才能开始）
- `generates`：产出文件（文件存在即代表完成）
- `optional`：可选步骤（跳过不阻塞下游）

**状态即文件**——`generates` 声明的文件存在于磁盘上，就代表这个阶段完成了。没有数据库，没有状态服务器。中断后重新运行，系统自动扫描已完成的文件，跳过对应阶段，从断点继续。

### 2.3 委托不重写

ClipForge 不重新发明轮子。HTML 渲染和视频合成委托给 HyperFrames，语音合成委托给 edge-tts（微软 Azure 语音服务的免费接口），音量校准委托给 FFmpeg 的 loudnorm 滤镜。

ClipForge 自己只做三件事：
1. **编排**：决定每个阶段做什么、按什么顺序做
2. **约束**：定义质量标准和错误恢复策略
3. **演化**：从反馈数据中学习，持续改进

---

## 三、九阶段管线详解

### 3.1 全景图

| 阶段 | 名称 | 产出 | 核心任务 |
|------|------|------|----------|
| Stage 0 | 环境检查 | env-check | 检测依赖，自动安装缺失工具 |
| Stage 1 | 内容获取 | content.md | 从 URL/PDF/文字/数据源提取素材 |
| Stage 2 | 导演设计 | design.md | 确定情感内核、配色、视觉风格 |
| Stage 3 | 旁白文案 | narration.txt + narration_segments.json | 场景拆解 + 分段旁白 + 旁白时长预估 |
| Stage 4 | 音频制备 | narration.mp3 + bgm.wav + segment_durations.json | 分段 TTS + BGM 选取 + 音量校准 |
| Stage 5 | 素材制备 | assets/ | 图片/图标等视觉素材（可选） |
| Stage 6 | 视频渲染 | index.html + output.mp4 | HTML + 组件 + 动画 → HyperFrames 渲染 |
| Stage 7 | 交付输出 | final.mp4 + cover.png + douyin.md | 封面 + 抖音文案 + 双版本输出 |
| — | 机器评分 | score_report.json | gate 全量校验 + 机器预测评分 |
| — | 清理 | .cleaned | 删除中间产物，保留最终成果 |

### 3.2 DAG 编排

阶段之间不是简单的线性流水线，而是通过 DAG 语义编排：

```
content → design ─┬→ narration → audio ──┬→ video → delivery → scoring → cleanup
                   │                assets ┘
                   └→ assets（可选）
```

关键设计点：
- `audio` 和 `assets` 可以**并行执行**（分属不同 SubAgent）
- `assets` 是 `optional`——没有素材也能完成视频
- `video` 对 `assets` 是 `requires_optional`——有素材就等，没有就跳过
- `movie-clips`（电影片段）通过 `condition` 触发——只有当 narration 中包含 `video_clip` 类型场景时才激活

### 3.3 黄金 3 秒法则

整个管线的所有阶段，都围绕一个核心指标：**前 3 秒的留存率。**

在短视频平台，用户划走一个视频只需要 1-3 秒。前 3 秒决定生死。因此：

- **旁白 hook**（Stage 3）：第一个场景必须是纯钩子——震撼数据、反直觉描述、强对比，不含任何信息性内容
- **画面视觉**（Stage 6）：hook 场景必须是全片视觉最强烈的画面——字号最大、对比最强、动画最干脆
- **音频开场**（Stage 4）：禁止任何形式的淡入，旁白和 BGM 在第一帧必须全音量

---

## 四、引擎层：四原子约束体系

### 4.1 设计动机

管线编排解决了「做什么、按什么顺序做」的问题，但没有解决「做得好不好」的问题。早期版本中，AI 经常犯一些反复出现的错误：

- CSS 动画在 HyperFrames 的 seek 渲染模式下永远不会执行（因为 seek 不触发 CSS animation）
- 安全区 padding 设了两层，内容被压缩到 74% 宽度
- 旁白里出现了 URL，被抖音审核限流
- BGM 音量太大盖住了旁白

这些错误不是偶发的——AI 每次都会犯，因为它的训练数据中没有「HyperFrames seek 模式的限制」这种特定知识。

### 4.2 四原子模型

ClipForge 引擎层引入了四原子约束体系：**Intent / Boundary / Gate / Trace**。

**Intent（意图）**：每个阶段的核心目标是什么。例如 Stage 4 的 Intent 是「产出与旁白完美同步的音频」。Intent 告诉 AI 「你在做什么」，但不告诉它「怎么做」。

**Boundary（边界）**：每个阶段允许和禁止的行为。Boundary 来自规则库（`rules/` 目录下的 YAML 文件），例如：
- `R-R-001`：禁止使用 `.anim-in` CSS 类（HyperFrames 不执行 CSS animation）
- `R-R-003`：禁止双重 padding（`.scene-wrap` 和 `.phase` 不能同时设置 padding）
- `R-R-010`：音频文件必须在 index.html 同级目录

每个规则包含：
- `pattern`：违反时表现出的行为模式
- `positive`：正确的做法是什么
- `severity`：HARD（必须通过）或 SOFT（建议修复）
- `detection`：如何检测（关键词、正则、语义检查）

**Gate（门禁）**：阶段完成后的自动校验。Gate 引擎（`engine/gate.py`）包含 22 种检查器：

```python
class GateType(str, Enum):
    file_exists = "file_exists"
    json_valid = "json_valid"
    loudnorm_verified = "loudnorm_verified"
    bgm_volume_set = "bgm_volume_set"
    no_forbidden_speech = "no_forbidden_speech"
    no_url_in_output = "no_url_in_output"
    duration_in_range = "duration_in_range"
    hook_pattern_verified = "hook_pattern_verified"
    composition_structure = "composition_structure"
    bg_visual_diversity = "bg_visual_diversity"
    fx_layer_not_empty = "fx_layer_not_empty"
    video_bitrate_valid = "video_bitrate_valid"
    html_no_css_visibility = "html_no_css_visibility"
    bgm_silence_valid = "bgm_silence_valid"
    data_duration_source_valid = "data_duration_source_valid"
    ...
```

每个检查器返回 `(passed: bool, message: str)` 元组。HARD 门禁失败时，系统展示违规详情并要求修复后重试；SOFT 门禁失败时，展示警告由用户决定是否接受。

**Trace（轨迹）**：记录每次执行的完整上下文——用了什么规则、哪些门禁通过/失败、Token 消耗多少、耗时多久。Trace 是自进化反馈的数据基础。

### 4.3 引擎代码规模

引擎层由 12 个 Python 文件组成，共 4,781 行代码：

| 文件 | 行数 | 职责 |
|------|------|------|
| `engine/inject.py` | ~400 | 约束注入：生成正向 prompt（规则 + 经验模式 + Guard Red Flags） |
| `engine/gate.py` | ~500 | 门禁引擎：22+ 检查器，HARD/SOFT 双轨校验 |
| `engine/attribution.py` | ~350 | 失败归因：强归因（规则匹配）+ 弱归因（概率推断） |
| `engine/trace.py` | ~250 | 执行轨迹：结构化记录上下文、结果、性能 |
| `engine/render_stage.py` | ~200 | 模板渲染：将分类配置值合并到通用 stage 模板 |
| `engine/skeleton_builder.py` | ~400 | 骨架构建：场景骨架 + 创意插槽数据模型 |
| `engine/slot_injector.py` | ~350 | 插槽注入：将创意内容填入骨架插槽 |
| `engine/visual_context.py` | ~300 | 视觉上下文：前后场景指纹 + 情绪曲线位置 |
| `engine/governance.py` | ~300 | 规则治理：冲突检测、膨胀预警 |
| `engine/success_analyzer.py` | ~280 | 成功分析：从 Trace 数据中沉淀经验模式 |
| `engine/delta_lifecycle.py` | ~250 | 增量规则生命周期管理 |
| `engine/lib/models.py` | ~313 | 核心数据模型：Rule/Gate/Violation/CreativeSlot 等数据类 |
| `engine/lib/rule_parser.py` | ~176 | 规则解析器 |
| `engine/lib/delta.py` | ~158 | 增量规则管理 |
| `engine/lib/positive_rewrite.py` | ~89 | 正向重写器 |

### 4.4 约束注入流程

在 AI 执行每个阶段之前，引擎自动运行约束注入：

```bash
python engine/inject.py --skill stage6-production [--category github]
```

输出包含四段内容，拼入 AI 的 prompt 前段：
1. **Intent**：本阶段的核心目标
2. **正向规则**：从规则库中筛选出本阶段适用的规则，以「应该做什么」的正面表述呈现
3. **经验模式**：从 `patterns/` 目录加载历史成功案例（90 天老化，过期自动清除）
4. **Guard Red Flags**：本阶段最容易犯的错误清单

这种设计的关键洞察是：**不要告诉 AI 「不能做什么」，而是告诉它「应该做什么」。** 正向指令比禁止指令更有效。

---

## 五、视觉系统：三层渲染架构

### 5.1 为什么是三层

短视频画面的核心矛盾是：**背景要有氛围感，特效要有视觉冲击力，但文字必须清晰可读。** 如果这三层混在一起，要么背景太抢眼文字看不清，要么特效遮挡关键信息。

ClipForge 的解决方案是严格的**三层分离架构**：

| 层级 | CSS class | z-index | 用途 | 内容 |
|------|-----------|---------|------|------|
| 底层 | `.layer-bg` | 1 | 场景背景 | 渐变色、光晕、网格底纹、等高线、光束 |
| 中间层 | `.layer-fx` | 2 | 视觉特效 | 粒子、爆炸、矩阵雨、双轨道粒子、漂浮物 |
| 顶层 | `.layer-content` | 3 | 可读内容 | 文字、数字、徽章、卡片、标签 |

每一层都有明确的职责边界：
- `.layer-bg` 至少包含渐变背景 + 2 种不同类型的视觉元素（渐变 + 纹理 + 光效，三者取二以上）
- `.layer-fx` 不能为空，必须包含至少 1 个特效子元素，且 `pointer-events: none` 防止遮挡交互
- `.layer-content` 包含所有用户需要阅读的元素

### 5.2 骨架 + 创意插槽模式

Stage 6 的 HTML 生成不是「从头写一整个页面」，而是分两步：

**第一步：骨架生成（skeleton_builder.py）**

系统根据 Stage 3 的场景定义，生成 HTML 骨架——包含每个场景的三层结构、`data-start`/`data-duration` 时间属性、Phase 分断点，但 bg/fx/content 三层的内容是空的。

**第二步：创意插槽填充（slot_injector.py）**

骨架中预留了**创意插槽**（CreativeSlot），每个插槽是一个 HTML 注释标记：

```html
<!-- CREATIVE_SLOT:s1-bg-html -->
<!-- CREATIVE_SLOT:s1-fx-html -->
<!-- CREATIVE_SLOT:s1-content-html -->
```

AI 看到的不是「画一个场景」，而是「在这个插槽里填入背景/特效/内容」。每个插槽附带丰富的上下文信息：

```python
@dataclass
class CreativeSlot:
    slot_id: str           # "s1-bg-html"
    scene_id: str          # "s1"
    layer: str             # bg / fx / content
    scene_duration: float  # 场景时长
    emotion_tags: list     # 情绪标签
    narration_text: str    # 对应旁白文本
    emotion_intensity: float  # 情感强度
    prev_scene_summary: dict  # 前一场景视觉指纹
    next_scene_summary: dict  # 后一场景视觉指纹
    visual_theme: dict     # 全片视觉主题
    rhythm_guidance: str   # 节奏引导文字
```

这种设计的妙处在于：**把「自由创作」限定在明确的空间里**。AI 可以在插槽内自由发挥，但不能改变骨架结构（三层分离、时间属性、Phase 分断点）。流程零自由度，内容最大自由度。

### 5.3 组件库

ClipForge 内置了 32 个视觉组件，按三层分类：

**背景组件（8 个）**：渐变网格、光场、噪声场、等高线、放射光束、扫描网格、暗角光晕、波纹

**特效组件（10 个）**：星爆、光球、矩阵雨、双轨道粒子、渐变波、漂浮粒子等

**内容组件（14+ 个）**：英雄卡片、项目全卡、数据可视化、市场柱状图、星级计数器、文字揭示、对话气泡、对比分屏等

每个组件都是一个自包含的 HTML+CSS 模板，带有 `@ComponentMeta` 注解（包含适用场景、情绪标签、推荐配色），可以被组件推导系统自动匹配到合适的场景。

### 5.4 GSAP 动画与 HyperFrames Seek 模式

HyperFrames 的渲染机制是 **seek-based**——逐帧推进，而不是实时播放。这意味着：

- CSS `animation` 和 `transition` **不会执行**（因为 seek 不触发 CSS 事件）
- GSAP timeline 是唯一可靠的动画机制（因为 GSAP 的 `.seek()` 方法可以正确回放所有动画）

这个限制催生了一系列硬性规则：
- 禁止 `.anim-in` CSS 类或任何 CSS `opacity:0` 入场动画
- 所有入场动画由 GSAP `.from({opacity:0})` 实现
- CSS animation 只用于可见位置之间的移动（如光球漂移），不能用于「从无到有」的过渡

---

## 六、音画同步：分段校准

### 6.1 核心挑战

音画同步是短视频制作中最难的技术问题。传统做法是先做画面、后配音，根据画面长度调整语速。但 AI 管线中，旁白文案（Stage 3）先于画面（Stage 6），时长只有预估值。

如果预估不准，画面和声音就会错位——画面已经切换到新项目，旁白还在说上一个项目。

### 6.2 分段 TTS + 实测校准

ClipForge 的解决方案是**分段校准**：

1. **Stage 3**：每个场景一段旁白，预估时长（基于字数 × 语速）
2. **Stage 4**：逐段 TTS 生成，输出 `segment_durations.json`（实际时长）
3. **Stage 6**：用 `segment_durations.json` 的实际时长设置 HTML `data-duration`，而非预估值

关键设计：`data-duration` 的**唯一权威来源**是 `segment_durations.json` 的 `actual_duration`，而不是 `narration_segments.json` 的 `estimated_duration`。门禁引擎会自动检测这个一致性——差值超过 0.5 秒即判定为 HARD 失败。

### 6.3 视觉分段的精细化

场景内部，通过 **Phase（视觉阶段）** 实现更精细的画面切换。人眼在静态画面上的注意力极限约 8-12 秒，超过这个阈值不切换视觉内容，观众注意力就会游离。

Phase 断点的计算不是时间均分（这会导致旁白与画面严重不同步），而是**逐段分析旁白文本，找到话题转换点，按字数比例换算为时间戳**。

---

## 七、自进化反馈系统

### 7.1 双闭环设计

ClipForge 不是一个固定输出的工具。它从两条反馈链路中持续学习：

**失败闭环（收紧规则）**：
```
门禁失败 → attribution.py 归因分析 → 定位违反的规则 → 修复重试或回退上游
```

归因引擎支持两种归因模式：
- **强归因**：规则匹配——能精确找到违反了哪条规则
- **弱归因**：概率推断——从 Trace 数据中推断可能的能力缺口或规则缺失

**成功闭环（沉淀模式）**：
```
门禁通过 → trace.py 记录轨迹 → success_analyzer.py 分析成功因素 → 写入 patterns/ 目录
```

成功分析会提取：哪些规则被触发了、用了什么组件组合、视觉风格是什么。这些经验模式会被 inject.py 在后续执行中加载，帮助 AI 避免重复成功路径。

### 7.2 播放数据驱动校准

更进一步的反馈来自**真实的播放数据**：

```
制作视频 → 机器评分 → 发布 → 用户导入播放数据 → 对比预测 vs 实际 → 自动调整规则
```

每条视频完成后，ClipForge 自动生成 `score_report.json`（机器预测评分）。视频发布 1-2 天后，用户从抖音、B站、视频号、小红书等平台导出播放数据。ClipForge 对比机器预测和实际表现，发现偏差并产出校准信号。

例如：
- 机器预测某条视频的 5 秒完播率是 45%，实际只有 30% → 说明 hook 场景的设计规则需要收紧
- 机器预测某类配色的点击率低，实际却很高 → 说明配色规则需要放宽

校准信号经人工确认后写入规则库，让下一次预测更准确。规则有 90 天老化机制——过期的经验模式自动清除，避免过时的经验影响当前决策。

### 7.3 规则的严格程度分档

ClipForge 的约束系统支持三种严格程度：

| 级别 | 适用场景 | 效果 |
|------|---------|------|
| LITE | 探索阶段、原型验证 | 只注入 SAFETY 类规则 |
| STANDARD | 日常生产 | 注入 SAFETY + EXPERIENTIAL 规则 |
| STRICT | 高质量要求、参赛作品 | 全量规则 + 所有经验模式 |

---

## 八、开发历程与关键决策

### 8.1 时间线

- **2026-05-22**：项目启动。60 次提交，182 个文件，23,262 行代码变更——全部在 8 天内完成。
- **Day 1-2**：基础管线搭建。9 阶段 DAG 定义，schema.yaml 确立为唯一真相源。
- **Day 3**：音画同步危机。发现整段 TTS 的时长偏差达 2-3 秒，催生了分段 TTS + `segment_durations.json` 校准机制。
- **Day 4**：渲染安全事故。CSS `.anim-in` 导致全片空白，HTML 实体字符导致整段不渲染。催生了 `render-safety.md` 185 行规范。
- **Day 5**：双层 padding 事故。内容被压缩到 74% 宽度，催生了「单层 padding 铁律」。
- **Day 6**：引擎层开发。四原子约束体系（4,781 行 Python），从「事后修复」升级为「事前预防」。
- **Day 7**：三层架构重构。组件库从扁平结构升级为 bg/fx/content 三层目录，创意插槽系统上线。
- **Day 8**：A/V 同步门禁加固。新增 `data_duration_source_valid` 和 `estimation_accuracy_valid` 检查器。

### 8.2 关键设计决策

**决策 1：状态即文件，不用数据库。**
为什么？因为 ClipForge 运行在 Claude Code 环境中，Claude Code 能直接读取文件系统，但无法连接外部数据库。文件系统是最简单、最可靠的状态存储。`schema.yaml` 声明每个阶段产出什么文件，文件存在即完成。这让中断恢复变得极其简单——重新运行，自动跳过已完成阶段。

**决策 2：正向规则优先，而非禁止清单。**
为什么？实验发现，当 AI 的 prompt 中充满了「禁止做 X」「禁止做 Y」时，AI 的注意力反而被这些禁止项吸引，犯错率更高。改为「应该做 X」「推荐用 Y 方法」的正向表述后，AI 的遵循率显著提升。

**决策 3：骨架 + 创意插槽，而非模板填充。**
为什么？模板填充的问题是：模板数量有限，视频之间容易雷同。骨架 + 插槽模式让 AI 在结构化的框架内自由创作——结构由系统保证（三层分离、时间对齐），内容由 AI 自主推导（颜色、特效、排版）。

**决策 4：委托不重写。**
为什么？HyperFrames 是一个成熟的开源项目，渲染质量和性能都经过验证。重新实现一个渲染引擎的 ROI 极低。ClipForge 专注于编排和约束，把渲染、TTS、音量校准等专项工作委托给专业工具。

### 8.3 从事故中学习

ClipForge 的很多核心规则不是设计出来的，而是从实际事故中总结的：

| 事故 | 根因 | 沉淀的规则 |
|------|------|-----------|
| 全片空白渲染 | CSS `.anim-in` 在 seek 模式下不执行 | R-R-001：禁止 CSS 入场动画 |
| 整段内容不渲染 | HTML 实体字符（`&#9733;`）解析失败 | R-R-002：禁止 HTML 实体 |
| 内容被压缩到 74% | 双重 padding 累积 | R-R-003：单层 padding 铁律 |
| 四面黑边 | `.clip` 设置了 top/right/bottom/left 偏移 | R-R-003a：背景铺满全画幅铁律 |
| BGM 盖住旁白 | bgm.wav 预衰减 + HTML data-volume 双重衰减 | 音量表扩展 7 档 + 峰值间距校验 |
| 旁白画面不同步 | 使用 estimated_duration 而非 actual_duration | data_duration_source_valid 门禁 |
| BGM 静音尾段 | 源文件后半段音量骤降 | bgm_pipeline.sh 前后半音量对比检测 |
| 场景视觉同质化 | 相邻场景使用相同渐变色值 | bg_visual_diversity + adjacent_bg_diversity 门禁 |

每一个事故都催生了至少一条 HARD 门禁规则，确保同类问题不会再次发生。这就是自进化的本质：**不是从理论推导规则，而是从失败中提取经验。**

---

## 九、技术实现细节

### 9.1 规则引擎实现

规则以 YAML 格式定义，每条规则包含完整的元数据：

```yaml
rules:
  - id: "R-R-001"
    type: FORBIDDEN_METHOD
    pattern: "使用 .anim-in CSS 类"
    positive: "使用 GSAP .from() 实现入场动画"
    severity: HARD
    class: SAFETY
    scope: GLOBAL
    detection:
      keywords: ["anim-in"]
      regex: "\\.anim-in"
    source: "shared/render-safety.md §1.1"
```

`inject.py` 加载规则后，按以下逻辑处理：
1. 按 `scope` 筛选适用于当前阶段的规则
2. 按 ID 去重（同 ID 规则只保留最新版本）
3. SAFETY 类规则在 LITE 模式下也会加载
4. 90 天老化的经验模式自动过滤
5. 生成正向 prompt 段（「应该做什么」而非「不能做什么」）

### 9.2 门禁引擎实现

`gate.py` 的核心是检查器注册表：

```python
CHECKERS: dict[GateType, Callable] = {
    GateType.file_exists: check_file_exists,
    GateType.json_valid: check_json_valid,
    GateType.loudnorm_verified: check_loudnorm_verified,
    GateType.bgm_volume_set: check_bgm_volume_set,
    GateType.no_forbidden_speech: check_no_forbidden_speech,
    ...
}
```

每个检查器签名统一为 `(project_dir: str, params: dict) -> tuple[bool, str]`。门禁分为 HARD 和 SOFT 两轨：

- **HARD 门禁**：必须全部通过，否则阶段失败
- **SOFT 门禁**：建议修复，用户可选择接受

门禁结果封装在 `GateReport` 中：

```python
@dataclass
class GateReport:
    hard_passed: bool
    soft_score: float
    hard_violations: list[Violation]
    soft_issues: list[str]
    details: dict[str, Any]
```

### 9.3 创意插槽的数据模型

```python
@dataclass
class CreativeSlot:
    slot_id: str           # "s1-bg-html"
    scene_id: str          # "s1"
    layer: str             # bg / fx / content
    slot_type: str         # css / html / gsap
    marker: str            # "<!-- CREATIVE_SLOT:s1-bg-html -->"

    # 上下文信息
    scene_duration: float
    emotion_tags: list[str]
    narration_text: str
    emotion_intensity: float
    prev_scene_summary: dict  # 前序场景视觉指纹
    next_scene_summary: dict  # 后续场景视觉指纹
    visual_theme: dict        # 全片视觉主题
    rhythm_guidance: str      # 节奏引导
```

每个插槽的上下文信息确保 AI 在填充内容时，能够考虑到前后场景的视觉连续性和全片的情感节奏。

---

## 十、成果与数据

### 10.1 项目规模

| 指标 | 数值 |
|------|------|
| 开发周期 | 8 天（2026-05-22 至 2026-05-30） |
| Git 提交数 | 60 次 |
| 文件变更 | 182 个文件，23,262 行插入，3,783 行删除 |
| 引擎代码 | 12 个 Python 文件，4,781 行 |
| 总代码+文档 | 16,314 行 |
| 视觉组件 | 32 个 HTML 模板（8 bg + 10 fx + 14+ content） |
| 门禁检查器 | 22+ 种 |
| 规则文件 | 多个 YAML 规则库（全局安全、渲染安全、各阶段特定） |

### 10.2 能力范围

ClipForge 当前支持三种视频模式：

| 模式 | 时长 | 场景数 | 适用场景 |
|------|------|--------|----------|
| 标准模式 | 45-55s | 6-8 个 | 多主题盘点、快速资讯 |
| 深度解析 | 45-60s | 7-8 个 | 单项目详细解读 |
| 长视频 | 3-10min | 不限 | 报告解读、深度剖析 |

### 10.3 已验证的视频类型

- GitHub 每日热门趋势（45s，每日自动执行）
- GitHub 单项目深度解读（50-60s）
- 互联网行业报告深度解读（55s）
- AI-Agent 商业价值 10 分钟长视频
- ClipForge 自我剖析（本视频）

---

## 十一、未来展望

### 11.1 分类扩展

ClipForge 的分类系统允许任何人扩展到新领域。运行 `/clipforge-category-setup`，回答几个问题（领域名称、数据来源、风格偏好），系统自动生成完整的分类配置。计划中的分类包括：医学健康科普、财经投资速报、读书知识、法律政策解读等。

### 11.2 多平台适配

当前主要面向抖音竖屏（1080×1920），但三层架构和组件系统天然支持多平台扩展。调整安全区 padding 参数和分辨率配置即可适配小红书、B站、微信视频号等平台。

### 11.3 社区驱动进化

自进化反馈系统目前依赖单个用户的播放数据。当更多创作者使用 ClipForge 并导入播放数据时，规则库将获得更丰富的训练信号，进化速度会指数级提升。

### 11.4 本视频的意义

本视频是 ClipForge 的「自我证明」——用自己制作关于自己的视频。如果这条视频的质量能够达到参赛水准，就证明了 ClipForge 的核心假设：**通过管线编排 + 约束引擎 + 自进化反馈，AI 可以持续产出高质量的短视频内容。**

---

## 十二、总结

ClipForge 的核心价值不在于它能做视频——很多工具都能做。它的价值在于：

1. **把做视频的隐性知识显性化**——每一个设计决策、每一个质量标准、每一个常见错误，都变成了可执行的规则和门禁
2. **把创意的自由和流程的严谨分离**——流程层零自由度（LETTER），内容层最大自由度（SPIRIT）
3. **从失败中学习，从数据中进化**——不是固定输出的工具，而是一个能自我改进的系统
4. **8 天，60 次提交，2 万行代码**——证明了 AI 辅助开发的惊人效率

ClipForge 是开源的。Apache 2.0 许可证。任何人都可以用它来制作自己领域的短视频。

---

*本报告生成于 2026-05-30，作为 VibeCoding 大赏参赛视频的内容源。*
*参赛标签：#vibecoding大赏 #ai新星计划 @抖音科技*
