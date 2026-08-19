# design.md — 视觉风格方向 + 故事板

> 8月19日 AI 风向标 · 小模型进设备专题（AI 装进口袋——mystery-box 趋势揭示）

## 风格
style: 暗色科技风（AI 电紫主题 · 本期微缩质感）
mood: 悬念揭秘，紧凑收束

## 导演 5 问（全局）
- Q1 情感内核：**悬念 × 惊喜**——「14MB 能装下 AI 大脑？」的不可置信，与一个个项目接力揭晓「AI 真的在离开云端」的趋势惊喜
- Q2 观众弧线：体积反差好奇（grab）→ 14MB 竟真存在（build）→ 家里就能训（reveal）→ Mac 变私人机房（climax）→ AI 从瞎猜变查证、文档喂得对（settle，回到自己身边）→ 想要哪个（summon）
- Q3 视觉手段：**微缩 vs 巨型的尺度张力**——电紫主色下，「14MB」等巨型数字与手表/菜单栏等微缩元素同框对比；趋势线用青色辅助递进，CTA 暖橙收束
- Q4 相邻反差：hook 大数字高对比留白 vs 项目场景信息密集（密度反转）；端侧线（电紫主导）与靠谱线（电紫+青递进）色温层次递变
- Q5 视线焦点：每场景唯一焦点=项目名+核心数据（14MB / 7.4万★ / 1.9万★），副信息降级

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深紫黑渐变（#0a0a14 → #1a0a2e，接近纯黑的 AI 电紫底）
  accent_primary: 电紫（主色：hook 巨型数字、端侧线项目主导）
  accent_cool: 冷青（辅色：靠谱线项目递进、趋势揭示点缀）
  accent_warm: 暖橙（点缀：涨星数据/CTA 强调）
  text: 白色主 + 浅灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter 900"
    weight: 900
    rationale: "「悬念×惊喜」的好奇驱动需要利落紧凑的科技气质，几何无衬线大数字最有冲击力（14MB 巨型数字全靠它撑）"
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
music_mood: 电子科技（悬念感起，节奏随线索链递进，climax 段最浓，CTA 收束回落）

## 素材预判（可选）
assets_needed: []    # 纯 CSS 渐变/光效 + 项目数据卡片 + avatars，无需外部素材

## 故事板
storyboard:
  narrative_template: "mystery-box"   # 好奇→线索→揭示→惊喜；14MB 是悬念盒，六项目是线索链；弃用上期 showdown（模板层新鲜度）
  emotion_curve: [0.5, 0.6, 0.7, 0.9, 0.55, 0.45]
  immersion_mode: "hyper-pace"     # 分类恒满足（AI 项目占比 100%）
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（14MB 装进手表的体积反差）"
    build: "project_needle（开盒：14MB AI 大脑真的存在）"
    reveal: "project_unsloth（家里图形界面就能训）"
    climax: "project_omlx（Mac 菜单栏变私人机房——端侧线收束最高点）"
    settle: "project_last30days, project_docling（AI 靠谱化：查证型+喂得对口粮）"
    summon: "cta（OpenViking 记忆底座一句 + 中性二选一 + 关注）"

## 场景规划（7 段，标准模式 6 项目盘点：hook + 5 项目段 + CTA 段含第 6 项目）
| 场景 | 类型 | 时长估 | 情感节拍 | 色彩主导 |
|------|------|--------|---------|---------|
| hook | hook | 4s | grab 0.5 | 电紫巨型数字 + 紫青双光晕 |
| project_needle | solution | 8s | build 0.6 | 电紫 |
| project_unsloth | solution | 9s | reveal 0.7 | 电紫+暖橙数据 |
| project_omlx | features | 8s | climax 0.9 | 电紫+青（机房感） |
| project_last30days | features | 9s | settle 0.55 | 紫青递进 |
| project_docling | features | 9s | settle 0.5 | 紫青递进+暖橙 |
| cta | cta | 10s | summon 0.45 | 紫青收束 + 暖橙 CTA |

## 方向
orientation: portrait
orientation_source: default
