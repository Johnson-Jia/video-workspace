# Design — E10 段3 风格学原理

- orientation: landscape
- resolution: 1920x1080
- duration: ~60s
- bg: dark_cipher（含 contour + glow，与前段 hook=scan_grid / intro=hex_grid / why=diamond_lattice / algorithm=scan_grid 不同）
- palette:
  - bg-deep #0F172A
  - accent-gold #FBBF24
  - accent-blue #3B82F6
  - accent-cyan #93C5FD
  - accent-emerald #34D399

## 视觉
四步流程图横向流水线（n-gram 切分 → TF 归一化 → 余弦相似度 → 置信度=1-sim）+ SVG 连线渐进绘制 + 相似度高→降置信 / 低→确认 AI 对比卡。

## 风格学算法四步
1. **n-gram 切分**：把代码切成字符级 n-gram，提取风格特征
2. **TF 归一化**：去掉高频词干扰
3. **余弦相似度**：算这个提交跟作者风格画像的相似度
4. **置信度=1-sim**：越像本人置信度越低越可能误标，越不像置信度越高越确认 AI

## 布局
单 tut-scene 横向四步流水线，下方双栏对比（高相似→降置信 / 低相似→确认 AI）。
