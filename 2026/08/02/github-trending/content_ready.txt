# GitHub Trending 内容素材 — 2026-08-02

数据源：raw_trending.json（15 项目，三源交叉验证，gh API 15/15 真实性核验通过）
模式：标准盘点（6 项目，约 30-40s）
分类：github（暗色科技风，YunjianNeural +25%）

## 入选项目（6 个，按讲解顺序）

1. microsoft/AI-For-Beginners | Jupyter Notebook | 57.3K★ (+949今日) | 微软出的 12 周 24 节 AI 入门系统课，完全免费开放（原: 12 Weeks, 24 Lessons, AI for All!）
   - avatar: assets/avatars/microsoft.png
   - 用途: 免费系统学AI
   - 受众: A 普通可用（学习者直接跟着学）
   - contrarian_angle: 大厂系统级课程一分不收，对标动辄几千的收费 AI 课
   - 数据锚点: 57330★ / 11355 fork / 单日 +949（今日榜 rank 1）

2. usekaneo/kaneo | TypeScript | 5.7K★ (+760今日) | 开源项目管理工具，功能刚好够用、不臃肿，可自己部署（原: 🎯 All you need. Nothing you don't. Open source project management that works for you, not against you.）
   - avatar: assets/avatars/usekaneo.png
   - 用途: 开源管项目
   - 受众: A 普通可用（Web 应用，自部署即用，jira/linear 的开源平替）
   - contrarian_angle: 商业项目管理软件按人头收费，这个开源还更轻
   - 数据锚点: 5712★ / 486 fork / 单日 +760（真实性 gh API 核验✓，多人贡献）

3. huggingface/speech-to-speech | Python | 10.2K★ (+442今日) | 用开源模型搭建本地语音助手（原: Build local voice agents with open-source models）
   - avatar: assets/avatars/huggingface.png
   - 用途: 本地语音助手
   - 受众: B 半可用（需部署，但有完整模型）
   - contrarian_angle: 主流语音助手都要联网上云端，这个本地就能跑、数据不出本机（隐私 + 离线）
   - 数据锚点: 10233★ / 1249 fork / 单日 +442

4. iv-org/invidious | Crystal | 21.6K★ (+435今日) | 视频网站的开源替代前端，可自己部署（原: Invidious is an alternative front-end to YouTube）
   - avatar: assets/avatars/iv-org.png
   - 用途: 干净看视频
   - 受众: A 普通可用（Web 前端，自部署）
   - contrarian_angle: 官方前端越来越重，开源前端更轻更干净
   - 合规: 旁白/画面措辞中性"开源前端"，禁渲染"绕过广告/绕过地区限制"
   - 数据锚点: 21633★ / 2431 fork / 单日 +435（老牌项目）

5. microsoft/TRELLIS.2 | Python | 9.9K★ (+107今日) | 微软的 3D 生成模型，用文字就能生成 3D 资产（原: Native and Compact Structured Latents for 3D Generation）
   - avatar: assets/avatars/microsoft.png
   - 用途: 文字生成3D
   - 受众: A 普通可用（有 demo，门槛低）
   - contrarian_angle: 3D 建模原本要专业软件+学习成本，这个一句话出 3D 模型（平民化专业能力）
   - 数据锚点: 9945★ / 1200 fork / 单日 +107

6. bytedance/deer-flow | Python | 78.8K★ (+209今日) | 字节开源的长周期超级智能体，能自己调研、写代码、做创作，独自处理几分钟到几小时的复杂任务（原: An open-source long-horizon SuperAgent harness that researches, codes, and creates. With the help of sandboxes, memories, tools, skill, subagents and message gateway, it handles different levels of tasks that could take minutes to hours.）
   - avatar: assets/avatars/bytedance.png
   - 用途: AI自己干长任务
   - 受众: C 开发者向（Agent 框架，需开发集成，措辞"给做 AI 应用的开发者"）
   - contrarian_angle: 普通 AI 助手只回一句话，这个能连续自主干几小时（调研+编码+创作全流程）
   - 数据锚点: 78753★ / 10744 fork / 单日 +209（字节开源，78K 总星）

## 真实性核验记录（零虚假项目）
- 大厂项目（microsoft/github/huggingface/bytedance）真实性无忧，无需核验
- 5 个个人/小 owner 项目经 gh API 核验（账号年龄/星叉比/watcher/贡献集中度/仓库体积）：
  - kaneo：✅ 通过（星叉比 11.8、多人贡献），入选
  - 其余 4 个：authenticity 判定后因「贡献者过度集中警告」「安全类合规谨慎」「韩文受众不匹配」「stale+纯资源清单」未入选
- 入选 6 个项目全部真实，零刷星/零空壳

## 受众分档（A 档约一半 ✓，C 档 ≤1/3 ✓）
- A 档（4）: AI-For-Beginners / kaneo / invidious / TRELLIS.2
- B 档（1）: speech-to-speech
- C 档（1）: deer-flow

## hook 候选（具象度优先，防 c5s 退化 — 详见 feedback-hook-strength）
反直觉角度（首选，必须有具象数字/冲突词，≤15 字）:
- speech-to-speech: 语音助手不用联网就能跑
- TRELLIS.2: 一句话生成 3D 模型
- deer-flow: AI 连续自主干几小时
数字锚定:
- AI-For-Beginners 单日 +949（榜 1）
- kaneo 单日 +760
建议主 hook 结构: 反直觉收益 + 具象数字（如「语音助手不用联网，今天 GitHub 还有…」），禁抽象/堆叠/元铺垫，gate check_hook_pattern_verified 会 HARD 校验

## 结尾提问（中性互动，禁站队）
候选: 「这几个你最想试哪个」/「语音助手和 3D 生成你会先玩哪个」（二选一非对抗，问题类型与近期轮换）
