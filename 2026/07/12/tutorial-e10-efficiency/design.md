# Design — E10 段9 提效同比靠 Excel

- orientation: landscape
- resolution: 1920x1080
- duration: ~50s
- bg: hex_grid（与 output=contour_lines 不同，与 demo3=hex_grid 重复但本批内首用 ok）
- palette:
  - bg-deep #0F172A
  - accent-gold #FBBF24
  - accent-blue #3B82F6
  - accent-emerald #34D399

## 视觉
Excel 表格卡（template.xlsx 列名：日期/定制或通用/应用/类型/jira_id/描述/开发人员）+ efficiency 输出（上线/需求/Bug/人均条目 对比）。

## 布局
单 tut-scene 多 region data-reveal stagger：顶部标题 → Excel 表格（左 7 列）+ efficiency 模块输出（右对比卡）。
