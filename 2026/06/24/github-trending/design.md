# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技·霓虹复刻        # 深色底 + 霓虹青/翠绿主调（冷色科技风，github 分类色偏冷）+ 金/橙强调（涨星/CTA），匹配「复刻专业能力」主题
mood: 紧凑灵动                   # AI 复刻平民化的灵动 + 涨星爆发的紧凑震撼

## Q1 情感内核推导
- 主情感：灵动震撼（今日涨星王 OpenMontage 把 AI 编程助手变成视频工作室，还有克隆网站/抄大佬配置，专业能力被复刻的冲击）
- 次情感：好奇（全球情报看板 + LLM 多市场数据的视野拓展）
- 适配字体气质：几何简洁（Inter 900）—— 紧凑/专业/利落，强化「复刻专业能力」的科技感

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑 + 深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于 AI 复刻/克隆类项目场景、build/reveal 节拍）
  accent_warm: 金色/琥珀橙（用于 hook 排名数字、涨星数据、CTA 召唤场景）
  accent_purple: 紫色（用于 gstack 大佬配置场景的尊贵感）
  text: 白色主 + 浅灰辅（信息层级：排名/星标 > 项目名 > 描述）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 灵动+科技复刻，几何无衬线体最贴合「AI 帮你复刻专业能力」的紧凑专业感，标题冲击力干脆利落"
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
music_mood: 科技/赛博（紧凑电子，匹配 hyper-pace 快速剪辑节奏，BPM 偏快；冷色科技风选电子/氛围）

## 素材预判
assets_needed: []
# 全部用 CSS/HTML 内联实现：渐变光晕背景、霓虹网格、粒子流、数字计数动画、卡片
# 项目头像已预下载到 assets/avatars/，Stage 6 ProjectFullCard 引用

## 故事板
storyboard:
  narrative_template: "contrast-arc"    # 钩子（复刻主题）→ OpenMontage 高潮（角色错位涨星王）→ 克隆网站+抄大佬配置（复刻支线）→ daily_stock+worldmonitor（数据情报）→ English 差异化收尾 → CTA沉淀召唤
  emotion_curve: [0.35, 0.55, 0.75, 0.95, 0.6, 0.4]  # grab平淡开场→build期待→reveal惊喜→climax爆点→settle思考→summon行动
  immersion_mode: "hyper-pace"          # AI/编程类项目占比 3/6 = 一半，按 immersion_mapping 选 hyper-pace（快速剪辑+密集粒子+霓虹青）
  humor_style: "dual-track"             # 旁白+视觉双线幽默（gstack 抄作业梗、克隆网站类比）
  character_presence: true              # GitHub 分类启用码力角色，climax/explode 出场
  beat_mapping:
    grab: "hook（复刻专业能力·反直觉钩子）"
    build: "OpenMontage（涨星王+角色错位）"
    reveal: "ai-website-cloner + gstack（克隆网站·抄大佬作业）"
    climax: "daily_stock + worldmonitor（多市场情报·全球视野·第二爆点）"
    settle: "English（非技术差异化收尾）"
    summon: "CTA（中性互动+关注）"

## 方向
orientation: portrait        # github 分类默认竖屏（1080×1920）
orientation_source: default
