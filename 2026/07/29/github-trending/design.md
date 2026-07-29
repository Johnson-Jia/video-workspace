# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技拼盘        # GitHub星探频道一致身份：暗色科技风，本期多方向项目对决感
mood: 紧凑利落带悬念        # 反直觉钩子开场→逐个项目交锋→数据高潮→沉淀收尾

## 配色方向（描述性，不指定具体色值；暗色底 + 双强调色，遵循分类 default_style）
color_direction:
  background: 深蓝/深紫渐变暗调（接近纯黑，科技感基底）
  accent_cool: 霓虹青/翠蓝（用于 NON-AI 项目场景：editor/jenkins/superfile，理性工程感）
  accent_warm: 橙色/金色（用于 hook/ECC 数据高潮/CTA，强调色拉冲击）
  text: 白色主 + 浅灰辅（文字清晰靠本身亮色 + bg 对比，禁发光）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "开源榜单的紧凑专业感 + 数据冲击，几何无衬线最利落；避近期毛笔/衬线"
    fallback: "'Inter','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向（GitHub 快速播报定位：低调辅助衬底，不抢人声；Stage 4 选 clean-corporate/warm-editorial 系）
music_mood: 低调科技衬底（clean-corporate 偏向，跨期去重避 neon-electric 连续用）

## 素材预判
assets_needed: []   # 纯 CSS/HTML 渐变光效 + 数据计数动画，无需外部素材；头像已预下载 assets/avatars/

## 故事板
storyboard:
  narrative_template: "showdown"    # 多方向项目交锋拼盘（避近期 hyper-pace/contrast-arc/mystery-box）
  emotion_curve: [0.5, 0.6, 0.75, 0.9, 0.65, 0.5]   # showdown 弧：紧张→交锋→揭晓→高潮→沉淀→行动
  immersion_mode: "versus"          # 分屏对比 + 硬朗强调（非 hyper-pace；暗色底兼容分类 default_style）
  humor_style: "dual-track"         # 双线幽默：settle 段吐槽 + 视觉梗
  character_presence: true          # GitHub 系列启用码力角色，climax 段（ECC 23万星）必出
  beat_mapping:
    grab: "hook（editor 反直觉钩子，NON-AI）"
    build: "editor（浏览器造3D建筑，lead 展开）"
    reveal: "speech-to-speech（本地语音不联网，HF 大厂）"
    climax: "ECC（半年23万星数据高潮，码力 explode）"
    settle: "jenkins + agent-governance（老牌基建 + 微软 AI 治理，思考段）"
    summon: "superfile 快报 + CTA（中性二选一互动）"

## 方向
orientation: portrait
orientation_source: default
