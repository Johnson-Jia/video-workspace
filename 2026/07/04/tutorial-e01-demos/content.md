# content.md — E01 段3（5 个可运行 demo 速览）

> 教程仓库 `D:/AI-Agent/ai-landing-tutorial/` 的 `demos/` 目录下 5 个自包含可运行 demo。每个 demo 自带 README + 依赖 + 源码 + 示例数据，开箱即跑。本段是 7 阶段方法论后的「落地工具箱巡礼」。

## 5 个 demo 概览（demos/README.md 索引）

| Demo | 对应教程章节 | 一句话定位 | 运行 |
|------|------------|-----------|------|
| ai-test-frame | 《AI 自动化测试》§8 | 最小可运行的 AI 自动化测试框架 | `python main.py` |
| ai-metrics | 阶段 5 推广与度量 | AI 代码占比度量（三层识别 + 反伪造）+ Excel 同比 | `python main.py` |
| report-templates | 《汇报材料 AI 生成指南》 | 5 类汇报 Prompt 模板包 | 复制 prompt 填数据 |
| role-handbooks | 《角色操作手册》 | 4 份角色手册（开发/测试/组长/产品）| 各级人员照做 |
| claude-skills | 阶段 3/4/6 | 4 个 Claude Code skill + 12 份团队规范 | 复制到 .claude/ |

核心原则（demos/README.md）：**任何 demo 都应开箱即跑**——自带被测对象/示例数据，不依赖读者私有环境。

## demo 1：ai-test-frame — 最小可运行 AI 自动化测试框架

**定位**（README 首行）：体现「AI 在编码期生成测试资产、运行期确定性执行」的完整架构，开箱即跑。

**架构（每个文件对应一个核心模块）**：
- `registry.py` 注册中心：装饰器注册 + 类引用 + get（type→handler 映射）
- `assertions.py` 软断言：失败不中断 + 截图 + 收集结果
- `base_page.py` 测试基类：通用操作 + 通用定位（role / placeholder / label）
- `runner.py` 测试运行器：用例调度 + 浏览器启停
- `handlers/` 操作处理器：每个操作类型一个 handler（AI 录制转生成的目标）
- `data/cases.json` 数据驱动用例
- `site/index.html` 自带的极简商品管理页（被测对象，demo 自带）

**核心思想**：「录制操作 → AI 生成测试类」——AI 在编码期生成测试资产，运行期确定性执行（不是 AI 现场跑测试，是 AI 写好测试代码后确定性跑）。

**运行预期**：Playwright 打开自带 site/index.html，按 data/cases.json 跑用例（新增商品 → 验证列表出现），终端输出断言汇总（通过 N / 失败 0）。

## demo 2：ai-metrics — AI 代码占比度量 + 提效同比

**定位**（README）：整合两个维度度量——AI 代码占比（三层识别算法）+ 提效同比（Excel 模板）。

**核心一：三层 AI 识别算法（为什么能真实识别 AI 代码）**
> 只靠 Co-authored-by 不够（会被误标——VS Code Copilot 对手写代码也自动加 trailer）。本 demo 用三层算法：

| 层 | 文件 | 作用 |
|---|---|---|
| ① Co-authored-by 初筛 | `detector/coauthored.py` | commit message 含 AI 工具名 → 判 AI（置信度 1.0）|
| ② 风格计量学复核 | `detector/stylometry.py` | 算 AI 提交与作者本人风格画像的余弦相似度——像本人 → 可能误标降置信度；不像本人 → 确认 AI |
| ③ 检测器注册表 | `detector/registry.py` | 组合 ①② 给最终判定 |

**风格学是反伪造关键**：用「代码本身像不像作者本人手写」复核 Co-authored-by。算法（提炼自 ai-code-ratio 的 ngram.go / stylometry.go）：字符级 n-gram → TF 归一化 → 余弦相似度 → 置信度 = 1 − 相似度。

**示例 git 仓库（gen_data.py 生成）演示三类提交**：
- Alice 干净提交（风格 A）→ 建风格画像
- Alice AI 提交（风格 B + Co-authored-by）→ 与画像差异大 → 风格学维持较高置信度（确认 AI）
- Alice 误标提交（风格 A + Co-authored-by）→ 与画像更像 → 风格学降低置信度（演示反伪造挡误标）

**核心二：提效同比 + Excel 模板**
- `data/template.xlsx` 录入模板（日期/定制或通用/应用/类型/jira_id/描述/开发人员）
- `data/sample_releases.xlsx` 示例（2025 基线 vs 2026 AI 推行后）
- `efficiency.py` 算同比：上线条目 / 需求 vs Bug / 参与人数 / 人均条目

## demo 3：report-templates — 5 类汇报 Prompt 模板包

**定位**：用 AI 一键生成 AI 转型的各类汇报材料（PPT / 计划书 / 周报 / 总结 / 度量报告）。

**工作流（4 步）**：
1. 准备数据（整理真实数据：产出/AI 占比/Bug/进展）
2. 复制 Prompt（打开对应 .prompt.md，复制填数据）
3. 发给 AI（任意 AI：Claude / ChatGPT / GLM）→ 生成 Markdown
4. 渲染（PPT 类 → ppt-master 生成原生可编辑 PPTX；文档类 → 直接用 / 转 PDF）

**5 类模板**：
| 模板 | 用途 | 输出格式 |
|------|------|---------|
| 01-战略汇报 PPT | 向上汇报进展 / 争取资源 | 可编辑 PPTX |
| 02-转型计划书 | 立项审批 | 文档 |
| 03-周报 | 关键节点跟踪 | 文档 |
| 04-阶段总结报告 | 结项 / 晋升述职 | 文档 |
| 05-效果度量报告 | 数据证明提效（可接 ai-metrics）| 文档 |

**亮点**：5 分钟最小可走通（没有数据也能先跑）——用占位数据跑一遍，30 秒拿到一份汇报，确认流程通了再补真实数据。ppt-master 把 Markdown 渲染成原生可编辑 PPTX（不是图片 PPT，是真 PPT）。

## demo 4：role-handbooks — 4 份角色操作手册

**定位**：4 个角色的 AI 转型操作手册（开发 / 测试 / 组长 / 产品），覆盖转型全员。

**手册清单**：
| 手册 | 角色 | 核心任务 |
|------|------|---------|
| 开发手册 | 开发 | 精通 Claude Code + CLAUDE.md + impact 影响分析 + 人审 AI 产出 + 沉淀 Skill |
| 测试手册 | 测试 | 录制转生成 + 测试资产规范 + AI 占比度量 + 防偷改测试 |
| 组长手册 | 组长 | 全员培训 + 规范资产化 + 带试点 + 数据汇报 |
| 产品手册 | 产品 | Codex 做原型 + 需求结构化 + 与开发 AI 协作 |

**使用方式**：各级人员拿自己那份手册照做。每份含 6 部分——角色定位 / 核心任务 / 怎么做（按优先级步骤）/ 工具箱 / 检查清单 / 常见坑。

**可单独交付**：本目录自包含（4 份手册 + 说明），可独立打包分发给各级人员。配合 ai-test-frame / ai-metrics / report-templates 上下游使用。

## demo 5：claude-skills — Claude Code Skill 仓库 + 团队规范

**定位**：一组适配 Claude Code 的通用化 skill + 团队规范。读者可整个复制到自己项目的 `.claude/` 下使用，也可作为「怎么写 Claude Code skill / 怎么资产化团队规范」的参考。

**Skill 清单（4 个）**：
| Skill | 类型 | 用途 |
|-------|------|------|
| devflow | 编排型 | 开发工作流：需求→交付 6 阶段（编排 OpenSpec + Superpowers），断点续传 + 规则覆盖 |
| sql-query | 工具型 | PostgreSQL 只读查询（三模式 + 安全护栏：仅 SELECT / SSH 隧道 / 租户隔离）|
| crud-gen | 工具型 | CRUD 代码脚手架生成（读表结构 → 分层 domain/dto/service/dao/controller）|
| code-review | 编排型 | AI 代码审查（红/黄/绿三级分级 + 依据规则自动核对 + 结构化报告）|

**团队规范集合（rules/，12 份通用 rule，复制到 .claude/rules/ 即用）**：
按职能分层，配合 team-conventions.md（通用 CLAUDE.md 总纲）：
- 入口：team-conventions（CLAUDE.md 总纲：技术栈/结构/核心原则/规范索引）
- 分层与接口：api-response（统一响应模型）/ service-dao（接口实现分离 + 事务归 Service）
- 质量与稳定：error-handling / logging / testing（Given-When-Then）
- 数据：database（表/字段/索引/向后兼容）/ batch（批量代替循环）
- 并发：async（线程池/上下文传递）/ distributed-lock（Redisson/锁粒度）
- 工程规范：git-branch（分支命名/Conventional Commits）/ naming（类后缀/方法动词/目录分层）

**三件套**：一个 skill = SKILL.md（入口）+ 可选 reference/scripts（按需加载）+ 可选 rules/<name>.md（覆盖规则）。best-practices.md 含 Claude Code 用得顺手的 8 条心法 + skill 写得值钱的 5 条方法论。

## 本段叙事重点（教程讲解口吻）

- **承接段2**：每个阶段都对应可运行 demo + 真实数据 → 现在快速过一下这 5 个 demo
- **核心反差**（contrarian_angle）：不是空谈概念，每个 demo clone 即跑；ai-metrics 三层识别算法是亮点（不只靠 Co-authored-by，加风格学反伪造）
- **教程讲解口吻**：「这一段快速过一下 5 个 demo…」「先看 ai-test-frame…」「ai-metrics 是重头戏…」——禁演讲开场
- **数据严谨**：风格学反伪造是机制描述（能降低误标置信度），不是「100% 准确」；提效同比标「相关性非因果」
