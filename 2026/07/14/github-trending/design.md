# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博（GitHub Dark）
mood: 紧凑快节奏盘点（每日热门播报）

## 配色方向（描述性，不指定具体色值；⛔ 领域色只用于视觉，旁白与画面文字禁说颜色词）
color_direction:
  background: 深色暗调（接近纯黑 #0d1117 系，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠蓝（用于 AI 应用/开发者工具项目卡——OpenCut/graphify/awesome-llm-apps/hallmark）
  accent_warm: 金色/琥珀（用于 hook 数字、星标数据、排名、CTA——破千数据锚定）
  text: 白色主 + 浅灰辅（描述层用浅灰，可读不抢）

> 双光晕原则：每场景一个暖光晕（左上，星标/数字锚点）+ 一个冷光晕（右下，技术氛围）。深色底让金色星标和青色标签更突出。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=紧迫快节奏盘点，几何无衬线粗体传递利落专业的科技播报感，与紧凑节奏同向"
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
music_mood: 科技/赛博（低调辅助，clean-corporate 首选，衬底不抢旁白——GitHub 系列快播报 BGM 定位）

## 素材预判
assets_needed: []
- 6 个项目头像已就位（assets/avatars/*.png）
- 数据全部来自 content_ready.txt，纯 CSS/HTML 实现星标数字 + 涨幅，无需外部图表素材

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.6, 0.5, 0.7, 0.8, 0.7, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（双破千数字锚定 + 开源剪映反差）"
    build: "topic1 OpenCut（视频工具，A 档，开源 CapCut 替代）"
    reveal: "topic2 graphify（开发者向，C 档，项目变知识图谱）"
    climax: "topic3 awesome-llm-apps（A 档，百款 AI 应用，最高总星 119554）"
    settle: "topic4 hallmark + topic5 exercises + topic6 Win11Debloat（反AI味/健身数据/系统工具，题材多元收尾）"
    summon: "CTA（中性互动 + 关注）"

## 方向
orientation: portrait
orientation_source: default
