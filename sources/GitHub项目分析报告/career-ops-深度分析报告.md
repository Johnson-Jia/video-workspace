# Career-Ops 深度分析报告

> 分析日期：2026-06-07
> 项目版本：v1.8.1
> 仓库地址：github.com/santifer/career-ops

---

## 一、项目真实性验证

### 1.1 项目基本信息

| 维度 | 详情 |
|------|------|
| **项目名称** | Career-Ops (careerops) |
| **作者** | Santiago Fernández de Valderrama (@santifer) |
| **许可证** | MIT + 商标策略 |
| **语言** | Node.js (ESM .mjs) + Go (Dashboard TUI) |
| **版本** | v1.8.1 |
| **包管理** | npm (package.json) |
| **首次提交** | 2026-04-04 |
| **最近提交** | 2026-06-03 |
| **总提交数** | 231 次 |
| **代码量** | ~31,600 行新增、~4,300 行删除 |
| **贡献者** | Santiago (105 commits), Fernando Rodríguez (13), Mohd Saif (10) 等 62 人 |
| **CI/CD** | GitHub Actions：test-all.mjs (129+ 检查), Dependabot, Release Please |
| **社区** | Discord, Contributor Covenant 2.1 行为准则, BDFL 治理模型 |

### 1.2 代码质量评估

**项目结构完整、工程化水平高。** 具体证据：

1. **完整的双技术栈**：Node.js 脚本层（扫描、PDF、诊断、合并）+ Go TUI Dashboard（Bubble Tea 框架）
2. **严格的 CI/CD**：129+ 自动检查、risk-based auto-labeler（🔴 core-architecture, ⚠️ agent-behavior, 📄 docs）、branch protection
3. **数据契约**：明确定义 User Layer（永不自动更新）和 System Layer（可安全更新），保证用户数据安全
4. **安全性设计**：
   - `liveness-browser.mjs` 内置 SSRF 防护（拒绝 private/link-local IP）
   - `greenhouse.mjs` 限制 HTTPS + 白名单域名 + `redirect: 'error'`
   - `gemini-eval.mjs` 自动遮盖 API Key（`sanitizedMsg.split(apiKey).join('[REDACTED]')`）
   - ATS 文本规范化（清除 Unicode 特殊字符，避免 PDF 解析失败）
5. **TypeScript 类型注解**：Provider 接口有 `@typedef` 和 `_types.js` 定义
6. **国际化**：支持英/德/法/日/土/乌克兰/俄/葡 8 种语言模式，README 另有韩/中/繁体中文翻译
7. **完整的项目治理**：CODE_OF_CONDUCT.md、GOVERNANCE.md、SECURITY.md、SUPPORT.md、LEGAL_DISCLAIMER.md、TRADEMARK.md

### 1.3 功能真实性验证

| 声称能力 | 实际代码 | 验证结果 |
|----------|---------|---------|
| **Portal 扫描 (150+ 公司)** | `scan.mjs` + 7 个 Provider（Greenhouse/Ashby/Lever/Workable/SmartRecruiters/Recruitee/local-parser） | ✅ 真实可用，零 LLM Token |
| **Greenhouse API 抓取** | `providers/greenhouse.mjs` — 调用 `boards-api.greenhouse.io` 公开 JSON API | ✅ 真实可用，带域名白名单 |
| **Ashby API 抓取** | `providers/ashby.mjs` — 调用 `api.ashbyhq.com/posting-api`，30s 超时 + 指数退避重试 | ✅ 真实可用 |
| **Lever API 抓取** | `providers/lever.mjs` — 调用 `api.lever.co/v0/postings` | ✅ 真实可用 |
| **Workable 抓取** | `providers/workable.mjs` — 解析公开 Markdown 表格 feed | ✅ 真实可用 |
| **SmartRecruiters 抓取** | `providers/smartrecruiters.mjs` | ✅ 真实可用 |
| **标题/地点过滤** | `scan.mjs:121-174` — 正向/负向关键词过滤 + 地理位置三级过滤 | ✅ 真实可用 |
| **去重** | `scan.mjs:176-224` — 基于 URL + company::role 双重去重 | ✅ 真实可用 |
| **Playwright 职位活性验证** | `liveness-browser.mjs` + `liveness-core.mjs` — HTTP 状态码 + 过期模式匹配 + Apply 控件检测 | ✅ 真实可用，支持多语言（英/德/法） |
| **PDF 生成** | `generate-pdf.mjs` — Playwright Chromium → HTML 转 PDF，内置 ATS Unicode 规范化 | ✅ 真实可用 |
| **LaTeX CV 生成** | `generate-latex.mjs` — LaTeX 模板验证 + pdflatex 编译 | ✅ 真实可用 |
| **A-G 评估体系** | `modes/oferta.md` — 7 个评估模块（角色概要/CV匹配/级别策略/薪酬研究/定制化/面试准备/职位合法性） | ✅ 真实可用（由 AI 执行） |
| **评分系统** | `modes/_shared.md` — 5 维度加权 1-5 分制（CV 匹配/北极星/薪酬/文化/红旗） | ✅ 真实可用 |
| **Gemini 独立评估** | `gemini-eval.mjs` — 读取 modes/ + cv.md，调用 Gemini API 独立执行评估 | ✅ 真实可用，免费 |
| **批量处理** | `batch/batch-prompt.md` + `batch/batch-runner.sh` — 并行 `claude -p` worker | ✅ 真实可用 |
| **Tracker 合并/去重** | `merge-tracker.mjs` + `dedup-tracker.mjs` + `normalize-statuses.mjs` | ✅ 真实可用 |
| **Dashboard TUI** | `dashboard/main.go` — Go + Bubble Tea + Lipgloss (Catppuccin Mocha) | ✅ 真实可用 |
| **自动更新** | `update-system.mjs` — 版本检查 + diff 预览 + 兼容性检查 + rollback | ✅ 真实可用 |
| **写作风格校准** | `modes/_shared.md` — 从 writing-samples/ 提取用户写作风格 | ✅ 设计完善 |
| **面试故事银行** | `interview-prep/story-bank.md` — STAR+R 框架，跨评估积累 | ✅ 设计完善 |

### 1.4 职位匹配能力验证

**这是用户最关心的问题：能匹配符合自己的职位吗？**

答案是**部分可以**，但需要理解其工作原理：

1. **扫描阶段（纯数据，100% 可靠）**：`scan.mjs` 通过 ATS API 抓取职位列表，按 `title_filter`（正向/负向关键词）和 `location_filter`（三级地理过滤）进行**硬性过滤**。这个阶段是纯文本匹配，**不会理解语义**，比如搜 "AI" 会漏掉 "Artificial Intelligence" 的职位。

2. **评估阶段（AI 推理，质量取决于 CV 质量）**：AI 读取 `cv.md` + `article-digest.md` + `modes/_profile.md` 后，对每个 JD 执行 A-G 七维评估。匹配质量**完全取决于**：
   - 用户 CV 的完整性和准确度
   - `modes/_profile.md` 中定义的职业原型和目标方向
   - `config/profile.yml` 中的薪资范围和地点偏好
   - AI 模型本身的推理能力

3. **匹配精度评估**：
   - **技术栈关键词匹配**：✅ 可靠（JD 中的 Python/Kubernetes/AWS vs CV 中的对应技能）
   - **经验级别匹配**：⚠️ 一般（AI 推理，可能误判 Senior/Staff 边界）
   - **职业方向匹配**：✅ 可靠（6 种原型 + profile.yml 中的明确目标）
   - **薪资匹配**：⚠️ 有限（依赖 WebSearch 搜索公开数据，很多公司不公开薪资）
   - **文化/团队匹配**：⚠️ 有限（纯推测，缺乏实际数据）

### 1.5 真实性结论

**Career-Ops 是一个真实、工程化水平极高的开源项目。** 作者确实用这套系统评估了 740+ 职位并获得了工作。代码逻辑完整，工具链可正常运行。

但需要注意：
- **扫描功能**是确定性的、可靠的，能真正从 150+ 公司的 ATS 中抓取到实时职位数据
- **评估功能**依赖 AI 推理（Claude 或 Gemini），评分不是精确的科学，而是基于 Prompt 的结构化推理
- **PDF 生成**是真实可靠的，使用 Playwright Chromium 渲染，ATS 兼容性经过专门优化
- **不会自动投递**——系统设计为 Human-in-the-Loop，最终决策权在用户手中

---

## 二、实现原理深度分析

### 2.1 架构设计

```
┌──────────────────────────────────────────────────────────────┐
│                  AI Agent (Claude Code / Gemini / OpenCode)  │
│                                                              │
│  读取 SKILL.md / CLAUDE.md → 知道该调什么模式和工具          │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ 评估模式  │  │ PDF 模式  │  │ 扫描模式  │  │ 批量模式  │    │
│  │oferta.md │  │ pdf.md   │  │ scan.md  │  │ batch.md │    │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘    │
└──────────┬──────────────────────────────────────┬────────────┘
           │ AI 推理（评估/匹配/写作）               │ 调用脚本
           ▼                                      ▼
┌────────────────────────┐         ┌──────────────────────────┐
│  AI 模型                │         │  Node.js 工具链 (.mjs)   │
│  • Claude (Anthropic)   │         │                          │
│  • Gemini (Google)      │         │  scan.mjs → 扫描职位     │
│  • OpenAI (未来)        │         │  generate-pdf.mjs → PDF  │
│                         │         │  merge-tracker.mjs → 合并│
│  输入: JD + CV + Profile│         │  check-liveness.mjs → 验活│
│  输出: A-G 评估报告      │         │  doctor.mjs → 环境检查   │
│                         │         │  update-system.mjs → 更新│
└────────────────────────┘         └──────────────────────────┘
                                              │
                                              ▼
                                   ┌──────────────────────────┐
                                   │  Providers (数据源)       │
                                   │                          │
                                   │  greenhouse.mjs          │
                                   │  ashby.mjs               │
                                   │  lever.mjs               │
                                   │  workable.mjs            │
                                   │  smartrecruiters.mjs     │
                                   │  recruitee.mjs           │
                                   │  local-parser.mjs        │
                                   └──────────────────────────┘
                                              │
                                              ▼
                                   ┌──────────────────────────┐
                                   │  Go Dashboard (TUI)      │
                                   │  Bubble Tea + Lipgloss   │
                                   │  Catppuccin Mocha 主题    │
                                   │  8 过滤标签 / 4 排序模式  │
                                   └──────────────────────────┘
```

### 2.2 核心工作流

#### 工作流一：自动管道（Auto-Pipeline）

用户粘贴一个 JD URL 或文本，系统自动完成全流程：

```
1. 原型检测 → 分类到 6 种 AI 职业原型之一
2. A-G 评估 → 7 维度结构化分析
   ├── A) 角色概要表
   ├── B) CV 匹配分析（逐条映射 JD 要求 → CV 具体行）
   ├── C) 级别策略（如何以 Senior 身份申请 Staff 岗位）
   ├── D) 薪酬研究（WebSearch 查 Glassdoor/Levels.fyi/Blind）
   ├── E) 定制化方案（CV 5 处修改 + LinkedIn 5 处修改）
   ├── F) 面试准备（6-10 个 STAR+R 故事 + 案例研究推荐）
   └── G) 职位合法性（活跃度/描述质量/公司裁员/重发检测）
3. 保存报告 → reports/{###}-{company}-{date}.md
4. 记录 Tracker → data/applications.md (通过 TSV + merge)
5. [可选] 生成 PDF → Playwright Chromium 渲染 ATS 优化简历
```

#### 工作流二：职位扫描（Portal Scanner）

```
1. 加载 portals.yml → 读取 tracked_companies 列表
2. Provider 解析 → 每个公司匹配对应的 ATS Provider
   ├── 有 provider 字段 → 直接用
   ├── 有 parser.command + parser.script → local-parser
   └── URL 模式匹配 → auto-detect
3. 并行抓取 → 10 并发度，每个 Provider 独立 fetch
4. 标题过滤 → positive/negative 关键词匹配
5. 地点过滤 → always_allow > block > allow 三级
6. 去重 → URL 集合 + company::role 集合
7. [可选] Playwright 验活 → 逐个打开 URL，检测职位是否过期
8. 写入 pipeline.md + scan-history.tsv
```

#### 工作流三：批量处理（Batch）

```
1. 读取 pipeline.md 中待处理的 URL
2. 为每个 URL 生成独立的 worker prompt (batch-prompt.md)
3. 并行启动 claude -p worker
4. 每个 worker 独立执行完整评估
5. 合并结果 → node merge-tracker.mjs
```

### 2.3 关键设计模式

#### 2.3.1 Prompt-as-Code 模式

项目的核心智能全部体现在 `modes/` 目录下的 Markdown 文件中。这些文件不是代码，而是**结构化的 AI Prompt**：

| 文件 | 作用 |
|------|------|
| `_shared.md` | 全局规则：评分系统、原型定义、工具配置、写作风格、ATS 规范 |
| `_profile.md` | 用户层：个人原型、叙事、谈判脚本（永不自动更新） |
| `oferta.md` | 评估逻辑：A-G 七块的详细执行步骤和输出格式 |
| `pdf.md` | PDF 生成：HTML 模板注入指令 |
| `scan.md` | 扫描指令：如何运行 scan.mjs |
| `batch.md` | 批量指令：并行 worker 协调 |

这种设计的优势：
- AI Agent 直接读取这些文件作为上下文，**零编译、零部署**
- 用户可以通过对话让 AI 修改这些文件，实现个性化
- 系统更新只需替换文件，不涉及代码编译

#### 2.3.2 Provider 插件架构

`providers/` 目录下的每个 Provider 实现统一的接口：

```javascript
// Provider 接口
{
  id: string,              // "greenhouse" | "ashby" | ...
  detect(entry): {url}|null,  // 从 careers_url 自动检测
  fetch(entry, ctx): [{     // 抓取职位列表
    title, url, company, location
  }]
}
```

新增 ATS 平台只需添加一个 `.mjs` 文件。

#### 2.3.3 数据契约（两层分离）

这是项目最精妙的设计之一：

| User Layer（永不自动更新） | System Layer（可安全更新） |
|---|---|
| `cv.md` — 用户简历 | `modes/_shared.md` — 评分逻辑 |
| `config/profile.yml` — 个人信息 | `modes/oferta.md` — 评估指令 |
| `modes/_profile.md` — 个人定制 | `*.mjs` — 工具脚本 |
| `data/applications.md` — Tracker | `dashboard/*` — Go TUI |
| `reports/*` — 评估报告 | `templates/*` — 模板 |
| `output/*` — 生成的 PDF | `VERSION` — 版本号 |

这确保了系统自动更新时不会覆盖用户的个人数据和定制。

#### 2.3.4 ATS 兼容性工程

PDF 生成模块有专门的 ATS（Applicant Tracking System）兼容性处理：

```
normalizeTextForATS() 处理：
├── 破折号 → 连字符（—/– → -）
├── 智能引号 → ASCII 引号（"" → ""）
├── 省略号 → 三个点（… → ...）
├── 零宽字符 → 删除（200B/FEFF）
├── 不间断空格 → 普通空格
├── 箭头 → 文字（→ → "to"）
├── 圆点 → 管道符（·/• → "|"）
└── 货币符号 → 文字（€ → "EUR"，£ → "GBP"）
```

这些处理确保 PDF 被企业 ATS 系统正确解析，不会因特殊字符导致乱码或信息丢失。

### 2.4 职位匹配的精度分析

系统的匹配精度在不同维度差异很大：

| 匹配维度 | 方法 | 精度 | 原因 |
|----------|------|------|------|
| **技术栈** | JD 关键词 vs CV 技能列表 | 高 | 具体技术名词匹配精确 |
| **职业方向** | 6 种原型 + profile.yml | 高 | 用户明确定义目标角色 |
| **经验级别** | AI 推理 Senior/Staff 边界 | 中 | JD 级别描述模糊，AI 可能误判 |
| **地理位置** | 三级关键词过滤 | 高 | 精确字符串匹配 |
| **薪资范围** | WebSearch + profile.yml | 中低 | 大量公司不公开薪资，AI 可能凭训练数据猜测 |
| **文化契合度** | AI 推理 | 低 | 缺乏实际数据，纯推测 |
| **团队/管理** | AI 推理 | 低 | JD 通常不描述团队细节 |

**关于"能拿到准确的数据吗"**：
- **职位列表数据**：✅ 准确（直接从 ATS API 抓取，实时数据）
- **职位活性**：✅ 较准确（Playwright 实际访问页面，检测过期信号）
- **薪资数据**：⚠️ 不确定（依赖 WebSearch 公开数据，很多公司不公开）
- **匹配评分**：⚠️ 是 AI 推理建议，不是精确匹配——作者明确标注为"recommendations, not truth"

---

## 三、使用场景分析

### 3.1 核心使用场景

#### 场景一：AI/Automation 领域求职者（核心用户）
作者是 AI/Automation 方向的从业者，系统中的 6 种原型（LLMOps/Agentic/PM/SA/FDE/Transformation）和 150+ 预配置公司（Anthropic、OpenAI、ElevenLabs、Retool 等）都面向这个群体。

#### 场景二：高效求职管理
用 AI 评估数百个职位，快速筛选出值得投递的少数几个。740+ 职位评估 → 100+ 简历生成 → 1 个录用，展示了系统在漏斗效率上的价值。

#### 场景三：定制化简历生成
每个职位生成 ATS 优化的定制简历，自动注入 JD 关键词，用 Space Grotesk + DM Sans 字体设计。

#### 场景四：面试准备
STAR+R 故事银行 + 公司深度研究 + 谈判脚本，形成完整的面试准备体系。

### 3.2 中国市场适配度

**Career-Ops 目前主要面向欧美市场**：

| 维度 | 适配情况 |
|------|---------|
| **ATS 平台** | Greenhouse/Ashby/Lever/Workable 是欧美主流，中国主流平台（Boss直聘/拉勾/猎聘）不支持 |
| **职位来源** | 150+ 公司都是欧美公司，无中国公司 |
| **薪资数据** | 依赖 Glassdoor/Levels.fyi/Blind，无中国薪资数据 |
| **语言支持** | 无中文 modes（有日/德/法/土/乌/俄/葡/韩），评估输出为英语 |
| **PDF 格式** | A4/Letter 格式，适合欧美简历风格 |
| **AI 模型** | Claude/Gemini 均可在中国通过 API 使用 |

**如果要在中文市场使用，需要**：
1. 添加 Boss直聘/拉勾/猎聘 的 Provider（这些平台没有公开 API，需要 Playwright 爬虫）
2. 创建 `modes/zh/` 中文评估模式
3. 修改简历模板为中国 HR 偏好的格式
4. 替换薪资数据源

### 3.3 不适合的场景

1. **非技术岗位**：原型和评分体系都是为 AI/ML/技术岗位设计的
2. **中国本土求职**：不支持 Boss直聘/拉勾等中国平台
3. **低信任自动化**：系统设计为 Human-in-the-Loop，不适合全自动投递
4. **大规模 spray-and-pray**：项目明确反对盲目投递，推荐 4.0/5 分以下不投

---

## 四、适配的第三方平台

### 4.1 ATS 平台（职位扫描数据源）

| ATS 平台 | Provider 文件 | 数据获取方式 | 需要认证 |
|----------|-------------|-------------|---------|
| **Greenhouse** | `greenhouse.mjs` | `boards-api.greenhouse.io` 公开 JSON API | 否 |
| **Ashby** | `ashby.mjs` | `api.ashbyhq.com/posting-api` 公开 API，30s 超时 + 重试 | 否 |
| **Lever** | `lever.mjs` | `api.lever.co/v0/postings` 公开 API | 否 |
| **Workable** | `workable.mjs` | 公开 Markdown Feed（`/jobs.md`） | 否 |
| **SmartRecruiters** | `smartrecruiters.mjs` | 公开 API | 否 |
| **Recruitee** | `recruitee.mjs` | 公开 API | 否 |
| **自定义** | `local-parser.mjs` | 执行用户配置的脚本 | 取决于配置 |

### 4.2 AI 模型（评估引擎）

| AI 平台 | 接入方式 | 费用 |
|---------|---------|------|
| **Claude** (Anthropic) | Claude Code CLI — 主推荐 | 按量计费 |
| **Gemini** (Google) | Gemini CLI 或 `gemini-eval.mjs` 独立脚本 | 免费层可用（15 RPM, 1M token/天） |
| **OpenAI** | 标注为 Codex (soon) | 未实现 |

### 4.3 预配置扫描公司（150+）

| 类别 | 公司 |
|------|------|
| **AI Labs** | Anthropic, OpenAI, Mistral, Cohere, LangChain, Pinecone |
| **Voice AI** | ElevenLabs, PolyAI, Parloa, Hume AI, Deepgram, Vapi, Bland AI |
| **AI Platforms** | Retool, Airtable, Vercel, Temporal, Glean, Arize AI |
| **Contact Center** | Ada, LivePerson, Sierra, Decagon, Talkdesk, Genesys |
| **Enterprise** | Salesforce, Twilio, Gong, Dialpad |
| **LLMOps** | Langfuse, Weights & Biases, Lindy, Cognigy, Speechmatics |
| **Automation** | n8n, Zapier, Make.com |
| **European** | Factorial, Attio, Tinybird, Clarity AI, Travelperk |

### 4.4 工具依赖

| 工具 | 用途 | 必需 |
|------|------|------|
| **Node.js >= 18** | 运行所有 .mjs 脚本 | 是 |
| **Playwright + Chromium** | PDF 生成 + 职位验活 | 是（PDF），可选（验活） |
| **Go >= 1.21** | Dashboard TUI | 可选 |
| **Claude Code CLI** | AI 评估主引擎 | 二选一 |
| **Gemini CLI 或 API Key** | 免费替代评估引擎 | 二选一 |
| **pdflatex** | LaTeX CV 生成 | 可选 |

---

## 五、项目亮点与不足

### 5.1 亮点

1. **Prompt-as-Code 架构**：所有 AI 行为逻辑都在 Markdown 文件中，零编译、透明可审、AI 自身可修改
2. **数据契约设计**：User/System 两层分离，自动更新永不覆盖用户数据
3. **零 Token 扫描**：`scan.mjs` 纯 HTTP/JSON 抓取，不消耗任何 AI Token
4. **ATS 工程深度**：Unicode 规范化、字体优化、Keyword 注入——每一个细节都在解决真实问题
5. **Human-in-the-Loop 哲学**：明确禁止自动投递、推荐低分不投、尊重招聘者时间
6. **免费替代方案**：`gemini-eval.mjs` 提供零成本独立评估，不依赖 Claude
7. **完整工程化**：CI/CD、Dependabot、测试、版本管理、自动更新、rollback
8. **多平台 Agent 支持**：Claude Code / Gemini CLI / OpenCode / Codex / Copilot / Qwen / Kimi 全覆盖

### 5.2 不足与风险

1. **仅面向欧美市场**：ATS 平台、公司列表、薪资数据源全部是欧美的
2. **AI 评估非精确**：评分是 AI 推理建议，不是科学计算，存在幻觉风险
3. **标题过滤是关键词匹配**：`title_filter` 用简单的字符串包含判断，无法理解语义
4. **ATS API 变化风险**：Greenhouse/Ashby/Lever 的公开 API 随时可能变更或关闭
5. **Playwright 依赖**：PDF 生成和验活都需要 Chromium，对服务器环境有要求
6. **无数据缓存**：每次扫描都是实时请求，大量公司时可能触发频率限制
7. **原型体系固化**：6 种 AI 原型不适合非 AI 领域的求职者
8. **缺乏职位推荐**：只能扫描已知公司，无法发现不在 portals.yml 中的机会

### 5.3 项目成熟度评估

| 维度 | 评分 (1-5) | 说明 |
|------|-----------|------|
| 代码质量 | ⭐⭐⭐⭐⭐ | 严格的 CI/CD、类型注解、安全防护、代码规范 |
| 工程化水平 | ⭐⭐⭐⭐⭐ | 数据契约、自动更新、rollback、Provider 插件、Dashboard |
| 文档质量 | ⭐⭐⭐⭐⭐ | README 多语言、DATA_CONTRACT、CLAUDE.md、AGENTS.md 极其完善 |
| 安全性 | ⭐⭐⭐⭐ | SSRF 防护、域名白名单、API Key 遮盖、ATS 规范化 |
| 可维护性 | ⭐⭐⭐⭐⭐ | User/System 分层、Provider 插件、Prompt-as-Code |
| 通用性 | ⭐⭐⭐ | 高度面向 AI/ML 求职市场，其他领域需要大量定制 |
| 匹配精度 | ⭐⭐⭐ | 技术栈匹配可靠，薪资/文化/团队匹配有限 |
| 中国市场适配 | ⭐⭐ | 不支持中国平台，无中文模式，薪资数据源不适用 |

---

## 六、总结

**Career-Ops 是一个工程化水平极高的 AI 求职管道系统。** 它的核心创新在于将 AI 行为逻辑完全外化为 Markdown Prompt 文件（Prompt-as-Code），实现了"AI 可以修改自己的行为规则"的递归个性化能力。

**扫描功能是确定性的、可靠的**——直接从 Greenhouse/Ashby/Lever 等 ATS 公开 API 抓取实时职位数据，零 AI Token 消耗。**评估功能是 AI 推理的建议**——A-G 七维评估提供了结构化的分析框架，但评分不是精确计算。

**对于目标用户（AI/ML 领域的欧美求职者），这是一个非常实用的系统。** 作者自己的成功案例（740+ 评估 → 100+ 简历 → 1 个录用）证明了其有效性。

**对于中国市场的求职者，需要大量定制化**才能使用：添加中国平台 Provider、创建中文评估模式、替换薪资数据源、调整简历模板。系统的架构设计（Provider 插件、modes 目录）为这些定制提供了良好的扩展点。

**最终回答"能匹配符合自己的职位吗"**：能，但匹配质量取决于你的 CV 质量、profile 配置完整度，以及你是否处于 AI/ML 领域的欧美市场。系统会为你筛选出技术栈匹配、方向对口的职位，但最终决策仍需要你自己判断。
