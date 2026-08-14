# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风（大厂科研基调）
mood: 神秘揭示→理性展开→震撼收束

## 配色方向（描述性，对齐 github 分类冷色+暖强调）
color_direction:
  background: 深紫至深蓝渐变暗调（接近纯黑底，大厂科研的厚重感）
  accent_cool: 霓虹青/翠蓝（用于代码/工具/数据场景，理性科技）
  accent_warm: 琥珀金/橙（用于 hook/天气模型/CTA 场景，冲击与温度）
  text: 白色主 + 浅灰辅（清晰靠本身亮色+bg对比，禁发光浮起）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1情感内核=震撼/科技揭示，紧凑利落的几何无衬线最契合GitHub科技盘点的现代感，hook冲击靠字号与对比而非毛笔"
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
music_mood: 低调科技衬底（clean-corporate / warm-editorial，不抢旁白；与近几期电子激昂区隔）

## 素材预判
assets_needed: []
（4项目均为概念/数据展示，纯 CSS/HTML 渐变光效+ProjectFullCard 即可，无需外部素材）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.35, 0.5, 0.65, 1.0, 0.6, 0.45]
  immersion_mode: "mega-update"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "S1 hook（谷歌居然开源天气模型）"
    build: "S2 weathernext（大厂科研开源·全球天气）"
    reveal: "S3 t3code（手机遥控AI·平民化惊喜）"
    climax: "S5 ComfyUI（星标十二万·最广认知·强收束进CTA）"
    settle: "S4 code-graph-rag（开发者deep-cut·知识图谱）"
    summon: "S6 CTA（中性二选一互动）"

## 方向
orientation: portrait
orientation_source: default

## 场景顺序与运镜预防
# camera_move 铁律（feedback-stage6-camera-move-scale）：hook 可"推"，4 个 PFC 项目段全"固定"（避免 layer-content scale 致 PFC 顶带上移溢出 top）
# 场景序列：S1 hook → S2 weathernext → S3 t3code → S4 code-graph-rag → S5 ComfyUI → S6 CTA
