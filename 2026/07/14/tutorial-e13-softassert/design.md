# E13 softassert 段 · 设计文档（软断言 vs 硬断言）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 50s
category: tutorial
segment: softassert

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：硬断言红 #FCA5A5/#EF4444（失败即停 ❌）+ 软断言绿 #34D399/#6EE7B7（失败截图+继续+汇总 ✓）+ 截图蓝 #60A5FA/#93C5FD（自动截图）+ 报告金 #FBBF24/#FCD34D（全记进报告）+ 终端青 #22D3EE（纯文本 [通过]/[失败] 输出）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码片段 assert / 终端 [通过][失败] / 编码标记）
- 整体调性：4 phase 纯切换（禁 data-reveal，多 phase 用 GSAP timeline 顺序切换）—— phase-1 软断言对比硬断言总览（双卡对比）→ phase-2 硬断言失败即停 → phase-3 软断言失败截图+继续+收集 → phase-4 纯文本输出兼容 GBK 收尾

## 情绪曲线 emotion_curve（4 点）
- 0.40（软断言对比硬断言 抛出核心对比）
- 0.58（硬断言 assert 失败立刻停 后面跑不到）
- 0.74（软断言 失败不中断+截图+收集+全跑完）
- 0.84（纯文本输出兼容 GBK 不靠表情符号 收尾）

## 沉浸模式 immersion_mode
phase 切换（4 phase，纯 GSAP timeline，禁 data-reveal）：对比总览 → 硬断言失败即停 → 软断言截图继续汇总 → 纯文本输出收尾

## 叙事模板 narrative_template
对比方法论（overview → hard-stop → soft-continue → plaintext-output）
- Step 1（0-13s）：软断言对比硬断言（双卡总览：硬断言失败即停 ❌ / 软断言失败截图+继续+汇总 ✓）
- Step 2（13-25s）：硬断言 assert 失败立刻停 后面的验证全跑不到
- Step 3（25-38s）：软断言 失败不抛异常不中断+自动截图+收集结果+多个验证都跑完
- Step 4（38-50s）：纯文本标记通过失败 兼容命令行编码不靠表情符号 收尾

## 组件
- bg：diamond_lattice（深蓝底菱形网格，与 E13 其他段同款，跨段视觉连贯）
- fx：fx-aura 静态光晕（红硬断言+绿软断言+蓝截图+金报告，冷色优先 alpha≤0.22 暖色）+ fx-particle + fx-blink（禁划过类 scan/stream/beam，教程铁律）
