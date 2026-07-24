# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博        # GitHub 分类默认暗色科技风
mood: 紧凑多元·新上榜密度冲击  # 4 新上榜 + 学习/营销题材，节奏紧凑但跨多个 AI 子方向

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/电蓝（用于编程代理/学习手册场景 openinterpreter/maths-cs-ai）
  accent_warm: 琥珀橙/金（用于 hook/DeepTutor/marketingskills/CTA 场景的暖冷对比）
  text: 白色主 + 浅灰辅
  contrast_strategy: 双光晕暖冷对比——AI 编程/学习偏冷光（青蓝），AI 辅导/营销/健身偏暖光（橙金），形成场景间视觉差异
  # ⛔ 领域色只用于视觉（卡片色环/边框/标签/渐变标题），旁白与画面文字禁说颜色词

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"            # 4 新上榜多元题材 + 紧凑盘点，几何无衬线传递'多元利落'视觉调性
    family: "Inter"
    weight: 900
    rationale: "AI/学习/营销多元题材 + 新上榜密度钩子，几何简洁字体传递'紧凑盘点'的视觉调性，与'4 新上榜'数字锚点呼应"
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
music_mood: 低调科技衬底（clean-corporate 系，不抢旁白）
bgm_style_hint: 首选 clean-corporate / warm-editorial，避免 bold-energetic（github 分类 bgm_style：激昂配乐抢人声）

## 素材预判
assets_needed: []   # 纯 CSS/HTML 实现，无需外部素材；avatar 已在 assets/avatars/

## 故事板
storyboard:
  narrative_template: "hyper-pace"    # 6 项目盘点快速切换，新上榜密度驱动
  emotion_curve: [0.4, 0.55, 0.65, 0.8, 0.6, 0.4]  # grab 数字锚定 → build → reveal → climax（skills 榜首）→ settle → summon
  immersion_mode: "hyper-pace"        # 6 项目盘点，AI 编程/辅导/学习/营销 + 健身多元，快速切换节奏
  humor_style: "dual-track"           # 旁白+视觉双线，build/reveal/settle 节拍注入类比幽默
  character_presence: true            # GitHub 分类启用码力角色
  beat_mapping:
    grab: "hook"                      # 4 新上榜 + 首榜 2130 数字锚定
    build: "openinterpreter"          # 低成本编程代理（钩子主角展开）
    reveal: "DeepTutor"               # AI 终身辅导（普世学习场景揭示）
    climax: "maths-cs-ai + marketingskills"  # AI 学习手册 + AI 营销（高潮：AI 给开发者/学习者/营销人赋能多元）
    settle: "exercises-dataset"       # 健身动作库（沉淀：非 AI 差异化）
    summon: "skills + CTA"            # 工程师技能包榜首带过 + 中性互动收尾

## 6 项目场景规划（7 场景，标准模式）
# S1 hook (4s) — 4 新上榜 + 今日榜首 2130 星，纯钩子不含项目名，数字锚定
# S2 openinterpreter (8s) — 低成本模型编程代理，Rust 本地跑 AI 编程，6.5 万星
# S3 DeepTutor (7s) — AI 终身辅导，国内高校团队，2.6 万星
# S4 maths-cs-ai-compendium (7s) — AI/ML 研究工程师学习手册，5.9K 星（给学习者的）
# S5 marketingskills (7s) — AI 营销技能包，转化率/文案/SEO/增长，4 万星
# S6 exercises-dataset (6s) — 1324 健身动作库带动画，非 AI 差异化，1.4 万星
# S7 skills + CTA (6s) — 工程师技能包榜首 +2130 带过 + 中性互动「这6个你会用哪个」
# 总字数目标：250-380 字，时长 ~45-50s

## 方向
orientation: portrait
orientation_source: default
