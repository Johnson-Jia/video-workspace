---
style: 暗色科技
mood: 紧凑明快·信息密集
orientation: portrait
orientation_source: default
character_presence: true
---

# design.md — 第33周 GitHub 周榜视觉方向

## 风格
style: 暗色科技风（GitHub 系列统一调性）
mood: 紧凑明快，周榜多项目快播报，节奏密、信息密、视觉强分组

## 配色方向
color_direction:
  background: 深色暗调（深蓝/深紫渐变基底，接近纯黑 #0B1020）
  accent_warm: 橙金 #FF8C32 / #FBBF24（用于 hook 与 CTA、涨星数字）
  accent_cool: 蓝/青 #4DA8DA / #00D4FF（用于 AI 智能体、安全学习分组）
  text: 白色主 + 浅灰辅
  domain_colors: 4 组领域色仅用于视觉（卡片色环/边框/标签/渐变标题文字），旁白与画面文字禁说颜色词
    - AI 智能体: #4DA8DA（蓝）
    - 本地大模型: #7B2FBE（紫）
    - 文档工具: #FF8C32（橙）
    - 安全学习: #00D4FF（青）

> 领域色是视觉分组手段，旁白按领域名分组引导（"AI 智能体这组""文档工具""安全学习"），禁出现"蓝/紫/橙/青/金/绿"等颜色词。

## 字体
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "周榜快播报紧凑利落的情感内核，需几何无衬线大字支撑信息密度与冲击力"
    fallback: "'Inter','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 低调科技衬底（clean-corporate / warm-editorial 类，不抢旁白；周榜快播报需 BGM 低调辅助）

## 素材预判
assets_needed: []
（纯 CSS/HTML 渐变光效 + 数据卡片，无需外部素材；项目 avatar 已预下载在 assets/avatars/）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.6, 0.75, 0.85, 0.6, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（第33周周榜+4G跑700亿反直觉）"
    build: "分类1 AI智能体"
    reveal: "分类2 本地大模型（呼应 hook 反直觉）"
    climax: "分类3 文档工具（项目最多，实用高潮）"
    settle: "分类4 安全学习 + 趋势总结"
    summon: "CTA（周次引导）"

## 方向
orientation: portrait
orientation_source: default
