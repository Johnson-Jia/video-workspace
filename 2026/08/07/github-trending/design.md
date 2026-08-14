# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技（多元基建）
mood: 沉稳清晰（非纯 AI 激昂，本期跨认证/Java库/代码图谱/agent 基建 4 领域，偏理性多元）

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于 code-review-graph / loopx 等 AI 工具场景）
  accent_warm: 琥珀/金（用于 hook / authentik / CTA 场景）
  text: 白色主 + 浅灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "多元基建盘点偏理性精准，紧凑专业的几何无衬线比毛笔/衬线更贴合"
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
music_mood: 低调科技/企业播报（clean-corporate 系，衬底不抢人声，符合 GitHub 快速播报定位）

## 素材预判
assets_needed: []（纯 CSS/HTML 卡片实现，ProjectFullCard 一屏一项目，无需外部素材）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.6, 0.5, 0.7, 0.75, 0.7, 0.4]
  immersion_mode: "contrast-arc"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（四个项目杀入，一半不是 AI）"
    build: "guava（Java 核心库长青）"
    reveal: "authentik（认证自己管）"
    climax: "code-review-graph（代码图谱省上下文）"
    settle: "loopx（agent 状态核）"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default
