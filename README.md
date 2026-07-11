<div align="center">

# GitHub 星探 · 视频存档

每天用 AI 把 GitHub 上最火的项目变成 45 秒短视频。

<!-- STATS -->
**59 天 · 137 条视频 · 6 个系列 · 全自动**
<!-- /STATS -->

数据驱动 · 开源解读 · 行业趋势

</div>

---

<div align="center">

**「什么样的人会关注一个讲开源项目的频道？——那些心里还相信"好东西应该分享给所有人"的人。」**

<a href="2026/06/06/github-star-intro/">
<img src="2026/06/12/clipforge-intro/cover_temp.png" width="320" alt="观看频道介绍" />
</a>

</div>

---

## 系列封面

每一条视频都由 [ClipForge](https://github.com/Johnson-Jia/video-clipforge) 自动生成 — 从数据抓取、文案编写、配音配乐到视频渲染，全程 AI 完成，无需人工干预。

<div align="center">

| | | | | |
|:---:|:---:|:---:|:---:|:---:|
| <img src="covers/cover-daily.png" width="150"> | <img src="covers/cover-spotlight.png" width="150"> | <img src="covers/cover-tech-dispatch.png" width="150"> | <img src="covers/cover-internet-reports.png" width="150"> | <img src="covers/cover-weekly.png" width="150"> |
| GitHub 星探<br>每日热门 | 开源亮点<br>单项目深度 | 科技速递<br>行业趋势 | 互联网报告<br>深度解读 | 周度汇总<br>一周精选 |

</div>

---

## 月度榜单

<!-- BEGIN MONTHLY -->
每天推荐的 GitHub 项目汇总到月度文档，点击查看完整榜单：

| 月份 | 链接 |
|:---|:---|
| 2026 年 7 月 | [GitHub Trending 7 月榜单](sources/github-trending/2026-07.md) |
| 2026 年 6 月 | [GitHub Trending 6 月榜单](sources/github-trending/2026-06.md) |
| 2026 年 5 月 | [GitHub Trending 5 月榜单](sources/github-trending/2026-05.md) |
<!-- END MONTHLY -->

---

## 近期作品

<!-- BEGIN RECENT -->
### 每日热门 · GitHub Trending

| 日期 | 作品 |
|:---|:---|
| 7月11日 | [GitHub 每日热门](2026/07/11/github-trending/) |
| 7月10日 | [GitHub 每日热门](2026/07/10/github-trending/) |
| 7月9日 | [GitHub 每日热门](2026/07/09/github-trending/) |
| 7月8日 | [GitHub 每日热门](2026/07/08/github-trending/) |
| 7月7日 | [GitHub 每日热门](2026/07/07/github-trending/) |

### 周度汇总 · Weekly

| 日期 | 作品 |
|:---|:---|
| 7月6日 | [GitHub 周度热门汇总](2026/07/06/github-trending-weekly/) |
| 6月29日 | [GitHub 周度热门汇总](2026/06/29/github-trending-weekly/) |
| 6月22日 | [GitHub 周度热门汇总](2026/06/22/github-trending-weekly/) |

### 深度解析

| 日期 | 作品 |
|:---|:---|
| 7月11日 | [沪江：1.87亿美金烧光](2026/07/11/goldminer/) |
| 7月5日 | [AI转型 E03：战略启动总览](2026/07/05/tutorial-e03-intro/) |
| 7月5日 | [AI转型 E03：转型卡在预算](2026/07/05/tutorial-e03-hook/) |
| 7月5日 | [AI转型 E03：目标量化](2026/07/05/tutorial-e03-goal/) |
| 7月5日 | [AI转型 E03：预算4块成本](2026/07/05/tutorial-e03-cost/) |

> 查看 [`2026/`](2026/) 目录浏览全部 137 条视频。
<!-- END RECENT -->

---

## 这些视频是怎么做的

<div align="center">

**[ClipForge](https://github.com/Johnson-Jia/video-clipforge)** — 把知识变成短视频的 AI 管线

告诉它你想讲什么，它帮你写稿、配音、做画面、出成片。

想在自己的领域做同样的事？ → **[了解 ClipForge →](https://github.com/Johnson-Jia/video-clipforge)**

</div>

---

> **以下为仓库结构和技术细节，面向开发者和贡献者。**

---

## 目录结构

```
workspace/
├── covers/                              # 系列封面模板（daily / weekly / spotlight / tech-dispatch / internet-reports）
├── bgm/                                 # BGM 素材库（17 种风格 × 2-10 首变体，跨项目复用）
├── sources/                             # 内容源文件（报告、数据、参考资料）
├── evolution/                           # 评估系统（模式检测、规则阈值进化、项目评估轨迹）
│
└── <YYYY>/<MM>/<DD>/                    # 按日期归档的视频项目
    ├── github-trending/                 #   每日 GitHub 热门视频
    ├── github-trending-weekly/          #   每周 GitHub 汇总视频
    ├── github-zhihu/                    #   每周知乎文章
    └── <项目名>/                        #   自定义主题视频
```

### 视频项目文件结构

清理后的项目目录保留核心产出物：

```
<项目目录>/
├── final.mp4                  # 最终视频（含 BGM）
├── final_no_bgm.mp4           # 无 BGM 版本（仅旁白）
├── cover.png                  # 封面图
├── cover.html                 # 封面 HTML（可重渲染）
├── index.html                 # HTML 组合（可重渲染）
├── design.md                  # 视觉风格
├── narration.txt              # 旁白文案
├── narration_segments.json    # 分段旁白定义
├── segment_durations.json     # 分段时长 + BGM 音量
├── douyin.md                  # 抖音发布文案（3 套风格）
└── narration.mp3              # 合并旁白
```

## 视频模式

| 模式 | 时长 | 场景数 | 说明 |
|------|------|--------|------|
| **标准模式** | 25-55s | 6-8 | 信息密度优先，多项目盘点 |
| **单主题深度解析** | 45-60s | 7-8 | 覆盖原理、能力、应用等维度 |
| **电影解读模式** | 3-5min | 不限 | 含电影片段提取与拼接 |

## BGM 素材库

<!-- BEGIN BGM -->
`bgm/` 目录按风格分类存储配乐，每种风格 2-10 首变体。来源为 Pixabay 无版权音乐（免版税，可商用）。当前共 **17** 种风格：

| 风格 | 适用场景 |
|------|---------|
| Bold Energetic | 科技动态、项目盘点 |
| Chill Lofi | 轻松氛围、日常分享 |
| Cinematic Grand | 电影级质感、宏大叙事 |
| Clean Corporate | 专业解读、行业报告 |
| Dark Premium | 深度分析、产品评测 |
| Epic Trailer | 震撼开场、重磅发布 |
| Epic Uplifting | 高潮推进、成就展示 |
| Inspiring Motivational | 激励叙事、成长故事 |
| Jewel Rich | 高端质感、精品推荐 |
| Monochrome | 极简风格、数据展示 |
| Motivational Energy | 积极向上、行动力驱动 |
| Nature Earth | 自然主题、环保话题 |
| Neon Electric | 前沿科技、赛博朋克 |
| Pastel Soft | 生活化、治愈话题 |
| Retro 80s | 复古怀旧、霓虹回忆 |
| Upbeat Pop | 活力节奏、轻松愉快 |
| Warm Editorial | 温暖叙事、人物故事 |
<!-- END BGM -->

## Git LFS

本仓库使用 Git LFS 管理大文件（`.wav` 等）。克隆后请确保已安装：

```bash
git lfs install
```

## 关联项目

- **[ClipForge](https://github.com/Johnson-Jia/video-clipforge)** — AI 短视频制作管线，负责从内容到成片的全流程编排
- **[HyperFrames](https://github.com/heygen-com/hyperframes)** — HTML 视频渲染引擎

## 支持作者

如果这些视频或素材对你有帮助，欢迎请创作者喝杯咖啡 ☕

毕竟，AI 不会累，但让 AI 干活的人会。

<table>
  <tr>
    <td align="center">
      <strong>支付宝</strong><br/>
      <img src="sources/images/ali_pay_qrcode.jpg" width="200" alt="支付宝">
    </td>
    <td align="center">
      <strong>微信</strong><br/>
      <img src="sources/images/wechat_pay_qrcode.png" width="200" alt="微信">
    </td>
  </tr>
</table>

## License

[Apache License 2.0](https://github.com/Johnson-Jia/video-clipforge/blob/main/LICENSE)
