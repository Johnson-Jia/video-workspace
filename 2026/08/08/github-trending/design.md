# design.md — 视觉风格方向 + 故事板（2026-08-08 github-trending）

## 风格
style: 暗色科技盘点
mood: 紧凑利落·数字驱动

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑 + 深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于 witr/mise/celld 工具基建项目段）
  accent_warm: 金色/琥珀（用于 hook / prime-agent 涨星数字 / CTA 强数据）
  text: 白色主 + 浅灰辅

> 配色执行约束（stage6 落地）：渐变文字同色系高饱和禁白色端点；text-shadow 极淡 drop rgba(30,41,59,0.08) 禁发光。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=紧凑/专业/利落的科技盘点，几何无衬线粗体最匹配数字驱动节奏"
    fallback: "'Inter','Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 低调科技/clean-corporate（衬底不抢人声，快速播报辅助）

## 素材预判
assets_needed: []
（纯 CSS/HTML 实现数字计数动画、ProjectFullCard 卡片、光晕渐变；avatars 已预下载）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.45, 0.7, 0.85, 0.6, 0.6, 0.4]
  immersion_mode: "contrast-arc"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（单日涨两千七 + AI 自进化反直觉）"
    build: "prime-agent、MiroFish（两个 AI 重点展开）"
    reveal: "witr（进程追根溯源反直觉）"
    climax: "mise（开发环境一统，三万星数据高点）"
    settle: "celld（deno 自托管基建沉淀）"
    summon: "CTA（想试哪个 + 关注）"

## 方向
orientation: portrait
orientation_source: default

## 黄金 3 秒视觉要求
hook 场景为全片视觉最强画面：单日涨星数字（两千七）超大字号 + 强调色金色 + 深色渐变光晕底，「AI 自己进化」反直觉副文案高对比。字号最大、对比最强、布局最精致。

## cinema 备注
- hook：特写 + 推（hero 居中，不影响安全区）+ 硬切
- 5 个项目 ProjectFullCard 段：中景 + 固定（避免 s6 scale 1.1 致 PFC 顶带溢出 top 安全区）+ 硬切
- CTA：中景 + 固定 + 叠化
