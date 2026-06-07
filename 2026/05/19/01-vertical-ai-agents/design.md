# Design: 垂直AI智能体商业分析

## 风格方向
- **style**: 商业科技 — 专业、冷静、数据驱动
- **mood**: 专业、有洞察力、前瞻性
- **color_direction**: 深色蓝黑底 + 蓝金双色体系

## 配色

| 变量 | 值 | 用途 |
|------|-----|------|
| bg_dark | #060d1f | 最深背景 |
| bg_mid | #0f172a | 中间色背景 |
| accent_blue | #3b82f6 | 主强调色（数据、标签） |
| accent_amber | #f59e0b | 次强调色（数字、重点） |
| accent_cyan | #06b6d4 | 辅助色（副信息） |
| accent_green | #10b981 | 正面/增长指标 |
| accent_red | #ef4444 | 风险/警示 |
| text_white | #f8fafc | 主文字 |
| text_gray | #94a3b8 | 辅助文字 |

## 字体
- 主字体: Inter, PingFang SC, Microsoft YaHei, sans-serif
- 等宽: JetBrains Mono, monospace

## 视觉特征
- 渐变背景: 纵向 linear-gradient(180deg, bg_dark → bg_mid → bg_dark)
- 光晕: 每场景 1-2 个大尺寸模糊光球 (blur 140px+, opacity 15-25%)
- 网格底纹: 极低透明度 3-5%
- 内容居中: flexbox，安全区 200-1600px
- 动画: 快入(0.3-0.5s) + 静止，power3.out

## 场景配色策略

| 场景类型 | 主色 | 辅色 |
|---------|------|------|
| hook | amber | blue |
| 痛点/问题 | amber/red | blue |
| 市场数据 | blue | amber |
| 技术框架 | cyan | blue |
| 趋势/未来 | green | cyan |
| 路径/方案 | blue | amber |
| 风险 | red | amber |
| 总结/策略 | amber | green |
| CTA | blue | amber |
