# E13 customize 段 · 设计文档（换你的系统·4 步改造）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 45s
category: tutorial
segment: customize

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：
  - 步骤序号蓝 #60A5FA/#93C5FD（其一/其二/其三/其四 编号）
  - 改造动作金 #FBBF24/#FCD34D（改定位/改地址/写 handler/编用例）
  - 文件/路径青 #22D3EE/#67E8F9（base_page / main / test_product / data）
  - 数据驱动绿 #34D399/#6EE7B7（生产可用·表格替 JSON·思想一致 收尾）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（文件名 base_page/main/test_product/data/cases.json）
- 整体调性：4 phase 纯切换（禁 data-reveal，多 phase 用 GSAP timeline 顺序切换，避 phase-2/3/4 不显示）—— phase-1 其一改 base_page 定位 → phase-2 其二改 main 跳转地址加登录 → phase-3 其三照 test_product 写 handler → phase-4 其四 data 编用例表格替 JSON 收尾

## 情绪曲线 emotion_curve（4 点）
- 0.55（demo 自带商品页为开箱跑 + 真实用四步改造 抛出框架）
- 0.62（其一改 base_page 定位匹配你系统界面保持通用定位策略）
- 0.62（其二改 main 跳转地址指向你系统加登录）
- 0.68（其三照 test_product 写法为业务写更多 handler）
- 0.72（其四 data 编用例 生产可用表格替 JSON 数据驱动思想一致 收尾）

## 沉浸模式 immersion_mode
phase 切换（4 phase，纯 GSAP timeline，禁 data-reveal）：改定位 → 改地址 → 写 handler → 编用例

## 叙事模板 narrative_template
步骤展开（intro-why → step1-locate → step2-route → step3-handler → step4-cases）
- Step 1（0-Xs）：demo 自带的商品页是为了开箱跑 + 真实用的时候四步改造 总览
- Step 2：其一改 base_page 定位匹配你系统界面保持通用定位策略
- Step 3：其二改 main 跳转地址指向你系统加登录
- Step 4：其三照 test_product 写法为业务写更多 handler
- Step 5：其四 data 编用例 生产可用表格替 JSON 数据驱动思想一致 收尾

## 组件
- bg：diamond_lattice（深蓝底菱形网格，与 E13 其他段同款，跨段视觉连贯）
- fx：fx-aura 静态光晕（蓝编号+金动作+青文件+绿收尾，冷色优先 alpha≤0.22）+ fx-particle + fx-blink（禁划过类 scan/stream/beam，教程铁律）

## fonts
title: Inter
body: Noto Sans SC
data: JetBrains Mono
