# 2026年7月第30周 GitHub 热门开源项目盘点

> 本周 GitHub Trending Weekly 榜单被"AI Skills 生态"和"AI 编程智能体"两股力量同时点燃——十几个项目里近一半围绕 Claude Code、Codex 等 AI 编程工具做技能包与基础设施，开源视频剪辑工具 OpenCut 单周涨星 1.27 万再创热度新高。

## 本周趋势速览

| 趋势 | 说明 |
|------|------|
| 最大赢家 | [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut) 本周涨星 **+12,743**，开源视频剪辑工具持续吸引关注 |
| 新面孔 | [Nutlope/hallmark](https://github.com/Nutlope/hallmark)（去 AI 味设计技能，4 月新建，本周 +9,193）、[iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)（专为 AI Agent 设计的 Office 套件）、[kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)（内容蒸馏为 Agent Skills） |
| 持续热门 | [mattpocock/skills](https://github.com/mattpocock/skills) 本周再涨 **+10,983**，总星 17.7 万；[openai/codex](https://github.com/openai/codex)、[openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter) 维持高位 |
| 领域集中 | 14 个上榜项目里，AI/Agent 相关项目占 10 个以上，"Skills for AI Agents" 成为本周最显著的主题 |

---

## 项目详细解读

### AI 编程智能体（Coding Agents）

本周终端侧 AI 编程智能体赛道持续升温，三个项目分别代表了"商业模型原生支持"、"开源模型友好"和"工具链统一"三种思路。

#### 1. [openai/codex](https://github.com/openai/codex)

**项目简介：** 一个轻量级的终端 AI 编程智能体，用 Rust 编写，可以在命令行环境中直接帮你读写代码、跑测试、提交 PR。它的定位不是 IDE 替代品，而是"在终端里就能调用的 AI 程序员"。

**核心亮点：**
- **Rust 实现 + 单二进制部署** — 相比 Node/Python 写的同类，启动快、内存占用低，安装即用，无需依赖运行时
- **终端原生 workflow** — 直接在你已有的 shell 环境里工作，配合 tmux、vim、git 等工具链无缝衔接，符合资深开发者的肌肉记忆
- **沙箱执行模型** — 命令执行有权限隔离，避免 AI 直接破坏系统，企业内部部署的合规友好性更高

**快速上手：**

```bash
# macOS / Linux
brew install codex
# 或下载 release 二进制
codex --help
codex "把这个项目里的 console.log 都改成结构化日志"
```

**适合人群：** 习惯终端工作流的资深后端/系统开发者，希望把 AI 编程嵌入既有 CLI 工具链而不是切到 IDE 里

> Star: 99,717 | Fork: 14,921 | 协议: Apache-2.0 | 语言: Rust | 本周涨幅: +2,361

---

#### 2. [openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)

**项目简介：** 一个面向开源大模型的编程智能体，新版用 Rust 重写。它能让开源模型（如 Kimi、DeepSeek、Qwen 等）在你的本地或远程机器上完成代码编写、命令执行、文件操作等任务，强调"不被任何商业模型绑定"。

**核心亮点：**
- **开源模型优先** — 原生支持 Kimi K3、DeepSeek、Qwen 等开源模型，对希望用自托管或国产模型的团队友好
- **Rust 重写后性能显著提升** — 旧版 Python 实现启动慢、依赖重，新版单二进制启动毫秒级
- **跨平台执行** — 同一个 Agent 既能跑代码、操作文件，也能控制浏览器、调用系统 API，覆盖完整的开发任务链

**快速上手：**

```bash
# 安装
curl -sSf https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/install.sh | sh
# 配置开源模型（以 Kimi K3 为例）
export OPENINTERPRETER_MODEL=kimi-k3
oi "帮我把这个 CSV 文件按日期排序并画一张折线图"
```

**适合人群：** 倾向使用开源/国产大模型、对数据出境有顾虑的团队，以及希望深度定制 Agent 行为的研究者

> Star: 66,842 | Fork: 5,741 | 协议: Apache-2.0 | 语言: Rust | 本周涨幅: +2,498

---

#### 3. [earendil-works/pi](https://github.com/earendil-works/pi)

**项目简介：** 一套面向 AI Agent 的工具包，把"统一 LLM API、Agent 循环、TUI 终端界面、编程智能体 CLI"四件事打包到一个项目里。你可以把它理解成"自建 Codex/Claude Code 的脚手架"。

**核心亮点：**
- **统一 LLM 抽象层** — 一份代码同时调用 OpenAI、Anthropic、本地模型，切换模型只改一个参数
- **Agent 循环可定制** — 提供完整的 ReAct/Plan-Execute 循环实现，方便研究者做实验、企业做定制工作流
- **TUI + CLI 双形态** — 既可交互式聊天，也可作为命令行工具嵌入脚本，覆盖"探索"和"自动化"两种使用场景

**快速上手：**

```bash
git clone https://github.com/earendil-works/pi
cd pi
cargo build --release
./target/bin/pi chat      # 交互式 TUI
./target/bin/pi run "修复 src/ 下的所有 lint 警告"
```

**适合人群：** 想自建 Agent 平台的工程团队、做 Agent 框架研究的开发者

> Star: 72,802 | Fork: 8,988 | 协议: MIT | 语言: TypeScript | 本周涨幅: +2,854

---

### AI Skills 生态（Skills for AI Agents）

本周最值得关注的趋势：围绕 Claude Code / Codex 等 AI 编程工具的"Skills 技能包"生态集体爆发。四个项目从不同角度（设计、工程实践、UI、知识蒸馏）补全了 AI Agent 的能力短板。

#### 4. [Nutlope/hallmark](https://github.com/Nutlope/hallmark)

**项目简介：** 一个"去 AI 味"设计技能包，专为 Claude Code、Cursor、Codex 等 AI 编程工具设计。它把"怎样让 AI 生成的界面不像 AI 生成"这件事沉淀成可加载的 skill 文件，让 AI 在写前端时遵循更"人类"的设计规则。

**核心亮点：**
- **直击 AI 生成内容的痛点** — AI 生成的前端常被吐槽"千篇一律的渐变 + 圆角 + emoji"，这个 skill 把"反 AI slop"的设计规则打包进 AI 编程流程
- **跨工具兼容** — 同时支持 Claude Code、Cursor、Codex，不绑定单一平台
- **CSS 主题化的设计语言** — 不只是规则文档，还包含可直接复用的设计 token 和组件样式

**快速上手：**

```bash
git clone https://github.com/Nutlope/hallmark
cd hallmark
# 把 skill 文件复制到你的 AI 工具配置目录
cp -r skills/* ~/.claude/skills/
# 在 Claude Code / Cursor / Codex 中加载，让 AI 自动遵循 hallmark 设计规则
```

**适合人群：** 经常用 AI 编程工具写前端、对"AI 味"介意的开发者与设计师

> Star: 13,411 | Fork: 677 | 协议: MIT | 语言: CSS | 本周涨幅: +9,193（本周新建项目中涨幅居首）

---

#### 5. [mattpocock/skills](https://github.com/mattpocock/skills)

**项目简介：** 知名 TypeScript 教育者 Matt Pocock 公开的个人 AI Agent skills 集合，"来自我的 .agents 目录"。每个 skill 都是一份经过实战打磨的提示词模板 + 工作流定义，覆盖代码审查、类型推导、测试生成等工程实践场景。

**核心亮点：**
- **真实生产环境的 skills** — 不是 demo，是作者每天用的工具，已经过反复迭代打磨
- **TTOS 强类型实践** — 作者本人是 TypeScript 顶级教育者，skills 在类型推导、类型体操等场景的质量显著高于通用模板
- **可直接 fork 改造** — MIT 协议，鼓励开发者 fork 出自己团队的 skills 库

**快速上手：**

```bash
git clone https://github.com/mattpocock/skills
# 浏览目录结构，挑选需要的 skill
ls skills/
# 把某个 skill 链接到 Claude Code 的 skills 目录
ln -s $(pwd)/skills/typescript-pro-tips ~/.claude/skills/
```

**适合人群：** TypeScript 开发者、想构建自己团队 Agent skills 库的工程负责人

> Star: 177,573 | Fork: 15,218 | 协议: MIT | 语言: Shell | 本周涨幅: +10,983（总星本周最高）

---

#### 6. [ibelick/ui-skills](https://github.com/ibelick/ui-skills)

**项目简介：** 面向 Design Engineer（设计工程师）的 AI Skills 集合，聚焦 UI/UX 设计与前端工程的交叉领域。它解决的问题是"让 AI 编程工具理解设计系统"——色板、间距、动效曲线、组件 token 等设计语言如何被 AI 正确使用。

**核心亮点：**
- **填补设计 × 工程的中间地带** — 市面大部分 skills 偏纯工程或纯设计，UI Skills 把 Design Token → 前端实现这条链路打通
- **配合 Tailwind / Radix / shadcn 等主流栈** — 落地即用，无需重新设计技术栈
- **每周更新的活项目** — 作者持续投入，issues 响应快，社区活跃度健康

**快速上手：**

```bash
git clone https://github.com/ibelick/ui-skills
cd ui-skills
# 按需引入特定 skill 到 Claude Code / Cursor
cp skills/design-system-tokens.md ~/.claude/skills/
```

**适合人群：** Design Engineer、前端团队负责人、构建内部设计系统的团队

> Star: 5,442 | Fork: 232 | 协议: MIT | 语言: TypeScript | 本周涨幅: +1,669

---

#### 7. [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)

**项目简介：** 把书、长视频、播客等"高价值长内容"蒸馏成可执行的 Agent Skills。它做的是知识工程化——把零散学习资料转成结构化的提示词和工作流，让 AI 在处理同类任务时有"积累的经验"可参考。

**核心亮点：**
- **从消费到生产的闭环** — 不是单纯总结一本书，而是把书里的方法论转成 AI 能直接执行的 skill 文件
- **支持多源输入** — 书籍、长视频、播客、技术文档都能作为原料，覆盖知识工作者的主流输入渠道
- **中文社区原生项目** — 文档与示例对中文场景友好，避免了直接套用海外框架时的语境错位

**快速上手：**

```bash
pip install cangjie-skill
# 把一份长内容蒸馏为 skill
cangjie distill --input my-podcast.mp3 --output skills/
# 加载到 Claude Code 自动使用
```

**适合人群：** 知识工作者、内容创作者、希望把学习沉淀复用到 AI 工作流的开发者

> Star: 3,841 | Fork: 540 | 协议: MIT | 语言: Python | 本周涨幅: +1,284

---

### AI 应用与教学

#### 8. [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)

**项目简介：** 一个收录了 100 多个"可直接运行"的 AI Agent 与 RAG 应用合集。与多数 awesome 列表只放链接不同，这里每个项目都附完整代码、可克隆、可改造、可上线，是上手 LLM 应用开发的高质量脚手架库。

**核心亮点：**
- **100+ 真实可运行应用** — 不是 demo 集合，是经过测试的完整项目，克隆下来 `pip install` 就能跑
- **覆盖主流场景** — 客服、研究助手、文档问答、代码审查、数据分析等典型 LLM 应用场景都有参考实现
- **支持多模型多框架** — OpenAI / Anthropic / 开源模型 + LangChain / LlamaIndex / 自研框架都有示例

**快速上手：**

```bash
git clone https://github.com/Shubhamsaboo/awesome-llm-apps
cd awesome-llm-apps
# 浏览感兴趣的分类
ls apps/
# 进入某个应用，按 README 安装运行
cd apps/customer-support-bot
pip install -r requirements.txt
python main.py
```

**适合人群：** LLM 应用初学者、需要快速搭建原型的产品经理、寻找参考实现的工程团队

> Star: 124,578 | Fork: 18,397 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +6,211

---

#### 9. [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)

**项目简介：** 香港大学数据科学研究院（HKUDS）开源的"终身个性化辅导"AI 智能体。它结合 RAG、多智能体协作和深度研究（DeepResearch）能力，定位是"长期陪你学习的 AI 家教"，而非一次性问答机器人。

**核心亮点：**
- **学术研究背书** — HKUDS 是港大的 AI 研究团队，方法论有论文支撑，工程实现严谨
- **长期记忆 + 个性化** — 会记住你之前学过什么、卡在哪里，下一次对话能基于历史上下文继续推进
- **CLI 工具形态** — 命令行即可调用，方便集成到学习工作流（如 Anki、Obsidian 等）

**快速上手：**

```bash
pip install deeptutor
deeptutor init --api-key YOUR_KEY
deeptutor chat "帮我从零开始系统学习线性代数，每周 3 小时"
```

**适合人群：** 自学者、需要长期 AI 学习伙伴的学生、研究个性化教学的教育工作者

> Star: 27,954 | Fork: 3,705 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +2,375

---

### 开发者工具与基础设施

#### 10. [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)

**项目简介：** 一个本地优先（local-first）的代码智能图谱工具，给 MCP 和 CLI 用。它会为你的整个代码库构建持久化的知识图谱，让 AI 编程工具在 review 代码或处理大型仓库时，只读取真正相关的部分，大幅降低 token 消耗。

**核心亮点：**
- **本地优先 + 隐私可控** — 图谱构建在本地，代码不外传，对闭源/企业项目友好
- **基准验证的上下文压缩** — 在代码 review 和大仓库工作流上有 benchmark 数据，平均能减少显著比例的无关上下文
- **MCP 协议兼容** — 直接接入 Claude Code、Cursor 等支持 MCP 的 AI 工具，无需切换工作流

**快速上手：**

```bash
pip install code-review-graph
# 在项目根目录构建代码图谱
crg build .
# 启动 MCP 服务供 Claude Code 调用
crg serve --mcp
# 在 Claude Code 配置 MCP server 指向 localhost:8080 即可
```

**适合人群：** 在大型代码库工作的资深工程师、追求 AI 工具调用效率与隐私的团队

> Star: 21,317 | Fork: 2,187 | 协议: MIT | 语言: Python | 本周涨幅: +1,103

---

#### 11. [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)

**项目简介：** 专为 AI Agent 设计的 Office 套件命令行工具，可让 AI 智能体读写、自动化操作 Word、Excel、PowerPoint 文件。免费、开源、单二进制部署，**不需要本机安装 Office**。

**核心亮点：**
- **零依赖单二进制** — C# 编写，跨平台，部署门槛低，企业内部下发方便
- **绕开 Office 安装** — 传统方案要么装 Office 要么用 LibreOffice，OfficeCLI 用纯代码处理 docx/xlsx/pptx，CI/CD 友好
- **AI Agent 原生 API** — 输入输出对 LLM 友好，让 Agent 能直接生成报表、改合同、做 PPT

**快速上手：**

```bash
# 下载 release 二进制
curl -L https://github.com/iOfficeAI/OfficeCLI/releases/latest/download/officecli-linux -o officecli
chmod +x officecli
./officecli excel --input template.xlsx --output report.xlsx \
  --set "A1=本月营收" "B1=123456"
./officecli word --input contract.docx --replace "{{client}}"="Acme Corp"
```

**适合人群：** 做 RPA / 自动化办公的工程师、需要让 AI Agent 处理 Office 文件的开发者

> Star: 19,683 | Fork: 1,323 | 协议: Apache-2.0 | 语言: C# | 本周涨幅: +4,269

---

### 开源创作工具

#### 12. [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)

**项目简介：** 一款开源的视频剪辑工具，定位是商业剪辑软件的开源替代。基于 TypeScript 与 Web 技术栈构建，可运行在浏览器与桌面端，让用户在不依赖闭源商业软件的前提下完成视频创作。

**核心亮点：**
- **纯 Web 技术栈 + 跨平台** — 同一份代码既能跑浏览器也能打包桌面应用，降低分发与维护成本
- **活跃的社区与快速迭代** — 总星 7.5 万，本周再涨近 1.3 万，issues 与 PR 响应迅速，处于高速演进期
- **面向创作者的功能设计** — 时间线、轨道、转场、字幕、特效等核心剪辑能力齐全，对短视频/中视频创作者友好

**快速上手：**

```bash
git clone https://github.com/OpenCut-app/OpenCut
cd OpenCut
pnpm install
pnpm dev        # 本地开发预览
pnpm build      # 构建生产版本
# 或直接使用官方在线版，无需本地安装
```

**适合人群：** 短视频/中视频创作者、希望摆脱闭源剪辑软件的内容团队、做视频工具开发的工程师

> Star: 75,907 | Fork: 7,629 | 协议: MIT | 语言: TypeScript | 本周涨幅: +12,743（本周涨幅最高）

---

## 本周总结

本周 GitHub Trending 释放出一个清晰信号：**"Skills for AI Agents" 正在从概念走向工程化**。当 Claude Code、Codex 等 AI 编程智能体的底层能力趋于稳定后，开发者社区的注意力开始上移——如何把设计经验、工程实践、领域知识封装成 AI 可加载的 skill 文件，已经成为新的赛道（hallmark / mattpocock.skills / ui-skills / cangjie-skill 集中上榜即为例证）。

如果只关注两个项目，我的推荐是：

1. **[OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)** — 本周涨幅居首（+12,743），开源视频剪辑工具赛道正在被全球创作者重新关注，无论你是用户还是想做类似产品的开发者，都值得跟踪它的演进
2. **[Nutlope/hallmark](https://github.com/Nutlope/hallmark)** — 它代表了一个全新品类的诞生："为 AI 编程工具定制的能力包"，跨工具兼容、直击"AI 味"这一具体痛点，是这个赛道早期项目的优秀样本

下周值得继续观察的方向：Skills 生态是否会进一步分化出垂直领域（如后端架构 skill、安全审计 skill），以及 AI 编程智能体赛道是否会出现新的 Rust 重写选手。

---

> **数据来源：** GitHub Trending Weekly（数据采集时间 2026-07-20，含 GitHub API 实时数据补全）。周涨幅以 Weekly 页面统计为准，Star/Fork/Issues 等数据通过 `gh api` 实时拉取。文中项目均按本榜单客观数据呈现，不构成投资或购买建议。
