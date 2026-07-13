# GitHub Weekly Trending 2026-07-13（第29周）内容分析

## 选题方向
本周 GitHub 被 **AI agent 工具全面占领**：14 个入选项目几乎全是 agent 编排、Claude 技能生态、AI 安全、agent 应用。题材高度集中于「AI agent 基础设施化」——agent 不再是单点工具，而是成体系（并行编排 / 技能市场 / 安全隔离 / 办公应用）。

四组分类（领域色仅视觉，旁白用领域名）：
- 组1 编码 Agent（4）：并行编排多个编程 agent
- 组2 技能生态（4）：Claude Code 技能/插件市场爆发
- 组3 安全工具（3）：AI 渗透 + agent 沙箱隔离
- 组4 应用办公（3）：agent 接管 Office/网页/设计

## 周次 + 钩子（SubAgent-1 stage0.5 参考）
- 周次：**第29周（07月06日-07月13日）**，hook 和 CTA 必须含周次（禁只用「本周」）
- 钩子方向：本周 GitHub 被 AI agent 刷屏——单是让 AI 写代码的工具就占了一组，还有给 Claude 装 345 个技能、AI 自动找漏洞、AI 接管 Office。数据锚定：OfficeCLI 周涨近七千星（组4 涨星王）、claude-video 周涨四千三、caveman 总星 88K。

## 受众配比
- A 普通可用 3 个（OfficeCLI / page-agent / astryx）
- B 半可用 7 个（codex-plugin-cc / DesktopCommanderMCP / caveman / claude-skills / claude-video / archify）
- C 开发者 6 个（orca / herdr / strix / pentagi / CubeSandbox + 部分 B）
周榜性质偏开发者（GitHub 周榜 AI agent 工具主导），A 档约 1/5 可接受；narration 对 C 档措辞「给做 XX 的开发者」。

## 真实性验证（gh API，2026-07-13）
14 项目全部 gh API 验证：0 HARD 违规。
- 大厂官方（openai 126k fl / facebook 36k fl / alibaba 20k fl / TencentCloud 990 fl）信誉强
- caveman 88.5K★ + 5K forks（爆款 skill）
- claude-video 警告：size 76KB（skill 项目代码少正常）+ watcher 0.5%（边界），但 fork 875 + 周涨 4353 + 活跃 push 实质支撑，判定通过
- OfficeCLI 警告：watcher 0.25% 低，但 15.4K★ + 1K forks + size 313MB（实质项目）支撑

## 合规
- ⛔ RuView（exclusion_list 永久排除）
- 排除 OmniRoute（白嫖 API）/ system_prompts_leaks（泄露）/ meetily（inactive）
- OfficeCLI 原文含「first and best」，中文描述去除（保真锚点保留原英文）
- 安全组（strix/pentagi）讲防御价值（找漏洞修复），不鼓励攻击
- token 统一写「词元」（caveman 省 65% 词元）

## 字数 + 场景（weekly_mode）
- 6-7 场景：hook → 组1 → 组2 → 组3 → 组4 → 趋势总结 → CTA
- 字数 300-450，时长 45-60s
- 每组 6-10s（3-4 项目快速带过 + 重点 1-2 个展开）
- 旁白禁颜色词，用领域名分组（「编码 agent 这组」「技能生态这组」）
