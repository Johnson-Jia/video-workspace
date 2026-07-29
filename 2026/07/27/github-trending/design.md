# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技·揭秘感（深色底 + 双强调色，揭 AI 套路的冷峻调性）
mood: 好奇紧凑·带点调侃（揭秘 AI 审美套路，节奏明快但不激昂）

## 配色方向（描述性，沿用 github 分类暗色科技风）
color_direction:
  background: 深色暗调（接近纯黑/深蓝紫，让强调色跳出来）
  accent_cool: 霓虹青蓝（用于工具/效率/金融场景，#4DA8DA 系）
  accent_warm: 琥珀橙金（用于 hook/CTA/反差强调，#FF8C32 系）
  text: 白色主 + 浅灰辅
  note: 双光晕（暖冷）做科技感，文字 text-shadow 极淡（rgba 0.08 禁发光），渐变文字用同色系高饱和禁白色端点

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核是'揭秘 AI 套路'的反差+知识感，几何简洁的标题字传递紧凑专业的科技工具调性，比衬线更利落、比毛笔更理性"
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
music_mood: 科技/低调辅助（clean-corporate 或 warm-editorial 系，衬底不抢人声，激昂电子避开）

## 素材预判
assets_needed: []
（纯 CSS/HTML 组件实现：ProjectFullCard 一屏一项目、数据计数动画、终端模拟界面、AI 套路对比卡）

## 故事板
storyboard:
  narrative_template: "mystery-box"    # 揭秘弧：好奇→线索→揭示→惊喜（避昨天 contrast-arc，换叙事结构做新鲜度）
  emotion_curve: [0.45, 0.6, 0.8, 0.75, 0.5, 0.4]   # 好奇抛出 AI 套路 → 逐个揭秘解法项目 → 惊喜高潮 → 沉淀快报 → 召唤
  immersion_mode: "fun-tool"           # 有趣工具：彩色弹跳+亮色（匹配工具/AI 应用切面，避近期 hyper-pace）
  humor_style: "dual-track"            # 旁白+视觉双线，build/reveal/settle 节拍注入调侃
  character_presence: true             # 启用码力角色，高潮与调侃段出场
  beat_mapping:
    grab: "hook（抛 AI 审美套路悬念）"
    build: "impeccable（揭设计套路解法）"
    reveal: "Kronos（揭金融跨界）、superfile（揭终端美学）"
    climax: "aisuite（揭 AI 办公同事，高潮）"
    settle: "霸榜快报（bitchat+buzz+Pumpkin 一句带过）"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default
