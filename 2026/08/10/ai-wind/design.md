# design.md — AI 风向标 2026-08-10 视觉风格方向 + 故事板

## 风格
style: 暗色电紫科技风（AI 风向标专属）
mood: 跨界冲击·紧凑凌厉

## 配色方向（电紫主题，描述性方向）
color_direction:
  background: 深紫渐变暗底（接近纯黑到深紫，#0a0a14 → #1a0a2e）
  accent_cool: 电紫主色（#A855F7 系，高饱和，用于 hook/项目排名/数字锚）
  accent_secondary: 辅青（#00D4FF 系，用于类别标签/三词卖点/科技光晕）
  accent_warm: 暖点缀橙（#FF6B35 系，克制使用，仅用于核心数字强调）
  text: 白色主 + 浅紫灰辅（渐变文字用紫同色系高饱和端点，禁白色端点）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "AI 跨界冲击的情感内核需要凌利干净的标题字体，电紫主题配几何无衬线最契合科技感"
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
music_mood: 科技/赛博·电紫紧凑（AI 风向标固定氛围，hyper-pace 快剪配套）

## 素材预判
assets_needed: []
- 4 项目 avatar 已下载（assets/avatars/）
- 项目卡片用 ProjectFullCard 8 层信息（类别/排名/英文名/中文描述/语言/总星/三词卖点/感性评语）
- 数字锚点（十四万/十二万/六万颗星）用计数动画

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.35, 0.55, 0.75, 0.95, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（AI 跨界反直觉）"
    build: "项目1 agency-agents（Agent 团队集合，数字锚 14万星）"
    reveal: "项目2 ComfyUI（节点式 AI 画图，12万星，A档）"
    climax: "项目3 daily_stock（金融跨界，6万星，中性化）"
    settle: "项目4 harvey-labs（法律跨界，能力基准）"
    summon: "CTA（跨界方向中性互动）"

## 方向
orientation: portrait
orientation_source: default
