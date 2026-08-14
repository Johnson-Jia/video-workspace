# design.md — AI 风向标 2026-08-14 视觉风格方向 + 故事板

## 风格
style: 暗色科技风（AI 电紫主题）
mood: 可信落地·紧凑凌厉

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
    rationale: "AI 落地基建的情感内核是扎实、可信赖，电紫主题配几何无衬线最契合紧凑科技感"
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
- 5 项目 avatar 已下载（assets/avatars/：macro-inc / cactus-compute / unslothai / infiniflow / semantica-agi）
- 项目卡片用 ProjectFullCard 8 层信息（类别/排名/英文名/中文描述/语言/总星+单日涨星/三词卖点/感性评语）
- 数字锚点（88K 总星 / 71K / 6.6K / 4.9K / 2.6K +1239 当日最高）用计数动画

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.45, 0.6, 0.8, 0.9, 0.65, 0.45]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only（analogy 类比为主）"
  character_presence: true
  beat_mapping:
    grab: "hook（AI 不瞎编、还能自证清白，可信反直觉切入）"
    build: "项目1 macro（用：AI 统一工作区，+1239 当日涨星最高）"
    reveal: "项目2 needle（端侧：14MB 小模型塞进手机）+ 项目3 unsloth（本地：自己电脑跑大模型，71K 总星）"
    climax: "项目4 ragflow（可信：AI 先读资料再回答，88K 总星）"
    settle: "项目5 semantica（可信：决策留痕可溯，AI 不再是黑盒）"
    summon: "CTA（五个 AI 基建中性二选一互动）"

## 方向
orientation: portrait
orientation_source: default
