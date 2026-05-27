<div align="center">

# ClipForge Workspace

由 [ClipForge](https://github.com/Johnson-Jia/video-clipforge) 驱动的短视频产出仓库

AI 编排 + HyperFrames 渲染，全自动生成抖音竖屏短视频

</div>

---

## 项目简介

本仓库是 [ClipForge](https://github.com/Johnson-Jia/video-clipforge) 的视频产出存档。所有视频均由 ClipForge 技能通过 Claude Code 自动编排和生成——从内容分析、场景拆解、TTS 旁白、配乐选取到 HTML 渲染，全程无需人工干预。

**核心流水线（8 阶段 DAG）：**

```
env-check → content → design → narration → audio + assets(并行) → video → delivery → cleanup
                                       └→ movie-clips（条件：仅电影解读模式）
```

| 阶段 | 产出 | 说明 |
|------|------|------|
| Stage 0 | `.env-checked` | 环境依赖检查 |
| Stage 1 | `content_ready.txt` | 原始内容获取与整理 |
| Stage 2 | `design.md` | 视觉风格方向规范 |
| Stage 3 | `narration_segments.json` + `narration.txt` | 场景拆解与旁白文案 |
| Stage 4 | `narration.mp3` + `bgm.wav` + `segment_durations.json` | TTS 旁白 + BGM 配乐 |
| Stage 5 | `assets/manifest.md` | 视觉素材制备（可选） |
| Stage 6 | `index.html` + `output.mp4` + `output_no_bgm.mp4` | HTML 编写 + 渲染 |
| Stage 7 | `final.mp4` + `cover.png` + `douyin.md` | 封面 + 交付 + 抖音文案 |
| Stage 8 | `.cleaned` | 项目清理 |

**生成一支 45 秒的短视频大约消耗：**
- AI 模型调用（内容分析、文案撰写、视觉设计）
- edge-tts 语音合成（多轮分段）
- HyperFrames 视频渲染（CPU/GPU 密集）
- 网络资源（配乐下载、素材搜索、数据采集）

如果这些视频或素材对你有帮助，欢迎请创作者喝杯咖啡续命 ☕

毕竟，AI 不会累，但让 AI 干活的人会。你的每一杯，都是下一个开源项目的燃料。

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

## 视频模式

| 模式 | 触发条件 | 时长 | 场景数 | 说明 |
|------|---------|------|--------|------|
| **标准模式** | 多主题盘点 / 快速资讯 | 25-55s | 6-8 | 信息密度优先，让观众快速掌握核心信息 |
| **单主题深度解析** | 只聚焦一个主题 | 45-60s | 7-8 | 覆盖原理、能力、应用、技术栈等维度 |
| **电影解读模式** | 场景含 `video_clip` 类型 | 3-5min | 不限 | 含电影片段提取与拼接，触发 `movie-clips` 条件阶段 |

## 分类系统

ClipForge 通过分类配置（`categories/`）支持不同内容类型，每个分类覆盖通用规则中的特定部分：

| 分类 | 状态 | 说明 |
|------|------|------|
| `github` | 已启用 | GitHub Trending 热门项目盘点和深度解析 |
| `comics` | 规划中 | 漫画分类 |
| `novel` | 规划中 | 小说分类 |

分类配置覆盖范围：数据获取方式、选取策略、默认风格、TTS 音色、标签列表、封面徽章等。未指定的部分沿用通用规则。

## 目录结构

```
workspace/
├── covers/                              # 公共封面库（系列封面模板）
├── bgm/                                 # BGM 素材库（10 种风格 × 5 首变体，跨项目复用）
├── sources/                             # 内容源文件
│   ├── github-trending/                 #   GitHub Trending 月度汇总数据
│   ├── images/                          #   打赏二维码等公共图片
│   ├── GitHub项目分析报告/               #   单项目深度分析
│   ├── 互联网需求分析报告/               #   行业分析报告源文件
│   ├── ppt分析报告/                      #   PPT 开源工具评测
│   └── 最佳视频/                         #   精选视频参考
│
└── <YYYY>/<MM>/<DD>/                    # 按日期归档的视频项目
    ├── github-trending/                 #   每日 GitHub 热门视频
    ├── github-trending-weekly/          #   每周 GitHub 汇总视频
    ├── github-zhihu/                    #   每周知乎文章
    └── <项目名>/                        #   自定义主题视频
```

### 路径约定

所有路径使用英文，避免 Windows 中文编码问题。

| 概念 | 路径 | 说明 |
|------|------|------|
| 工作根目录 | `workspace/` | 所有项目的根 |
| 日目录 | `workspace/<YYYY>/<MM>/<DD>/` | 当天所有项目 |
| 项目目录 | `workspace/<YYYY>/<MM>/<DD>/<项目名>/` | 单个项目的完整工作空间 |
| 公共封面库 | `workspace/covers/` | 系列封面模板（daily / weekly / spotlight / internet-reports） |
| BGM 库 | `workspace/bgm/` | 配乐素材，10 种风格各 5 首，保留原始文件供复用 |
| 源文件 | `workspace/sources/` | 报告、数据等内容原文 |

## 视频项目

### 制作中的文件结构

```
<项目目录>/
├── design.md                  # Stage 2 视觉风格定义
├── narration.txt              # Stage 3 旁白文案
├── narration_segments.json    # Stage 3 分段旁白定义
├── segment_durations.json     # Stage 4 分段实际时长 + BGM 音量
├── narration.mp3              # Stage 4 合并旁白（嵌入 HTML <audio>）
├── narration.srt              # Stage 4 字幕文件
├── bgm.wav                    # Stage 4 配乐（嵌入 HTML <audio>）
├── assets/                    # Stage 5 视觉素材（可选阶段）
│   └── manifest.md            #   素材清单
├── index.html                 # Stage 6 HTML 组合（含 <audio> 嵌入）
├── output.mp4                 # Stage 6 渲染输出（含旁白+BGM）
├── output_no_bgm.mp4          # Stage 6 渲染输出（仅旁白）
├── cover.html                 # Stage 7 封面 HTML
├── cover.png                  # Stage 7 封面图
├── douyin.md                  # Stage 7 抖音发布文案（3 套风格）
├── final.mp4                  # Stage 7 最终成品（含封面帧+BGM）
└── final_no_bgm.mp4           # Stage 7 最终成品（含封面帧，仅旁白）
```

### 电影解读模式（额外文件）

当场景包含 `video_clip` 类型时，`movie-clips` 条件阶段自动触发，增加以下文件：

```
<项目目录>/
├── clips_16x9/                # 提取的电影片段（16:9 原始比例）
├── movie_audio.wav            # 电影原音合并
└── clip_durations.json        # 片段实际时长
```

### 清理后的文件结构

Stage 8 自动删除中间产物，保留核心产出物和重生成所需的文件：

**视频项目：**

```
<项目目录>/
├── final.mp4                  # 最终视频（含 BGM）
├── final_no_bgm.mp4           # 无 BGM 版本（仅旁白）
├── output.mp4                 # 渲染原始（换封面需要）
├── output_no_bgm.mp4          # 渲染原始无 BGM（换封面需要）
├── cover.html                 # 封面 HTML（可重渲染）
├── cover.png                  # 封面图
├── index.html                 # HTML 组合（可重渲染）
├── design.md                  # 视觉风格
├── narration_segments.json    # 分段旁白定义
├── narration.txt              # 旁白文案
├── segment_durations.json     # 分段时长
├── narration.mp3              # 合并旁白（可选保留）
└── douyin.md                  # 抖音文案
```

**文章项目：**

```
<项目目录>/
├── article.md                 # 文章正文
├── cover.png                  # 封面图
├── content.md                 # 内容摘要
└── raw_trending.json          # 原始数据（GitHub 项目）
```

## BGM 素材库

`bgm/` 目录按风格分类存储配乐，每种风格 5 首变体。来源为 Pixabay 无版权音乐（免版税，可商用）。

| 风格 | 文件前缀 | 适用场景 |
|------|---------|---------|
| Bold Energetic | `bold-energetic-*` | 科技动态、项目盘点 |
| Clean Corporate | `clean-corporate-*` | 专业解读、行业报告 |
| Dark Premium | `dark-premium-*` | 深度分析、产品评测 |
| Warm Editorial | `warm-editorial-*` | 温暖叙事、人物故事 |
| Neon Electric | `neon-electric-*` | 前沿科技、赛博朋克 |
| Pastel Soft | `pastel-soft-*` | 生活化、治愈话题 |
| Jewel Rich | `jewel-rich-*` | 高端质感、精品推荐 |
| Monochrome | `monochrome-*` | 极简风格、数据展示 |
| Nature Earth | `nature-earth-*` | 自然主题、环保话题 |
| Warm Ambient | `warm-ambient*` | 轻松背景、氛围铺垫 |

配乐选取优先级：用户自提供 > BGM 素材库 > yt-dlp 下载 > Pixabay 搜索 > AI 二创（需参考样本）。

## DAG 依赖图

```
env-check → content → design ─┬→ narration → audio ──┬→ video → delivery → cleanup
                               │                assets ┘
                               └→ assets
                                                  narration → movie-clips（条件）
```

| 依赖类型 | 含义 | 示例 |
|---------|------|------|
| `requires` | 硬依赖，必须完成 | audio 依赖 narration |
| `requires_any` | 条件依赖，触发时变硬依赖 | audio 等待 movie-clips |
| `optional` | 可选阶段，不阻塞下游 | assets 可跳过 |
| `condition` | 条件触发判断 | movie-clips 检测 video_clip 场景 |

## Git LFS

本仓库使用 Git LFS 管理大文件（`.wav` 等）。克隆后请确保已安装：

```bash
git lfs install
```

## 关联项目

- **[ClipForge](https://github.com/Johnson-Jia/video-clipforge)** — Claude Code 技能，负责视频编排和制作
- **[HyperFrames](https://github.com/heygen-com/hyperframes)** — HTML 视频渲染引擎

## License

[Apache License 2.0](https://github.com/Johnson-Jia/video-clipforge/blob/main/LICENSE)
