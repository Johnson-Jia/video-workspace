# design.md — 视觉风格方向 + 故事板

> 8月16日 AI 风向标 · 双线对决（平民化造 AI vs 给 AI 配装备）

## 风格
style: 暗色科技风（AI 电紫主题 · 本期双色对决编码）
mood: 紧凑对决

## 导演 5 问（全局）
- Q1 情感内核：**震撼 × 对决**——硬件门槛被砍到 4GB 的惊叹，与两派路线并进的军备赛紧张感
- Q2 观众弧线：数字反差震撼（grab）→ 平民化线期待（build）→ 转折发现另一派（reveal）→ 装备线全揭晓（climax）→ 两线对比思考（settle）→ 想试哪个（summon）
- Q3 视觉手段：**双色系叙事编码**——平民化线电紫主导、装备线冷青主导，色彩切换即叙事线切换（本期模板层差异化核心，近三期均为全程单色电紫）
- Q4 相邻反差：平民线（暖紫调）与装备线（冷青调）色温反转；hook 高对比大数字与项目场景信息密集做密度反转
- Q5 视线焦点：每场景唯一焦点=项目名+核心数据，副信息降级

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深紫黑渐变（AI 电紫底，接近纯黑）
  accent_primary: 电紫（平民化线主色：ToolJet/Soup 场景主导）
  accent_cool: 冷青（装备线主色：CLI-Anything/computer/skills 场景主导；两线交锋的 reveal 场景紫青并存）
  accent_warm: 暖橙点缀（数据/涨星/CTA 强调）
  text: 白色主 + 浅灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter 900"
    weight: 900
    rationale: "「震撼×对决」的情感内核是紧凑利落的力量感，几何无衬线最贴合科技对决气质"
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
music_mood: 电子科技（对决感，节奏随双线推进渐强，climax 段最浓）

## 素材预判（可选）
assets_needed: []    # 纯 CSS 渐变/光效 + 项目数据卡片，无需外部素材

## 故事板
storyboard:
  narrative_template: "showdown"   # 紧张→交锋→揭晓→结论；弃用连续三期 contrast-arc（模板层新鲜度）
  emotion_curve: [0.5, 0.55, 0.7, 0.95, 0.55, 0.45]
  immersion_mode: "hyper-pace"     # 分类恒满足（AI 项目占比 100%）
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（4GB vs 8B 数字对比冲击）"
    build: "project1_tooljet, project2_soup（平民化线 · 电紫主导）"
    reveal: "project3_cli_anything（转折进装备线 · 紫青交锋）"
    climax: "project4_computer, project5_skills（装备线高潮 · 冷青主导）"
    settle: "cta 前半（两线对比收束）"
    summon: "cta 后半（中性互动提问 + 关注）"

## 场景规划（7 段，标准模式 5 项目盘点）
| 场景 | 类型 | 时长估 | 情感节拍 | 色彩主导 |
|------|------|--------|---------|---------|
| hook | hook | 4s | grab 0.5 | 紫青双光晕对峙 |
| project1_tooljet | solution | 7s | build 0.55 | 电紫 |
| project2_soup | solution | 7s | build 0.6 | 电紫 |
| project3_cli_anything | features | 7s | reveal 0.7 | 紫青交锋（转场重点） |
| project4_computer | features | 7s | climax 0.95 | 冷青 |
| project5_skills | features | 7s | climax 0.9 | 冷青 |
| cta | cta | 5s | settle+summon 0.5 | 紫青收束 + 暖橙 |

## 方向
orientation: portrait
orientation_source: default
