# design.md — 视觉风格方向 + 故事板（2026-07-24 GitHub Trending）

## 风格
style: 暗色科技协作流（GitHub Dark + 冷暖双轨：人/机双辉光）
mood: 紧凑冷静 / 协作感（"AI 不是工具，是队友"）

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，#0a0e14 系深空蓝灰，全片统一深色底）
  accent_cool: 电子蓝/翠青（用于 buzz 人机协作、likec4 架构图、jellyfin 媒体系统的开发者/理性向场景，传达"协作理性"）
  accent_warm: 琥珀金/橙（用于 hook、harper 语法、Pumpkin 游戏、text-to-cad 设计的钩子和强调场景，传达"温度与人味"）
  text: 白色主 + 浅灰辅 + 同色系高饱和渐变（橙 #FF8C32→#FB923C→#FDBA74；蓝 #4DA8DA→#60A5FA→#93C5FD；金 #FBBF24→#F59E0B→#FCD34D）
  text_shadow: 极淡 drop（rgba(30,41,59,0.08)），禁发光

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "本期情感内核是'协作理性'——人+AI 在同一工作空间，需要利落、几何、专业的标题气质，避免毛笔/圆润带来的温度分散注意力"
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
music_mood: 低调科技衬底（clean-corporate / warm-editorial，避开 bold-energetic 抢旁白）
music_keywords: ["clean corporate ambient", "minimal tech underscore", "steady editorial pulse"]
bgm_volume_target: 0.22-0.25

## 素材预判
assets_needed:
  - "buzz 人机协作示意图（人 + AI 同房间，AI agent 开仓库/发补丁/审代码/跑工作流多轨道）"
  - "harper 离线语法检查链路（输入 → 本地 → 不上传云端）"
  - "Pumpkin Rust 重写 Minecraft 服务器（性能 + 开服一键）"
  - "likec4 从代码生成架构图（代码 ↔ 图实时同步）"
  - "text-to-cad 文字描述 → CAD 三维模型"
  - "jellyfin 自建媒体库（影视/音乐本地托管）"

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.45, 0.55, 0.75, 0.9, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（AI 不是工具是队友反差钩子）"
    build: "buzz（人+AI 同房协作新范式，本期重点）"
    reveal: "harper（离线语法检查）+ Pumpkin（Rust Minecraft 服务器）"
    climax: "likec4 + text-to-cad（开发者图形 + CAD 创作能力）"
    settle: "jellyfin（自建媒体库，普通人收尾）"
    summon: "CTA"

## 5 场景视觉规划（对齐 6 项目，标准模式 30-45s）
scenes_plan:
  - id: S1_hook
    type: hook
    duration: 4s
    projects: ["buzz（隐式钩子，不报名）"]
    visual_focus: "大字'AI 不是工具 是队友'反差对比，渐变金橙/电子蓝双辉光"
    narration_beat: "黄金 3 秒，纯钩子，禁项目名禁铺垫"
    bg_component: "diamond_lattice 或 dark_cipher（冷光协作感）"

  - id: S2_buzz
    type: solution
    duration: 10s
    projects: ["buzz（人+AI 协作工作空间，本期主角）"]
    visual_focus: "buzz 多轨道协作示意（人 + AI agent 开仓库/发补丁/审代码/跑工作流）"
    narration_beat: "build，buzz 的'同一房间协作'新范式展开"
    bg_component: "hex_grid 冷光（协作理性）"

  - id: S3_harper_pumpkin
    type: features
    duration: 10s
    projects: ["harper（5s 离线语法）", "Pumpkin（5s Rust Minecraft 服务器）"]
    visual_focus: "harper 离线语法链路（不联网做云端的事）；Pumpkin Rust 重写提速"
    narration_beat: "reveal，A 档可用性的两段并置"
    bg_component: "scan_grid（功能扫描）+ 双卡片对比"

  - id: S4_likec4_texttocad
    type: capabilities
    duration: 11s
    projects: ["likec4（5s 架构图）", "text-to-cad（6s 文字转 CAD）"]
    visual_focus: "likec4 代码 ↔ 架构图实时同步；text-to-cad 文字 → 三维 CAD 模型"
    narration_beat: "climax，开发者向创作能力"
    bg_component: "contour（结构感）+ 双卡片对比"

  - id: S5_jellyfin_cta
    type: cta
    duration: 8s
    projects: ["jellyfin（6s 自建媒体库）", "CTA（2s）"]
    visual_focus: "jellyfin 影视/音乐本地托管链路；结尾中性互动'哪个让你想打开电脑试试'"
    narration_beat: "settle + summon，A 档可用性收尾"
    bg_component: "wave 或 noise（柔和收束）"

## 渲染安全铁律遵守清单（HARD，gate 机器拦截）
- ✅ 禁 CSS opacity:0 入场，所有内容默认 opacity:1，入场用 GSAP `.from({opacity:0})`
- ✅ Phase 1 CSS 可见，Phase 2+ 用 GSAP `.set({opacity:0})`（不在 CSS 写 .phase-2{opacity:0}）
- ✅ 单层 padding 原则（.scene-wrap 或 .phase 设一层，禁双层）
- ✅ .layer-bg 铺满全画幅，.clip 无 top/right/bottom/left 偏移
- ✅ 禁 CSS class 切换可见性（HyperFrames seek 不执行 CSS animation）
- ✅ 禁 .anim-in 类、禁 HTML 实体字符
- ✅ .layer-fx 禁空 div，opacity 下限 0.15
- ✅ 单 timeline + DOM 三层直系（scene-wrap / phase / 元素）
- ✅ 禁 section-tag 小徽章标题
- ✅ 渐变文字同色系高饱和，禁白色端点
- ✅ text-shadow 极淡 rgba(30,41,59,0.08)，禁 0 0 Xpx 发光

## 方向
orientation: portrait
orientation_source: default
