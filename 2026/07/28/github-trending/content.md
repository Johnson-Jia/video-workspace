# 内容摘要

## 来源
分类数据（GitHub Trending daily，2026-07-28）— `raw_trending.json`（15 项目，python_requests+gh_api 抓取，cache_warning=false，7 overlapping + 8 new entries，活跃度 14/15 > 80% 门禁）

## 核心主题
7月28日 GitHub Trending 速览——本期主线「AI 能力扩展」：3 个 AI 项目分别让 AI 学会看视频、跨平台查资料、陪玩家打游戏，配云原生 GIS 地图与老牌 CI/CD 基建，区别于近期的断网群聊/AI 审美/AI 队友/企业转型主题。

## 关键信息点
- AI 伴侣走向自托管：把 AI 角色装在自己电脑上，数据自己掌握，还能进游戏陪玩（airi）
- 专业级 GIS 跑进浏览器：地图可视化+空间分析，数据本地不上云，多端通吃（GeoLibre）
- AI 反向操作——不生成视频，而是「看懂」任意视频：下载、抽帧、转录全交给 AI（claude-video）
- AI 当调研员：跨 Reddit/X/YouTube 等多平台研究任意主题，输出有据可查的总结（last30days-skill）
- 老牌 CI/CD 服务器新上榜：自动化流水线领域的常青树回到 Trending（jenkins）
- 蓝牙断网群聊连续霸榜，本期快报位提及增量（bitchat）

## 数据（gh api 实时，2026-07-27T23:34 UTC）
| 项目 | 语言 | 总星 | 今日涨 | 受众 |
|------|------|------|--------|------|
| moeru-ai/airi | TypeScript | 44003 | +554 | A 普通可用 |
| opengeos/GeoLibre | TypeScript | 2647 | +420 | A 普通可用 |
| bradautomates/claude-video | Python | 11037 | +412 | B 半可用 |
| mvanhorn/last30days-skill | Python | 54148 | +221 | B 半可用 |
| jenkinsci/jenkins | Java | 25873 | +179 | C 开发者向 |
| permissionlesstech/bitchat | Swift | 32202 | +2344 | A 普通可用（快报位） |

## 选题规划对齐
- 题材：工具/效率（AI 能力扩展为主），topic-tool
- 受众配比：A 档 3 个（airi/GeoLibre/bitchat）= 50%，B 档 2 个，C 档 1 个（≤1/3）✓
- 项目类型多样性：AI 伴侣/GIS 地图/AI 视频理解/AI 调研/CI-CD 基建/蓝牙通讯 = 6 方向 ✓
- hook 主题：AI 能力扩展（让 AI 看视频），区别近 7 期所有 hook 主题 ✓

## 真实性验证（gh api 全通过）
- airi：star/fork 10:1，watchers 166，owner moeru-ai 2024-03 老号 50 repos ✅
- GeoLibre：star/fork 7.6:1，watchers 21，owner opengeos（GIS 领域权威，168 repos/3860 followers）✅
- claude-video：star/fork 9.7:1，watchers 51，README 19.5KB + 完整 plugin/hooks/tests 结构（skill 项目体积小属正常，非空壳）✅
- last30days-skill：star/fork 11.5:1，watchers 199，owner mvanhorn 2010 老号 1894 repos ✅
- jenkins：Jenkins 官方仓库，watchers 892 ✅
- bitchat：star/fork 6.4:1，watchers 294 ✅

## 排除记录
- amnezia-vpn/amnezia-client（rank 2）—— VPN 客户端，国内平台违法风险，零容忍排除
- NanmiCoder/MediaCrawler（rank 6）—— 多平台爬虫（小红书/抖音/B站/快手），灰色敏感，排除

## 原始素材路径
`raw_trending.json`（PROJECT_DIR 根目录，gh api 实时数据）
