# Design — E10 段10 报告 ECharts 可视化

- orientation: landscape
- resolution: 1920x1080
- duration: ~40s
- bg: scan_grid（report 主题用扫描网格切合数据可视化）
- palette:
  - bg-deep #0F172A
  - accent-gold #FBBF24
  - accent-blue #3B82F6
  - accent-cyan #60A5FA
  - accent-emerald #34D399

## 视觉
report.html 截图框（饼图 + 柱状图 ECharts 可视化模拟），左右双图表，旁标数据标签。

## 布局
单 tut-scene 多 region data-reveal stagger：顶部标题 → 浏览器窗口（左饼图 AI 占比 / 右柱状图 同比）→ 底部「给老板汇报直接讲」条。
