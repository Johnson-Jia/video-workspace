# design.md — 视觉风格方向 + 故事板（GitHub 第31周周榜）

## 风格
style: 暗色科技（GitHub Dark + 周榜盘点）
mood: 紧凑盘点 + 节奏感强 + 分组层次清晰

## 配色方向（描述性，不指定具体色值；四分组用领域色环，旁白/画面文字禁颜色词）
color_direction:
  background: 深色暗调（接近纯黑，#0d1117 系，渐变深蓝/深紫基底）
  group_ai_coding: 蓝（AI 编程助手组的卡片色环/边框/标签/渐变标题文字）
  group_dev_tool: 橙（开发者效率工具组的视觉色环/边框）
  group_info_learn: 紫（信息与学习组的视觉色环/边框）
  group_utility: 金（实用工具组的视觉色环/边框）
  accent_warm: 橙/金（用于 hook 涨幅王场景强调）
  text: 白色主 + 浅灰辅

> ⛔ weekly_mode 色彩铁律：领域色（蓝/橙/紫/金）只用于视觉（卡片色环/边框/标签/渐变标题文字），旁白与画面文字禁说颜色词（"冷蓝""暖橙""紫色""金色""绿色"等）。颜色是视觉概念，观众听/看颜色词无意义且突兀；旁白按项目内容/领域名分组引导（"AI 编程助手这组""开发者工具""信息与学习""实用工具"），不用颜色词。

> ⛔ 渐变文字配色（禁白色端点 + 同色系高饱和）：background-clip:text 渐变禁 #fff/white 端点（OLED 过曝泛光）。用同色系高饱和：橙 #FF8C32→#FB923C→#FDBA74 / 蓝 #4DA8DA→#60A5FA→#93C5FD / 紫 #A78BFA→#C4B5FD→#DDD6FE / 金 #FBBF24→#F59E0B→#FCD34D。

> ⛔ text-shadow 规则（极淡 0.08，禁发光）：text-shadow: 0 2px 6px rgba(30,41,59,0.08)（几乎看不见）。禁发光 0 0 Xpx rgba(...)。文字清晰靠本身亮色 + bg 对比。

## 字体（三层）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "盘点节奏紧凑，几何粗体配数字锚定最有力；标题大字号+紧凑字距突出'涨幅王/第31周/周涨近一万六千星'等关键数字"
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
> 周榜项目数据已由 stage1 gh API 验证（rank1/3/4/18 四个高涨幅项目 watchers/size 复核通过）+ raw_trending weekly stars 已补全，avatars 已预下载，无需额外素材

## 故事板（7 场景，45-60s）
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.65, 0.55, 0.6, 0.6, 0.65, 0.7, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  scene_count: 7
  beat_mapping:
    grab: "scene1 hook（涨幅王 ai-agent-book +15909 + 第31周 + 领域分布）"
    build: "scene2 AI 编程助手组（ai-agent-book/orca/pi/jcode，蓝色环）"
    reveal: "scene3 开发者效率工具组（OmniRoute/code-review-graph/hallmark/awesome-claude-skills，橙色环）"
    develop: "scene4 信息与学习组（worldmonitor/ai-engineering-from-scratch/DeepTutor，紫色环）"
    climax: "scene5 实用工具组（open-seo/croc/Instatic，金色环）"
    settle: "scene6 趋势总结（本周领域分布 + 一半能直接用的利益角度）"
    summon: "scene7 CTA（第31周周榜收尾 + 中性二选一）"

## 方向
orientation: portrait
orientation_source: default

## weekly_mode 合规检查清单（HARD）
- [x] 6-7 场景（本期 7 场景：hook + 4 分组 + 趋势总结 + CTA）
- [x] 字数 300-450
- [x] hook 含"第31周"（禁只用"本周"）
- [x] CTA 含"第31周"或"07月20日-27日" + 中性二选一（禁站队）
- [x] 旁白/画面文字禁颜色词（冷蓝/暖橙/紫/金/绿），用领域名分组
- [x] ai-agent-book 泛化"国内技术作者"（禁"李博杰"真实人名）
- [x] DeepTutor 旁白/画面去 URL
- [x] OmniRoute 用"免费 AI 网关/一个接口接多家服务商"（中文泛化，禁裸报 Kimi/Claude/GPT 等品牌名）
- [x] open-seo 用"开源 SEO 工具"（禁 Semrush/Ahrefs 商业产品名）
- [x] Instatic 用"开源自托管建站系统"（禁 Webflow/Framer/WordPress 商业产品名）
- [x] jcode 用"智能 agent 框架"（原文 most intelligent 含极限词，中文去极限词）
- [x] 项目名必报（每组首个项目报全名 owner/repo）
- [x] >15s 场景拆 visual_phases（anchor dict，{start_sentence: N}）
- [x] 禁 R-G-016 六词（一带而过/快速带过/老朋友/熟面孔/先放一边/信息节制）
