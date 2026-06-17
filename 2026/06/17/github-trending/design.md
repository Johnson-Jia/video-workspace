# design.md — GitHub Trending 2026-06-17

## 风格
style: 暗色科技风
mood: 紧凑专业·数据驱动

## 配色方向（github 分类 default_style）
color_direction:
  background: 深蓝/深紫渐变底（科技感基底）
  accent_warm: 橙(#FF8C32)用于数字/星标/涨星/hook 锚点
  accent_cool: 蓝(#4DA8DA)用于技术说明/项目名/标签
  text: 白色主 + 浅灰辅
rationale: 暖橙=价值/数据锚点，冷蓝=技术理性，双色光晕营造科技纵深（github 分类 color_bias）。

## 字体
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1=紧凑专业/数据驱动，GitHub 项目盘点需利落科技感，Inter 900 几何简洁"
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
music_mood: 科技/紧凑电子（节奏推进，数据感）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.6, 0.65, 0.72, 0.78, 0.62, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: false
  beat_mapping:
    grab: "S1 hook（反直觉双锚+数字）"
    build: "S2-S3 VoxCPM/iroh（反直觉项目展开）"
    reveal: "S4-S5 meshery/teslamate（能力揭示）"
    climax: "S6 zvec（AI基建性能高点）"
    settle: "S7 Universal-Debloater（实用工具）"
    summon: "S8 CTA（结尾争议站队提问）"

## 场景总览（8场景标准模式，~45s）
scenes_overview:
  - S1: hook——6个项目今日冲榜，反直觉双锚(iroh钥匙拨号 + VoxCPM不用分词器)
  - S2: VoxCPM——AI拟声克隆，不用分词器的多语言TTS，+413
  - S3: iroh——IP会坏改用钥匙拨号，去中心化网络，+326
  - S4: meshery——画图管云原生，+229
  - S5: teslamate——特斯拉自记数据，+214
  - S6: zvec——进程内闪电向量库，本地RAG，+188
  - S7: Universal-Debloater——免root清安卓预装，+146
  - S8: CTA——结尾争议站队 + 关注

## 方向
orientation: portrait
orientation_source: default
