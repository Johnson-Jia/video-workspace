# design.md — 视觉风格方向 + 故事板

> 选题方向：今日 GitHub 换到开发者基石层（运行时/网络/IaC/框架），AI 只占两个。情感内核 = 理性/精准/极客 + 一点点「换层」的转折惊喜。

## 风格
style: 极客暗夜终端        # 终端黑底 + 代码绿/电光蓝 + 暖金强调，呼应「开发者基石」主题
mood: 沉稳利落带转折       # 开头沉稳报数据，中段揭示反直觉，结尾回到理性总结

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑的深蓝灰，终端 bg 感）
  accent_cool: 电光蓝/代码绿（用于运行时/框架/网络/基础设施场景，理性极客）
  accent_warm: 琥珀金/橙（用于 AI 编程配置场景 + 强调涨星数字，破冷调单一）
  text: 白色主 + 浅灰辅 + 等宽亮色数据

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "理性/精准/极客"          # Q1 情感内核：开发者基石主题，等宽体最贴合
    family: "JetBrains Mono"
    weight: 800
    rationale: "开发者基石/底层主题，等宽体（JetBrains Mono）天然极客感，比 Inter 更贴合'底层/代码/终端'调性"
    fallback: "'JetBrains Mono','Consolas','PingFang SC','Microsoft YaHei',monospace"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 低调科技/极客衬底    # 呼应 github 分类 bgm_style：clean-corporate/warm-editorial 首选，禁 bold-energetic
# 选曲关键词：clean-corporate / monochrome / 温暖编辑型，避开 neon-electric（连续两期科技高频）+ bold-energetic

## 素材预判（可选）
assets_needed: []
# 纯数据盘点，无图表/图标需求；用 CSS 渐变 + 数据大字 + ProjectFullCard 组件表达

## 故事板（6 拍）
storyboard:
  narrative_template: "contrast-arc"   # 默认模板（github 分类默认 contrast-arc）：平稳报数据 → 对比反直觉 → 震撼数字 → 高潮总结
  emotion_curve: [0.4, 0.5, 0.7, 0.9, 0.6, 0.4]  # 沉稳起步 → 中段揭示 → mattpocock 16万星高潮 → 沉淀 CTA
  immersion_mode: "hyper-pace"         # github 分类 AI 类项目 < 50%（2/6），但盘点类仍用 hyper-pace 快剪密集信息
  humor_style: "narration-only"        # 旁白偶有开发者文化梗（如'私人配置当宝贝藏'），视觉保持稳重不搞笑
  character_presence: true             # github 分类默认启用码力角色，高潮段（mattpocock skills 揭示）出场
  beat_mapping:
    grab: "hook"                       # 「今天换到开发者基石层，AI 只占两个」转折钩子
    build: "mattpocock/skills"         # 涨星榜首 +16 万星揭示（build 阶段已有冲击力）
    reveal: "DesktopCommanderMCP, bun" # AI 操作电脑 + JS 运行时基石，反直觉揭示
    climax: "tailscale, next.js"       # 网络互联 + 9 年老牌框架，数字与故事高潮
    settle: "terraform"                # 11 年 IaC 鼻祖，沉淀到「开发者世界的钢筋水泥」
    summon: "CTA"                      # 「今天这层你日常在用几个」中性互动

## 方向
orientation: portrait        # 任务指定竖屏 portrait（标准模式 4-5 场景 20-45s）
orientation_source: user_explicit   # 任务 prompt 明确「画布：竖屏 portrait」
