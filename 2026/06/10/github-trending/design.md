# 视觉风格设计 — GitHub Trending 2026-06-10

## 基本信息
- 画布: 1080x1920 竖屏
- 方向: portrait
- orientation_source: 分类默认
- 分类: github
- 内容类型: GitHub Trending 项目盘点
- 日期: 2026年6月10日

## 主题
AI 全面接管打工人——从调研、求职、重构到产品管理，GitHub 今日趋势全部指向同一个方向：AI 替你干活。

## 色彩方案
- 主背景: 深蓝渐变 #0a0e1a → #0d1333
- 强调色暖: #FF8C32（橙色，用于数据锚定和钩子）
- 强调色冷: #4DA8DA（蓝色，用于项目名和标签）
- 文字主色: #FFFFFF
- 文字辅色: #B0BEC5
- 数据高亮: #FFD54F（金色，用于涨星数字）

## 场景规划（4 个场景）

### Scene 1: Hook — AI 全面接管
- 时长: 5-6s
- 内容: 数据锚定钩子，"6月10日 GitHub 杀入的项目全是 AI 替人干活的"
- 视觉: 大字标题 + 涨星数据流
- bg 层: 深蓝渐变 + 网格线
- fx 层: 光粒子上升 + 脉冲光圈

### Scene 2: last30days-skill + turbovec（调研 + 向量搜索）
- 时长: 10-12s
- 内容: AI 跨 7 平台调研 / Rust 向量索引快 10 倍
- 视觉: 项目名 + 核心数据 + 功能图标
- bg 层: 深蓝底 + 斜线纹理
- fx 层: 连接线动画 + 节点脉冲

### Scene 3: career-ops + pm-skills（求职 + 产品管理）
- 时长: 10-12s
- 内容: AI 一键求职自动化 / PM 不写代码也能用 AI
- 视觉: 流程图式展示
- bg 层: 深紫底 + 圆点阵列
- fx 层: 流动光带 + 数字翻转

### Scene 4: tolaria + agent-skills + CTA（重构 + Agent 技能 + 收尾）
- 时长: 10-12s
- 内容: AI 一键重构 / Chrome 团队的 Agent 技能集 / CTA
- 视觉: 瀑布式展示 + CTA
- bg 层: 深蓝底 + 几何碎片
- fx 层: 棱镜光效 + 粒子消散

## 字体规范
- 标题: 粗体无衬线, 42-56px
- 项目名: 中粗无衬线, 36-42px
- 正文: 常规无衬线, 28-34px
- 数据: 粗体等宽/无衬线, 48-64px
- 标签: 常规无衬线, 22-26px

## 动效规范
- 项目切入: GSAP fromTo x:±200, opacity 0→1, duration 0.6
- 数据高亮: scale pulse 1→1.05→1, duration 0.4
- 场景切换: timeline seek，禁止 CSS class toggle
- fx 元素: 最少 2 个不同类型（粒子 + 光效 / 连接线 + 脉冲）
