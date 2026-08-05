# design.md — AI 风向标 视觉风格方向 + 故事板

> 新专辑首期视觉识别：电紫主题（AI 识别色）。配色参照已验证渲染 OK 的 `workspace/covers/collection-ai-wind.html`。

## 风格
style: 暗色科技风（AI 电紫主题）
mood: 紧凑激烈（hyper-pace 快剪 + 密集粒子 + 霓虹电紫）

## 配色方向（电紫主色 #A855F7 — 新专辑视觉识别，已验证）
color_direction:
  background: 深紫渐变（#0a0a14 → #1a0a2e），接近纯黑的深紫底
  primary: 电紫 #A855F7（AI 识别色，hook/CTA/项目名强调）
  accent_cool: 霓虹青 #00D4FF（数据/辅光/卖点标签）
  accent_warm: 暖橙 #FF6B35（星标增量/排名数字点缀，低占比）
  text: 白色主 + 浅紫灰辅（#C084FC 标题辅 / #8892b0 正文辅）
  glow: 双光晕（电紫主光晕 opacity 0.28 + 青辅光晕 0.18 + 橙暖点缀 0.12），紫调网格底纹 5% 透明度

> ⛔ text-shadow 极淡 drop（0 2px 6px rgba(30,41,59,0.08)），禁发光 0 0 Xpx。
> ⛔ 渐变文字 background-clip:text 禁白色端点，用同色系高饱和（紫 #A855F7→#C084FC→#E9D5FF / 青 #00D4FF→#60A5FA→#93C5FD）。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=紧凑/专业/利落（AI 快剪科技感），几何无衬线粗体最匹配；项目英文名与数据用同族强化科技调"
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
music_mood: 科技/赛博（暗色电子，紧凑节奏匹配 hyper-pace 快剪，电紫霓虹氛围）

## 素材预判
assets_needed: []
> 纯 CSS/HTML 实现：项目卡（ProjectFullCard）、星标数据计数、双光晕背景、紫调网格、霓虹分割线。无需外部素材。

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.7, 0.6, 0.9, 0.55, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（S1：4GB/70B 硬件反差悬念）"
    build: "airllm（S2：揭晓悬念——消费级显卡跑大模型）"
    reveal: "Agent-Reach（S3：给 AI 看全网的眼睛）"
    climax: "AI-For-Beginners（S4：微软系统课单日 +2617 冲上榜首）"
    settle: "TencentDB + generative-ai（S5/S6：团队记忆中枢 + 11 万星生成式 AI 课）"
    summon: "CTA（S7：中性互动 + 关注引导）"

## 黄金 3 秒视觉
hook 场景为全片视觉最强画面：4GB / 70B 巨大字号对撞、电紫 #A855F7 主光晕全开、霓虹分割线、白主色 + 电紫强调，制造硬件反差的视觉冲击。

## 方向
orientation: portrait
orientation_source: category_hint
