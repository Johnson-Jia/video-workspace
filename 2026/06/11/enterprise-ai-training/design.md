# design.md — 视觉风格方向 + 故事板

> 项目：企业 AI 技能培训深度商业分析
> 报告日期：2026-06-10（70+ 来源 URL 交叉验证）

## 风格
style: 科技商业数据感（暗色底 + 数据可视化质感，强调"分析师洞察"的专业感与"机会"的吸引力并存）
mood: 从震撼（失败教训）到洞察（AI 机会）的理性张力

导演 5 必答题：
1. 这是什么内容？— 一份用 $17.1B 失败投资反向验证"AI 企业培训真实机会"的商业分析
2. 给谁看？— 创业者、投资人、关注 AI 商业化的职场人
3. 要什么情绪？— 先震撼（失败规模）→ 再反转（AI 修复逻辑）→ 最后理性（落地路径）
4. 一句话钩子？— "170 亿美元烧光，证明了这个赛道是真需求"
5. 观众该带走什么？— 需求真实，但打法必须变：嵌入式 + 按效果计费

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑 #0a0a12，营造分析师屏幕感）
  accent_warm: 金色/琥珀（用于 hook、CTA、金钱/估值数字——代表"价值与机会"）
  accent_cool: 霓虹青（用于数据、统计、科技修复逻辑——代表"理性与数据"）
  accent_alert: 暗红/橙红（仅用于失败案例、归因、死亡红线——代表"警示"）
  text: 白色主 + 浅灰辅（高对比，数据可读性优先）

## 配乐方向
music_mood: 商业科技 / 理性紧张感（前段克制铺垫，AI 转折处适度上扬，落地理性收尾）
music_keywords: corporate tech, analytical, building tension, subtle uplift

## 素材预判（可选）
assets_needed: []
# 全程纯 CSS/HTML 实现：数据卡片、对比柱、成本阶梯、时间轴。无外部图片需求。

## 故事板
storyboard:
  narrative_template: "contrast-arc"      # 失败 vs 机会 的对比弧
  emotion_curve: [0.9, 0.6, 0.8, 1.0, 0.5, 0.7]   # grab 震撼开场 → climax AI 修复高潮
  immersion_mode: "hyper-pace"            # 数据密集快速呈现，分析师节奏
  humor_style: "narration-only"           # 商业严肃题材，纯旁白驱动，不加视觉噱头
  character_presence: false               # 无角色，全数据驱动
  scenes_planned: 17                      # 5 分钟深度解析，17 场景（s01-s17）
  target_duration: "~300s"                # 约 5 分钟

  beat_mapping:
    grab: "s01-hook"                      # $17.1B 失败投资震撼开场
    build: "s02-market, s03-gap"          # 市场规模 + 供需缺口铺垫
    reveal: "s04-byjus, s05-2u, s06-udacity, s07-juni-mooc"   # 失败案例真相
    climax: "s08-attribution, s09-death-formula, s10-ai-fix"  # 归因 + 死亡公式 + AI 修复转折
    settle: "s11-academic, s12-enterprise, s13-differentiation, s14-model, s15-redline, s16-roadmap"  # 验证 + 商业模式 + 红线 + 路线图
    summon: "s17-cta"                     # 行动召唤

## 16 场景叙事规划
1. s01-hook：170 亿美元烧光，验证了这是真需求（金色大数字冲击）
2. s02-market：$340-418B 全球培训市场 + $6-9.3B AI 子市场（数据卡片）
3. s03-gap：92% 想做 vs 1% 做好（供需缺口对比柱）
4. s04-byjus：$22B 估值 → 归零（崩塌时间轴）
5. s05-2u：$945M 债务破产（债务堆叠）
6. s06-udacity：$1B → $80M 甩卖（价值蒸发对比）
7. s07-juni-mooc：人力线性成本 + 完成率<10%（不可扩展陷阱）
8. s08-attribution：失败死因分布（43.3/17.9/16.4/11.9% 饼图式）
9. s09-death-formula：EdTech 死亡公式 5 要素（公式拆解）
10. s10-ai-fix：导师成本 $100+/h → $0.02-1.80/次（成本阶梯断崖，全片高潮）
11. s11-academic：哈佛 2 倍效果 + CMU 混合模式（学术背书）
12. s12-enterprise：Unilever/PwC/IBM 已落地（企业验证三联卡）
13. s13-differentiation：嵌入式 + 按效果计费 vs 按席位（竞争空白对比）
14. s14-model：90%+ 毛利率（单位经济对比表）
15. s15-redline：5 条死亡红线（警示清单）
16. s16-roadmap：4 阶段落地（$50K→$50M 时间轴）
17. s17-cta：行动召唤（关注/收藏，价值收束）

## 方向
orientation: portrait
orientation_source: default
