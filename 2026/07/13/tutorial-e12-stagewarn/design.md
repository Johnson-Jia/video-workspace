# E12 stagewarn 段 · 设计文档（别用错阶段）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 50s
category: tutorial
segment: stagewarn

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：警示红 #F87171/#FCA5A5（⛔ 禁编造验证数据）+ 冷蓝 #60A5FA/#93C5FD（启动版现状+目标）+ 暖金 #FBBF24/#FCD34D（成果版实测+104%）
- 字体：Inter（大字/警示）/ Noto Sans SC（正文）/ JetBrains Mono（数据/阶段标注）
- 整体调性：alert_border 红框警示 + 启动版 vs 成果版对比

## 情绪曲线 emotion_curve（5 点）
- 0.40（关键提醒：别用错阶段 抛出警示）
- 0.62（启动版禁编造验证数据：人均翻倍/AI七成 不信穿帮）
- 0.75（翻倍数据归成果版：阶段五度量工具跑出来）
- 0.85（启动版正确：现状+目标+先试点 更诚实有力）

## 沉浸模式 immersion_mode
phase 切换：警示抛出 → 启动版禁编造详情 → 翻倍归成果版 → 启动版正确做法收尾

## 叙事模板 narrative_template
警示（warning → launch-fabricate → result-belong → launch-correct）
- Step 1（0-11s）：关键提醒 alert_border（⛔ 别用错阶段的数据）
- Step 2（11-28s）：启动版绝对不要写 人均翻倍/AI七成（验证成果）· 还没跑出来 一追问穿帮
- Step 3（28-38s）：翻倍这类数据 阶段五度量工具跑出来 归成果版
- Step 4（38-50s）：启动版正确做法 现状+目标+先试点 更诚实有力 收尾

## 组件
- bg：diamond_lattice（深蓝底菱形网格）
- fx：fx-aura 静态光晕（红警示 + 蓝启动 + 金成果）+ fx-particle + fx-blink（禁划过类 scan/stream/beam）
