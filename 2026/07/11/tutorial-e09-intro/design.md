# E09 intro 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 30s
category: tutorial
segment: intro

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感）
- 强调色：冷蓝 #60A5FA/#93C5FD（个体脑/团队仓库流向）+ 暖金 #FBBF24/#FCD34D（沉淀三路强调）+ 翠绿 #34D399/#6EE7B7（自我改进）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（标签）
- 整体调性：沉稳科技 + 转折明朗（个体→组织）

## 情绪曲线 emotion_curve（4 点，对应 0% / 30% / 60% / 100%）
- 0.40（点题「沉淀复用」）
- 0.55（反差「前五集能力长在个人」）
- 0.75（转折「阶段六变团队资产」）
- 0.65（预告三路 + 学习目标）

## 沉浸模式 immersion_mode
data_reveal：个体→组织流向 + 沉淀三路横排 + 学习目标三栏

## 叙事模板 narrative_template
方法论预告（topic → contrast → transition → learning goals）
- Step 1（0-6s）：点题「沉淀复用」
- Step 2（6-13s）：反差——前五集能力长在个人身上
- Step 3（13-21s）：转折——阶段六变团队资产 + 沉淀三路预告
- Step 4（21-30s）：学习目标三栏

## 场景规划（visual_phases）

### Phase 1（0-6s）：标题区
- 视觉：标题「沉淀复用 · 个体→组织」+ 标签「E09 · 方法论」
- 大字渐变（暖金同色系亮端）+ text-shadow 深蓝 rgba(30,41,59,0.32)

### Phase 2（6-13s）：个体→组织流向
- 视觉：左侧「个人脑」图标（单人头像）→ 右侧「团队仓库」图标（多人/数据库）
- 中间箭头流向，标注「人走经验走 → 团队默认能力」
- data-reveal stagger 左滑入

### Phase 3（13-21s）：沉淀三路预告横排
- 视觉：三段卡片横排「Skill 复用 / 知识沉淀 / 自我改进」
- 每卡图标 + 一句话（高频操作/规范避坑/边用边学）
- data-reveal 底部上滑

### Phase 4（21-30s）：学习目标三栏
- 视觉：三栏胶囊「七种 Skill 范式怎么选 / 规范怎么资产化 / AI 怎么自我改进」
- 底部「个体经验 → 组织资产」收尾
- data-reveal stagger

## 布局规则（tutorial.md）
- 单 .phase phase-1 tut-scene，多 tut-region data-reveal stagger
- center→space-between（撑满 1920×1080）
- 标题 flex-start 左对齐
- padding-top ≥ 60
- 卡片 flex:1

## 配色规范
- 渐变文字：同色系亮端（暖金 #FBBF24 → #FCD34D / 蓝 #60A5FA → #93C5FD / 绿 #34D399 → #6EE7B7），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32）
- fx 冷色优先（蓝/紫/绿），alpha ≤ 0.22

## bg 组件
dark_cipher（深蓝底 + 同色系暗纹）— 保留 `<!-- bg-component: dark_cipher -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
