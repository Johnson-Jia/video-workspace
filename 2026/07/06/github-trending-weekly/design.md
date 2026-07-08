# design.md — 视觉风格方向 + 故事板（GitHub 第28周周榜）

## 风格
style: 暗色科技周榜        # 周榜汇总调性：信息密集但层次清晰
mood: 紧凑科技·节奏感强      # 周榜 13 项目速览，hyper-pace 快节奏

## 配色方向（描述性，不指定具体色值；领域色仅视觉，旁白禁说颜色词）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫底渐变）
  accent_warm: 橙金/琥珀（用于 hook 周次数字、CTA 收尾、排名编号）
  accent_cool: 冷青蓝（用于 AI Agent 场景强调、数据指标）
  text: 白色主 + 浅灰辅
  领域色环（仅视觉·卡片色环/边框/标签）:
    AI_Agent: "冷青蓝 #00D4FF"
    AI记忆: "紫 #7B2FBE"
    视频图像: "品红 #FF3B7B"
    AI入口: "青绿 #00E5A0"
    安全隐私: "琥珀 #FFB800"

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"            # Q1 情感内核=紧凑专业（周榜信息密集，需利落）
    family: "Inter"
    weight: 900
    rationale: "周榜 13 项目速览需紧凑专业的标题气质，几何简洁体支撑信息密度"
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
music_mood: 科技/赛博（紧凑电子，匹配 hyper-pace 周榜节奏）

## 素材预判
assets_needed:
  - 21 个 owner 头像（已下载 assets/avatars/，卡片 avatar 锚点）
  - 周次时间窗视觉（06.29-07.06 区间条）
  - 5 领域色环卡片组件（每分类一组多项目并列）

## 故事板
storyboard:
  narrative_template: "hyper-pace"      # 周榜 13 项目速览，快速密集爆发呼吸
  emotion_curve: [0.9, 0.7, 0.75, 0.8, 0.7, 0.6, 0.5]  # hook 高能→分类速览维持→CTA 收束
  immersion_mode: "hyper-pace"          # 信息密集快节奏
  humor_style: "narration-only"         # 周榜信息密度高，幽默仅旁白调剂不占画面
  character_presence: false             # 周榜速览不放码力角色，专注信息呈现
  beat_mapping:
    grab: "S1 hook（周次+涨幅数字）"
    build: "S2 AI Agent 工具组"
    reveal: "S3 AI 记忆组 / S4 视频图像组"
    climax: "S5 AI 入口组（多Agent网关高潮）"
    settle: "S6 安全隐私组（节奏放缓）"
    summon: "S7 CTA 周次收尾"

## 7 场景规划
scenes:
  - id: S1_hook
    type: hook
    duration: 6s
    focus: "第28周周榜 + 一周涨一万多星数字冲击"
    领域色: 橙金+深蓝
  - id: S2_ai_agent
    type: features
    duration: 9s
    focus: "AI Agent 工具组（strix/herdr/orca/codex-plugin-cc）"
    领域色: 冷青蓝 #00D4FF
    备注: "strix/herdr/codex-plugin-cc 一句带过，orca 略展开"
  - id: S3_ai_memory
    type: features
    duration: 8s
    focus: "AI 记忆/代码理解组（codebase-memory-mcp/cognee）"
    领域色: 紫 #7B2FBE
  - id: S4_video
    type: features
    duration: 9s
    focus: "视频图像组（OpenMontage/video-use/lingbot-map）"
    领域色: 品红 #FF3B7B
  - id: S5_ai_entry
    type: features
    duration: 9s
    focus: "AI 入口/网页组（OmniRoute/page-agent/ai-website-cloner）"
    领域色: 青绿 #00E5A0
  - id: S6_privacy
    type: features
    duration: 8s
    focus: "安全隐私/效率组（simplex-chat/meetily）"
    领域色: 琥珀 #FFB800
    备注: "meetily 一句带过"
  - id: S7_cta
    type: cta
    duration: 5s
    focus: "第28周周榜收尾 + 中性互动"
    领域色: 综合渐变

## 方向
orientation: portrait
orientation_source: default   # github 无 orientation_hint，默认竖屏
