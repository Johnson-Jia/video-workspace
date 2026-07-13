# Design — E10 段4 三类提交演示

- orientation: landscape
- resolution: 1920x1080
- duration: ~60s
- bg: hex_grid（与前段 stylometry=dark_cipher 不同）
- palette:
  - bg-deep #0F172A
  - accent-gold #FBBF24
  - accent-blue #3B82F6
  - accent-cyan #60A5FA
  - accent-emerald #34D399
  - accent-rose #F87171

## 视觉
三栏对比卡（干净A建画像 / AI风格B确认 / 误标风格A挡住）+ 每栏风格画像 + Co-authored-by 标记 + 最终置信度数值。

## 三类提交
1. **Alice 干净提交**（风格 A）：建立 Alice 的风格画像
2. **Alice AI 提交**（风格 B + Co-authored-by）：跟画像差异大，置信度高，确认 AI
3. **Alice 误标提交**（风格 A + Co-authored-by）：跟画像更像，置信度低，挡住误标

## 布局
单 tut-scene 横向三栏对比卡，每栏含提交信息 + 风格画像 + Co-authored-by 标记 + 置信度。
