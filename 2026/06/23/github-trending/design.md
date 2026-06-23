# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技·霓虹爆点        # 深色底 + 霓虹青主调 + 金/橙强调，匹配「AI做视频当道」爆点主题
mood: 紧凑震撼                   # 涨星爆发 + 角色错位反转的震撼紧凑基调

## Q1 情感内核推导
- 主情感：震撼（今日涨星王+第二都是AI视频方向，写代码的AI助手居然变成做视频工作室）
- 次情感：期待（AI做视频工具平民化的趋势信号）
- 适配字体气质：几何简洁（Inter 900）—— 紧凑/专业/利落，强化「科技爆点」的冲击感

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑 + 深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于 AI 视频/AI 编程类项目场景、build/reveal 节拍）
  accent_warm: 金色/琥珀橙（用于 hook 排名数字、涨星数据、CTA 召唤场景）
  text: 白色主 + 浅灰辅（信息层级：排名/星标 > 项目名 > 描述）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 震撼+科技爆点，几何无衬线体最贴合「AI做视频当道」的紧凑专业感，标题冲击力干脆利落"
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
music_mood: 科技/赛博（紧凑电子，匹配 hyper-pace 快速剪辑节奏，BPM 偏快）

## 素材预判
assets_needed: []
# 全部用 CSS/HTML 内联实现：渐变光晕背景、霓虹网格、粒子流、数字计数动画、卡片
# 项目头像已预下载到 assets/avatars/，Stage 6 ProjectFullCard 引用

## 故事板
storyboard:
  narrative_template: "contrast-arc"    # 钩子（AI做视频当道）→ 各项目对比展开 → OpenMontage高潮（角色错位）→ airllm第二反直觉 → CTA沉淀召唤
  emotion_curve: [0.35, 0.55, 0.75, 0.95, 0.6, 0.4]  # grab平淡开场→build期待→reveal惊喜→climax爆点→settle思考→summon行动
  immersion_mode: "hyper-pace"          # AI/编程类项目占比 4/6 > 50%，按 immersion_mapping 选 hyper-pace（快速剪辑+密集粒子+霓虹青）
  humor_style: "dual-track"             # 旁白+视觉双线幽默（gstack 抄作业梗、airllm 大象进盒子类比）
  character_presence: true              # GitHub 分类启用码力角色，climax/explode 出场
  beat_mapping:
    grab: "hook（AI做视频当道·反直觉钩子）"
    build: "OpenMontage（涨星王+角色错位）"
    reveal: "penpot + Stirling-PDF（免费平替·本地隐私）"
    climax: "gstack（硅谷大佬作业）+ airllm（大象进盒子·第二反直觉爆点）"
    settle: "趋势沉淀（AI做视频平民化）"
    summon: "CTA（中性互动+关注）"

## 方向
orientation: portrait        # github 分类无 orientation_hint，默认竖屏（1080×1920）
orientation_source: default
