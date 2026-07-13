# Design — E10 段5 实跑 main.py（terminal）

- orientation: landscape
- resolution: 1920x1080
- duration: ~70s
- bg: scan_grid（与 stylometry=dark_cipher / demo3=hex_grid 不同）
- palette:
  - bg-deep #0F172A
  - accent-gold #FBBF24
  - accent-blue #3B82F6
  - accent-emerald #34D399

## 视觉
terminal 打字（cd demos/ai-metrics → pip install openpyxl → python main.py）+ scan_line 逐行扫输出（# === 1. AI 代码占比 === / # === 2. 提效同比 === / # === 3. 生成报告 ===）。

## 命令序列
1. `cd demos/ai-metrics`
2. `pip install openpyxl`
3. `python main.py`

## 输出段落
- `# === 1. AI 代码占比度量（含风格学反伪造）===`
- `# === 2. 提效同比 ===`
- `# === 3. 生成报告（Markdown + HTML）===`

## 布局
单 tut-scene：terminal 窗口左侧，输出区右侧（或上下）。代码语法高亮（蓝kw/绿str/紫fn/金num）。
