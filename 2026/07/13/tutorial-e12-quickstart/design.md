# E12 quickstart 段 · 设计文档（5 分钟最小可走通）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 55s
category: tutorial
segment: quickstart

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：终端绿 #34D399/#6EE7B7（命令行输出/30秒出活）+ 冷蓝 #60A5FA/#93C5FD（打开模板/粘AI）+ 暖金 #FBBF24/#FCD34D（占位数据 28天/22%）
- 字体：Inter（大字）/ Noto Sans SC（正文）/ JetBrains Mono（终端命令/数据）
- 整体调性：terminal 终端演示（打开模板→填占位→粘AI→30秒出Markdown）+ scan_line 扫输出

## 情绪曲线 emotion_curve（5 点）
- 0.32（没有真实数据也能先跑通 抛出）
- 0.55（打开模板 填占位数据 28天/22%）
- 0.68（粘到免费 AI Kimi/通义千问）
- 0.85（三十秒出活 AI 吐结构齐全汇报）
- 0.80（先跑通再补真实数据 收尾）

## 沉浸模式 immersion_mode
phase 切换：开场（没有数据也能先跑通）→ 终端 step1-2（打开模板+填占位）→ 终端 step3（粘AI）→ 终端 step4（30秒出活）→ 收尾（先跑通再补数据）

## 叙事模板 narrative_template
终端演示（intro → open-template+fill → paste-ai → output-30s → finale）
- Step 1（0-9s）：没有真实度量数据也能先跑通 开场
- Step 2（9-26s）：终端 打开模板 + 填占位（28天/22%）step1-2
- Step 3（26-34s）：终端 粘到免费 AI（Kimi/通义千问）step3
- Step 4（34-46s）：终端 三十秒出活 AI 吐结构齐全汇报 step4
- Step 5（46-55s）：先跑通一遍 再补真实数据 收尾

## 组件
- bg：diamond_lattice（深蓝底菱形网格）
- fx：fx-aura 静态光晕（绿终端+蓝模板+金数据）+ fx-particle + fx-blink（禁划过类 scan/stream/beam）
