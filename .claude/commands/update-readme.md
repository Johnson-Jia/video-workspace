---
name: update-readme
description: 扫描项目目录，更新 README.md 中的统计数据、月度榜单和近期作品，然后提交推送。
---

# README 自动更新

全自动执行。扫描 `2026/` 下所有已完成视频，更新 README 动态板块，提交并推送。

## Step 1: 扫描数据

```bash
# 所有已完成视频目录（按日期倒序）
find 2026/ -name "final.mp4" -printf '%h\n' | sort -r

# 月度榜单文件
ls sources/github-trending/*.md

# 系列封面数
ls covers/cover-*.png | wc -l

# BGM 风格列表（排除衍生文件，只取 base 风格名）
ls bgm/ | grep -E '^[a-z].*-[0-9]+\.(mp3|wav)$' | sed 's/-[0-9]*\..*//' | sort -u
```

## Step 2: 分类规则

对每个 `final.mp4` 所在目录名分类：

| 目录名模式 | 分类 |
|---|---|
| `*/github-trending`（不含 weekly） | 每日热门 |
| `*weekly*` | 周度汇总 |
| 其余 | 深度解析 |

## Step 3: 提取标题

读取每个项目的 `douyin.md`，按优先级提取标题：

1. `## 标题` 下方第一个非空行（去掉前导 `### ` 或 `**标题：**`）
2. `# 抖音文案 — ` 后的副标题部分
3. 都没有则用目录名生成人类可读标题（如 `project-nomad` → `Project Nomad`，`ai-gamedev-report` → `AI 游戏开发报告`）

特殊规则：
- `github-trending` 目录统一显示为 `GitHub 每日热门`
- `github-trending-weekly` 目录统一显示为 `GitHub 周度热门汇总`

## Step 4: 更新 README

### 统计行

找到 `<!-- STATS -->` 和 `<!-- /STATS -->` 之间的内容，替换：
- 天数 = 有 final.mp4 的日期目录去重数（`2026/MM/DD` 去重）
- 视频数 = final.mp4 总数
- 系列数 = `covers/cover-*.png` 数量

格式（注释和加粗文本各占独立行）：
```
<!-- STATS -->
**XX 天 · XX 条视频 · XX 个系列 · 全自动**
<!-- /STATS -->
```

### 月度榜单

替换 `<!-- BEGIN MONTHLY -->` 和 `<!-- END MONTHLY -->` 之间的内容。格式：

```markdown
| 月份 | 链接 |
|:---|:---|
| YYYY 年 M 月 | [GitHub Trending M 月榜单](sources/github-trending/YYYY-MM.md) |
```

按月份倒序（最新在上）。

### 近期作品

替换 `<!-- BEGIN RECENT -->` 和 `<!-- END RECENT -->` 之间的内容。每个类别取数：
- 每日热门：最近 **5** 条
- 周度汇总：最近 **3** 条
- 深度解析：最近 **5** 条（排除 `github-star-intro`，该项目已在顶部介绍区展示）

全部按日期倒序。日期格式中文：`6月7日`。链接路径以 `/` 结尾。

末尾加：
```
> 查看 [`2026/`](2026/) 目录浏览全部 XX 条视频。
```

### BGM 素材库

替换 `<!-- BEGIN BGM -->` 和 `<!-- END BGM -->` 之间的内容。

扫描 `bgm/` 目录，提取风格名（排除 `driving-*`、`tense-*`、`uplift-*`、`alexgrohl-*` 等衍生文件，只保留基础风格），每个风格生成一行。

更新风格总数（`当前共 **X** 种风格`）。每个风格需给出适用的场景描述。风格名称首字母大写转为人类可读（如 `bold-energetic` → `Bold Energetic`）。

**禁止修改 README 中其他任何内容。**

## Step 5: 提交推送

```bash
git add README.md
if ! git diff --cached --quiet; then
  git commit -m "auto-update README $(date +%Y-%m-%d)"
  git push || (sleep 5 && git push)
fi
```

push 失败重试一次。仍失败则停止，不强制推送。

## Step 6: 续期定时任务

执行完成后，查找包含 `update-readme` 关键词的 CronCreate，使用 `clipforge/shared/cron-renew` 续期。如果没有找到，创建新的：
- 定时：每天 03:00
- 命令：`/update-readme`
