# Design — 6/30 GitHub Trending（竖屏 / 暗色科技风）

style: 暗色科技风，深蓝/深紫渐变基底，强调色橙金（#FF8C32 橙 + #FFD23F 金）+ 安全主题用青绿（#00E5A0）。双光晕冷暖对比。无衬线粗体，数字与项目名突出。竖屏 1080×1920，安全区 padding 180/90/220/90。

mood: 理性克制中有危机感与实用感交织。前 3 秒钩子制造"用户名扒全网"的紧迫好奇，中段逐个项目平稳介绍（扒信息→挖漏洞→防偷看的对称叙事），结尾温和互动。情绪靠数字和反直觉撑张力，不爆裂。

color_direction: 基底深蓝 #0A1628 → 深紫 #1A0F2E 渐变；强调色橙 #FF8C32（涨星数字）+ 金 #FFD23F（项目名/星标）；辅助青 #4DA8DA（科技线条）+ 安全青绿 #00E5A0（安全/加密项目）。文字白 #F5F5F5 主文 + 灰 #8B9DAF 辅文。各场景按项目类型微调：council=紫蓝、VulnClaw=红橙（攻击）、tolaria=暖金、VeraCrypt=青绿（防御）、maigret=橙（侦察）。

orientation: portrait

storyboard:
- narrative_template: contrast-arc（"扒与防"对称叙事：攻击类→防御类对比）
- immersion_mode: versus（对比/VS 主题，分屏对比 + 脉冲能量 + 硬朗色 #FF3B30）
- emotion_curve: [0.85, 0.6, 0.7, 0.55, 0.65, 0.5]
- 场景规划（6 个场景）：
  1. hook（3-4s）：纯钩子"6月30日 GitHub 冲上来几个新项目，有个工具能用一个用户名扒出 3000 多个站点的公开信息"。数字锚点 3000+，反直觉"用户名扒全网"，利益"公开信息"
  2. council-of-high-intelligence（6-7s）：AI 决策，反直觉"让亚里士多德费曼替你拿主意"，数字 18 位人物。A 档"一条命令 /council 即可"
  3. VulnClaw（6-7s）：AI 渗透，动作"一句话挖漏洞全流程"，危机感。B 档"给安全从业者，命令行门槛"
  4. tolaria（5-6s）：markdown 知识库桌面应用，实用"笔记秒变知识库"。A 档"桌面 GUI 下载即用"
  5. VeraCrypt（5-6s）：磁盘加密，实用"U盘硬盘上锁防偷看"，与 maigret 形成对称。A 档"老牌开源，桌面 GUI"
  6. maigret（6-7s）：OSINT 用户名搜索，呼应 hook"3000+站点"，反直觉"一个名字扒全网"。B 档"命令行 pip 安装"。CTA"这几个你最想试哪个"

font_palette: 无衬线粗体（Noto Sans SC / Inter），数字用 JetBrains Mono 等宽体。

## 钩子设计（hook，前 5 秒纯钩子不报名）
- 核心句（≤12字）："一个名字扒出 3000 站"（反直觉"扒"+ 数字"3000站"）
- 利益补充："6月30日 GitHub 冲上来几个新项目"（数字"几个"+ 动作"冲上"）

## 安全区与布局
- 竖屏 1080×1920，安全区 padding 180/90/220/90（top/right/bottom/left）
- 内容 absolute inset [180, 1700] 不溢出，居中聚拢
- 字号层级：标题 92px / 项目名 60px / 数据 48px / 描述 32px / 标签 24px（层级 ≥2x）
- ProjectFullCard 项目名 owner+repo 完整，owner 32px + repo 60px，word-break 禁 nowrap

## 技术栈
- HTML + CSS + GSAP（单 timeline，__timelines 独立注册）
- 三层结构 layer-bg/fx/content（bg 层强制 components/bg/ 选 1 组件）
- bg 层：dark_cipher 或 hex_grid 网格 + 渐变光晕（安全主题用密码/网格质感）
- fx 层：≥2 种特效（扫描线 + 脉冲环 / 粒子流）
- 渐变文字用 background-image 非 background 简写
- text-shadow blur 普通≤12px / 大字≤16px
- 卡片 bg rgba alpha ≥ 0.6（深色不透明底挡 fx 光晕），字深色描边
- 渐变禁纯白端点（手机 OLED 过曝，director_gate 查），glow ≤ 30
