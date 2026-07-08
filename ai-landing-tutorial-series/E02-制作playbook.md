# E02 制作 Playbook（subagent 执行用）

> 基于已完成的 hook + intro 段经验。剩余 7 段照此执行。

## 范式参考（必读）

- **intro 段**（最简范式，1 场景多 region）：`workspace/2026/07/05/tutorial-e02-intro/`
  - `design.md` / `creative/s01.html` / `creative/style.css` / `cover_params.json`
- **hook 段**（双场景，含 count-up）：`workspace/2026/07/05/tutorial-e02-hook/`

先 Read intro 的 4 个范式文件，理解结构。各段照 intro 改内容。

## 通用流程（每段，目录 `workspace/2026/07/05/tutorial-e02-{段名}/`）

```bash
# 每条 Bash 开头 cd 回项目根（避免 cwd 漂移到 CF_DIR）
cd D:/AI-Agent/video-clipforge && source .claude/commands/clipforge/shared/clipforge-env.sh
P="D:/AI-Agent/video-clipforge/workspace/2026/07/05/tutorial-e02-{段名}"

# 1. 创意轨文件（Write 工具）：content_ready.txt + narration.txt + narration_segments.json + design.md
# 2. BGM + TTS + BGM管线 + prepare
cp "D:/AI-Agent/video-clipforge/workspace/bgm/clean-corporate-3.mp3" "$P/bgm.wav"
bash scripts/tts_pipeline.sh --project-dir "$P" "zh-CN-YunjianNeural" "+0%"
bash scripts/bgm_pipeline.sh --project-dir "$P"
bash scripts/s6_prepare.sh --project-dir "$P"
# 3. creative 碎片（Write，覆盖 prepare 骨架）：creative/s01.html + creative/style.css + cover_params.json
#    ⚠ 写 creative 前先 Read 骨架（s01.html/style.css），Write 要求先 Read
# 4. 组装 + 渲染 + 交付
bash scripts/s6_assemble.sh --project-dir "$P"
bash scripts/s6_render.sh --project-dir "$P"
bash scripts/s7_delivery.sh --project-dir "$P"
```

## 坑清单（每个都踩过，必读）

| 坑 | 规避 |
|----|------|
| **R-R-010 相邻同质**（2 场景段永远过不了 min_styles=3） | **每段用 1 seg 单场景多 region**（narration_segments 只 1 个 seg，scenes=1 自动跳过 R-R-010）|
| **字号下限 32px** | 所有可见文字 font-size ≥ 32px（胶囊/小标签也要）|
| **text-shadow 必须**（深色背景文字浮起，HARD） | 关键文字（标题/卡片头/列表项/结论）都加 text-shadow；**blur 大字≤20px、普通≤12px**（>28px 触发泛光门禁）|
| **违禁词「第一」**（绝对化用语，子串匹配 HARD） | 用「起手」「头一个」替代「第一」；narration + creative + cover_params 都不能有「第一」|
| **「转」多音字读音**（edge-tts 单字读 zhuàn 四声） | 用「转型」不用单字「转」（"必须转型"而非"必须转"）|
| **fx 划过类禁用**（tutorial.md HARD） | 用 `fx-pulse`/`fx-blink`/`fx-dot`（静态/脉冲）；**禁 fx-scan/fx-stream/fx-beam**（划过追线）|
| **bg 组件** | creative s01 的 layer-bg 只写 `<!-- bg-component: clean_slate -->` 注释（assemble 自动注入 DOM + data-bg-types），**删手写 bg DOM** |
| **教程 reveal 范式** | 单 phase：`<div class="phase phase-1 tut-scene">`；多 region：`<div class="tut-region" data-reveal="N" data-reveal-dir="left/top/fade">`；data-reveal-dir=left 从 x:-40 / top 从 y:-40 / fade 纯 opacity |
| **assemble_final 时长断言严** | final.mp4 比 output 长 0.1-0.15s 触发 FAIL，但 **final.mp4 已正常生成**（含 Mastering），接受此 FAIL，final 可用 |
| **完成门禁 R-R-010** | 1 场景段 scenes=1 跳过，hard_passed=true；若 2 场景段 hard_passed=false 但 output.mp4 已生成，接受（E01 先例）|

## creative 碎片结构模板（照 intro，每段改 region 内容）

s01.html（1 场景 + N region）：
```html
<!-- 场景: seg1 | 时长: ~XXs | bg: clean_slate | {段描述} -->
<div class="layer-bg">
  <!-- bg-component: clean_slate -->
</div>
<div class="layer-fx">
  <div class="fx-pulse" style="position:absolute;...;background:radial-gradient(ellipse, hsla(...,0.18) 0%, transparent 65%);filter:blur(50px);opacity:0.7"></div>
  <div class="fx-blink" style="position:absolute;...;width:12px;height:12px;border-radius:50%;background:hsla(...,0.85);box-shadow:0 0 16px ..."></div>
</div>
<div class="layer-content">
<div class="phase phase-1 tut-scene">
  <div class="tut-grid">
    <div class="tut-region {区域类}" data-reveal="0" data-reveal-dir="fade">...</div>
    <div class="tut-region {区域类}" data-reveal="N" data-reveal-dir="left">...</div>
    ...
  </div>
</div>
</div>
<div class="layer-cinema"></div>
```

style.css（照 intro，含教程色板 + tut-scene + tut-region + 渐变 + 段特定类 + **text-shadow**）。

cover_params.json（照 intro 模板，改 badge/title/data_subtitle/cards）。

---

## 7 段 spec

### 1. mindset（思想转变，~90s，1 场景 5 region）
- **目录**：tutorial-e02-mindset
- **narration**（1 seg）：转型里最容易栽的两个坑，刚好是两个极端。一端是抗拒——觉得 AI 是噱头、怕被替代，碰都不碰。半年后回头发现，不是 AI 替代了你，是会用 AI 的人替代了你——差距是数量级的。另一端是盲目崇拜——觉得它万能，全盘交付不验证，产出不可控、质量崩塌。正确姿态四个字：拥抱，加验证。把 AI 当一个不知疲倦但会犯错的资深实习生——委派任务，但审查产出。信任，但验证。光有态度不够——得懂它怎么运作，才能精准驾驭。
- **视觉**：
  - region1（reveal 0，fade）：标题「两个极端 · 都要避免」
  - region2（reveal 6，left）：左卡「抗拒 AI」红边框 + 表现（觉得噱头/怕替代）+ 代价（被会用的人替代）
  - region3（reveal 18，left）：右卡「盲目崇拜」红边框 + 表现（万能/全盘交付）+ 代价（产出不可控）
  - region4（reveal 32，top）：金句「拥抱 + 验证」绿边框 + 「信任但验证」+ 「当资深实习生」
  - region5（reveal 50，fade）：转折「光有态度不够 → 要懂原理」（引出后半段）
- **色**：左/右卡红（#EF4444 边框）/ 金句绿（#10B981）/ 转折蓝（#3B82F6）

### 2. essence（原理① AI 本质，~80s，1 场景 4 region）
- **目录**：tutorial-e02-essence
- **narration**（1 seg）：原理一，先搞懂 AI 到底是什么。当前所有 AI——ChatGPT、Claude、GPT-5——全是弱 AI，擅长特定任务，但没有真正理解和意识。强 AI 也就是 AGI，目前只是理论。所以 AI 不是万能的，是它的本质决定的。AI 有两大流派：符号推理用规则模拟逻辑，已被淘汰；神经网络模拟大脑结构从数据学，是当前主流，大模型属于这一类。判断机器算不算智能？图灵测试——人分不清对面是人还是机器就算通过。但通过图灵测试不等于真有智能，可能只是巧妙的模仿。
- **视觉**：
  - region1（reveal 0，fade）：原理编号「原理 ①」+ 标题「AI 到底是什么」
  - region2（reveal 8，left）：弱 AI vs 强 AI 对比卡（弱AI=当前所有/擅长特定任务；强AI=AGI/理论）
  - region3（reveal 28，left）：两大流派（符号推理 GOFAI 已淘汰 / 神经网络 当前主流·大模型）
  - region4（reveal 50，top）：图灵测试 + 注解「通过≠真有智能，可能只是模仿」

### 3. token（原理② token 预测，~85s，1 场景 4 region）
- **目录**：tutorial-e02-token
- **narration**（1 seg）：原理二，大模型本质。一句话——根据上文预测下一个 token，也就是词元。比如输入"今天天气真"，预测下一个字大概率是"好"。它不是真理解你的代码，而是基于海量模式生成最可能的续写。这解释了幻觉——AI 会一本正经地胡说，因为生成的是看起来对的，不是验证过对的。所以从原理上就明白：AI 产出必须验证。这不是不信任，是它的运作方式决定的。信任但验证，根在这。
- **视觉**：
  - region1（reveal 0，fade）：原理编号「原理 ②」+ 标题「预测下一个 token」
  - region2（reveal 8，left）：token 预测示意「今天天气真 → 好」（大字 + 箭头）
  - region3（reveal 30，top）：幻觉揭示卡「一本正经地胡说 · 看起来对 ≠ 验证过对」
  - region4（reveal 50，fade）：金句「必须验证」+ count-up 验证率 0→100%（用 data-count-to="100" data-count-at="52"）

### 4. context（原理③ 上下文 1M，~75s，1 场景 3 region）
- **目录**：tutorial-e02-context
- **narration**（1 seg）：原理三，上下文窗口。现在模型上下文到 1M——一百万 token，听着很大。但虽大还是会填满。一个大代码库、一段长会话、一堆 MCP 工具定义，都会把它撑爆，一旦填满性能就下降。几乎所有最佳实践都在围这一个约束转：精简 CLAUDE.md、按需加载 Skill、保持干净会话、能用 CLI 就别堆 MCP。上下文是稀缺资源，每一段常驻内容，都要挣它的一席之地。
- **视觉**：
  - region1（reveal 0，fade）：原理编号「原理 ③」+ 标题「上下文 1M · 约束原点」
  - region2（reveal 8，left）：上下文桶示意 + count-up 填充度 0→100%（data-count-to="100" data-count-at="10"，旁注：大代码库/长会话/MCP 撑爆）
  - region3（reveal 30，top）：最佳实践清单（精简 CLAUDE.md / 按需 Skill / 干净会话 / CLI 优于 MCP）

### 5. agent（原理④⑤ Agent+REACT，~100s，1 场景 3 region）
- **目录**：tutorial-e02-agent
- **narration**（1 seg）：原理四和五是一对——Agent 和 REACT。大模型本身只能输出文字，读不了文件、调不了接口、跑不了命令。把大模型和一堆工具组装起来，让它能感知和改变环境，就是 Agent。模型先思考再行动的奥秘，藏在系统提示词里——定义什么时候调什么工具，靠提示词工程不是训练。Agent 怎么跑？靠 REACT——思考、行动、观察，然后把结果加回上下文继续循环，直到给出最终答案。思考、行动、观察、再思考——AI 就是这样一圈圈跑下来，把复杂任务拆成可控小步。
- **视觉**：
  - region1（reveal 0，fade）：原理编号「原理 ④ ⑤」+ 标题「Agent + REACT」
  - region2（reveal 10，left）：Agent 公式卡「大模型 + 工具 = Agent」+ 注「先思考再行动靠系统提示词，不是训练」
  - region3（reveal 35，top）：REACT 循环图（4 节点：Thought 思考 → Action 行动 → Observation 观察 → 循环 → Final）用环形或方框流程布局，data-reveal 各节点

### 6. instruct（原理⑥ 精准指令 + 人是根本，~85s，1 场景 4 region）
- **目录**：tutorial-e02-instruct
- **narration**（1 seg）：原理六，精准下达指令。前面五条懂了，下指令方式就得变。差的指令：帮我优化一下这个功能——没上下文没目标没验证。好的指令：这个接口慢 SQL 18 秒，附执行计划，目标降到 1 秒内，先分析瓶颈给方案，确认后再改，改完用 EXPLAIN 验证——给现状、明目标、定流程、要验证。一句话：像给聪明的实习生下指令——给够上下文、说清目标、定好流程、要求验证。五条原理讲完，每一条都指向同一结论——AI 放大的是会用 AI 的人。人的能力边界决定 AI 产出上限。人加 AI，人是根本。
- **视觉**：
  - region1（reveal 0，fade）：原理编号「原理 ⑥」+ 标题「精准下达指令」
  - region2（reveal 8，left）：差指令（红，✗「帮我优化一下」）vs 好指令（绿，✓「SQL 18秒→1秒内，先分析后改，EXPLAIN 验证」）对比卡
  - region3（reveal 35，top）：金句「像给聪明的实习生下指令 · 给上下文/明目标/定流程/要验证」
  - region4（reveal 55，fade）：收尾大字「人 + AI · 人是根本」+ 五原理缩略回显（①token②上下文③Agent④REACT⑤指令）

### 7. cta（收尾，~30s，1 场景 3 region）
- **目录**：tutorial-e02-cta
- **narration**（1 seg）：思想跟上了，下一步是落地。下集讲战略启动——怎么向老板要预算、算 ROI、回答老板三个问题。预算批不下来，转型就停在嘴上。合集 12 集，从总纲到六个实施阶段逐集拆，点关注不走丢。教程仓库在评论区，所有原理的详解文档都能看。最后问你：你的团队里，谁还在抗拒 AI，谁已经在用？这差距半年后会变成什么？
- **视觉**：
  - region1（reveal 0，fade）：E03 预告卡「下集 · 战略启动：向老板要预算」（+ ROI/老板三问）
  - region2（reveal 10，top）：合集引导「12 集深度解析 · 点关注不走丢」+ 评论区引导
  - region3（reveal 18，fade）：互动问题「你团队里，谁还在抗拒 AI？谁已经在用？」（中性提问，禁站队）

## 完成判据（每段）

- `final.mp4` 存在 + 时长 ≈ narration 时长 + 0.1s + 有音频轨道
- s6_render `hard_passed: true`（1 场景段应过）
- 无违禁词「第一」、无 fx 划过类、字号≥32、text-shadow 有

## 完成后

各段 final.mp4 齐后，主 agent 拼接 E02-final.mp4（filter concat）+ PIL 验证。
