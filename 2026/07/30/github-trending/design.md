# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技工具台
mood: 利落紧凑带好奇感
rationale: 本期 5 个「知识/资源形态转换提效」工具（书变技能/省内存终端/技能框架/语音AI/IT资产），调性是「让死资源活起来」的实用科技感——暗色底 + 暖冷双强调色，呼应当下 GitHub 圈「工具下沉、效率优先」的情绪

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变底）
  accent_cool: 霓虹蓝青系（用于 build/reveal 场景，技能/终端/语音的理性面）
  accent_warm: 橙金系（用于 hook/climax/CTA 场景，知识激活的暖冲击）
  text: 白色主 + 浅灰辅
  shadow_note: 文字 text-shadow 极淡 drop（rgba(30,41,59,0.08)），禁发光；渐变文字同色系高饱和，禁白色端点

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核是「利落实用的工具感」，几何无衬线粗体最匹配 GitHub 工具盘点的科技理性，hook 大字清晰锐利"
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
music_mood: 低调科技衬底（clean-corporate / monochrome 系，衬底不抢旁白，避开 bold-energetic 激昂电子）

## 素材预判
assets_needed: []
- 5 项目均用 ProjectFullCard 一屏一项目（主项目独占，其余两两组合）
- 数据层用等宽体展示「+1428 ★」「26.3K★」等星标增量
- avatar 已预下载到 assets/avatars/，中部引用

## 故事板
storyboard:
  narrative_template: "story-time"
  narrative_rationale: "避近 4 期已用的 contrast-arc/mystery-box/hyper-pace/showdown；本期主线「知识形态转换」适合 story-time 弧线——从「书只能读」的平静认知开场，转折到「压成技能」的惊喜，递进展示 5 个转换/提效工具，收尾共鸣"
  emotion_curve: [0.8, 0.5, 0.7, 1.0, 0.6, 0.5]
  immersion_mode: "fun-tool"
  immersion_rationale: "5 个有趣工具盘点，fun-tool 的弹跳节奏 + 亮色点缀适合轻松实用调性，视觉底仍暗色科技风"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "scene0 hook（技术书不用读）"
    build: "scene1 book-to-skill 主项目展开"
    reveal: "scene2 superpowers + jcode（技能框架 + 省内存终端）"
    climax: "scene3 VibeVoice + snipe-it（语音 AI + IT 资产）"
    settle: "scene3 尾句过渡"
    summon: "scene4 CTA 结尾互动"

## 场景规划（5 场景，标准模式，一屏一项目/组合）
scenes:
  - scene0: hook（全片视觉最强，大字「书不用读」反直觉冲击）
  - scene1: book-to-skill 独占（主项目，+1428 今日榜首，PDF→技能的形态转换）
  - scene2: superpowers + jcode（技能框架方法论 + 最省内存终端）
  - scene3: VibeVoice + snipe-it（大厂开源语音 AI + 开源 IT 资产管理）
  - scene4: CTA（中性二选一互动 + 关注引导）

## 方向
orientation: portrait
orientation_source: default
