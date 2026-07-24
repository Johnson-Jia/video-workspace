# E13 hook 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 30s
category: tutorial
segment: hook
episode: E13（合集收官）

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，自动化测试/确定性执行主题）
- 强调色：暖红 #EF4444/#F87171（虚假通过痛点 + 红叉警示）+ 冷蓝 #60A5FA/#93C5FD（ai-test-frame 框架 + 数据驱动确定性）+ 翠绿 #34D399/#6EE7B7（根治虚假通过 + 通过2失败0）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（测试报告/终端/ai-test-frame）
- 整体调性：痛点警示 + 确定性执行根治虚假通过

## 情绪曲线 emotion_curve（5 点，对应 0% / 25% / 50% / 75% / 100%）
- 0.42（开场：AI 写测试最大的坑，痛点抛出）
- 0.78（虚假通过揭示：AI 幻觉看着跑通实际没验证 + 绿灯上线翻车）
- 0.65（ai-test-frame 引入：最小可运行框架，开箱就跑）
- 0.82（核心思路揭示：AI 只生成，运行期零 AI 确定性数据驱动）
- 0.55（收尾定调：根治虚假通过）

## 沉浸模式 immersion_mode
phase 切换：大字「虚假通过」红叉 + 绿灯上线翻车 / ai-test-frame 开箱跑 + AI 只生成运行期零 AI + 根治虚假通过

## 叙事模板 narrative_template
虚假通过警示开篇（fake-pass → green-light-crash → framework → deterministic → rootfix）
- Step 1（0-13s）：大字「虚假通过」红叉 + AI 幻觉看着跑通实际没验证 + 绿灯上线翻车
- Step 2（13-30s）：ai-test-frame 开箱跑 + 核心思路（AI 只生成测试代码，运行期全是确定性数据驱动，零 AI）+ 根治虚假通过

## 场景规划（visual_phases）—— phase 切换（单场景类 hook-scene，phase-1/phase-2 依次显示，绕过 s6_assemble 多 phase 重叠 bug）

### Phase 1（0-13s）：虚假通过痛点
- 大字「虚假通过」红叉（核心警示）
- AI 幻觉让测试看着跑通 + 实际没验证到点子上
- 你以为是绿灯 + 上线就翻车

### Phase 2（13-30s）：ai-test-frame 开箱跑 + 根治
- ai-test-frame 胶囊（最小可运行 AI 自动化测试框架 + 开箱就跑）
- 核心思路：AI 只负责生成测试代码 + 运行期全是确定性数据驱动 + 零 AI
- 根治虚假通过 收尾

## 布局规则（tutorial.md）
- 单场景类 hook-scene，phase-1/phase-2 切换（一次显示一个 phase）
- center→space-between（撑满 1920×1080）
- .hook-scene flex-start（内容从顶排列，padding-top 188）
- .region flex-shrink:0（不压缩）

## 配色规范
- 渐变文字：同色系亮端（暖红 #EF4444 → #F87171 / 冷蓝 #60A5FA → #93C5FD / 翠绿 #34D399 → #6EE7B7），禁白端点 / 禁暗端（#B8842B/#1E6FB8/#DC2626/#1e3a8a）
- text-shadow：深蓝 rgba(30,41,59,0.32)（非黑，alpha ≤ 0.32，禁发光 0 0 Xpx）
- fx 冷色优先（蓝/紫/绿），暖色（红/橙）alpha ≤ 0.22

## bg 组件
gradient_mesh（渐变网格 + 流动光斑 + 柔和氛围，匹配「自动化测试/确定性执行」主题，深蓝科技底）— 保留 `<!-- bg-component: gradient_mesh -->`

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性（黑屏事故）
- 禁 opacity 入场（GSAP 单 timeline + phase 切换）
- 禁暗端渐变（#B8842B/#1E6FB8/#DC2626/#1e3a8a 等）
- 禁创作指令泄露（不录屏/真操作/信息节制）
- 禁「一定」（「不一定」→「未必」）
- 禁商业言论（售卖/卖/付费）
- 渐变文字禁胶囊 grad-* clip:text（小标签用纯场景色 + border-box）
