# GitHub Trending 2026-07-13 内容分析

## 选题方向
今日 6 片覆盖 6 个方向：金融 AI / 数据库重写 / AI 安全 / 智能家居 IoT / 反 AI 设计 / AI 控电脑。
题材轮换：避免纯 AI 扎堆（自进化 P-topic-ai 已 deprecated，连续 6 次下降），纳入 home-assistant（生活 IoT）+ pgrust（数据库内核）两个非 AI 强题材。

受众配比：A 普通可用 3 个（home-assistant / hallmark / DesktopCommanderMCP）+ B 半可用 2 个（Vibe-Trading / destructive_command_guard）+ C 开发者 1 个（pgrust），A 档占一半 ✓。

## 项目分析

### 1. HKUDS/Vibe-Trading（今日涨星王 +776）
- 背景：香港大学数据科学实验室 HKUDS（12.2k followers，91 repos），学术背景
- 亮点：个人交易 AI Agent，集成回测、量化策略、多 agent 协作、MCP 支持
- 钩子：今日涨星最高（776），「让 AI 帮你做交易」强利益
- 合规口径：讲技术架构（AI agent + 回测 + 量化），不讲投资建议、不荐股、不承诺收益

### 2. malisper/pgrust（+518）
- 亮点：用 Rust 从零重写 PostgreSQL，已通过全部 Postgres 回归测试——数据库内核重写是硬核工程
- 钩子：技术震撼（重写工业级数据库）
- 受众：C 档，旁白定调「给做数据库的开发者」，不伪装普通人能用
- owner：malisper（2013 年老号，35 repos）

### 3. Dicklesworthstone/destructive_command_guard（+444）
- 亮点：阻挡 AI agent 执行 rm -rf / 危险 git 命令的守护工具，AI 安全赛道
- 钩子：反直觉 + 安全焦虑（AI 越来越强，没它可能删你硬盘 / 推危险命令）
- 受众：用 AI 编程的开发者（B 档，CLI 配置）
- owner：Dicklesworthstone（知名 AI 技术作者，2.8k followers，187 repos）

### 4. home-assistant/core（总 89K 星，+404）
- 背景：2013 年老牌开源智能家居，行业标杆，本地控制 + 隐私优先
- 亮点：总星 89K 震撼，Docker / 树莓派一键部署，集成千余设备
- 钩子：非 AI 题材轮换 + 总星数据震撼
- 受众：A 普通人（智能家居爱好者），「自己搭智能家居，数据不出门」

### 5. Nutlope/hallmark（+210）
- 亮点：反 AI 味设计 skill，给 Claude Code / Cursor / Codex 用，去除设计里的「AI 味」（anti-AI-slop）
- 钩子：反 AI 题材（meta 角度新颖）——用 AI 的工具去反 AI 的毛病
- 受众：用 AI 做设计/前端的人（A/B 档）
- owner：Nutlope（8.2k followers，知名开源作者）

### 6. wonderwhy-er/DesktopCommanderMCP（+207）
- 亮点：MCP 服务器，让 Claude 控制终端、文件系统搜索、差异编辑——AI 接管整台电脑
- 钩子：强利益（AI 操作你的电脑）
- 受众：A 普通人用 AI 操电脑
- owner：wonderwhy-er（2011 年老号）

## 钩子方向建议（SubAgent-1 stage0.5 参考）
数字锚定 + AI 安全反直觉。例：「今天 GitHub 涨星最高的一个，单日近八百星，让 AI 帮你做交易；还有一个更反直觉——专门防着 AI 别删你硬盘」。避免纯 AI 盘点感，突出 home-assistant（89k 总星生活向）做题材平衡。

## 合规
- Vibe-Trading：讲技术架构不荐股、不承诺收益
- 已排除：FlClash（翻墙代理红线）/ Wand-Enhancer（WeMod 游戏作弊修改器）/ sharpemu（PS5 模拟器版权灰色）
- 无 exclusion_list 命中（ruvnet/RuView 不在今日榜）

## 真实性验证（gh API，2026-07-13）
6 项目全部通过：0 HARD 违规，pgrust/destructive_command_guard/hallmark 各 1 轻警告（star-fork 比或 watcher 比略偏），但 owner 均老号 + 多仓库 + 高 followers，信誉支撑，判定通过。
