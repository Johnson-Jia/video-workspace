# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博
mood: 紧凑利落

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于 AI/工具/基础设施场景）
  accent_warm: 金色/琥珀（用于 hook/涨星数据/CTA 场景）
  text: 白色主 + 浅灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "等宽极客"
    family: "JetBrains Mono"
    weight: 800
    rationale: "GitHub 开源项目盘点，理性/精准/极客的情感内核需要等宽极客标题字体，强化代码圈身份认同"
    fallback: "'JetBrains Mono','Consolas',monospace"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/赛博（紧凑节奏，霓虹电子）

## 素材预判
assets_needed:
  - assets/avatars/Panniantong.png
  - assets/avatars/NVIDIA.png
  - assets/avatars/rohitg00.png
  - assets/avatars/trycua.png
  - assets/avatars/Raphire.png
  - assets/avatars/meshery.png

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.4, 0.55, 0.7, 0.9, 0.7, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "topic1_agentreach"
    reveal: "topic2_skillSpector"
    climax: "topic3_aieng, topic4_cua"
    settle: "topic5_win11debloat, topic6_meshery"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default

## 选题维度
- 今日涨星最高：NVIDIA/SkillSpector（+1,079）和 Panniantong/Agent-Reach（+1,045），双 AI 项目并驾齐驱
- 钩子锚点：AI agent 领域爆发（2 个 agent 工具 + 1 个 agent 基础设施 + 1 个 AI 安全 = 4/6 是 AI 主题）
- 反直觉角度覆盖：Agent-Reach（免费读全网平台）/ SkillSpector（AI 审 AI）/ cua（AI 操控桌面）/ Win11Debloat（社区清微软预装）
- 领域多样性：AI 工具 / AI 安全 / AI 教程 / AI 基础设施 / Windows 优化 / 云原生（6 个不同方向）
