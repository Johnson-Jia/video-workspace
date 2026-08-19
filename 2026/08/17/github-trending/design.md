# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风·快节奏榜单
mood: 紧凑密集·高信息密度·轻快利落

> Q1 情感内核：反直觉冲击 + 快节奏盘点——「代码平台上最火的居然是一份不写代码的清单」。观众感受：连续的"哦？还有这种事"小惊讶，五连发不停顿。

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（深蓝到深紫的暗底，接近纯黑）
  accent_cool: 蓝青色系（清单条目/框架类场景，理性信息层）
  accent_warm: 橙金琥珀（hook/数字锚点/CTA 场景，冲突与热度）
  text: 白色主 + 浅灰辅，数字用暖强调色
  contrast_principle: 深底亮刀——每个项目卡用一枚高饱和强调色做"钩子数字"，全片橙蓝双轴交替保持节奏感

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "快节奏盘点 + 反直觉冲击需要利落无装饰的标题，几何无衬线最贴紧凑专业感"
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
music_mood: 低调电子·科技衬底（clean-corporate / monochrome 系优先，快速播报节奏但高频不吵，避开 bold-energetic 电子激昂）

## 素材预判（可选）
assets_needed: []（纯 CSS 渐变+光效+数字卡，无外部素材；头像用 assets/avatars/）

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.6, 0.75, 0.85, 1.0, 0.7, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook（不写代码冲上46万星的反直觉冲突 + 单日1588，全片视觉最强画面）"
    build: "public_apis（清单主角展开：代码平台上46万人收藏一份文档）"
    reveal: "cordis + MoneyPrinterTurbo（框架的框架 / 关键词进成片出的自动化惊喜）"
    climax: "yt-dlp（18万星常青树，AI 满屏榜单上纯命令活下来的工程韧性）"
    settle: "timesfm（预测未来做成基础模型，科研沉淀）"
    summon: "CTA（五项目你会收藏哪个，中性二选一互动 + 关注）"

## 方向
orientation: portrait
orientation_source: default
