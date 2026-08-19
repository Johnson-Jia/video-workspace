# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 紧凑利落

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深蓝/深紫暗调（接近纯黑，科技底色）
  accent_warm: 价值橙/金（用于 hook/星标/「免费平替」利益点/CTA，传递省钱的获得感）
  accent_cool: 工具蓝（用于项目功能/技术标签/数据，传递理性与工具感）
  text: 白色主 + 浅灰辅（信息层级：星标数字 > 项目名 > 用途利益 > 描述）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核为利落/掌控/获得感和创意工具气质，平替盘点需要紧凑专业的标题气质，几何无衬线体传递工具的干脆"
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
music_mood: 科技/低调轻快（衬底不抢人声，clean-corporate/warm-editorial 系，避开电子激昂）

## 素材预判（可选）
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.55, 0.7, 0.85, 0.75, 0.6, 0.45]
  immersion_mode: "fun-tool"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（剪视频控电脑都免费的反直觉+二十万星数字锚）"
    build: "OpenCut（剪辑平替，建立『付费场景→免费开源』对比）"
    reveal: "rustdesk（远控平替，自托管连数据都自己管）"
    climax: "spec-kit（GitHub 官方出手+今日单日 1147，官方背书高潮）"
    settle: "ego-lite（AI 用你的登录态替你跑网页，沉淀到开发者效率）"
    summon: "CTA（四个工具中性二选一互动 + 关注）"

## 方向
orientation: portrait
orientation_source: default
