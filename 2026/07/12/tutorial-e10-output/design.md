# Design — E10 段8 看输出

- orientation: landscape
- resolution: 1920x1080
- duration: ~50s
- bg: contour_lines（与 runmain=scan_grid / demo3=hex_grid / stylometry=dark_cipher / algorithm 等不同）
- palette:
  - bg-deep #0F172A
  - accent-gold #FBBF24
  - accent-blue #3B82F6
  - accent-cyan #60A5FA
  - accent-emerald #34D399

## 视觉
terminal 三段输出窗口（AI 占比 / 提效同比 / 报告路径），scan_line 高亮关键数字（42.3% / 38.7% / 1.8x / report.html）。

## 三段输出
- `# === 1. AI 代码占比 ===`：提交占比 42.3% · 行数占比 38.7% · AI 提交作者占比
- `# === 2. 提效同比 ===`：每年上线/需求/Bug/参与人数/人均条目（2025→2026 对比）
- `# === 3. 报告生成完成 ===`：workspace/report.md + workspace/report.html

## 布局
单 tut-scene 多 region data-reveal stagger：顶部标题 → 三段输出卡（蓝/绿/金 accent 区分）。
