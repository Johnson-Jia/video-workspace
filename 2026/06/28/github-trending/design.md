# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技·发现感
mood: 紧凑利落·带温度的科技调

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于 cognee 记忆、open-seo、PowerToys 等工具/能力场景）
  accent_warm: 金色/琥珀（用于 hook/CTA/openpilot 反直觉钩子场景）
  text: 白色主 + 浅灰辅
  rationale: 暗色底让「让 AI 记住你」「文档秒变 PPT」「装进 300 多款车」的能力点更突出；冷暖双色对应 AI 应用与硬件工具两类内容

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "本期讲 AI 能力与开源工具，情感内核是「紧凑/专业/利落」的发现感，几何简洁字体放大这种干净利落的科技调，支撑 hook 场景的视觉冲击"
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
music_mood: 科技/紧凑·带发现的兴奋感（轻电子，节奏明快不喧宾夺主）

## 素材预判（可选）
assets_needed:
  - cognee 记忆：AI 记忆图谱节点动画（CSS/光效节点）
  - ppt-master：文档→PPT 转换示意（CSS 流程箭头）
  - openpilot：车型轮廓 + 300+ 数字计数（数据动画）
  - open-seo：付费 vs 开源对比（双栏对比卡片）
  - PowerToys：Windows 工具图标网格

## 故事板（新增）
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.4, 0.6, 0.85, 1.0, 0.65, 0.45]
  immersion_mode: "hidden-gem"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（让 AI 记住你说过的话 + 文档秒变 PPT + 开源自动驾驶装车）"
    build: "cognee（AI 有长期记忆）"
    reveal: "ppt-master（文档秒变可编辑 PPT）"
    climax: "openpilot（开源驾驶辅助装进 300+ 车·反直觉）"
    settle: "open-seo（付费 SEO 工具的开源替代）+ PowerToys（微软工具集·快速带过）"
    summon: "CTA（中性二选一提问 + 关注）"

## 方向（新增）
orientation: portrait
orientation_source: default
