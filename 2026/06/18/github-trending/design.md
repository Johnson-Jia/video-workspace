# 视觉设计 · 2026-06-18 GitHub Trending

## 元信息

- **orientation**: portrait
- **orientation_source**: default
- **category**: github
- **mode**: standard
- **scene_count**: 6
- **total_target_duration**: 约 60-75 秒（250-380 字旁白）

## 沉浸模式

- **immersion_mode**: dark_tech
- **核心范式**：暗色科技风，深蓝/深紫渐变基底 + 双色光晕（暖橙 + 冷蓝）+ 项目卡片纵向铺满
- **理由**：本期覆盖 AI 代码智能 / 开发者技能 / AI agent / 安卓隐私 / 设计 / 项目管理，多元题材需统一暗色基底收敛视觉，暖橙（动作/数字锚点）与冷蓝（理性/数据）双色光晕分担 hook 冲击与展开。

## 色板

| 角色 | 色值 | 用途 |
|------|------|------|
| 基底主色 | `#0B1426`（深蓝近黑） | 全局背景 |
| 基底渐变 | `#1A1B3A` → `#2D1B4E`（深蓝→深紫） | 背景层渐变 |
| 强调暖色 | `#FF8C32`（暖橙） | 数字锚点 / 涨幅 / hook 冲击 |
| 强调金 | `#FFD580`（柔金） | 暖橙高光配对 |
| 强调冷色 | `#4DA8DA`（亮蓝） | 数据 / 项目名 / 理性表达 |
| 文字主色 | `#F5F7FA`（近白） | 正文 |
| 文字次色 | `#A8B3C5`（雾灰蓝） | 注释 / 副信息 |

## 字体

- **标题/数字**：思源黑体 Heavy / 字体调色板 default
- **正文**：思源黑体 Regular
- **代码/项目名**：JetBrains Mono / 等宽
- **最小字号门禁**：竖屏正文 ≥ 36px，数字/标题 ≥ 72px

## 故事板（6 场景）

### 场景 0 — Hook（数字锚定 + 反直觉）
- **emotion**: shock
- **visual_type**: dark_tech_card
- **画面**：全屏暗背景，中央暖橙巨字「砍掉 99%」砸入，副标题冷蓝「AI 看代码的输入」。底部冷蓝小字「6月18日 涨星榜」。光晕：橙金双层 glow 由中心向外脉冲。
- **焦点**：「砍掉 99%」数字
- **节奏**：单 phase，3-4 秒

### 场景 1 — codebase-memory-mcp（反直觉爆点展开）
- **emotion**: curiosity
- **visual_type**: dark_tech_card
- **画面**：ProjectFullCard 纵向铺满。项目名独占行（冷蓝）「codebase-memory-mcp」。中部对比图：左「喂整个代码库」（灰），右「索引成图谱 → 砍 99% token」（暖橙）。avatar 中部锚点。底部 C 档标签「开发者向」。
- **焦点**：token 砍 99% 对比
- **节奏**：单 phase

### 场景 2 — mattpocock/skills（涨幅王 +1523）
- **emotion**: excitement
- **visual_type**: dark_tech_card
- **画面**：ProjectFullCard。项目名「skills」。中部巨字暖橙「+1523」+ 副标题冷蓝「单日涨星王」。背景：知识胶囊阵列（技能卡浮起）。avatar 锚点。
- **焦点**：+1523 涨幅数字
- **节奏**：单 phase

### 场景 3 — Agent-Reach（涨幅第二 +1161）
- **emotion**: wonder
- **visual_type**: dark_tech_card
- **画面**：ProjectFullCard。项目名「Agent-Reach」。中部「+1161」+ 副标题「让 AI 替你刷全网」。背景：六平台图标网格（Twitter/Reddit/YouTube/GitHub/B站/小红书 抽象化色块，无英文文字）。
- **焦点**：+1161 + 平台覆盖
- **节奏**：单 phase

### 场景 4 — Universal-Debloater（A 档·可操作·免 root 清预装）
- **emotion**: relief
- **visual_type**: dark_tech_card
- **画面**：ProjectFullCard。项目名「universal-android-debloater」。中部图标：安卓机器人轮廓 + 预装应用图标被一只手「划掉」（暖橙删除线）。副标题冷蓝「免 root 清预装 · 提升隐私/续航」。
- **焦点**：免 root + 卸预装的可操作感
- **节奏**：单 phase

### 场景 5 — penpot（A 档·免费设计）
- **emotion**: inspiration
- **visual_type**: dark_tech_card
- **画面**：ProjectFullCard。项目名「penpot」。中部：设计画布 + 代码窗口并列（设计↔代码双向箭头）。副标题冷蓝「免费设计工具 · 浏览器即开」。
- **焦点**：设计 ↔ 代码协作
- **节奏**：单 phase

### 场景 6 — plane（A 档·项目管理 + 结尾争议提问）
- **emotion**: decisive
- **visual_type**: dark_tech_card
- **画面**：ProjectFullCard。项目名「plane」。中部：看板/迭代/任务卡片网格（抽象色块）。底部转场：争议提问巨字暖橙「codebase-memory-mcp 和 Agent-Reach，你站谁？」+ 冷蓝「关注我 下期见」。
- **焦点**：争议站队提问
- **节奏**：单 phase

## 视觉统一约束

- **统一组件**：ProjectFullCard（项目名独占行 + avatar 中部锚点 + 三带纵向铺满 1920）
- **统一色温**：6 场景共用同一暗色基底 + 双色光晕，避免场景间视觉跳脱
- **统一节奏**：标准模式一屏一项目，phase 时长 8-15s（每场景单 phase）
- **门禁对齐**：max-width 块居中兜底（BASE_CSS margin:0 auto）、列表左对齐（图标+文字垂直成列）、渐变文字禁白色端点、bg/fx 层含 noise/beams/contour 等非纯 glow 组件
