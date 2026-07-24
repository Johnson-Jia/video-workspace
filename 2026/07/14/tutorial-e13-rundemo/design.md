# E13 rundemo 段 · 设计文档（实跑演示·终端）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 55s
category: tutorial
segment: rundemo

## 视觉风格
- 主色：终端黑底 #0A0E14（深于常规 #0F172A，模拟真实终端）
- 强调色：命令蓝 #60A5FA/#93C5FD（cd/install/playwright 命令行）+ 成功绿 #34D399/#6EE7B7（通过 2）+ 跳过灰 #94A3B8/#CBD5E1（第四条关闭跳过）+ 失败红 #FCA5A5/#EF4444（失败 0 零个）+ 汇总金 #FBBF24/#FCD34D（断言汇总）+ 确定性青 #22D3EE（零 AI 确定性执行）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（终端命令 + 输出 + 代码标记）
- 整体调性：3 phase 纯切换（禁 data-reveal，多 phase 用 GSAP timeline 顺序切换）—— phase-1 装依赖装浏览器内核准备（terminal cd+install+playwright）→ phase-2 跑 main 用例执行（python main.py + 新增商品验证 + 通过2失败0）→ phase-3 确定性执行零 AI 收尾（第四条跳过 + 运行期零 AI）

## 情绪曲线 emotion_curve（3 点）
- 0.55（开箱跑 装依赖装浏览器 命令行准备）
- 0.72（python main.py 跑 用例执行 通过2失败0）
- 0.88（第四条跳过 + 运行期零 AI 确定性执行 收尾）

## 沉浸模式 immersion_mode
phase 切换（3 phase，纯 GSAP timeline，禁 data-reveal）：装依赖准备 → 跑用例通过2失败0 → 第四条跳过+零AI确定性收尾

## 叙事模板 narrative_template
终端演示（prepare → run-test → deterministic-finale）
- Step 1（0-18s）：开箱跑 装依赖装浏览器内核（terminal: cd ai-test-frame → pip install → playwright install chromium）
- Step 2（18-37s）：python main.py 跑 Playwright 打开商品页 新增商品验证 通过两个失败零个
- Step 3（37-55s）：第四条用例开关关闭自动跳过 整个流程确定性执行运行期零 AI 收尾

## 组件
- bg：diamond_lattice（深蓝底菱形网格，与 E13 其他段同款，跨段视觉连贯）
- fx：fx-aura 静态光晕（蓝命令+绿通过+灰跳过+金汇总+青确定性，冷色优先 alpha≤0.22 暖色）+ fx-particle + fx-blink（禁划过类 scan/stream/beam，教程铁律）
