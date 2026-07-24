# design.md — 视觉风格方向 + 故事板（GitHub 第30周周榜）

## 风格
style: 暗色科技（GitHub Dark + 周榜盘点）
mood: 紧凑盘点 + 节奏感强

## 配色方向（描述性，不指定具体色值；五分组用领域色环，旁白/画面文字禁颜色词）
color_direction:
  background: 深色暗调（接近纯黑，#0d1117 系）
  accent_cool: 霓虹青/翠绿（用于开发者技能、AI 编程场景的视觉色环/边框）
  accent_warm: 金色/琥珀（用于 hook/CTA/OpenCut 涨幅王场景的强调）
  accent_mid: 紫/品红（用于 AI 应用、AI 垂直的卡片色环，仅视觉）
  text: 白色主 + 浅灰辅

> ⛔ weekly_mode 色彩铁律：领域色只用于视觉（卡片色环/边框/标签/渐变标题文字），旁白与画面文字禁说颜色词（"冷蓝""暖橙""紫色""金色""绿色"等）。颜色是视觉概念，观众听/看颜色词无意义且突兀；旁白按项目内容/领域名分组引导（"创作工具这组""AI 编程""AI 应用"），不用颜色词。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "盘点节奏紧凑，几何粗体配数字锚定最有力；标题大字号+紧凑字距突出'涨幅王/第30周'等关键数字"
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
music_mood: 低调辅助（clean-corporate 系，衬底不抢人声；详见 categories/github.md audio.bgm_style）

## 素材预判
assets_needed: []
> 周榜项目数据已由 stage1 gh API 14/14 验证 + HTTP 直连补全 weekly stars，无需额外素材

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.6, 0.5, 0.55, 0.65, 0.7, 0.6, 0.45]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "scene1 hook（涨幅王 + 周次）"
    build: "scene2 创作工具组"
    reveal: "scene3 开发者技能组"
    climax: "scene4 AI 编程组 + scene5 AI 应用组"
    settle: "scene6 AI 垂直与工具组"
    summon: "scene7 CTA（周次收尾 + 中性二选一）"

## 方向
orientation: portrait
orientation_source: default

## weekly_mode 合规检查清单（HARD）
- [x] 6-7 场景（本期 7 场景：hook + 5 分组 + CTA）
- [x] 字数 300-450
- [x] hook 含"第30周"
- [x] CTA 含"第30周"或"7月13日-20日" + 中性二选一（禁站队）
- [x] 旁白/画面文字禁颜色词（冷蓝/暖橙/紫/金/绿），用领域名分组
- [x] OpenCut 用"开源视频剪辑工具"（禁 CapCut/剪映）
- [x] hallmark 用"去 AI 味设计技能"（禁 Claude Code/Cursor/Codex）
- [x] openinterpreter 用"开源模型编程智能体"（禁 Kimi K3）
- [x] OfficeCLI 用"专为 AI 做的 Office 套件"（禁"首个/最佳"绝对化）
- [x] codex 项目名保留（openai/codex）
- [x] 项目名必报（每组首个项目报全名 owner/repo）
- [x] >15s 场景拆 visual_phases（anchor dict）
