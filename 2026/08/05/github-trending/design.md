# design.md — 视觉风格方向 + 故事板（2026-08-05 github-trending daily，2 AI + 3 非 AI 多元）

## 风格
style: 暗色科技风
mood: 紧凑明快，发现感（日榜快速播报 + 主推反直觉「方法论比 AI 模型还火」的认知钩子）

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑 + 深蓝紫渐变基底），40px 网格 opacity 0.04 数字纹理
  accent_cool: 霓虹青/翠绿（用于 AI 类项目场景：superpowers / uber-ADR，传递理性技术感）
  accent_warm: 金色/琥珀（用于 hook / 排名数字 / 星标 / CTA，以及 deno/tailwindcss 非 AI 基建场景做色温反转，传递价值与落地感）
  text: 白色主 + 浅灰辅（描述/正文用浅灰，排名/星标/项目名用白色或金色强对比）

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=好奇+紧凑专业利落，GitHub 日榜快速播报的标志性音色，几何简洁最契合；主推反直觉钩子靠字号与对比冲击，而非毛笔/衬里的庄严"
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
music_mood: 科技/赛博低调辅助（clean-corporate 偏向，衬底不抢旁白；github 快速播报定位，不连续两期用 neon-electric）

## 素材预判
assets_needed: []
（5 项目均用 ProjectFullCard 一屏一项目 8 层信息呈现，纯 CSS/HTML 实现，无需外部素材；avatar 已下载 assets/avatars/）

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.40, 0.60, 0.65, 0.70, 0.90, 0.45]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（S1：26 万星「方法论比模型火」反直觉钩子）"
    build: "superpowers（S2 主推：26 万星方法论 + 子代理分工展开）"
    reveal: "deno（S3：非 AI JS 运行时，Node 原作者另起炉灶）"
    climax_pre: "tailwindcss（S4：非 AI CSS 框架，原子类反而更快）"
    climax: "uber/ADR（S5：企业 AI 安全，Uber 当监工，能力高潮）"
    settle: "pdf-inspector（S6：今日 top1 涨星一句带过增量，色温转暖冷却）"
    summon: "CTA（S7：中性二选一 + 关注）"

## 方向
orientation: portrait
orientation_source: default

## 备注
- 主推 superpowers 反直觉：26 万星不是 AI 模型，是「AI 编程怎么干才靠谱」的方法论 + 技能框架（人教 AI 干活）。hook 用认知反差（方法论比模型火）+ 26 万星单数字锚定，避纯数字堆叠。
- daily 回归多元：2 AI + 3 非 AI。deno/tailwindcss 作为非 AI 基建置于 reveal/climax_pre，暖色处理，破 AI 单一题材（P-topic-ai declining + ai-wind 专项同日承接 AI 深度）。
- pdf-inspector 近 2 天选过但今日 top1 涨星例外，置于 settle 一句带过增量不展开（gate project_no_consecutive_repeat 例外放行）。
- 色温叙事：AI 类冷色（青/翠绿）→ 非 AI 基建暖色（琥珀）反转 → CTA 金色收束，制造段落张力。
- immersion_mode=hyper-pace（AI/工具盘点，快速剪辑 + 密集粒子 + 霓虹冷色），但非 AI 场景色温转暖避免单调。
