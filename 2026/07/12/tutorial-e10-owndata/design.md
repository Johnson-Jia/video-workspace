# Design — E10 段11 换成你自己的数据

- orientation: landscape
- resolution: 1920x1080
- duration: ~40s
- bg: diamond_lattice（与其他段不同）
- palette:
  - bg-deep #0F172A
  - accent-gold #FBBF24
  - accent-blue #3B82F6
  - accent-cyan #60A5FA
  - accent-emerald #34D399
  - accent-rose #F87171（警告色）

## 视觉
terminal 配置（REPO = "/path/to/your/repo"）+ 注意卡（人数偏高约两倍 / 趋势准确）。

## 布局
单 tut-scene 多 region data-reveal stagger：顶部标题 → 改 main.py REPO + 替换 sample_releases.xlsx → 注意卡（开发人员字段含多人/写法不规范 → 人数偏高约两倍）。
