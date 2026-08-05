# design.md — 视觉风格方向 + 故事板

## 风格
style: AI 电紫赛博（暗色科技风）
mood: 紧凑 / 极客 / 震撼

## 配色方向（描述性）
color_direction:
  background: 深紫渐变（接近纯黑 #0a0a14 → 深紫 #1a0a2e），命令行终端底色感
  accent_cool: 电紫 #A855F7（主色，AI 核心强调）+ 霓虹青 #00D4FF（辅助，数据/科技）
  accent_warm: 暖橙 #FF6B35（点缀，仅 hook/CTA 强对比用）
  text: 白色主 + 浅紫灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "等宽极客"
    family: "JetBrains Mono"
    weight: 800
    rationale: "命令行 AI 主题 + 极客震撼情感内核，等宽体呼应终端字体感"
    fallback: "'JetBrains Mono','Noto Sans SC','PingFang SC',monospace"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/赛博/紧凑（电子鼓点 + 合成器，匹配 hyper-pace 快剪）

## 素材预判
assets_needed: []   # 纯 CSS 渐变 + 粒子光晕实现终端/AI 视觉，无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.6, 0.75, 0.9, 0.65, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（8 个 AI 4 个钻命令行）"
    build: "DeepSeek-Reasonix（终端编程助手）"
    reveal: "airllm（层流式推理单卡跑超大模型）"
    climax: "Agent-Reach（一命令读全网零接口费）"
    settle: "last30days + 合并记忆/课（调研+提增量）"
    summon: "CTA（命令行 vs 网页中性二选一）"

## 方向
orientation: portrait
orientation_source: category_hint
