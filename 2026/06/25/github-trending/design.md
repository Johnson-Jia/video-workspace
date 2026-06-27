# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风（双光晕冷暖叙事）
mood: 紧凑利落 + 反直觉冲击

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底，配 40px 网格 opacity 0.04 数字纹理）
  accent_cool: 霓虹青/翠蓝（用于容器/agent/工具类项目场景，理性技术隐喻）
  accent_warm: 金色/琥珀橙（用于 hook 排名数字、星标、CTA，价值与紧迫隐喻）
  text: 白色主（项目名/标题）+ 浅灰辅（描述/评语）
  dual_glow: 每场景一暖一冷双光晕，暖偏左上、冷偏右下，制造纵深感

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "等宽极客"
    family: "JetBrains Mono"
    weight: 800
    rationale: "Q1 情感内核=震撼/好奇（苹果不用 Docker 的反直觉冲击），技术盘点需要精准冷峻的极客音色，等宽体像节拍器一样传递「数据可信」"
    fallback: "'JetBrains Mono','Consolas','PingFang SC','Microsoft YaHei',monospace"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/赛博（紧凑电子，配合 hyper-pace 快速剪辑节奏）

## 素材预判（可选）
assets_needed:
  - 6 个 owner avatar（assets/avatars/ 已预下载，ProjectFullCard 中部锚点引用）
  - 纯 CSS/HTML 实现的排名数字、星标增量、技术栈药丸（无需外部图片素材）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.85, 0.5, 0.65, 0.8, 0.55, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（苹果不用 Docker 反直觉冲击，全片视觉最强）"
    build: "apple/container（主角展开，原生 Swift 容器）"
    reveal: "hermes-agent（成长型 agent）+ ai-website-cloner（一键克隆）"
    climax: "orca（agent 舰队 ADE，A 档即装即用高潮）+ no-mistakes（git 防误推）"
    settle: "OpenMontage（连续霸榜快速带过，仅提增量）"
    summon: "CTA（中性二选一提问）"

## 方向
orientation: portrait
orientation_source: default
