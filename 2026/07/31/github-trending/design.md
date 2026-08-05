# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 紧凑专业，开源/本地化主线带轻微反差感

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（深蓝/深紫渐变底，接近纯黑衬底）
  accent_cool: 蓝/青（#4DA8DA→#60A5FA 系，用于 AI 项目/数据场景）
  accent_warm: 橙/金（#FF8C32→#FBBF24 系，用于 hook/排名数字/CTA 强调）
  text: 白色主 + 浅灰辅
  双光晕: 暖冷双调（橙暖 + 蓝冷）低强度叠加，营造科技层次感

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "工具/效率盘点内容调性紧凑利落，Q1 情感内核为'专业/省事/反差'，几何无衬线粗体最匹配"
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
music_mood: 低调科技/企业播报（clean-corporate 或 warm-editorial，衬底不抢人声，避开 bold-energetic/epic 激昂系）

## 素材预判
assets_needed: []
（纯 CSS/HTML 实现项目卡片、排名数字、数据指标；owner avatar 已在 assets/avatars/ 由 ProjectFullCard 引用）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.7, 0.85, 0.75, 0.6, 0.45]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（本地语音反直觉）"
    build: "openwork（涨星最高，商业工具开源）"
    reveal: "speech-to-speech（本地语音钩子兑现）"
    climax: "editor（3D 视觉冲击）"
    settle: "last30days（AI 调研实用）"
    summon: "tuicr+PowerToys+CTA（效率工具速览 + 中性提问）"

## 方向
orientation: portrait
orientation_source: default

## 风格补充约束
- text-shadow 极淡 0.08 禁发光（`text-shadow: 0 2px 6px rgba(30,41,59,0.08)`），文字清晰靠本身亮色 + bg 对比
- 渐变文字同色系高饱和禁白色端点（橙 #FF8C32→#FB923C→#FDBA74 / 蓝 #4DA8DA→#60A5FA→#93C5FD / 金 #FBBF24→#F59E0B→#FCD34D）
- 黄金 3 秒：hook 场景字号最大、对比最强、双光晕精致布局
