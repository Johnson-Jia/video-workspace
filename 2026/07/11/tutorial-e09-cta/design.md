orientation: landscape
resolution: 1920x1080
# E09 cta 段 · 设计文档

## 元数据
duration: 25s
category: tutorial
segment: cta

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，承接 E09 essence 收尾）
- 强调色：暖金 #FBBF24/#FCD34D（合集标识 + E10 预告卡 ai-metrics 高亮 + 关注 CTA）+ 冷蓝 #60A5FA/#93C5FD（合集卡 + 组织能力底座）+ 紫 #A78BFA/#C4B5FD（互动问「你的团队」）+ 青 #22D3EE/#67E8F9（E10 度量实操 AI 占比点缀）
- 字体：Inter（合集大字/E10 标题/关注）/ Noto Sans SC（正文/互动问）/ JetBrains Mono（ai-metrics / E10 / 集数）
- 整体调性：合集归属感（强标识）+ E10 预告钩子（ai-metrics 度量）+ 关注引导清晰

## 情绪曲线 emotion_curve（5 点）
- 0.62（点题「Skill 范式整合 = 组织能力底座」）
- 0.78（E10 预告 ai-metrics 看 AI 占比，钩子拉起）
- 0.72（合集还有四集，归属感）
- 0.85（关注 CTA 高潮 + 教程仓库评论区）
- 0.68（收尾互动问，中性留白）

## 沉浸模式 immersion_mode
cta_reveal：合集标识 → E10 预告卡 → 关注 CTA stagger

## 叙事模板 narrative_template
CTA（点题底座 → E10 预告 → 合集四集 → 关注+仓库 → 互动问）
- Phase 1（0-4s）：合集标识 + 点题「Skill 范式整合 = 组织能力底座」
- Phase 2（4-12s）：E10 预告卡（ai-metrics 看 AI 占比）+ 合集还有四集
- Phase 3（12-19s）：关注 CTA（点关注不走丢）+ 教程仓库在评论区
- Phase 4（19-25s）：互动问「你的团队，高频操作做成 Skill 共享了吗？」中性留白

## bg_component
hex_grid

## 文字安全
- 渐变文字两端亮色（#FCD34D/#FBBF24/#60A5FA/#93C5FD/#A78BFA/#C4B5FD/#22D3EE/#67E8F9）
- text-shadow alpha ≤0.32
- 文字溢出防御：word-break / overflow-wrap / flex min-width:0
- 多音字：本段无多音字陷阱
- 禁"第一"用"其一/首"（本段无）
- 创作指令禁泄露
