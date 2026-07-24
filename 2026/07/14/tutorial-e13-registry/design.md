# E13 registry 段 · 设计文档（注册中心模式）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 55s
category: tutorial
segment: registry

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：注册金 #FBBF24/#FCD34D（@register 装饰器 / 全局表登记）+ 调度蓝 #60A5FA/#93C5FD（调度器按 type 取 handler）+ 延迟解析紫 #C4B5FD/#A78BFA（类引用延迟解析关键细节）+ 自动发现绿 #34D399/#6EE7B7（自动发现零改代码好处）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码片段 @register / registry.get / type）
- 整体调性：4 phase 纯切换（禁 data-reveal，多 phase 用 GSAP timeline 顺序切换）—— phase-1 灵魂+@register 代码 → phase-2 调度器按 type 取 → phase-3 延迟解析关键细节 → phase-4 自动发现零改代码收尾

## 情绪曲线 emotion_curve（4 点）
- 0.40（注册中心是灵魂 + @register 装饰器代码 抛出核心）
- 0.60（调度器按 type 自动取 全局表登记）
- 0.72（延迟解析关键细节——类引用放到创建实例时再解析）
- 0.82（自动发现零改代码收尾 企业级核心模式）

## 沉浸模式 immersion_mode
phase 切换（4 phase，纯 GSAP timeline，禁 data-reveal）：灵魂+@register → 调度器按 type 取 → 延迟解析关键细节 → 自动发现零改代码

## 叙事模板 narrative_template
方法论 + 代码（intro-soul → dispatcher-by-type → deferred-resolve → auto-discover）
- Step 1（0-14s）：注册中心是灵魂 + @register 装饰器代码片段（写装饰器把方法登记进全局表）
- Step 2（14-28s）：调度器按类型自动取（type → registry.get 全局表）
- Step 3（28-41s）：关键细节 类引用延迟解析（装饰器执行时类还没定义完→拿到空，放到创建实例时再解析）
- Step 4（41-55s）：好处 自动发现零改调度器代码 收尾（企业级测试框架核心模式）

## 组件
- bg：diamond_lattice（深蓝底菱形网格，与 E12 promptasset 同款，跨段视觉连贯）
- fx：fx-aura 静态光晕（金注册+蓝调度+紫延迟解析+绿自动发现，冷色优先 alpha≤0.22 暖色）+ fx-particle + fx-blink（禁划过类 scan/stream/beam，教程铁律）
