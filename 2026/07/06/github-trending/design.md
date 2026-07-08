# Design — GitHub Trending 2026-07-06

## 视频定位
- 日期：2026-07-06
- 分类：github
- 模式：标准模式（6 场景，~40s）
- 方向：portrait（竖屏，1080×1920）
- orientation_source：github 分类无 orientation_hint，默认竖屏

## 沉浸模式
hyper-pace（AI 类项目 >50%）：快速剪辑 + 密集粒子 + 霓虹冷色

## 视觉风格（暗色科技风）
- 背景渐变：#0a0e1a（顶）→ #1a1f3a（中）→ #0d0a1f（底，紫调）
- 强调色暖：#FF8C32（橙，A 档利益色，meetily/immich）
- 强调色冷：#4DA8DA（蓝，开发者工具组）
- 数据色：#FFD24A（金，星标数字）
- 字体：思源黑体 Heavy（主标题），JetBrains Mono（数据/英文）
- 光晕：双光晕（暖橙左上 0.18 + 冷蓝右下 0.10）

## 场景情绪曲线（emotion_curve）
- s1 hook：惊讶/紧迫（反直觉钩子）
- s2 meetily：安心/信任（隐私本地）
- s3 immich：惊叹/熟悉（10万星老牌）
- s4 codex+page-agent：好奇/探索（AI 协同）
- s5 strix+herdr：紧张/专业（安全+终端）
- s6 CTA：温和/互动

## 场景规划（6 段，每段 visual_phases）
| 场景 | 时长 | 项目 | 视觉重点 |
|------|------|------|---------|
| s1 | 4s | hook | 全屏钩子文字 + 粒子爆发 |
| s2 | 7s | meetily | ProjectFullCard + 本地化图标动画 |
| s3 | 7s | immich | ProjectFullCard + 10万星徽章 |
| s4 | 7s | codex+page-agent | 双卡片对比 |
| s5 | 7s | strix+herdr | 双卡片对比 + 安全色调 |
| s6 | 4s | CTA | 提问 + 关注引导 |

## ProjectFullCard 数据
所有项目用 ProjectFullCard 组件，pfc-use 顶部用途标签（利益），中部 avatar，底部星标数据。

## 角色启用
码力角色（character_presence: true）— 简短出现在 hook 与 CTA
