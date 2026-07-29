# 内容摘要

## 来源
GitHub Trending daily（2026-07-29），raw_trending.json 12 项目，gh API 交叉验证数据真实性

## 核心主题
今日 GitHub 榜单跨方向：浏览器 3D 建筑创作工具领衔，搭配半年涨到 23 万星的 AI 编程优化工具、本地语音助手、十六年 CI/CD 老牌、微软 AI 治理工具包。NON-AI 项目占一半，破近期 AI 题材主导的同质化。

## 关键信息点
- 浏览器里直接造 3D 建筑并分享（pascalorg/editor，非 AI，A 档普通人即开）
- AI 编程助手的性能优化系统，半年涨到 23 万星（affaan-m/ECC，真实性已验证：star-fork 6.6:1 健康，1516 提交+多贡献者）
- 开源模型本地搭建语音助手，数据不外传（huggingface/speech-to-speech，HF 大厂）
- 十六年老牌 CI/CD 自动化服务器仍在今日榜单（jenkinsci/jenkins，非 AI 基建）
- 微软亲自下场做 AI 智能体治理，覆盖 OWASP 智能体安全榜单全部十项（microsoft/agent-governance-toolkit）
- 好看现代的终端文件管理器（yorukot/superfile，非 AI，近两期已展开，今日快报增量）

## 数据（gh API 实时，2026-07-29）
| 项目 | 总星 | 今日 | fork | 语言 | 受众 |
|------|------|------|------|------|------|
| pascalorg/editor | 18656 | +415 | 2524 | TypeScript | A 普通可用 |
| affaan-m/ECC | 234771 | +692 | 35773 | JavaScript | B 半可用（开发者） |
| huggingface/speech-to-speech | 7198 | +177 | 950 | Python | B 半可用 |
| jenkinsci/jenkins | 26064 | +180 | 9686 | Java | C 开发者向 |
| microsoft/agent-governance-toolkit | 5173 | +17 | 833 | Python | C 开发者向 |
| yorukot/superfile | 21455 | +660 | 695 | Go | B 半可用（快报） |

## 真实性验证结论
- **affaan-m/ECC（234K★）**：通过（0 HARD）。owner 账龄 3 年/27 公开仓库/8742 follower；star-fork=6.6:1（健康，非刷星典型 >100:1）；主贡献者 affaan-m 1516 提交+dependabot/pangerlkr(47)/gaurav0107(25) 等多真实贡献者；仓库 48MB 实质内容；watcher 1224（0.52%，临界过线）。234K 为真实病毒式增长，非刷榜。
- **paperswithbacktest/awesome-systematic-trading**：不虚假但 inactive（pushed 2025-01-22，552 天未更新），awesome-list 性质虽可解释停更，作为「今日热门」推荐会误导观众，已剔除补选 superfile 快报位。
- **jenkinsci/jenkins**：通过。2010 年创建老牌，star-fork=2.7:1 成熟基建比例，watcher 892 健康。

## 排除/剔除
- 排除列表命中：无（ruvnet/RuView 不在今日榜单）
- 剔除：paperswithbacktest/awesome-systematic-trading（inactive 552 天，详见上）
- 避免重复展开：bradautomates/claude-video、moeru-ai/airi、opengeos/GeoLibre（0728 已展开，今日不入选）；yorukot/superfile 仅快报位

## 原始素材路径
raw_trending.json（PROJECT_DIR，gh API + python_requests 采集，cache_warning=false，project_count=12）
