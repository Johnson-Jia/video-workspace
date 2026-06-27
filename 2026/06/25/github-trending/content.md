# 内容获取记录 — GitHub Trending 2026-06-25（daily）

## 数据源（三源交叉验证）
- 主源：scripts/github_trending.py（python_requests 直连抓取）
- 验证源：gh API 逐项验证 13/13 项目实时数据
- 昨日比对：workspace/2026/06/24/github-trending/raw_trending.json

## 采集结果
- 日期：2026-06-25
- 项目数：13（>= 8 门禁通过）
- 活跃度：13/13 recently pushed（100%，>= 80% 通过）
- 缓存检查：Fresh（与昨日 5 重叠 / 8 新上榜，非缓存命中）

## 真实性验证（authenticity_verification，gh API 九项检查）
对 6 个入选项目执行真实性验证，全部通过：
- ✅ calesthio/OpenMontage：1 警告（贡献者集中，但主贡献者提交 111 次足），0 HARD
- ✅ apple/container：苹果官方，贡献者多元（jglogan/katiewasnothere/dcantah），0 警告
- ✅ JCodesMore/ai-website-cloner-template：template 项目 fork 高属正常特性，0 HARD
- ✅ stablyai/orca：YC 背书，贡献者健康（nwparker/AmethystLiang/Jinwoo-H），0 HARD
- ✅ NousResearch/hermes-agent：Nous Research 知名 AI 组织背书，贡献者多元，0 HARD
- ✅ kunchenguid/no-mistakes：owner 2013 年老号健康，git hook 工具小众 watcher 偏少属合理特性，0 HARD

## 选取策略（selection_strategy）
- 排除列表过滤：本期 trending 未出现永久排除项
- 按 selection_strategy 优先级选取 6 个：钩子潜力 + 新上榜 + 涨星加速 + 跨圈补充
- 跨方向覆盖 6 个：AI视频 / 系统容器 / 成长型agent / 网站克隆 / agentIDE / git工具
- 受众分档：A 普通可用 2 个（apple/container、orca）+ B 半可用 4 个，A 档约占一半

## 下游交付
- 中文素材：content_ready.txt（6 项目，每个内嵌原始英文 description 作保真锚点）
- 全量数据：raw_trending.json（13 项目）
