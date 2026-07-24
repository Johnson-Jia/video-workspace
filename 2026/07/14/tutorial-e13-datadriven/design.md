# E13 datadriven 段 · 设计文档（数据驱动·数据代码解耦）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 55s
category: tutorial
segment: datadriven

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：
  - data 用例数据绿 #34D399/#6EE7B7（cases.json 4 条用例 3 跑 1 关）
  - 调度器 runner 蓝 #60A5FA/#93C5FD（读用例按 type 路由）
  - 基础操作字典紫 #C4B5FD/#A78BFA（BASIC 字典 text/button/app/selector）
  - 模块操作注册中心金 #FBBF24/#FCD34D（handler_registry.get）
  - 变量传递青 #22D3EE/#67E8F9（_save_as 保存 + ${变量名} 引用）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码片段 cases.json / runner / ${变量}）
- 整体调性：4 phase 纯切换（禁 data-reveal，多 phase 用 GSAP timeline 顺序切换，避 phase-2/3/4 不显示）—— phase-1 数据代码解耦总览 → phase-2 runner 按 type 路由（基础字典/模块注册中心）→ phase-3 变量传递 _save_as/${name} → phase-4 运营编步骤开发写 handler 分工收尾

## 情绪曲线 emotion_curve（4 点）
- 0.45（数据代码彻底解耦 + data cases.json 4 条用例 抛出核心）
- 0.60（runner 读用例按 type 路由 基础操作走字典）
- 0.72（模块操作走注册中心 + 变量传递 _save_as 保存花括号引用）
- 0.82（运营编步骤开发写 handler 分工清晰 收尾）

## 沉浸模式 immersion_mode
phase 切换（4 phase，纯 GSAP timeline，禁 data-reveal）：解耦总览 → runner 按 type 路由 → 变量传递 → 分工收尾

## 叙事模板 narrative_template
方法论 + 代码（decouple-overview → runner-by-type-route → var-passing → role-division）
- Step 1（0-14s）：数据与代码彻底解耦 + data/cases.json 用例（4 条 3 跑 1 关，纯粹步骤 JSON 运营编不碰代码）+ handlers/ 代码实现
- Step 2（14-28s）：调度器 runner 读用例按 type 路由——基础操作走字典（text/button/app/selector → 基类方法）/ 模块操作走注册中心（handler_registry.get）
- Step 3（28-41s）：变量传递 _save_as 保存到 ctx + 花括号变量名引用 步骤间用例间都能传
- Step 4（41-55s）：分工清晰（运营编步骤，开发写 handler）收尾

## 组件
- bg：diamond_lattice（深蓝底菱形网格，与 E13 hook/intro/arch/registry 同款，跨段视觉连贯）
- fx：fx-aura 静态光晕（绿数据+蓝调度+紫字典+金注册+青变量，冷色优先 alpha≤0.22 暖色）+ fx-particle + fx-blink（禁划过类 scan/stream/beam，教程铁律）
