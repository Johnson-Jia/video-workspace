# Design Analysis — 2026-06-12 GitHub Trending

## 基本信息
- date: "2026-06-12"
- content_type: "GitHub Trending 项目盘点"
- orientation: "portrait"
- orientation_source: "github 分类无 orientation_hint，默认竖屏"

## 沉浸模式
- immersion_mode: "hyper-pace"
- 判定依据: 6 个入选项目中 4 个是 AI Agent 技能（agent-skills / superpowers / pm-skills / SkillSpector），AI/Agent 项目占比 >50%，匹配 hyper-pace 视觉风格
- 视觉特征: 快速剪辑 + 密集粒子 + 霓虹 #00D4FF + 高对比度文字 + 脉冲能量

## 风格
- style: "暗色科技风"
- 基底: 深蓝/深紫渐变（#0A0E27 → #1A0B2E）
- 强调色: 暖冷双光晕——#FF8C32（橙）+ #4DA8DA（蓝）
- 字体: 无衬线粗体，大字号高对比
- 光效: 霓虹描边 + 粒子飘浮 + 脉冲光圈

## 情绪基调
- mood: "紧迫感 + 顿悟交替"
- AI Agent 技能爆发带来紧迫感（"别人都在装技能"），每个项目的反直觉角度制造顿悟时刻

## 色彩方向
- color_direction: "冷色为主（深蓝 #0A0E27 / 深紫 #1A0B2E 基底），强调色暖冷双光晕（#FF8C32 橙 + #4DA8DA 蓝），数据高亮用 #FFD700 金色"
- 粒子色: #00D4FF 霓虹蓝（hyper-pace 标志色）
- 文字渐变: 从 #4DA8DA 到 #00D4FF 的冷色渐变用于标题，数据用 #FFD700 纯色

## 情绪曲线
- emotion_curve: ["shock", "intrigue", "awe", "recognition", "tension", "resolve"]
- 说明:
  1. shock — hook 阶段：苹果跨界做容器，反直觉冲击
  2. intrigue — agent-skills / superpowers：AI 不靠变聪明靠装技能，技能框架 22 万星
  3. awe — pm-skills：PM 工作流被 100+ 技能拆解，能力全面技能化
  4. recognition — SkillSpector：AI 技能需要杀毒，安全是必然命题
  5. tension — openmed：医疗数据隐私的紧迫性
  6. resolve — CTA 收束：关注获取每日热门

## 场景分镜 (storyboard)

### 场景 1: Hook（3-5s）
- visual_type: "hook-shock"
- 情感内核: 反直觉冲击——苹果居然做容器工具
- 视觉手段: 全屏暗底 + 霓虹脉冲 + 大字冲击 + 粒子爆发
- 数据/文字: 钩子文案大字呈现，无项目名
- 转场: 快速粒子消散

### 场景 2: apple/container（5-7s）
- visual_type: "project-card"
- 情感内核: 跨界颠覆——容器本是 Docker 的活
- 视觉手段: 深蓝底 + Apple 风格极简卡片 + 容器图标动效 + 冷蓝强调
- 数据/文字: 32.3K Star / +2419 / Swift / "轻量虚拟机容器"
- 转场: 向左滑出

### 场景 3: agent-skills + superpowers（6-8s）
- visual_type: "project-card"
- 情感内核: 技能生态爆发——AI 在"装技能"不是"变聪明"
- 视觉手段: 深紫底 + 双卡片并排（或快速切换）+ 技能图标网格 + 霓虹 #00D4FF 粒子密集
- 数据/文字: agent-skills 54.6K / +3275（今日最高）+ superpowers 224.8K（史上前几）
- 转场: 技能图标消散为粒子

### 场景 4: pm-skills（5-7s）
- visual_type: "project-card"
- 情感内核: 能力技能化——连 PM 工作流都被拆成了 100+ 可调用技能
- 视觉手段: 深蓝底 + 技能市场网格动效 + 暖橙 #FF8C32 强调色 + 技能标签飞入
- 数据/文字: 16.2K Star / +1944 / "100+ Agent 技能"
- 转场: 标签收缩消失

### 场景 5: SkillSpector + openmed（6-8s）
- visual_type: "project-card"
- 情感内核: 安全 + 隐私——AI 技能需要杀毒 + 医疗 AI 坚持本地化
- 视觉手段: 深紫底 + 安全盾牌动效 + 隐私锁图标 + 冷蓝强调 + 脉冲警报
- 数据/文字: SkillSpector 2.6K / +308 + openmed 2.7K / +427
- 转场: 盾牌碎裂为粒子

### 场景 6: CTA（3-4s）
- visual_type: "cta"
- 情感内核: 收束号召——关注获取每日热门
- 视觉手段: 暗底 + 频道名大字 + 粒子收束 + 渐变光晕
- 数据/文字: "关注 GitHub 星探，每天更新"
- 转场: 淡出

## 视觉设计备注
- 所有场景使用 hyper-pace 风格：快速剪辑节奏，粒子密度高，霓虹光效贯穿
- 项目卡片使用大字号项目名 + 数据行 + 一句话描述的三层结构
- 场景间转场保持快速（0.3-0.5s），用粒子/光效过渡而非简单淡入淡出
- 场景 3 和场景 5 各包含 2 个项目，采用快速切换或双卡片布局，保持节奏紧凑
