# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 紧凑警觉

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深蓝/深紫暗调（接近纯黑，安全主题的冷峻底色）
  accent_warm: 警示橙（#FF8C32 系，用于 hook/排名/星标/CTA，传递警觉与价值）
  accent_cool: 扫描蓝（#4DA8DA 系，用于功能描述/技术标签/数据，传递理性与分析）
  text: 白色主 + 浅灰辅（信息层级：排名星标 > 项目名 > 描述）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核为警觉/紧迫/掌控感，安全自查主题需要紧凑专业的标题气质，几何无衬线体传递理性与可信"
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
music_mood: 科技/悬疑低调（衬底不抢人声，clean-corporate/warm-editorial 系，避开电子激昂）

## 素材预判（可选）
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.65, 0.8, 0.7, 0.6, 0.45]
  immersion_mode: "hidden-gem"
  humor_style: "analogy"
  character_presence: true
  beat_mapping:
    grab: "hook（信息泄露反直觉钩子）"
    build: "spiderfoot（攻击面自查，建立危机感）"
    reveal: "holehe（邮箱痕迹反查，揭示泄露面）"
    climax: "过渡（安全→本地工具的叙事转折）"
    settle: "FluidVoice（离线语音，沉淀到本地防御）"
    summon: "modly + CTA（本地图生3D + 中性二选一互动）"

## 方向
orientation: portrait
orientation_source: default
