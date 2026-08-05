# design.md — 视觉风格方向 + 故事板（github 暗色科技风 portrait）

## 风格
style: 暗色科技风
mood: 紧凑专业、信息密集、数据驱动

## 配色方向（描述性，不指定具体色值；具体色值由 Stage 6 按组件库决定）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/翠绿（用于数据、技术栈、安全/硬件场景；hyper-pace 主色 #00D4FF 系）
  accent_warm: 橙/琥珀（用于 hook、排名数字、CTA、亮点强调 #FF8C32 系）
  text: 白色主 + 浅灰辅
  text_shadow_rule: 极淡 drop 0.08，禁发光；渐变文字禁白端点，用同色系高饱和

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "信息密度高+震撼数据的盘点调性需要紧凑专业的标题气质，几何无衬线最贴合暗色科技风"
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
music_mood: 低调科技/衬底不抢（clean-corporate / monochrome 系，避开 bold-energetic/epic）

## 素材预判
assets_needed: []   # 纯 CSS/HTML 实现，ProjectFullCard 卡片 + 数据动画，无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.5, 0.6, 0.8, 1.0, 0.6, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（ESP32 反直觉钩子）"
    build: "AI-For-Beginners（最高涨星+大厂教育）"
    reveal: "openwork（大厂收费→免费开源）、ESP32-Bit-Pirate（硬件安全研究）"
    climax: "reverse-skill（AI 自动做安全研究）、chatwoot（免费搭全渠道客服）"
    settle: "last30days-skill（高频霸榜快速带过）"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default

## 各项目视觉规划（含 contrarian_angle）
projects:
  - name: AI-For-Beginners
    contrarian_angle: "微软把价值上万的 AI 培训整套免费放了，12 周 24 节系统课"
    类别标签: "大厂免费课"
    核心指标: "+1592 今日最高涨星"
    三词卖点: "系统入门·完全免费·大厂出品"
  - name: openwork
    contrarian_angle: "大厂月收费的 AI 协同编程工具，这里开源免费用（旁白/画面不点大厂品牌名，用泛化）"
    类别标签: "开源替代版"
    核心指标: "+796 单日涨星"
    三词卖点: "免费开源·AI协同·本地可控"
  - name: ESP32-Bit-Pirate
    contrarian_angle: "几十块的芯片当硬件安全研究站，网页终端撬开几十种通信协议"
    类别标签: "硬件安全研究"
    核心指标: "20+ 通信协议 / 5K★"
    三词卖点: "网页终端·全协议·低价硬件"
  - name: reverse-skill
    contrarian_angle: "AI 自动路由帮你做逆向和安全研究，按需配工具链和经验库"
    类别标签: "AI安全路由"
    核心指标: "+612 单日涨星"
    三词卖点: "AI自动路由·安全研究·自进化"
  - name: chatwoot
    contrarian_angle: "几万块的客服软件，开源免费自己搭，在线聊天邮件一体化"
    类别标签: "开源客服系统"
    核心指标: "35K★ 老牌项目"
    三词卖点: "全渠道·免费自建·多平台"
  - name: last30days-skill
    contrarian_angle: "AI 自动跨平台帮你做话题调研（高频霸榜，本期快速带过）"
    类别标签: "AI跨平台调研"
    核心指标: "56K★ 连续霸榜"
    三词卖点: "AI调研·多平台·自动总结"
