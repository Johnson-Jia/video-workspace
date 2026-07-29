# 内容摘要

## 来源
分类数据（GitHub Trending Weekly，since=weekly，fetched_at 2026-07-27T00:38 UTC，python_requests+gh_api 直连）。数据源已交叉验证，project_count=23，活跃度 22/23（Kronos 不活跃已降权剔除），cache_warning=false。

## 核心主题
第31周（07月20日-07月27日）GitHub 周榜盘点：本周涨星最猛的 14 个开源项目，按领域分四组——AI 编程助手、开发者效率工具、信息与学习、实用工具。最高一个一周涨了近一万六千星。

## 分组结构（14 项目 / 4 组）

### 组1·AI 编程助手（4 个，领域色：蓝）
- bojieli/ai-agent-book（+15909★）国内技术作者写的 AI Agent 设计原理开源书
- stablyai/orca（+7392★）管一群并行 agent 的开发环境，桌面/移动/服务器
- earendil-works/pi（+5389★）AI agent 工具包，统一接口+编程 agent CLI
- 1jehuang/jcode（+2909★）给代码用的智能 agent 框架

### 组2·开发者效率工具（4 个，领域色：橙）
- diegosouzapw/OmniRoute（+10912★）免费 AI 网关，一个接口接 290 多家服务商
- tirth8205/code-review-graph（+6006★）本地代码知识图谱，AI 编程只读关键部分
- Nutlope/hallmark（+4932★）反 AI 味设计技能，让设计不千篇一律
- ComposioHQ/awesome-claude-skills（+2820★）AI 技能精选资源集

### 组3·信息与学习（3 个，领域色：紫）
- koala73/worldmonitor（+12615★）实时全球情报仪表盘，AI 聚合新闻+地缘监测
- rohitg00/ai-engineering-from-scratch（+4317★）AI 工程从零学课程
- HKUDS/DeepTutor（+2199★）终身个性化辅导工具

### 组4·实用工具（3 个，领域色：金）
- every-app/open-seo（+3639★）开源 SEO 工具
- schollz/croc（+2993★）安全传文件，电脑到电脑
- CoreBunch/Instatic（+1893★）开源自托管可视化建站系统

## 关键信息点
- 周涨幅 TOP3：ai-agent-book(+15909)、worldmonitor(+12615)、skills(+12238，本期高频不选)
- 跨领域分布：AI 编程 4 + 开发工具 4 + 信息学习 3 + 实用工具 3，避免单一 AI Agent 同质化
- 受众配比：A 档普通可用 8 个（57%）、B 档 1 个、C 档开发者向 5 个（36%），符合 weekly 约一半可上手的配比
- ai-agent-book 是本周最大黑马（新书发布周暴涨），也是国内技术作者作品

## 排除与泛化
- ⛔ ruvnet/RuView（rank9 +5497）永久排除：WiFi 信号感知人体虚假宣传
- ⚠ ai-agent-book：description 含「李博杰 著」真实人名 → 旁白/画面泛化「国内技术作者」，原文锚点在 content_ready 保留（素材层保真）
- ⚠ DeepTutor：description 含 https URL → 旁白/画面去 URL，原文锚点保留
- ⚠ OmniRoute/open-seo/Instatic/jcode：原文 description 含商业品牌名/极限词 → 中文翻译泛化，原文锚点保留
- 不选 mattpocock/skills（近期高频 + skills 类与 hallmark/awesome-claude-skills 重复）、text-to-cad（涨幅偏低）、Kronos（不活跃）、t3code（描述空）

## 数据
- 数据源：raw_trending.json（23 项目，weekly stars_today 周涨幅已补全）
- 真实性验证：对 rank1/3/4/18 四个高涨幅项目 gh api 复核 watchers/contributors/size，全部通过（watchers 62-86 健康，star/fork 9-14:1，size 实质内容）

## 原始素材路径
raw_trending.json（PROJECT_DIR/raw_trending.json）
