# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技反潮流
mood: 紧凑利落 + 反直觉惊喜

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深蓝深紫渐变基底（接近纯黑，#0a0a14 系），暗色科技
  accent_cool: 蓝色 #4DA8DA 双光晕之一（features/技术栈场景）
  accent_warm: 橙色 #FF8C32 双光晕之二（hook/星标/CTA 场景）
  text: 白色主（90%→40% 调控，ProjectFullCard 精简强色原则）+ 浅灰辅
  rationale: 双光晕（暖冷色调）形成对比，冷色为主暖色做刀，符合 github 分类 default_style

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "本期 hook 反直觉冲击（山顶洞人省 token）需要利落现代感，几何简洁字体传递「轻量化/反潮流」气质，避免毛笔的厚重感"
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
music_mood: 低调科技衬底（clean-corporate / warm-editorial 类，禁 bold-energetic / epic-trailer 抢旁白）

## 素材预判（可选）
assets_needed:
  - owner avatars（已下载到 assets/avatars/，ProjectFullCard 中部引用）
  - 项目用途图标用 emoji 或纯 CSS 图标内联（轻量级，不引入外部 icon font）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.6, 0.5, 0.8, 0.7, 0.9, 0.4]
  immersion_mode: "hidden-gem"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（caveman 反直觉钩子）"
    build: "topic1 caveman 展开"
    reveal: "topic2 page-agent + topic3 meetily（新工具揭示）"
    climax: "topic4 romm + topic5 herdr（自托管/多 agent 高潮）"
    settle: "topic6 terax-ai（7MB 轻量沉淀）"
    summon: "CTA"

rationale: 6 个项目用 contrast-arc（反直觉钩子→逐项揭示），不用 hyper-pace 密集盘点（避免节奏过快）；immersion_mode 选 hidden-gem（小众宝藏揭示，渐近揭示 + 温暖光效），因本期主题是「反潮流轻量工具」而非「重大更新」；AI 项目占比低（仅 caveman 算 AI 周边工具），不用 hyper-pace。

## 视觉签名（ProjectFullCard 一屏一项目）
- 每项目独占一场景（6-8s），含 8 层信息：类别标签 / 排名 / 项目名 / 一句话描述 / 语言 / 核心指标（星标增量）/ 三词卖点 / 感性评语
- avatar 中部锚点（圆形 owner 头像），项目名 owner/repo 完整（不 nowrap），用途胶囊顶部 pfc-use（4-6字利益前置）
- 精简强色原则（白字 90%→40%）：用途强调色胶囊 + 星标 92px 大字 + repo 渐变文字

## 方向
orientation: portrait
orientation_source: category_hint
rationale: github 分类为竖屏短视频（1080×1920），手机端抖音就绪
