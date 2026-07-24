# E12 cta 段 · 设计文档（CTA + E13 预告）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 25s
category: tutorial
segment: cta

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：CTA 金 #FBBF24/#FCD34D（关注/合集标识）+ E13 蓝 #60A5FA/#93C5FD（下集预告/ai-test-frame）+ 提问紫 #C4B5FD/#DDD6FE（中性互动）
- 字体：Inter（大字）/ Noto Sans SC（正文）/ JetBrains Mono（E13/ai-test-frame/合集标识）
- 整体调性：合集标识 + E13 预告卡（测试实操）+ 关注 CTA + 中性提问

## 情绪曲线 emotion_curve（3 点）
- 0.50（汇报材料是转型对外发声 收束）
- 0.72（E13 预告 AI 自动化测试实操）
- 0.85（合集还有一集 关注 + 中性提问 收尾）

## 沉浸模式 immersion_mode
phase 切换：开场（汇报材料 对外发声）→ E13 预告（ai-test-frame 录制转生成 软断言）→ 收尾（关注 + 合集 + 中性提问）

## 叙事模板 narrative_template
CTA（recap → e13-preview → follow-cta-question）
- Step 1（0-6s）：汇报材料是转型的对外发声 把成果变成上级看得懂的 PPT 和报告 收束
- Step 2（6-16s）：E13 预告 AI 自动化测试实操 ai-test-frame 录制转生成 软断言
- Step 3（16-25s）：合集还有一集 点关注 + 教程仓库 + 中性提问 收尾

## 组件
- bg：diamond_lattice（深蓝底菱形网格）
- fx：fx-aura 静态光晕（金关注+蓝E13+紫提问）+ fx-particle + fx-blink（禁划过类 scan/stream/beam）
