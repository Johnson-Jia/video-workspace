# 2026-07-12 GitHub Trending 内容素材

## 数据来源
- raw_trending.json（24 项目，daily 模式，2026-07-11T23:34 UTC 抓取）
- 采集方式：python_requests + gh_api 双源交叉验证，24/24 真实性验证通过
- avatars 已预下载到 assets/avatars/（fetch_avatars.py）

## 排除列表命中
- 永久排除项目（命中跳过，不记录）：本期无命中

## 入选 5 个项目（按钩子潜力 + 多元题材 + 受众分档组合）

### 1. malisper/pgrust — 反直觉爆点（C 档·开发者向）
- avatar: assets/avatars/malisper.png
- 用途: Rust重写Postgres内核
- 语言: Rust
- stars_total: 2025 | stars_today: +789 | forks: 50
- 中文描述: 用 Rust 重写的 Postgres，目前已通过 100% 的 Postgres 回归测试
- 保真锚点（原: Postgres rewritten in Rust, now passing 100% of the Postgres regression tests）
- 反直觉角度：Postgres 是 30 年的 C 代码铁王座，一个开发者用 Rust 重写并通过 100% 回归测试——颠覆性在于"一个人重写工业级数据库内核还能完全兼容"，AI 辅助开发的代表案例
- 受众: C 开发者向（数据库内核，需开发者集成；旁白用「给做数据库的开发者」定调）

### 2. microsoft/PowerToys — Windows 效率工具集（A 档·普通可用）
- avatar: assets/avatars/microsoft.png
- 用途: Windows效率工具集
- 语言: C
- stars_total: 136421 | stars_today: +65 | forks: 8366
- 中文描述: 微软 PowerToys 是一组提升 Windows 生产力和自定义的实用工具集合
- 保真锚点（原: Microsoft PowerToys is a collection of utilities that supercharge productivity and customization on Windows）
- 反直觉角度：微软自家开源给所有人免费用——大厂下场做的"系统级瑞士军刀"，普通用户也能直接受益
- 受众: A 普通可用（GUI/桌面 app，开箱即用）

### 3. nasa/fprime — NASA 飞行软件开源（C 档·开发者向）
- avatar: assets/avatars/nasa.png
- 用途: NASA开源飞行软件框架
- 语言: C++
- stars_total: 11473 | stars_today: +64 | forks: 1731
- 中文描述: F´ - 一个飞行软件和嵌入式系统框架
- 保真锚点（原: F´ - A flight software and embedded systems framework）
- 反直觉角度：NASA 把送航天器上天的飞行软件框架开源给所有人——"上天的代码你也能用"，平民化专业航天能力
- 受众: C 开发者向（嵌入式系统框架，需 C++ 集成；旁白用「给做嵌入式/硬件的开发者」定调）

### 4. DayuanJiang/next-ai-draw-io — AI 改流程图（A 档·普通可用）
- avatar: assets/avatars/DayuanJiang.png
- 用途: AI自然语言画流程图
- 语言: TypeScript
- stars_total: 33277 | stars_today: +74 | forks: 3604
- 中文描述: 一个集成 AI 能力与 draw.io 图表的 Next.js Web 应用，允许通过自然语言指令创建、修改和增强图表，并由 AI 辅助可视化
- 保真锚点（原: A next.js web application that integrates AI capabilities with draw.io diagrams. This app allows you to create, modify, and enhance diagrams through natural language commands and AI-assisted visualization.）
- 反直觉角度：流程图不用手动画，自然语言交流 AI 就改——"画图从拖拽升级到说话"，普通人做专业图表
- 受众: A 普通可用（浏览器即开 Web 应用）

### 5. home-assistant/core — 本地智能家居（A 档·普通可用）
- avatar: assets/avatars/home-assistant.png
- 用途: 本地控制智能家居
- 语言: Python
- stars_total: 88677 | stars_today: +169 | forks: 38048
- 中文描述: 开源家庭自动化平台，把本地控制和隐私放在首位
- 保真锚点（原: 🏡 Open source home automation that puts local control and privacy first.）
- 反直觉角度：智能家居通常=数据传云端，这个项目反着来——本地控制、隐私至上，拔掉网线照样管家里的设备
- 受众: A 普通可用（Docker 一键 / 树莓派部署）

## 受众分档统计
- A 普通可用：3 个（PowerToys / next-ai-draw-io / home-assistant）→ 占 60%，满足"5 选 2-3 个"门槛
- C 开发者向：2 个（pgrust / fprime）→ 占 40%，≤一半，满足约束

## 未入选候选说明（备选）
- catchorg/Catch2 / abseil/abseil-cpp / chriskohlhoff/asio / zeux/meshoptimizer：纯 C++ 开发者库，C 档扎堆风险，本期已选 2 个 C 档，不再加
- google-labs-code/stitch-skills / davila7/claude-code-templates / anthropics/claude-cookbooks：claude-code / Agent skills 类近期已多次出现（07-08~11），避免疲劳
- wonderwhy-er/DesktopCommanderMCP / obra/superpowers / oven-sh/bun / vercel/next.js / hashicorp/terraform：07-09~11 刚展开，避免重复
- openai/plugins：3 年未大更新（pushed 2026-07-10 但仓库内容陈旧），真实性存疑降权
- prisma/prisma / dotnet/aspnetcore / cypress-io/cypress / ansible/ansible / nuxt/nuxt / actions/checkout：成熟框架/平台，新意不足
- microsoft/PowerToys / home-assistant 虽是常客但近期（07-08~11）未展开，可正常入选
