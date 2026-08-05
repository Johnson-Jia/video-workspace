# AI 风向标 内容素材 — 2026-08-02

数据源：raw_trending.json（ai_trending.py 独立 AI 源，8 个 AI 项目，gh API 三源验证）
模式：标准盘点（5 项目，约 30-40s）
分类：ai-wind（暗色电紫科技风，YunjianNeural +25%）

## 入选项目（5 个，按讲解顺序）

1. lyogavin/airllm | Jupyter Notebook | 25.2K★ (+242今日) | 用 4GB 显卡就能推理 70B 大模型，把大模型推理门槛打到消费级显卡（原: AirLLM 70B inference with single 4GB GPU）
   - avatar: assets/avatars/lyogavin.png
   - 用途: 普通电脑跑大模型
   - 受众: A 普通可用（本地能跑，门槛低）
   - contrarian_angle: 主流跑 70B 大模型要专业卡（A100/H100 几万元），这个 4GB 消费级显卡就能跑（平民化 AI 能力）
   - 数据锚点: 25245★ / 2844 fork / 单日 +242（真实性 gh API 核验✓，老账号 2011+68 repos）

2. Panniantong/Agent-Reach | Python | 64.3K★ (+645今日) | 给 AI agent 一双看全网的眼睛，能读各大社交平台内容、零 API 费用的命令行工具（原: Give your AI agent eyes to see the entire internet. Read & search Twitter, Reddit, YouTube, GitHub, Bilibili, XiaoHongShu — one CLI, zero API fees.）
   - avatar: assets/avatars/Panniantong.png
   - 用途: AI读全网资料
   - 受众: A 普通可用（CLI 一行命令，零 API 费）
   - contrarian_angle: AI agent 通常只能聊天，这个给它"眼睛"看全网社交平台（不用花 API 费）
   - 数据锚点: 64335★ / 5320 fork / 单日 +645（真实性核验：Star/Fork 12:1 正常 + 290 真实提交，2 警告边界但非刷星，保留）
   - 合规: 中文泛化「各大社交平台」，raw 原文锚点保留平台名（保真）

3. microsoft/AI-For-Beginners | Jupyter Notebook | 58.5K★ (+2617今日) | 微软 12 周 24 节 AI 入门系统课，完全免费开放（原: 12 Weeks, 24 Lessons, AI for All!）
   - avatar: assets/avatars/microsoft.png
   - 用途: 免费系统学AI
   - 受众: A 普通可用（学习者直接跟着学）
   - contrarian_angle: 大厂系统级 AI 课一分不收（对标动辄几千的收费 AI 课）
   - 数据锚点: 58479★ / 单日 +2617（今日 AI 榜 rank 1）

4. TencentCloud/TencentDB-Agent-Memory | TypeScript | 10.6K★ (+604今日) | 腾讯开源的 AI agent 团队级记忆中枢，把对话/文档/代码变成可复用的记忆资产（原: TencentDB Agent Memory is a team-level memory hub for AI Agents — turning conversations, docs, and code into four reusable memory assets (Chat Memory, Skill, LLM-Wiki, Code-Graph) that are governed, shared, and equipped across agents and frameworks.）
   - avatar: assets/avatars/TencentCloud.png
   - 用途: 给AI团队记忆
   - 受众: C 开发者向（Agent 框架集成，措辞「给做 AI 应用的开发者」）
   - contrarian_angle: AI agent 普遍没记忆（每次重新说），这个给整个团队共享的记忆中枢
   - 数据锚点: 10621★ / 604 fork / 单日 +604（腾讯开源，真实性无忧）

5. microsoft/generative-ai-for-beginners | Jupyter Notebook | 114.5K★ (+588今日) | 微软 21 节生成式 AI 入门课，从零开始动手构建（原: 21 Lessons, Get Started Building with Generative AI）
   - avatar: assets/avatars/microsoft.png
   - 用途: 动手学生成式AI
   - 受众: A 普通可用（零基础动手）
   - contrarian_angle: 生成式 AI 是当下最热方向，微软出 21 节免费动手课（11 万星认可）
   - 数据锚点: 114501★ / 单日 +588（11 万星，最高总星）

## 真实性核验记录（零虚假）
- 大厂（microsoft×2 / TencentCloud）真实性无忧
- lyogavin/airllm：✅ 通过（老账号 2011 + 68 repos + 925 followers + Star/Fork 8.9:1）
- Panniantong/Agent-Reach：2 警告边界（watcher 0.34% / 贡献集中度 96.7%），但 Star/Fork 12:1 正常 + 290 真实提交 + 64K 星，判定为真实活跃项目保留
- 未选：reverse-skill（安全/逆向类 + 343 字超长 description，降权）；last30days-skill（综合盘点近期高频，避免重复）；DeepSeek-Reasonix（C 档已满 + 含 AI 品牌名需泛化）

## 受众分档（A 档约一半 ✓，C 档 1/5 ≤1/3 ✓）
- A 档（4）: airllm / Agent-Reach / AI-For-Beginners / generative-ai-for-beginners
- C 档（1）: TencentDB-Agent-Memory

## hook 候选（具象度优先，防 c5s 退化）
反直觉角度（首选，≤12 字 + 具象数字/冲突词）:
- airllm: 「4GB 显卡跑 70B 大模型」（11 字，反直觉 + 具象数字 4GB/70B）← 推荐 hook 锚点
- Agent-Reach: 「给 AI 装上眼睛看全网」（10 字，反直觉）
数字锚定:
- AI-For-Beginners 单日 +2617（AI 榜 rank 1）
建议主 hook: airllm 反直觉悬念（「4GB 显卡，跑起 70B 大模型」），悬念揭晓放在场景 2 airllm

## 结尾提问（中性互动，禁站队）
候选: 「这几个 AI 项目你最想试哪个」/「本地跑大模型和 AI 课你会先玩哪个」（二选一非对抗）
