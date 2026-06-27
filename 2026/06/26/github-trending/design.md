# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博
mood: 紧凑·信息密集·节奏明快

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深蓝/深紫渐变（接近 #0d1117 暗调，深空感）
  accent_cool: 霓虹青/翠绿（#00D4FF / #4DA8DA 系，用于 AI/agent 类项目场景与 features 段）
  accent_warm: 琥珀/橙（#FF8C32 / 金色，用于 hook 大数字、CTA、星标指标）
  text: 白色主 + 浅灰辅（数据用强调色发光）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=紧凑/专业/利落——AI 规范化主题需要冷静理性的标题气质，几何无衬线让信息前 3 秒击中"
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
music_mood: 科技/赛博（紧凑电子，节奏明快，AI 未来感，无歌词）

## 素材预判
assets_needed: []
- 纯 CSS/HTML 实现：星标数字计数动画、光晕背景、霓虹边框、卡片列表、对比栏
- 5 个项目 avatar 已在 assets/avatars/ 预下载（ProjectFullCard 引用）
- 无需外部图片/视频素材

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.6, 0.7, 0.85, 0.95, 0.7, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（黄金3秒：Google 一天 1407 星 + 利益翻译）"
    build: "design.md（AI 时代说明书反直觉）"
    reveal: "gstack（23 个角色配置）"
    climax: "MinerU（PDF 秒变 AI 口粮）+ page-agent（说话操控网页）"
    settle: "TREK（普通人自托管，温度回归）"
    summon: "CTA（中性二选一 + 关注下期）"

## 方向
orientation: portrait
orientation_source: default
