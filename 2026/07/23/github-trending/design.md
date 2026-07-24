# design.md — 视觉风格方向 + 故事板（2026-07-23 GitHub Trending）

## 风格
style: 暗色科技冷锋（GitHub Dark + 冷光收敛）
mood: 紧凑冷静 / 收敛感（"把碎片收成一件"）

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，#0a0e14 系深空蓝灰）
  accent_cool: 翠青/电子蓝（用于 OmniRoute/dioxus/outlines/Hyprland 的开发者向场景，传达"理性收敛"）
  accent_warm: 琥珀金（用于 hook / worldmonitor 情报 / cloudflare 免费邮箱的钩子和 CTA 场景，传达"价值锚点"）
  text: 白色主 + 浅灰辅 + 同色系高饱和渐变（橙 #FF8C32→#FB923C→#FDBA74；蓝 #4DA8DA→#60A5FA→#93C5FD；金 #FBBF24→#F59E0B→#FCD34D）
  text_shadow: 极淡 drop（rgba(30,41,59,0.08)），禁发光

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "本期情感内核是'收敛感'——把碎片整合成一件，需要利落、几何、专业的标题气质，避免毛笔/圆润带来的温度分散注意力"
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
  - "OmniRoute 网关收敛示意图（一个入口 → 多家服务商辐射）"
  - "dioxus 跨端矩阵图（一套代码 → web/desktop/mobile 三端）"
  - "outlines 结构化输出对比（自由文本 vs JSON Schema 约束）"
  - "Hyprland 平铺桌面示意（动态分屏 + 高定制）"
  - "cloudflare 临时邮箱收发链路图"
  - "worldmonitor 全球情报仪表板带过镜头（不展开）"

## 故事板
storyboard:
  narrative_template: "showdown"
  emotion_curve: [0.45, 0.55, 0.75, 0.9, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（OmniRoute 反直觉钩子）"
    build: "worldmonitor（一带过）+ OmniRoute（重点展开）"
    reveal: "dioxus（一套代码跨端）"
    climax: "outlines + Hyprland（结构化 + 桌面美学）"
    settle: "cloudflare（免费邮箱收尾）"
    summon: "CTA"

## 5 场景视觉规划（对齐 6 项目，标准模式 30-45s）
scenes_plan:
  - id: S1_hook
    type: hook
    duration: 4s
    projects: ["OmniRoute（隐式钩子，不报名）"]
    visual_focus: "一个大字'一个接口'对'两百多家'反差对比，渐变金橙"
    narration_beat: "黄金 3 秒，纯钩子，禁项目名禁铺垫"
    bg_component: "diamond_lattice 或 dark_cipher（冷光收敛感）"

  - id: S2_worldmonitor_omniroute
    type: solution
    duration: 9s
    projects: ["worldmonitor（3s 带过）", "OmniRoute（6s 重点）"]
    visual_focus: "worldmonitor 一句话全球情报仪表板；OmniRoute 网关收敛示意（一入口多服务商辐射）"
    narration_beat: "build，世界情报一带过，OmniRoute 展开'一个接口接 268 家'"
    bg_component: "hex_grid 冷光（理性收敛）"

  - id: S3_dioxus
    type: features
    duration: 8s
    projects: ["dioxus"]
    visual_focus: "一套 Rust 代码 → web/desktop/mobile 三端辐射矩阵"
    narration_beat: "reveal，'一套代码同时跑网页桌面手机'反直觉"
    bg_component: "scan_grid（跨端扫描感）"

  - id: S4_outlines_hyprland
    type: capabilities
    duration: 12s
    projects: ["outlines（6s）", "Hyprland（6s）"]
    visual_focus: "outlines 自由文本 vs JSON Schema 结构化对比；Hyprland 动态平铺桌面 + 颜值"
    narration_beat: "climax，开发者向能力展示"
    bg_component: "contour（结构感）+ 双卡片对比"

  - id: S5_cloudflare_cta
    type: cta
    duration: 7s
    projects: ["cloudflare_temp_email（5s）", "CTA（2s）"]
    visual_focus: "免费临时域名邮箱收发链路；结尾中性互动'你最想试哪个'"
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
