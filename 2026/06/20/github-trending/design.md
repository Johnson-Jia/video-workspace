# design.md — 视觉风格方向 + 故事板（2026-06-20 GitHub Trending）

## 风格
style: 暗色科技赛博（GitHub 系列统一基调）
mood: 紧凑干练，hook 段冲击力强，正文段信息密度高，CTA 段温暖收束

## 配色方向
color_direction:
  background: 深色暗调（接近纯黑 #0A0E1A，深蓝/深紫渐变做底）
  accent_cool: 霓虹青蓝（#4DA8DA / #00D4FF，用于工具/AI 类项目场景与数据高亮）
  accent_warm: 琥珀橙金（#FF8C32 / #FFB800，用于 hook 场景数字锚定、涨星指标、CTA 场景）
  text: 白色主 + 浅灰辅（#E8EDF5 / #8B95A8）
  glow: 双光晕（冷青蓝外晕 + 暖橙金内晕，对应 GitHub 分类「双光晕」配置）

## 字体
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "工具盘点类的紧凑专业气质，需要几何简洁的标题字体承载反直觉数字锚点的冲击力"
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
music_mood: 科技/赛博，紧凑节奏，hook 段能量饱满，正文段稳定推进，CTA 段温暖收束
关键词: tech, cyber, energetic, focus, modern

## 素材预判
assets_needed: []
- 项目卡片用 ProjectFullCard 组件（avatar + 8 层信息），无需额外外部素材
- 涨星数字用 data 计数动画，纯 CSS/JS 实现
- hook 场景用 hero 大标题 + 数字光晕

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.35, 0.5, 0.75, 0.95, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "headroom"
    reveal: "palmier-pro, worldmonitor"
    climax: "penpot, insomnia"
    settle: "codebase-memory-mcp"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default

## 场景规划（6 项目标准模式）
- hook（4s, grab）: 反直觉钩子 — headroom 砍掉 AI 输入大半，答案还一样
- headroom（8s, build）: 反直觉钩子王展开，60-95% 更少 token
- palmier-pro（7s, reveal）: macOS AI 视频编辑器 GUI
- worldmonitor（7s, reveal）: 全球情报仪表盘 GUI
- penpot + insomnia（10s, climax）: 开源设计工具 + API 客户端双工具
- codebase-memory-mcp（4s, settle）: 连续霸榜快速带过
- CTA（5s, summon）: 结尾争议站队 + 关注引导
预估总时长: 45-50s，字数 250-380
