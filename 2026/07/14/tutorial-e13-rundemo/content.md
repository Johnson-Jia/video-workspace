# E13 rundemo 段 · 内容文档（实跑演示·终端）

## 来源
对应教程 demos/ai-test-frame（README §快速运行）。本段是 E13 合集段6，实跑演示：cd 进目录 → 装依赖装浏览器 → python main.py 跑用例 → 通过两个失败零个 → 第四条用例关闭跳过 → 确定性执行零 AI。

## 核心信息
- **开箱跑通**：cd ai-test-frame → pip install -r requirements.txt → playwright install chromium → python main.py
- **Playwright 自动化**：打开自带的商品管理页，按 data/cases.json 用例跑
- **用例结果**：4 条用例，3 条 enable=true（新增商品验证列表出现等），1 条 enable=false（第四条开关关闭自动跳过）
- **断言汇总**：通过两个，失败零个（纯文本输出兼容命令行编码）
- **确定性执行**：运行期零 AI 插手，数据驱动调度

## narration（逐字）
开箱跑一遍。确认进到 ai-test-frame 目录，装依赖，装浏览器内核，跑 main。Playwright 打开自带的商品管理页，按用例跑，新增商品验证列表出现，终端输出断言汇总：通过两个，失败零个。第四条用例开关是关闭，自动跳过。整个流程确定性执行，没有 AI 在运行期插手。
