# design.md — AI 风向标 2026-08-12 视觉风格方向 + 故事板

## 风格
style: 暗色科技风（AI 电紫主题）
mood: 工程化落地·紧凑凌厉

## 配色方向（电紫主题，描述性方向）
color_direction:
  background: 深紫渐变暗底（#0a0a14 → #1a0a2e，接近纯黑到深紫）
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
    rationale: "智能体工程化的情感内核是利落、可落地，电紫主题配几何无衬线最契合紧凑科技感"
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
- 5 项目 avatar 已下载（assets/avatars/：stablyai / HKUDS / paperclipai / addyosmani / anthropics）
- 项目卡片用 ProjectFullCard 8 层信息（类别/排名/英文名/中文描述/语言/总星+单日涨星/三词卖点/感性评语）
- 数字锚点（16.8万总星 / 8.6万 / 7.7万 / 4.2万 / 3.4万）用计数动画

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.4, 0.55, 0.75, 0.9, 0.6, 0.45]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only（analogy 类比为主）"
  character_presence: true
  beat_mapping:
    grab: "hook（AI 不用人盯、一群自己干活，反直觉切入）"
    build: "项目1 orca（用：并行智能体干活，多端盯进度）"
    reveal: "项目2 DeepTutor（用：记得你学过的 AI 家教）+ 项目5 skills（装技能：官方技能库，16.8万总星二次高点）"
    climax: "项目3 paperclip（管：一个面板统管所有智能体）"
    settle: "项目4 agent-skills（装技能：工程师实战经验打包）"
    summon: "CTA（三件套中性二选一互动）"

## 方向
orientation: portrait
orientation_source: default
