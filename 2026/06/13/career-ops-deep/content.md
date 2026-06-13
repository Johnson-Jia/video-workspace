# Career-Ops 开源项目讲解视频 — 内容素材

> 内容真相源：workspace/sources/GitHub项目分析报告/career-ops-深度分析报告.md
> 项目源码：D:/AI-Agent/github-analyze/career-ops/
> 目标时长：约 3 分钟（180s）| 模式：单主题深度解析 | 场景：9 个
> 旁白总字数目标：~690 字（+25% 语速约 180s）

## 项目基本信息（事实清单，供内容保真校验）

- 项目名：Career-Ops（careerops）
- 仓库：github.com/santifer/career-ops
- 作者：Santiago Fernández de Valderrama (@santifer)
- 版本：v1.8.1 | 许可证：MIT
- 技术栈：Node.js (ESM .mjs) + Go (Dashboard TUI, Bubble Tea)
- 提交：231 次 | 贡献者：62 人
- 核心架构：Prompt-as-Code（智能全部写在 modes/ 的 Markdown 文件）
- 扫描数据源：7 个 ATS Provider（Greenhouse/Ashby/Lever/Workable/SmartRecruiters/Recruitee/local-parser）| 150+ 预配置公司 | 零 AI Token
- 评估体系：A-G 七维 + 5 维度加权 1-5 分制
- 数据契约：User Layer（cv.md/profile.yml/_profile.md 永不自动更新）/ System Layer（modes/*.mjs 可安全更新）
- 作者战绩：740+ 评估 → 100+ 简历 → 1 录用
- 限制：仅欧美 ATS 平台（不支持 Boss直聘/拉勾/猎聘）| AI 评分是推理建议非精确计算 | 依赖 Node.js+Playwright+Chromium
- 适用人群：AI/ML/自动化方向，尤其想投海外公司的求职者

## 原始项目自述（英文 description，保真基准）

Career-Ops: An AI-driven job-hunting pipeline system. Prompt-as-Code architecture — all AI behavior logic lives in Markdown files under modes/. Scans 150+ companies via ATS public APIs (Greenhouse, Ashby, Lever) with zero AI token cost. Evaluates jobs across A-G seven dimensions. User/System two-layer data contract. Human-in-the-loop — never auto-applies.

## 九场景叙事内容

### S1 hook（~12s | ~45 字）
**叙事功能**：反差钩子（740→1），制造悬念
**关键事实**：作者 740+ 评估 → 100+ 简历 → 1 录用
**画面**：数字 740 巨大冲击 → 收缩到 1 → 引出"系统"

### S2 what（~22s | ~85 字）
**叙事功能**：项目定位
**关键事实**：Career-Ops / Santiago / Node.js + Go 双栈 / 全流程自动化
**画面**：项目名 + 双技术栈示意（Node 扫描器 + Go 看板）

### S3 philosophy（~24s | ~95 字）★ 架构哲学
**叙事功能**：核心创新点 Prompt-as-Code
**关键事实**：智能在 Markdown 非 code / 零编译零部署 / AI 可自改规则
**画面**：Markdown 文件图标 → 流入 AI 大脑 → AI 反写规则

### S4 scan（~22s | ~85 字）★ 核心功能一
**叙事功能**：职位扫描能力
**关键事实**：7 个 ATS Provider / 150+ 公司 / 零 Token / Playwright 验活
**画面**：多平台 logo 汇聚 → 扫描雷达动效 → 职位卡片瀑布

### S5 eval（~24s | ~95 字）★ 核心功能二
**叙事功能**：A-G 七维评估体系
**关键事实**：七维度（角色概要/CV匹配/级别策略/薪酬/定制化/面试准备/合法性）/ 1-5 分
**画面**：A-G 七格仪表盘 → 评分填充动画

### S6 data-contract（~20s | ~78 字）★ 架构哲学
**叙事功能**：数据契约设计
**关键事实**：User Layer 永不更新 / System Layer 可更新 / 更新不覆盖用户数据
**画面**：两层分离示意（用户层锁 / 系统层刷新）

### S7 limits（~24s | ~92 字）★ 软硬件限制
**叙事功能**：诚实陈述边界
**关键事实**：仅欧美 ATS / AI 评分非精确 / 依赖 Node+Playwright+Chromium / 反对海投 4 分以下不投
**画面**：限制清单 + 警示色

### S8 usecase（~18s | ~70 字）★ 适用场景
**叙事功能**：目标人群 + 推荐建议
**关键事实**：AI/ML 工程师投海外 / 国内需大量定制 / 作者成功案例
**画面**：目标人群画像 + 适用/不适用对比

### S9 cta（~12s | ~45 字）
**叙事功能**：收尾金句 + 关注引导（无搜索引导）
**画面**：项目 logo + 关注引导动效
