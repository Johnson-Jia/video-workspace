# Stage 1 内容分析 — GitHub Trending 2026-07-08

## 数据源
- `raw_trending.json`：13 个项目，python_requests + gh API 双源交叉验证
- 排除：ruvnet/RuView（永久排除，虚假不可实现）；bradautomates/claude-video（size 76KB < 100KB HARD 剔除）

## 选题（6 个，5 新 + 1 霸榜带过）

### 1. MadsLorentzen/ai-job-search（涨星王，+2402★）
- **A 档普通可用**：fork 即用，AI 求职框架
- **能力**：评估岗位匹配度、改简历、写求职信、准备面试，基于 Claude Code
- **反直觉钩子**：求职这件高度个性化的事，居然能整成一个框架让 AI 跑流程
- **数字**：今日 +2402，总星 10704，fork 3628（fork 数说明真有人在用）
- **钩子定位**：开场 hook 首选，涨星王 + 反直觉（AI 代跑求职流程）

### 2. Zackriya-Solutions/meetily（霸榜，+1781★）
- **A 档普通可用**：本地会议纪要，macOS/Windows
- **霸榜处理**：3-4s 快速带过，"上次说的 meetily 又涨了近一千八"，不重复介绍功能
- **增量信息**：今日 +1781，总星破 2 万（20667）

### 3. kyutai-labs/pocket-tts（+510★）
- **B 档半可用**：kyutai 出品，CPU 跑 TTS
- **反直觉**：TTS 通常吃 GPU 或调云 API，这个 100M 参数 CPU 6x 实时跑
- **数字**：今日 +510，总星 6139
- **钩子备选**：CPU 跑 TTS 不用 GPU，平民化反直觉

### 4. iOfficeAI/OfficeCLI（+802★）
- **B 档半可用**：给 AI agent 用的 Office 命令行
- **反直觉**：Office 居然有命令行版，还能让 AI 自动读写 Word/Excel/PPT
- **数字**：今日 +802，总星 9881，单文件免装 Office
- **利益翻译**：让 AI 批量处理 Office 文档，省手工

### 5. TencentCloud/CubeSandbox（+665★）
- **C 档开发者向**：腾讯云做的 agent 沙盒
- **反直觉**：大厂亲自下场做轻量沙盒（通常大厂做重平台）
- **数字**：今日 +665，总星 8437
- **受众措辞**：给开发者，agent 跑代码的隔离环境

### 6. addyosmani/agent-skills（+1311★）
- **C 档开发者向**：addyosmani（Chrome 团队）出品，agent 工程技能库
- **反直觉**：agent 也要"技能库"沉淀工程经验，像程序员积累套路
- **数字**：今日 +1311，总星 72093（总星高，说明持续受欢迎）
- **受众措辞**：给开发者，生产级工程技能

## 题材轮换对照（近 5 期）
- 07/03：6 个 AI 工具合集（hook「6个AI完成不可能任务」）
- 07/04：AI 说穴位（system_prompts_leaks 相关，hook「让AI说穴位」）
- 07/05：AI 模型记录（hook「让AI学山歌」）
- 07/06：7/6 GitHub 杀入几个新项目（meetily 在内）
- 07/07：英文记录全屏不识别（system_prompts_leaks）

**本期差异化**：
- hook 主题换「求职/找工作」+「CPU 跑 TTS」反直觉，避开「杀入/猛项目」疲劳词
- 项目集 5 新，meetily 霸榜带过不重复展开
- 叙事结构：涨星王开场（求职反直觉）→ 霸榜带过 → CPU TTS 反直觉 → Office 命令行 → 大厂沙盒 → agent 技能库收尾

## 受众分布
- A 档（普通可用）：2 个（ai-job-search、meetily）— 约三分之一，符合 github 受众筛选规范
- B 档（半可用）：2 个（pocket-tts、OfficeCLI）
- C 档（开发者向）：2 个（CubeSandbox、agent-skills）— 约三分之一，标「给开发者」

## 数据保真
所有中文描述基于 raw_trending.json 的 description 字段翻译，未从 owner/repo 名推断。原英文 description 内嵌于 content_ready.txt 每行（原: ...）段，供保真度门禁校验。

## 平台合规预检
- 无违禁工具（翻墙/盗版/破解）
- 无医疗资质内容
- 无真实人名/校名（owner/repo 是项目名非人名）
- 无绝对化用语（禁用词清单已规避：最强/第一/绝对/必备/神器）
- 无搜索引导话术
