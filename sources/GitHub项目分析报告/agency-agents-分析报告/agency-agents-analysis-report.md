# agency-agents 项目多维度分析报告

> 分析日期：2026-05-22 | 分析对象：[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)

---

## 1. 项目定位与起源

agency-agents 是一个 AI 智能体角色库项目，起源于 Reddit 的一条帖子，经过数月迭代发展而来。项目核心理念是为 AI 编程工具提供**开箱即用的专家角色**——不是通用的提示词模板，而是具有独立人设、专业流程和可交付成果的完整智能体定义。

项目口号："A complete AI agency at your fingertips"——指尖上的完整 AI 机构。

**核心差异化**：
- 每个智能体有**明确的身份**（不是"你是一个专家"，而是定义了专家怎么思考、怎么做事、交付什么）
- 每个智能体有**可量化的成功指标**
- 每个智能体有**经过实战验证的工作流程**

---

## 2. 项目规模

| 指标 | 数值 |
|------|------|
| 智能体总数 | 184 个 |
| 部门/分类 | 15 个 |
| Markdown 文件总数 | 410 个 |
| Markdown 总行数 | 75,614 行 |
| 脚本文件 | 5 个（1,473 行） |
| 最新提交 | 2026-04-12 |

---

## 3. 部门分布

| 部门 | 数量 | 占比 | 定位描述 |
|------|------|------|---------|
| Specialized | 41 | 22.3% | 不走寻常路的专家，覆盖面最广 |
| Marketing | 30 | 16.3% | 全平台营销专家团队 |
| Engineering | 29 | 15.8% | 技术实施核心力量 |
| Game Development | 20 | 10.9% | 跨引擎游戏开发专家 |
| Finance | 5 | 2.7% | 财务与金融分析 |
| Sales | 8 | 4.3% | 销售全流程 |
| Design | 8 | 4.3% | 设计体验 |
| Testing | 8 | 4.3% | 质量保障 |
| Paid Media | 7 | 3.8% | 广告投放 |
| Support | 6 | 3.3% | 运营支持 |
| Project Management | 6 | 3.3% | 项目协调 |
| Spatial Computing | 6 | 3.3% | 空间计算与XR |
| Product | 5 | 2.7% | 产品管理 |
| Academic | 5 | 2.7% | 学术研究支撑 |

---

## 4. 智能体设计哲学

每个智能体遵循五层设计框架：

```
┌─────────────────────────────────┐
│  Layer 1: 身份与人设 (Identity)    │  ← 独特的个性、沟通风格
├─────────────────────────────────┤
│  Layer 2: 核心使命 (Mission)      │  ← 做什么、不做什什么
├─────────────────────────────────┤
│  Layer 3: 关键规则 (Rules)        │  ← 领域特定的硬约束
├─────────────────────────────────┤
│  Layer 4: 技术交付物 (Deliverables)│  ← 具体产出、含代码示例
├─────────────────────────────────┤
│  Layer 5: 成功指标 (Metrics)      │  ← 可量化的质量标准
└─────────────────────────────────┘
```

**关键设计原则**：
1. **强个性**：不是通用模板，而是有真实性格和声音的角色
2. **清晰交付物**：具体的输出物，不是模糊的指导
3. **可衡量**：每个智能体有明确的成功指标和质量标准
4. **可验证流程**：经过实战验证的逐步流程
5. **学习记忆**：模式识别和持续改进机制

---

## 5. 智能体亮点摘录

| 智能体 | 典型语录 | 体现的个性 |
|--------|---------|-----------|
| Evidence Collector | "I default to finding 3-5 issues and require visual proof for everything." | 严格、证据驱动 |
| Reddit Community Builder | "You're not marketing on Reddit — you're becoming a valued community member." | 社区优先、真实互动 |
| Whimsy Injector | "Every playful element must serve a functional or emotional purpose." | 有目的的趣味性 |
| Reality Checker | "Default to 'needs improvement' — require overwhelming evidence to certify production ready." | 质量守门人 |

---

## 6. 工具集成生态

### 6.1 支持的工具清单（11 种）

| 工具 | 安装位置 | 格式 | 转换需求 |
|------|---------|------|---------|
| Claude Code | `~/.claude/agents/` | .md 原生 | 无需转换 |
| GitHub Copilot | `~/.github/agents/` + `~/.copilot/agents/` | .md 原生 | 无需转换 |
| Antigravity | `~/.gemini/antigravity/skills/` | SKILL.md | 需转换 |
| Gemini CLI | `~/.gemini/extensions/` | 扩展+SKILL.md | 需转换 |
| OpenCode | `.opencode/agents/` | .md | 需转换 |
| Cursor | `.cursor/rules/` | .mdc 规则文件 | 需转换 |
| Aider | `CONVENTIONS.md` | 单文件 | 需转换 |
| Windsurf | `.windsurfrules` | 单文件 | 需转换 |
| OpenClaw | 三文件(SOUL/AGENTS/IDENTITY) | 工作区 | 需转换 |
| Qwen Code | `.qwen/agents/` | .md SubAgent | 需转换 |
| Kimi Code | `~/.config/kimi/agents/` | YAML+提示词 | 需转换 |

### 6.2 安装脚本能力

```bash
# 核心命令
./scripts/convert.sh --parallel        # 并行转换所有工具
./scripts/install.sh --interactive      # 交互式安装（复选框UI）
./scripts/install.sh --tool cursor     # 安装到指定工具
./scripts/lint-agents.sh               # 检查智能体文件格式
```

**脚本特色**：
- 支持 `--parallel` 并行构建，多核加速
- 交互式安装带复选框 UI，自动检测已安装工具
- 支持 `--jobs N` 控制并行度
- 提供 PowerShell 版本（convert.ps1, install.ps1）支持 Windows

---

## 7. 内容质量分析

### 7.1 文件结构标准

每个智能体 `.md` 文件遵循统一结构：

```yaml
---
name: agent-name
description: 一句话描述
color: "#hex"
---
```

```markdown
# Agent Name

## Identity & Memory
## Core Mission
## Critical Rules
## Technical Deliverables
## Workflow Process
## Success Metrics
```

### 7.2 代码示例丰富度

Engineering 部门的智能体普遍包含可运行的代码示例：
- Frontend Developer: React/Vue 组件示例
- Backend Architect: API 设计示例、数据库 Schema
- DevOps Automator: CI/CD Pipeline YAML
- Security Engineer: 安全审查 Checklist

### 7.3 内容深度指标

| 维度 | 评估 |
|------|------|
| 单个 agent 平均行数 | ~310 行 |
| 代码示例覆盖率 | Engineering 部门 > 80%，其他部门约 30% |
| 工作流程完整度 | 大部分 agent 有 3-5 步明确流程 |
| 成功指标可量化度 | ~60% 的指标可量化 |

---

## 8. 社区与生态

### 8.1 社区渠道

| 渠道 | 用途 |
|------|------|
| GitHub Discussions | 成功案例分享 |
| GitHub Issues | Bug 报告、功能请求 |
| Reddit (r/ClaudeAI) | 项目发源地、持续讨论 |
| Twitter/X | #TheAgency 标签 |

### 8.2 社区贡献

- 多个社区翻译版本（中文、繁体中文）
- [awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) 衍生项目
- 社区成员通过 PR 持续贡献新智能体

### 8.3 影响力事件

- Reddit 帖子发布后 12 小时内收到 50+ 请求
- 7 天内达到 10,000 GitHub Stars
- CodeFactor 代码质量评级 A+

---

## 9. 项目成熟度评估

| 维度 | 成熟度 | 说明 |
|------|--------|------|
| 内容完整度 | ⭐⭐⭐⭐⭐ | 15 个部门、184 个智能体，覆盖全面 |
| 格式规范 | ⭐⭐⭐⭐⭐ | 统一的 frontmatter + 章节结构 |
| 工具集成 | ⭐⭐⭐⭐ | 11 种工具，脚本自动化程度高 |
| 脚本质量 | ⭐⭐⭐⭐⭐ | 并行构建、交互式UI、跨平台支持 |
| 文档质量 | ⭐⭐⭐⭐ | README 详尽，缺少独立索引文档 |
| 国际化 | ⭐⭐⭐ | 有社区翻译，但非官方支持 |
| 测试覆盖 | ⭐⭐ | 有 lint 脚本，但无自动化测试 |

---

## 10. SWOT 分析

### Strengths (优势)
- **先发优势**：定义了 AI agent 角色库这一品类
- **设计哲学清晰**：五层框架确保每个智能体质量一致
- **社区活跃**：Reddit 起源，全球开发者参与
- **工具集成成熟**：脚本工程化程度高
- **英文内容天然全球化**

### Weaknesses (劣势)
- **中国市场空白**：无中国平台运营智能体
- **工具数量**：落后于中文版（11 vs 17）
- **文档治理**：缺少独立索引文件和版本追踪
- **非技术角色偏弱**：金融、法务、HR 等领域覆盖不足

### Opportunities (机会)
- AI 编程工具市场爆发式增长
- Agent 角色库成为 AI 编程基础设施
- 企业级应用场景扩展（合规、审计等）

### Threats (威胁)
- 竞品角色库涌现
- 工具生态碎片化加剧
- AI 模型能力提升可能降低角色定义的必要性

---

## 11. 总结

agency-agents 是 AI 智能体角色库品类的**开创者和标准制定者**。它通过清晰的设计哲学（个性→使命→规则→交付→指标）确保了 184 个智能体的质量一致性，通过成熟的脚本生态实现了 11 种工具的无缝集成。

项目的核心价值不在于"有多少个提示词"，而在于**每个智能体都是一个小型专家系统**——有思考方式、有做事流程、有可衡量的产出。这种"深度优于广度"的理念使其区别于市面上的通用提示词库。
