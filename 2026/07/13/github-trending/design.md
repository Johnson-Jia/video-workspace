# design.md — 视觉风格方向 + 故事板

## 风格
style: 科技赛博数据感
mood: 紧凑反差（开篇数字冲击 + 中段硬核信息密度 + 收尾对比张力）

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，承载 6 个项目高强度信息）
  accent_cool: 霓虹青/翠绿（用于 destructive_command_guard / pgrust 等开发者向 + AI 安全场景，技术冷感）
  accent_warm: 金色/琥珀（用于 Vibe-Trading 涨星王 + home-assistant 生活 IoT + CTA 场景，利益钩子暖色）
  text: 白色主 + 浅灰辅（深色底高对比）

## 字体（三层 + voice 链接）
fonts:
  title:
    voice: "数据冲击力"
    family: "Ma Shan Zheng"
    weight: 400
    rationale: "数字锚点 hook 需要毛笔体的力量感做单日近八百星的视觉锤"
    fallback: "'Ma Shan Zheng','PingFang SC','Microsoft YaHei',cursive"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/赛博（github 分类 default_style，beat-heavy 但需校准，避免抢旁白）

## 素材预判
assets_needed: [home-assistant 截图意象可用 emoji/svg，其余以数据卡片为主，无需外部素材]

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.6, 0.5, 0.8, 0.9, 0.7, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: false
  beat_mapping:
    grab: "hook（涨星王 +776 数字锚定 + AI 反差对照悬念）"
    build: "Vibe-Trading + pgrust（两个硬核技术：金融AI + 数据库重写）"
    reveal: "destructive_command_guard（反直觉反转：专门防 AI 干蠢事）"
    climax: "home-assistant（89K 总星生活向题材平衡 + 强利益）"
    settle: "hallmark + DesktopCommanderMCP（去 AI 味 + AI 接管电脑）"
    summon: "CTA（中性互动：想试哪个）"

## 方向
orientation: portrait
orientation_source: default
