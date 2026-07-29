# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技
mood: 紧凑利落（快播报节奏，多项目盘点不拖沓）

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深蓝/深紫渐变底（接近纯黑，呼应 GitHub Dark）
  accent_cool: 霓虹青/翠绿（用于工具类项目：skills / Chat2DB / superfile）
  accent_warm: 橙金/琥珀（用于 hook / 反直觉亮点 / CTA）
  text: 白色主 + 浅灰辅（高对比，缩略图可读）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"          # Q1 情感内核=紧凑/专业/利落（GitHub 快播报节奏）
    family: "Inter"
    weight: 900
    rationale: "GitHub 日榜快播报信息密度高，几何简洁标题字体承载紧凑节奏，避免衬线字体的厚重感拖慢视觉"
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
music_mood: 低调辅助/科技衬底（clean-corporate 优先，避开 bold-energetic / epic-trailer；不抢旁白）

## 素材预判
assets_needed: []    # 5 项目均由 ProjectFullCard 一屏一项目 + CSS 渐变光效承载，无需外部素材

## 故事板
storyboard:
  narrative_template: "hyper-pace"    # 多项目盘点：快速/密集/爆发/呼吸
  emotion_curve: [0.3, 0.5, 0.7, 0.9, 0.6, 0.4]
  immersion_mode: "hyper-pace"        # AI 类项目占 2/5 + 工具类占 3/5，按 github immersion_mapping 取 hyper-pace
  humor_style: "dual-track"           # 旁白+视觉双线（每 3-4 段至少 1 次幽默，本期偏数据/反直觉，幽默轻量）
  character_presence: true            # 启用码力角色（cool/think/explode 表情跟随节拍）
  beat_mapping:
    grab: "hook（反直觉+数字锚双锚定）"
    build: "ego-lite（反直觉主角铺垫）"
    reveal: "skills（大佬同款揭示）"
    climax: "Instatic（自托管+AI 参与建站，最高亮）"
    settle: "Chat2DB（实用缓和）"
    reveal_secondary: "superfile（次高潮：终端美学小惊喜）"
    summon: "CTA（中性二选一提问）"

## 方向
orientation: portrait
orientation_source: default    # 默认竖屏（无用户显式指定 / 无分类 hint 覆盖）
