# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技悬疑
mood: 紧凑悬疑（hook 抛悬念 → 结尾揭晓）

## 配色方向（描述性，不指定具体色值；具体色值由 Stage 6 按 github default_style 取 #FF8C32 橙 + #4DA8DA 蓝）
color_direction:
  background: 深蓝/深紫暗调（接近纯黑底，衬亮色元素）
  accent_cool: 霓虹青/翠绿（用于项目卡、build/reveal 场景）
  accent_warm: 橙金/琥珀（用于 hook 与 deer-flow climax 揭晓场景，强对比）
  text: 白色主 + 浅灰辅（清晰靠本身亮色 + bg 对比，禁发光浮起）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核为震撼/好奇的科技悬念盘点，紧凑专业利落的几何无衬线最匹配暗色科技快播报"
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
music_mood: 科技/赛博低调（clean-corporate / warm-editorial 首选，衬底不抢人声；github bgm_style 定位低调辅助）

## 素材预判
assets_needed: []
# ProjectFullCard 所需 owner avatar 已由 fetch_avatars.py 预下载到 assets/avatars/（microsoft/usekaneo/iv-org/huggingface/bytedance），Stage 6 从 content_ready.txt 的 avatar 行引用，无需额外抓取

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.85, 0.55, 0.65, 0.95, 0.6, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（抛「AI 连续干几小时」悬念，不点名）"
    build: "AI-For-Beginners, kaneo（你能直接用的开源项目）"
    reveal: "invidious, TRELLIS.2（开源前端 / 一句话生 3D 的反直觉揭示）"
    climax: "deer-flow（揭晓 hook：长周期 SuperAgent，C 档开发者向定调）"
    settle: "沉淀在 deer-flow 揭晓后，过渡到 CTA"
    summon: "CTA（中性二选一互动 + 关注）"

## 方向
orientation: portrait
orientation_source: user_explicit
