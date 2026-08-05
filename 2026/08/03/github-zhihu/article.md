# 2026 年第 31 周 GitHub 热门开源项目盘点（7 月 27 日 - 8 月 2 日）

> 本周 GitHub Trending 周榜被一个主题彻底点燃：**AI 编程助手与 Claude Code Skills 生态集体爆发**。19 个上榜项目里，超过一半围绕「让 AI 编程助手更强、更省、更可控」，从阿里开源的代码审查工具，到把技术书变成可调用技能的脚本，再到人和 AI agent 在同一个频道里协作的工作区——AI 正在从「回答问题的工具」变成「干活的同事」。

## 本周趋势速览

| 趋势 | 说明 |
|------|------|
| **最大赢家** | [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book) 以 **+9,298 ★/周** 居首，一本系统讲 AI Agent 的开源书；紧随其后是 [block/buzz](https://github.com/block/buzz) **+9,003 ★/周**，人与 AI agent 共建的工作区 |
| **新面孔** | 2026 年新建项目扎堆涌入：buzz、jcode、i-have-adhd、book-to-skill、ego-lite、openwork、t3code、OmniRoute 等，几乎都是围绕 coding agent 与 skills 的新生力量 |
| **持续热门** | [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat) 连续上榜（iOS 端 +5,737、安卓端 +1,049）；[moeru-ai/airi](https://github.com/moeru-ai/airi)（46.5K ★）和微软 [AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)（58.9K ★）长青 |
| **本周总热度** | 19 个项目合计 **+75,239 ★/周**，覆盖 AI 编程、Skills 生态、AI 接入层、隐私通讯、3D/空间计算、学习资源 6 个方向 |

---

## 一、AI 编程助手 & Agent 工作区

本周的绝对主角。当 AI agent 开始「真的干活」，围绕它的协作空间、代码审查、运行框架和遥控器成了最热的赛道。

### 1. [block/buzz](https://github.com/block/buzz)

**项目简介：** 一个可以自托管的「人与 AI agent 共建」工作区。人和 AI agent 共享同一个频道、同一个房间，底层是一个 Nostr relay——每条消息、每次代码审查、每个 workflow 步骤、每个 git 事件都是一条签名事件，人和 agent 用同一套身份模型和审计轨迹。

**核心亮点：**
- **agent 真正能动手**：进入 Buzz 后，agent 可以开仓库、提交 patch、审查代码、跑 workflow、编辑画布、编排其他 agent、甚至加入语音讨论——拥有和人类队友一样的操作权限，只是用不同的密钥对
- **按身份而非权限位隔离**：agent 有自己的密钥、频道成员资格和审计记录，像给队友分配 scope 一样给 agent 分配作用域，而不是堆权限开关
- **一个频道即一条完整记录**：把功能分支变成一个房间，patch、CI、审查、合并决策都在里面，频道本身就是「这段代码为什么存在」的证据链

**快速上手：** Rust 编写，Apache-2.0 协议，单 relay 部署即可起一个社区，按 URL 区分工作区。详见仓库 `ARCHITECTURE.md`。

**适合人群：** 想让 AI agent 深度参与团队协作、又要把数据攥在自己手里的研发团队。

> Star: 21,064 | Fork: 2,253 | 协议: Apache-2.0 | 语言: Rust | 本周涨幅: +9,003 | 创建于 2026-03

---

### 2. [alibaba/open-code-review](https://github.com/alibaba/open-code-review)

**项目简介：** 阿里巴巴开源的代码审查工具，采用「确定性流水线 + LLM Agent」混合架构，能给出精确到行的审查意见，内置多语言规则集（空指针、线程安全、XSS、SQL 注入等），兼容主流大模型 API。

**核心亮点：**
- **混合架构双保险**：确定性规则兜底常见缺陷（不依赖模型猜测），LLM Agent 处理语义层面的逻辑问题，兼顾稳定性和深度
- **精确到行级评论**：审查意见直接定位到具体代码行，可直接作为 PR review 使用
- **经过阿里规模验证**：在阿里内部大规模实战打磨后开源，规则集覆盖 Java/Go 等后端语言的典型缺陷模式

**快速上手：** Go 编写，Apache-2.0 协议，支持 OpenAI/Anthropic 兼容接口接入模型。详见仓库 README。

**适合人群：** 需要自动化代码审查、又想兼顾规则确定性和 AI 深度的中大型研发团队。

> Star: 17,857 | Fork: 1,207 | 协议: Apache-2.0 | 语言: Go | 本周涨幅: +4,708 | 创建于 2026-05

---

### 3. [1jehuang/jcode](https://github.com/1jehuang/jcode)

**项目简介：** 自称「最省内存的 agent harness」——即运行 coding agent 的底层框架/外壳。在 coding agent 越来越重、内存占用越来越高的当下，主打一个轻量、低资源消耗。

**核心亮点：**
- **内存效率优先**：把 agent harness 的内存占用压到最低，适合长时间挂机、多实例并跑或资源受限的环境
- **Rust 编写**：天然低开销、高性能，契合「轻量」定位
- **聚焦 harness 本身**：不绑定单一模型供应商，作为承载 agent 运行的框架层，可对接多种 coding agent

**快速上手：** Rust 编写，MIT 协议，终端/TUI 形态。详见仓库 README。

**适合人群：** 苦于 coding agent 吃内存、想要一个轻量稳定运行框架的开发者。

> Star: 15,255 | Fork: 1,688 | 协议: MIT | 语言: Rust | 本周涨幅: +3,548 | 创建于 2026-01

---

### 4. [pingdotgg/t3code](https://github.com/pingdotgg/t3code)

**项目简介：** Create T3 Stack 作者 Theo 出品的「agent harness 控制台」——用一个移动 App（iOS/Android）、Web 应用或 Electron 桌面端，统一遥控你本机上已经装好的各种 coding agent。

**核心亮点：**
- **一个面板控多个 agent**：只要本机装好并登录了 Claude Code、Codex、Cursor、Grok Build、OpenCode 等，T3 Code 都能统一操控
- **移动端遥控是杀手锏**：出门在外用手机就能给本机的 agent 派活、看进度，把 coding agent 从桌面解放出来
- **真正开放**：作者强调若方向走偏，用户有足够材料 fork 出自己想要的编辑器，定位是「远程就绪、真正开放」的开发体验

**快速上手：** `npx t3@latest` 免安装试用（需 Node.js 22.16+）；桌面端 Windows 用 `winget install T3Tools.T3Code`，macOS 用 `brew install --cask t3-code`。使用前需先装好并登录至少一个 agent 供应商。

**适合人群：** 同时用多个 coding agent、希望集中管理和移动遥控的开发者。

> Star: 16,341 | Fork: 3,638 | 协议: MIT | 语言: TypeScript | 本周涨幅: +1,439 | 创建于 2026-02

---

## 二、Claude Code Skills 生态

「Skills」（可复用的 AI 技能模块）正在成为 AI 编程工具的新扩展范式。本周多个项目围绕「把东西变成 skill」或「让 agent 输出更顺手」涌入榜单。

### 5. [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)

**项目简介：** 把任意一本技术书的 PDF，转换成一个 Claude Code skill——转换后既能用来系统学习、随时查阅，还能在你写代码时直接调用书里的知识。

**核心亮点：**
- **书 → 可调用技能**：不只是把 PDF 扔进去，而是结构化成 skill，让 AI 在工作时能引用书的内容
- **学习与实操合一**：同一份材料，既能当学习资料读，又能当工作中的知识库查，打通「学」和「用」
- **降低知识搬运成本**：技术书通常是深度知识的最佳载体，把它变成 skill 等于给 AI 装上一个「读过这本书」的外脑

**快速上手：** Python 编写，MIT 协议，输入技术书 PDF 即可生成 skill。详见仓库 README。

**适合人群：** 想把架上技术书的精华变成 AI 可调用知识库的开发者。

> Star: 15,323 | Fork: 1,653 | 协议: MIT | 语言: Python | 本周涨幅: +5,105 | 创建于 2026-05

---

### 6. [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

**项目简介：** 一个改变 coding agent 输出风格的 skill——让 agent 别再把答案「埋」在一大段话里，给出对注意力更友好的结构化输出。

**核心亮点：**
- **直击 AI 输出痛点**：很多人吐槽 AI 回答冗长、重点被埋没，这个 skill 强制 agent 把结论前置、结构清晰
- **小而美的 productivity skill**：不解决复杂技术问题，但显著改善每天最高频的「读 AI 输出」体验
- **Skills 生态多样性的缩影**：从书到输出风格，skill 正在覆盖 AI 工作流的每个环节

**快速上手：** Python 编写，MIT 协议，作为 Claude Code skill 加载。详见仓库 README。

**适合人群：** 觉得 AI 回答太啰嗦、想要更清晰输出结构的所有 AI 工具用户。

> Star: 15,648 | Fork: 874 | 协议: MIT | 语言: Python | 本周涨幅: +5,232 | 创建于 2026-05

---

### 7. [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)

**项目简介：** 面向 AI agent 的浏览器——让 agent 跑浏览器自动化时，能直接复用你已经登录好的浏览器状态，零成本、零配置。定位是「给 AI agent 用的最快浏览器」。

**核心亮点：**
- **共享登录态**：agent 直接用你已登录的浏览器环境，免去反复登录、处理验证码的麻烦
- **不打扰用户**：与 Codex、Claude Code 等 agent 配合时，不会抢占或干扰你正在用的浏览器
- **零配置**：开箱即用，降低 agent 做浏览器自动化的门槛

**快速上手：** JavaScript 编写，MIT 协议，配合主流 coding agent 使用。详见仓库 README。

**适合人群：** 需要 AI agent 操作网页自动化（且要复用登录态）的开发者。

> Star: 7,648 | Fork: 380 | 协议: MIT | 语言: JavaScript | 本周涨幅: +4,090 | 创建于 2026-04

---

### 8. [different-ai/openwork](https://github.com/different-ai/openwork)

**项目简介：** 某闭源 AI 协作工具（Claude Cowork）的开源替代，基于 opencode 构建。让用户用开源方案获得类似的 AI 协作开发体验。

**核心亮点：**
- **开源替代闭环工具**：为不想被单一闭源协作工具锁定的团队提供开源选项
- **站在 opencode 肩上**：基于成熟的 opencode 构建，而非从零造轮子
- **契合本周「开源反攻闭源 AI 工具」的暗线**：从代码审查、agent 工作区到协作工具，开源生态正在系统性地补齐闭源 AI 工具的能力

**快速上手：** TypeScript 编写，协议未声明（NOASSERTION），详见仓库 README 确认许可后再商用。

**适合人群：** 偏好开源 AI 协作工具、注重数据自主的团队。

> Star: 20,278 | Fork: 2,086 | 协议: 未声明 | 语言: TypeScript | 本周涨幅: +2,720 | 创建于 2026-01

---

## 三、AI 接入层 & 多模型 & 创意应用

当模型越来越多，如何统一接入、自由切换，成了新的基建需求；与此同时，AI 也开始渗透到伴侣、虚拟形象等更感性的领域。

### 9. [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)

**项目简介：** 一个免费（MIT）的 AI 网关：一个端点接入 290+ 家模型供应商（其中 90+ 家免费）、500+ 个模型，兼容主流 AI 编程工具（Claude Code、Codex、Cursor、OpenCode、Cline、Copilot 等）。带配额感知的自动故障转移，以及能省 15-95% token 的压缩方案。

**核心亮点：**
- **一个端点统管海量模型**：290+ 供应商、500+ 模型，免去找各家 API、逐个对接的麻烦
- **配额感知自动切换**：某家限流或配额耗尽时自动 fallback，保障可用性
- **token 压缩是真省钱**：15-95% 的 token 节省对高频 AI 调用方是实打实的成本降低
- **500+ 贡献者共建**：社区驱动，生态覆盖广

**快速上手：** TypeScript 编写，MIT 协议，提供 Desktop/PWA，可作为 Claude Code/Codex 等工具的统一后端。详见仓库 README。

**适合人群：** 同时用多家模型、想统一网关 + 降本增效的 AI 重度用户和团队。

> Star: 37,837 | Fork: 4,925 | 协议: MIT | 语言: TypeScript | 本周涨幅: +7,259 | 创建于 2026-02

---

### 10. [andrewyng/aisuite](https://github.com/andrewyng/aisuite)

**项目简介：** 吴恩达（Andrew Ng）开源的轻量库，提供一套简单、统一的接口调用多家生成式 AI 供应商。代码层抽象掉各家 API 差异，换个供应商只需改一行配置。

**核心亮点：**
- **极简统一接口**：一套 API 调多家模型，迁移成本极低
- **吴恩达背书**：来自 AI 教育领域标杆人物，代码质量和教学友好度有保障
- **轻量无负担**：定位是薄薄一层抽象，不引入重框架，适合嵌入现有项目

**快速上手：** Python 编写，MIT 协议，`pip install` 后配置各供应商 API key 即可。详见仓库 README。

**适合人群：** 想低成本试通多家模型、不想被单一供应商锁定的 Python 开发者。

> Star: 15,897 | Fork: 1,683 | 协议: MIT | 语言: Python | 本周涨幅: +584 | 创建于 2024-06

---

### 11. [moeru-ai/airi](https://github.com/moeru-ai/airi)

**项目简介：** 自托管、数据自有的 AI 伴侣/虚拟形象（VTuber）项目。支持实时语音对话，能玩 Minecraft、Factorio，覆盖 Web/macOS/Windows。目标是做出有灵魂感的数字生命。

**核心亮点：**
- **数据完全自有**：自托管，你的 AI 伴侣交互数据不外传
- **能玩游戏的 AI**：不止聊天，还能在 Minecraft、Factorio 里行动，交互维度丰富
- **跨平台 + 实时语音**：Web/桌面端齐全，实时语音对话体验接近真实陪伴
- **社区高度活跃**：46.5K ★，VTuber/数字生命赛道的开源标杆

**快速上手：** TypeScript 编写，MIT 协议，支持 Web/macOS/Windows 自部署。详见仓库 README。

**适合人群：** 想要数据自有的 AI 伴侣、对 VTuber/数字生命感兴趣的开发者和创作者。

> Star: 46,538 | Fork: 4,590 | 协议: MIT | 语言: TypeScript | 本周涨幅: +3,335 | 创建于 2024-12

---

## 四、隐私通讯 & 3D/空间计算 & 学习资源

榜单另一半，是「不卷 AI 也能很硬核」的方向：去中心化加密通讯、3D 建模与生成、地理信息，以及系统化的学习资源。

### 12. [permissionlesstech/bitchat](https://github.com/permissionlesstech/bitchat)（含 [安卓客户端](https://github.com/permissionlesstech/bitchat-android)）

**项目简介：** 去中心化的蓝牙 mesh 聊天应用，IRC 风味。不依赖中心服务器，靠蓝牙在设备间组网传递消息，端到端加密，定位是无网无服务环境下的通讯保障。

**核心亮点：**
- **蓝牙 mesh 自组网**：手机之间直接中继传消息，无需运营商网络或 Wi-Fi，适合户外、灾区、断网场景
- **端到端加密 + Nostr 协议**：消息加密且去中心化，隐私和抗审查性强
- **全平台客户端**：iOS（Swift，34.1K ★）+ 安卓（Kotlin，7.3K ★）双端齐发，本周两端合计 +6,786 ★
- **IRC 复古体验**：怀旧频道文化 + 现代加密，气质独特

**快速上手：** iOS 端 Swift/Unlicense 协议，安卓端 Kotlin/GPL-3.0 协议。详见各仓库 README。

**适合人群：** 注重隐私、关注去中心化通讯、或有断网通讯需求的用户和极客。

> Star: 34,149（iOS）+ 7,257（安卓）| Fork: 5,454 + 1,788 | 协议: Unlicense / GPL-3.0 | 语言: Swift / Kotlin | 本周涨幅: +6,786（合计）| 创建于 2025-07

---

### 13. [pascalorg/editor](https://github.com/pascalorg/editor)

**项目简介：** 创建并分享 3D 建筑项目的工具。让用户在浏览器里搭建、编辑三维建筑方案并分享，降低 3D 建筑设计的门槛。

**核心亮点：**
- **3D 建筑「所见即所得」**：把专业 3D 建模能力做成更易上手的编辑器
- **创建 + 分享一体**：不只是建模，还能把项目分享出去，带社区属性
- **Web 端 TypeScript**：浏览器即开即用，无需安装重型建模软件

**快速上手：** TypeScript 编写，MIT 协议，浏览器端使用。详见仓库 README。

**适合人群：** 建筑/空间设计从业者、3D 爱好者，以及想快速搭建建筑方案原型的人。

> Star: 20,732 | Fork: 2,662 | 协议: MIT | 语言: TypeScript | 本周涨幅: +3,028 | 创建于 2025-10

---

### 14. [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)

**项目简介：** 一组面向 CAD、CAE、CAM 的 agent skills 库。用文字描述需求，生成可用于工业设计的 CAD 模型与工程文件。

**核心亮点：**
- **文字直出工业级模型**：从自然语言到 CAD/CAE/CAM，覆盖机械工程、机器人等硬核领域
- **Skills 库形态**：可组合、可复用的技能集合，适配 agent 工作流
- **打通 AI 与实体制造**：把生成式 AI 的能力延伸到工业设计与制造的链路

**快速上手：** JavaScript 编写，MIT 协议，作为 agent skills 加载。详见仓库 README。

**适合人群：** 机械工程师、机器人开发者、工业设计从业者。

> Star: 12,503 | Fork: 1,326 | 协议: MIT | 语言: JavaScript | 本周涨幅: +2,009 | 创建于 2026-04

---

### 15. [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)

**项目简介：** 微软研究院的 3D 生成项目，主打「原生且紧凑的结构化潜空间」（Native and Compact Structured Latents for 3D Generation）。用更紧凑的表示方法做高质量的 3D 资产生成。

**核心亮点：**
- **紧凑潜空间**：用更高效的中间表示做 3D 生成，兼顾质量与效率
- **微软研究院出品**：前沿 3D 生成研究的开源延续（TRELLIS 系列的第二代）
- **学术 + 工程价值**：既是研究参考，也推动 3D 生成走向实用

**快速上手：** Python 编写，MIT 协议，适合有 GPU 环境的研究者与开发者。详见仓库 README。

**适合人群：** 3D 生成研究者、计算机图形学开发者、AIGC 方向工程师。

> Star: 10,147 | Fork: 1,219 | 协议: MIT | 语言: Python | 本周涨幅: +898 | 创建于 2025-11

---

### 16. [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre)

**项目简介：** 轻量级、云原生的 GIS（地理信息系统）平台，用于地理数据的可视化、探索与分析。能在浏览器、桌面、移动端和 Jupyter notebook 里运行。

**核心亮点：**
- **全端覆盖**：Web/桌面/移动/Jupyter 四端通吃，地理数据随处可用
- **轻量 + 云原生**：基于 DuckDB、MapLibre、Tauri 等现代栈，轻量高效
- **降低 GIS 门槛**：把传统笨重的 GIS 工具做成轻量现代版，让更多开发者能用上地理分析

**快速上手：** TypeScript 编写，MIT 协议，Tauri 应用形态。详见仓库 README。

**适合人群：** 地理/空间数据分析师、GIS 开发者、数据科学家。

> Star: 4,970 | Fork: 498 | 协议: MIT | 语言: TypeScript | 本周涨幅: +2,951 | 创建于 2026-05

---

### 17. [microsoft/AI-For-Beginners](https://github.com/microsoft/AI-For-Beginners)

**项目简介：** 微软出品的 AI 入门课程，12 周 24 节课，覆盖 CNN、RNN、GAN、NLP、计算机视觉等深度学习核心主题。面向所有想系统学 AI 的学习者。

**核心亮点：**
- **体系化课程**：12 周 24 课，从基础到前沿，结构完整
- **微软背书 + 长青**：2021 年开源至今 58.9K ★，持续维护，质量稳定
- **面向所有人**：标题就是「AI for All」，门槛友好，适合自学和教学

**快速上手：** Jupyter Notebook 形式，MIT 协议，直接 clone 仓库按周学习。详见仓库 README。

**适合人群：** AI/深度学习零基础学习者、想系统补课的开发者、教学者。

> Star: 58,933 | Fork: 11,593 | 协议: MIT | 语言: Jupyter Notebook | 本周涨幅: +3,246 | 创建于 2021-03

---

### 18. [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)

**项目简介：** 《深入理解 AI Agent：设计原理与工程实践》（李博杰 著）的开源主仓库，包含全书正文、编译版 PDF 与按章配套代码。本周涨幅榜首（+9,298 ★）。

**核心亮点：**
- **系统讲透 AI Agent**：从设计原理到工程实践，覆盖 agent 记忆、上下文工程、多 agent、RAG、强化学习等核心议题
- **书 + 代码一体**：不只是电子书，按章配代码，边读边练
- **中文社区的 AI Agent 权威读本**：填补了中文世界系统讲 agent 工程的空白，热度反映刚需

**快速上手：** Python 配套代码，Apache-2.0 协议，仓库内可直接读正文或下载编译版 PDF。详见仓库 README。

**适合人群：** 想系统理解 AI Agent 设计与工程实践的开发者、架构师。

> Star: 29,872 | Fork: 3,183 | 协议: Apache-2.0 | 语言: Python | 本周涨幅: +9,298 | 创建于 2025-09

---

## 本周总结

本周 GitHub 周榜传递出一个清晰信号：**AI 编程工具的竞争，已经从「谁的模型强」升级到「谁的工程化生态完整」**。

围绕 coding agent，从底层运行框架（jcode 省内存）、到代码审查（阿里 open-code-review）、到统一遥控（t3code 移动端）、到人机协作工作区（buzz），整条链路都在被开源重塑；而 Skills 生态（book-to-skill、i-have-adhd、ego-lite）说明 AI 工具的扩展方式正在标准化——「能力」正变成可插拔的模块。

如果只关注两个项目，我的建议是：
1. **[block/buzz](https://github.com/block/buzz)** — 它代表了「AI agent 作为同事」的终极形态，人和 agent 在同一套协作体系里干活，值得所有重视 AI 协作的团队研究其架构思路。
2. **[bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)** — 想真正搞懂 agent 工程而非停留在调 API，这本开源书是目前中文世界最系统的入门到进阶路径。

至于工具选型上，[diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)（统一 AI 网关 + token 压缩）和 [alibaba/open-code-review](https://github.com/alibaba/open-code-review)（混合架构代码审查）是最快能落地产生价值两个。

---

> **数据来源：** GitHub Trending Weekly 页面（2026-08-03 抓取）+ GitHub API（`gh api` 实时校验 Star/Fork/协议/活跃度）。周涨幅以 Weekly 页面为准，总星数以 GitHub API 实时数据为准。两个数据源项目交集 100%（19/19），全部项目 30 天内有更新。本文不点名商业品牌产品，项目描述忠实于各仓库原始 description。
