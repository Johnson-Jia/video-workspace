# design.md — 视觉风格方向 + 故事板（2026-06-21 GitHub Trending，重做版）

## 风格
style: 暗色科技赛博（GitHub 系列统一基调）
mood: hook 段反差冲击力强（个人 vs 大厂 + 13.8万星数字），正文段一屏一项目信息密度高，CTA 段温暖收束

## 配色方向
color_direction:
  background: 深色暗调（接近纯黑 #0A0E1A，深蓝/深紫渐变做底）
  accent_cool: 霓虹青蓝（#4DA8DA / #00D4FF，用于开发者技能/AI类项目场景与数据高亮）
  accent_warm: 琥珀橙金（#FF8C32 / #FFB800，用于 hook 场景总星数字锚定、ProjectFullCard 排名编号、CTA 场景）
  text: 白色主 + 浅灰辅（#E8EDF5 / #8B95A8）
  glow: 双光晕（冷青蓝外晕 + 暖橙金内晕，对应 GitHub 分类「双光晕」配置）

## 字体
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "工具盘点类的紧凑专业气质，需要几何简洁的标题字体承载反差钩子（一个人13.8万星盖过大厂）与数字锚点（+3786/41,990★）的冲击力"
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
music_mood: 科技/赛博，紧凑节奏，hook 段能量饱满（个人 vs 大厂反差+数字冲击），正文段稳定推进（一屏一项目节奏），headroom 段高潮数据爆点，CTA 段温暖收束
关键词: tech, cyber, energetic, focus, modern

## 素材预判
assets_needed: []
- 6 项目卡片用 ProjectFullCard 组件（avatar + 8 层信息：类别标签/排名/项目名/描述/语言/星标增量/三词卖点/感性评语），无需额外外部素材
- 总星/涨星数字用 data 计数动画，纯 CSS/JS 实现
- hook 场景用 hero 大标题 + 数字光晕（13.8万 总星锚定 + 个人 vs 大厂反差）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.4, 0.55, 0.7, 0.85, 0.95, 0.65, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（skills 反差开场）"
    build: "skills（反直觉展开）"
    reveal: "Pake"
    climax: "palmier-pro, headroom（涨星王数据爆点）"
    settle: "codebase-memory-mcp, SmsForwarder"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default

## 场景规划（6 项目标准模式，一屏一项目，新顺序）
- hook（4s, grab）: 反差+数字锚定钩子 — 一个人.claude目录里的技能整理，总星十三万八，盖过众多大厂项目（彻底避开砍token主题，换个人 vs 大厂反差）
- skills（7s, build）: 反直觉展开 — 一位工程师公开的 .claude 实用技能合集，拿来即用；一个人的目录整理，总星 13.8 万，盖过众多大厂项目（A 档普通人可抄）
- Pake（7s, reveal）: 一条命令把网页打包成桌面应用，Rust 写的体积小启动快，普通人开箱即用
- palmier-pro（7s, climax）: macOS 上的视频编辑器，反过来为 AI 设计，把 AI 能力做成剪辑主轴
- headroom（7s, climax）: 单日涨星王 — 当日 +3786★ 冲上四万星（41,990★）。角度用「单日涨星最猛」强调数据，不点破压缩比例，不复述06/20的砍token机制
- codebase-memory-mcp（6s, settle）: 给开发者，把整个代码库索引成可查询图谱，查询不到一毫秒（C 档明确受众）
- SmsForwarder（5s, settle）: 旧安卓手机化身通知中枢，短信验证码自动转发到常用渠道
- CTA（4s, summon）: 结尾站队二选一 + 关注引导（Pake 和 palmier-pro 你更想用哪个，避开上版问题）
预估总时长: 45-50s，字数 280-340

## 黄金 3 秒视觉要求
hook 场景必须是全片视觉最强画面——字号最大（反差词「盖过」+ 数字「13.8万星」）、对比最强（深色底 + 琥珀橙金数字光晕 + 个人 vs 大厂双栏反差）、布局最精致（hero 大标题居中 + 总星数字计数动画）。
