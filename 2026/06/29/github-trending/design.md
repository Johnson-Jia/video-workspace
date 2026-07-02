# Design — 6/29 GitHub Trending（竖屏 / 暗色科技风）

style: 暗色科技风，深蓝/深紫渐变基底，强调色橙金（#FF8C32 橙 + #FFD23F 金），双光晕冷暖对比。无衬线粗体，数字与项目名突出。竖屏 1080×1920，安全区 padding 180/90/220/90。

mood: 理性克制中有惊喜感。前 3 秒钩子制造"AI 工具扎堆上榜"的紧迫感与好奇，中段逐个项目平稳介绍（理性可信），结尾回归温和互动（你想用哪个）。情绪不爆裂，靠数字和反直觉撑张力。

color_direction: 基底深蓝 #0A1628 → 深紫 #1A0F2E 渐变；强调色橙 #FF8C32（涨星数字）+ 金 #FFD23F（项目名/星标）；辅助青 #4DA8DA（科技线条/边框）；文字白 #F5F5F5 主文 + 灰 #8B9DAF 辅文。各场景按项目类型微调：MCP代码=青蓝、端侧语音=暖橙、AI交易=金、AI视频=紫红、安全=红橙。

orientation: portrait

storyboard:
- narrative_template: hyper-pace（AI 工具密集盘点，快速剪辑 + 密集粒子 + 霓虹色）
- immersion_mode: hyper-pace（AI 项目占比高，符合 github.md immersion_mapping）
- emotion_curve: [0.85, 0.55, 0.6, 0.65, 0.7, 0.5]
- 场景规划（6 个场景）：
  1. hook（3-4s）：纯钩子"单日涨两千星的 AI 工具，一半能帮你省掉重复活"。数字锚点 +2162，动作词"涨"，利益翻译"省掉重复活"
  2. codebase-memory-mcp（6-7s）：MCP 代码智能，强调"让 AI 看懂整个代码库"，数字 158 语言/毫秒级。C 档措辞"给做工程的开发者"
  3. FluidVoice（5-6s）：macOS 离线听写，端侧隐私"不联网数据不外传"，A 档"桌面即开即用"
  4. Vibe-Trading（5-6s）：个人交易 agent，"AI 帮你看盘做决策"，B 档"研究型项目需配置"。泛化"国内高校团队"不提校名
  5. video-use（6-7s）：用代码剪视频，反直觉"写代码而非拖时间线"，A/B 档"browser-use 出品门槛中等"
  6. strix（5-6s）：AI 找漏洞修 bug，危机感"你的应用可能正在被攻击"，A/B 档"可 Docker 部署"。CTA 收尾"这几个你会试哪个"

font_palette: 无衬线粗体（Noto Sans SC / Inter），数字用 JetBrains Mono 等宽体。

## 钩子设计（hook，前 5 秒纯钩子不报名）
- 核心句（≤12字）："单日涨两千星的 AI 工具"（动作词"涨" + 数字"两千星"）
- 利益补充："一半能帮你省掉重复活"（观众能带入的利益）

## 安全区与布局
- 竖屏 1080×1920，安全区 padding 180/90/220/90（top/right/bottom/left）
- 内容 absolute inset [180, 1700] 不溢出，居中聚拢
- 字号层级：标题 92px / 项目名 60px / 数据 48px / 描述 32px / 标签 24px（层级 ≥2x）
- ProjectFullCard 项目名 owner+repo 完整，owner 32px + repo 60px，word-break 禁 nowrap

## 技术栈
- HTML + CSS + GSAP（单 timeline，__timelines 独立注册）
- 三层结构 layer-bg/fx/content（bg 层强制 components/bg/ 选 1 组件）
- bg 层：grid 网格 + 渐变光晕（科技感）
- fx 层：≥2 种特效（粒子流 + 脉冲环 / 扫描线）
- 渐变文字用 background-image 非 background 简写
- text-shadow blur 普通≤12px / 大字≤16px
