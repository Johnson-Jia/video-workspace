# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技·自家机房        # 暗色基底上的暖金"归属感"层，本地优先的从容笃定
mood: 从容笃定、带一点回家的暖

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（近黑深蓝基底，40px 网格纹理低透明度衬底）
  accent_cool: 青蓝（工具/技术类项目场景的理性层，讲能力与参数）
  accent_warm: 金琥珀（hook/主推 immich/CTA 的价值层，讲星标与"拿回自己手里"）
  text: 白色主 + 浅灰辅（描述用浅灰，排名/星标用暖强调色）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=从容/掌控——把数据拿回自己手里的笃定不靠呐喊（排除毛笔）也不冷峻（排除等宽），几何简洁的利落感最贴『自己管好自己的机器』"
    fallback: "'Inter','Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 低调清洁企业感（clean-corporate 系，衬底不抢人声；科技感靠画面与音色，不用激昂电子）

## 素材预判（可选）
assets_needed: []       # 全部走组件与 CSS 渐变，项目头像已在 assets/avatars/

## 故事板
storyboard:
  narrative_template: "contrast-arc"      # 云端会员/账号体系 vs 本地自己管 的对照弧
  emotion_curve: [0.6, 0.5, 0.7, 0.9, 0.6, 0.45]
  immersion_mode: "hidden-gem"            # 小众宝藏/渐进揭示/温暖光效——五个常青与新生工具的"发现感"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"                          # 11万人把照片搬回家（反直觉+数字）
    build: "openlogi"                     # 免账号调鼠标（冲突共鸣）
    reveal: "immich, strix"               # 主角揭示 + 安全体检揭示
    climax: "motrix"                      # 7年常青 5.3万星，全片高点
    settle: "llmfit"                      # 先测后下，连接观众实用场景
    summon: "cta"

## 方向
orientation: portrait   # portrait | landscape
orientation_source: default  # default | user_explicit | category_hint（github 分类无 orientation_hint，默认竖屏）
