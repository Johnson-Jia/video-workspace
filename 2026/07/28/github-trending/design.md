# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博（AI 能力扩展主题）
mood: 紧凑利落·密度感·未来感

## 配色方向（描述性，具体色值由 Stage 6 按 github 分类配置落地）
color_direction:
  background: 深蓝/深紫暗调，接近纯黑（#0a0e1a 基底），承载霓虹光晕
  accent_cool: 霓虹青/翠绿（用于 AI 能力场景：看视频/陪玩/查资料的科技感）
  accent_warm: 金色/琥珀（用于 hook 钩子数字、星标数据、CTA 召唤）
  text: 白色主 + 浅灰辅，禁白色端点渐变（OLED 过曝），用同色系高饱和
  shadow_rule: text-shadow 极淡 drop（rgba(30,41,59,0.08)），禁发光 0 0 Xpx

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "本期主题「AI 能力扩展」情感内核是紧凑/专业/利落的科技工具感，几何无衬线粗体最匹配；避免毛笔/衬线的厚重感压制工具盘点的节奏"
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
music_mood: 科技/赛博低调衬底（clean-corporate 或 monochrome 首选，低调不抢旁白；避开 bold-energetic/epic 激昂高频）

## 素材预判
assets_needed: []
- 数据对比用 CSS 柱状/计数动画（星标增量）
- 功能列表用 emoji/HTML 内联图标
- 氛围感用 CSS 渐变光晕背景（霓虹青/金双光晕）
- 纯 CSS/HTML 实现，无需外部素材

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  narrative_rationale: "多项目快速盘点（6 项目）+ AI 主题占半，适合 hyper-pace 快速→密集→爆发→呼吸弧线；刻意避开近期的 contrast-arc/mystery-box 模板做差异化"
  emotion_curve: [0.4, 0.6, 0.75, 0.9, 0.65, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（钩子：让 AI 看视频的反直觉）"
    build: "claude-video（hook 主体延伸，AI 看懂视频的能力展开）"
    reveal: "airi（自托管 AI 伴侣陪玩家打游戏，惊喜揭示）"
    climax: "last30days-skill（AI 跨平台调研，能力高潮）"
    settle: "GeoLibre + jenkins + bitchat（GIS 地图/CI-CD 基建/蓝牙快报，节奏回落收束）"
    summon: "CTA（关注引导）"

## 方向
orientation: portrait
orientation_source: default

## 场景规划（7 场景，标准模式，预估总时长 47-52s，字数 260-300）
# 1. hook（grab, 4s）—— 纯钩子，前 5 秒无项目名
# 2. claude-video（build, 8s）—— 让 AI 看懂视频，反直觉展开
# 3. airi（reveal, 8s）—— 自托管 AI 伴侣，陪玩 Minecraft
# 4. last30days-skill（climax, 7s）—— AI 跨平台调研
# 5. GeoLibre（settle, 7s）—— 浏览器里的 GIS 地图
# 6. jenkins + bitchat 快报（settle, 8s）—— 老牌 CI/CD + 蓝牙断网群聊增量
# 7. CTA（summon, 5s）—— 结尾二选一互动 + 关注

## 受众与配比
- A 档 3 个（airi/GeoLibre/bitchat）= 50%，B 档 2 个（claude-video/last30days），C 档 1 个（jenkins）≤1/3
- hook 突出 A/B 档「你能直接用」利益；C 档 jenkins 用「给做运维的开发者」定调

## 新鲜度对齐
- hook 主题「AI 能力扩展（让 AI 看视频）」≠ 近 7 期任何主题（断网群聊/AI 审美/AI 队友/企业转型/周榜 AI 编程/砍 AI 输入）
- 数字锚点：6 个项目 + 反直觉「让 AI 看视频」（避近期「单日涨星/砍输入」锚点）
- 叙事模板：hyper-pace（避近期 contrast-arc/mystery-box）
