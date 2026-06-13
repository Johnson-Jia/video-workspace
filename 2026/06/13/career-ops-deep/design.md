# Career-Ops 视频设计文档

## 视觉风格
style: 暗色科技风
mood: 理性、深刻、工程感
rationale: 项目是工程化水平极高的 AI 求职系统，深蓝/深紫底色传达"深度解析"的庄重感，琥珀强调色锚定关键数据，衬线标题体呼应"架构哲学"主题

## 配色方向
color_direction:
  bg: 深空蓝紫（#080818 ~ #0c0c24）
  accent_warm: 琥珀金 #FFB800（用于关键数据 740/150+/A-G）
  accent_cool: 电青 #00D4FF（用于架构/技术概念 Prompt-as-Code/数据契约）
  accent_emerald: 翡翠 #10B981（用于"成功/推荐"信号）
  accent_red: 警示红 #FF5252（用于限制/不足）
  text: 白色主 + 浅蓝灰辅 #a0a0c0

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "衬线庄重"
    family: "Noto Serif SC"
    weight: 900
    rationale: "讲架构哲学思想需要深度感和庄重感，衬线宋体比无衬线更有思想分量"
    fallback: "'Noto Serif SC','Songti SC','SimSun',serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/理性，中低节奏，渐进展开
rationale: 3 分钟深度解析需稳定推进感，避免激烈节奏干扰信息吸收；中段（架构哲学/评估）渐强，结尾（推荐）温和收束

## 沉浸模式
immersion_mode: hidden-gem
rationale: 单项目深度解析，渐进揭示（项目→架构→功能→限制→建议），适合"深度发现"叙事

## 画布方向
orientation: portrait
orientation_source: default

## 故事板
narrative_template: deep-analysis
emotion_curve: [0.35, 0.5, 0.8, 0.6, 0.65, 0.45, 0.3, 0.5, 0.4]
beat_mapping:
  - S1 hook: 好奇（740→1 反差悬念）
  - S2 what: 认知（项目定位）
  - S3 philosophy: 敬佩（Prompt-as-Code 核心创新，全片峰值）
  - S4 scan: 兴趣（零 Token 扫描能力）
  - S5 eval: 分析（A-G 评估体系）
  - S6 data-contract: 赞赏（数据契约设计）
  - S7 limits: 诚实（边界陈述，情绪走低）
  - S8 usecase: 实用（适用场景回升）
  - S9 cta: 行动（温和收尾）

## 场景视觉意图

### S1 hook（~12s）
- 巨大数字 740 居中冲击 → 收缩动画 → 数字 1 → 引出"系统"
- 数据等宽体，琥珀金强调
- 视觉类型：data-impact

### S2 what（~21s）
- 项目名 "Career-Ops" 衬线大标题
- 双技术栈示意：Node.js（扫描器）+ Go（看板）双流汇聚
- 视觉类型：title-card

### S3 philosophy（~23s）★ 峰值场景
- Prompt-as-Code 概念可视化：Markdown 文件图标 → 流入 AI 大脑 → AI 反向写出规则（递归箭头）
- 全片最高潮，电青色为主
- 视觉类型：concept-flow

### S4 scan（~22s）
- 7 个招聘平台汇聚 → 扫描雷达动效 → 职位卡片瀑布流
- "零 Token" 徽章强调
- 视觉类型：radar-cascade

### S5 eval（~23s）
- A-G 七格仪表盘 → 逐格填充评分（1-5 分）
- 等宽体数字
- 视觉类型：dashboard-grid

### S6 data-contract（~20s）
- 两层分离示意：上层"用户层"带锁图标（永不更新）+ 下层"系统层"带刷新图标（可更新）
- 视觉类型：layer-split

### S7 limits（~22s）
- 限制清单列表，每条配警示色
- 仅欧美平台 / AI 非精确 / 依赖 Node+Chromium / 反对海投
- 视觉类型：caution-list

### S8 usecase（~19s）
- 适用人群画像（AI/ML 工程师）+ 适用✓/不适用✗ 对比
- 视觉类型：audience-compare

### S9 cta（~11s）
- 项目名 + 金句"帮你看清，而非替你决定"
- 关注引导动效（无搜索引导）
- 视觉类型：cta-finish
