# 内容摘要

## 来源
分类数据（GitHub Trending daily，2026-07-04，gh API 验证 20/20 真实，avatar 已下载）

## 核心主题
2026-07-04 GitHub 每日热门项目盘点。本期主题「工具/效率」——围绕「省 token、换角度看开发工具」展开，覆盖开发工具链 / UI 设计系统 / 自托管娱乐应用 / 机器学习系统教材四个不同方向，避免单一 AI Agent 扎堆。钩子主力是 caveman（用穴居人方式说话砍 65% token，强反直觉）。

## 关键信息点
- caveman：Claude Code 技能，让 AI 用穴居人简短方式说话，单日涨 2851 星（涨幅最高）
- graphify：AI 编码助手技能，把任意文件夹（代码/SQL/文档/图片）变可查询知识图谱
- herdr：Rust 写的终端 agent 多路复用器，类 tmux 但面向 AI agents
- astryx：大厂开源的可定制、agent-ready 设计系统
- romm：自托管 ROM 游戏库管理器，Docker 一键部署，带漂亮 GUI
- cs249r_book：机器学习系统开源教材（连续霸榜，快速带过）

## 数据（2026-07-04 gh API 实时）

| 项目 | 语言 | 总星 | 今日涨幅 | 受众 |
|------|------|------|---------|------|
| JuliusBrussee/caveman | JavaScript | 82.9K | +2851 | B 半可用 |
| safishamsi/graphify | Python | 77.1K | +937 | B 半可用 |
| ogulcancelik/herdr | Rust | 10.8K | +513 | B 半可用 |
| facebook/astryx | TypeScript | 4.6K | +943 | A 普通可用 |
| rommapp/romm | Python | 9.8K | +236 | A 普通可用 |
| harvard-edge/cs249r_book | Python | 26.1K | +792 | A 普通可用 |

## 反直觉角度（每项目挖一个 contrarian_angle）
- caveman：通常省 token 靠压缩上下文/换模型；这个反其道——让 AI「说话方式变短」，用穴居人语法砍 65% token，思路反常识
- graphify：一堆代码 + 数据库 schema + 文档通常散在各处；这个把它们织成一张可查询的知识图谱，整个仓库变一个可问的图
- herdr：终端里跑多 agent 通常要开多个 tmux 窗口手动切换；这个像 tmux 但为 AI agent 设计，一个面板管多个 AI 并行
- astryx：设计系统通常是大厂定制闭源；这个开源还能让 AI agent 直接调用定制
- romm：游戏 ROM 管理通常要桌面软件；这个自托管 Docker 部署，浏览器即开即用
- cs249r_book：ML 系统教材通常几百块买书；这个高校课程教材全开源免费读

## 原始素材路径
- 数据：`workspace/2026/07/04/github-trending/raw_trending.json`（20 项目 gh API 验证）
- 昨日数据：`workspace/2026/07/03/github-trending/raw_trending.json`（识别霸榜项）
- avatar：`assets/avatars/{owner}.png`（fetch_avatars.py 已下载）
