# Design — GitHub Trending 2026-05-31

## 情感基调
**核心情绪**: 科技惊奇 × 数据冲击
**情绪曲线**: hook震撼 → 递进式探索 → 高潮惊叹 → 温暖收尾

## 视觉风格
**风格方向**: 赛博极简 — 深色背景 + 数据流动 + 亮色强调
**配色**:
- 主色: #0a0a1a (近黑蓝)
- 强调色: #00d4ff (科技蓝)
- 辅助色: #7c3aed (紫光)
- 警示色: #ff6b35 (活力橙，用于数据指标)
- 文字: #f0f0f0 (高对比白)

**字体**: 系统默认无衬线，标题粗体

## 音乐方向
**风格**: 电子/科技感，中速 BPM 100-120
**情绪**: 前段神秘探索，中段节奏加快，后段温暖收尾
**音量**: bgm_volume = 0.15（背景级）

## 分镜

### s1-hook (0-4s) — WiFi 黑科技
- **视觉**: WiFi 信号波纹扩散 + 人体轮廓浮现
- **bg**: noise_field（神秘感纹理）
- **fx**: pulse_orb（信号脉冲）
- **content**: 大字反直觉 hook 文案
- **情绪**: 震撼/好奇

### s2-top1 (4-13s) — RuView
- **视觉**: 路由器 → WiFi 波 → 人体检测示意
- **bg**: scan_grid（科技扫描感）
- **fx**: scan_line（扫描线配合"检测"概念）
- **content**: 项目卡片 + 三词卖点 + ★数据
- **情绪**: 惊奇/探索

### s3-top2 (13-21s) — markitdown
- **视觉**: 文件图标 → 箭头 → Markdown 符号
- **bg**: contour_lines（数据结构感）
- **fx**: data_stream（数据流动）
- **content**: 项目卡片 + 转换示意 + 微软品牌标识
- **情绪**: 认可/实力

### s4-top3 (21-28s) — liteparse
- **视觉**: 速度仪表 + 文档飞过
- **bg**: gradient_mesh（流动渐变）
- **fx**: light_streak（速度光效）
- **content**: 项目卡片 + 速度对比 + Rust 标签
- **情绪**: 速度感/惊喜

### s5-top4 (28-35s) — VoxCPM
- **视觉**: 声波 → 语言切换
- **bg**: wave_ripple（声波涟漪）
- **fx**: float_particles（声音粒子飘散）
- **content**: 项目卡片 + 清华标识 + 语音克隆概念
- **情绪**: 颠覆感

### s6-top5 (35-42s) — ECC
- **视觉**: 智能体网络 + 记忆节点连接
- **bg**: radial_beams（放射光芒，突出20万星）
- **fx**: alert_border（强调框，突出重要性）
- **content**: 大数字 ★199K + 项目卡片 + Agent 概念
- **情绪**: 赞叹/高潮

### s7-misc (42-46s) — MoneyPrinterTurbo
- **视觉**: 快速闪卡
- **bg**: light_field（轻柔过渡）
- **fx**: 无（简洁快速）
- **content**: 项目名 + ★数据，快速带过
- **情绪**: 轻松/过渡

### s8-cta (46-49s) — 关注引导
- **视觉**: 频道名 + 关注按钮
- **bg**: vignette_glow（温暖聚焦）
- **fx**: 无
- **content**: "GitHub星探" + CTA 文案
- **情绪**: 温暖/邀请

## 节奏映射
| 区间 | 节奏 | 视觉密度 |
|------|------|----------|
| 0-4s | 爆发 | 高（hook 冲击） |
| 4-21s | 稳定推进 | 中（项目介绍） |
| 21-42s | 递进加速 | 中高（连续亮点） |
| 42-49s | 缓收 | 低（收尾温暖） |

## bg 多样性保障
8 个场景使用 8 种不同 bg 组件：noise_field → scan_grid → contour_lines → gradient_mesh → wave_ripple → radial_beams → light_field → vignette_glow。相邻场景 bg 零重复。
