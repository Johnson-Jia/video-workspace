# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技盘点
mood: 紧凑爆发

## 配色方向（描述性，不指定具体色值；领域色仅用于视觉层）
color_direction:
  background: 深色暗调（接近纯黑，深空蓝底）
  accent_cool: 青/翠蓝（用于工具/工程师/系统类项目卡片）
  accent_warm: 琥珀金（用于 hook 场景排名数字与 CTA 强调）
  accent_signal: 信号红/紫（用于安全类项目 destructive_command_guard）
  accent_play: 游戏紫/电光（用于游戏模拟器 sharpemu）
  text: 白色主 + 浅灰辅

> 视觉领域色映射（仅画面，旁白与画面文字禁说颜色词，按领域名分组）：
> - 视频工具（OpenCut）→ 琥珀金强调
> - 工程师技能/系统（mattpocock skills / Win11Debloat）→ 青冷强调
> - AI 安全（destructive_command_guard）→ 信号红紫强调
> - 团队设计（penpot）→ 翠蓝强调
> - 游戏模拟器（sharpemu）→ 电光紫强调

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "多项目盘点的紧凑节奏需要利落的几何标题，传递效率与爆发感"
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
music_mood: 科技/紧凑电子（balanced 档，间歇鼓点不压旁白）

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.35, 0.5, 0.65, 0.85, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: false
  beat_mapping:
    grab: "hook（OpenCut 4349 爆发锚定）"
    build: "OpenCut 项目介绍"
    reveal: "mattpocock skills + destructive_command_guard"
    climax: "penpot + sharpemu"
    settle: "Win11Debloat 霸榜带过"
    summon: "CTA（中性互动）"

## 方向
orientation: portrait
orientation_source: default
resolution: 1080x1920
