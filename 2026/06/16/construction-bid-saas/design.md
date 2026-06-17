# design.md — 建筑投标分析SaaS 商业逻辑深度解析

## 风格
style: 金融科技研报（深色理性·数据驱动）
mood: 严谨·洞察·有张力（巨大市场与极薄利润的反差感）

## 配色方向（描述性，不指定具体色值——Stage 6 据此推导）
color_direction:
  background: 深蓝灰暗调（接近纯黑，带微蓝调），传递数据/金融科技的理性底色
  accent_cool: 钴蓝/青蓝（用于数据、技术、分析、理性叙事——市场规模、效率倍数、AI 能力）
  accent_warm: 琥珀金（用于利润、机会、价值、CTA——利润率、毛利率、收入预测、行动召唤）
  text: 白色主 + 浅灰辅（信息层级：数字/结论 > 标题 > 正文 > 装饰）
  danger: 克制暗红（仅用于失败案例/风险红线/死亡公式场景，不滥用）
rationale: 钴蓝=理性数据隐喻，琥珀金=商业价值隐喻，冷暖交替制造叙事张力（director-toolkit 色温叙事）。深色做底、亮色做刀。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "衬线庄重"
    family: "Noto Serif SC"
    weight: 900
    rationale: "Q1 情感内核=洞察/理性/权威。深度商业分析报告需研报级权威感，衬线庄重传递严谨、可信、值得深读的洞察气质"
    fallback: "'Noto Serif SC','Songti SC','SimSun',serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 理性商业/数据科技（沉稳推进，带张力，中段有上升感，避免过于激烈或抒情）

## 素材预判
assets_needed: []   # 纯 CSS/HTML 实现所有图表与数据可视化，无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"   # 平淡→对比→震撼→高潮→沉淀：匹配 $13T vs 2-5% 反差 + 失败→修复对比逻辑
  emotion_curve: [0.55, 0.65, 0.7, 0.95, 0.6, 0.55]
  immersion_mode: "hyper-pace"          # 深底数据科技骨架（具体暖色由 color_direction 覆盖为金）
  humor_style: "narration-only"         # 商业分析无角色，幽默/反差仅在旁白文案层
  character_presence: false
  beat_mapping:
    grab: "S1-S4 钩子+背景现状（$13T vs 2-5% 反差、数字化<1%、数据空白、机会规模）"
    build: "S5-S9 失败教训（Katerra 崩溃、五大根因、WeWork 同源、ConTech 死亡公式）"
    reveal: "S10-S12 市场机会（$5.78B→$10.2B、大厂留白中型、五大教训→AI 修复逻辑）"
    climax: "S13-S18 解决方案+技术可行性（AI 投标决策引擎、四大能力、技术架构、30-50倍/100-1000倍）"
    settle: "S19-S24 商业模式+风险（阶梯收费、85-95%毛利、收入预测、数据壁垒、风险红线）"
    summon: "S25-S30 落地实操+展望（4阶段路线、核心逻辑闭环、行动召唤）"

## 场景总览（30 场景，~5-5.5 分钟，深度解析 deep_research 模式）
scenes_overview:
  part1_背景现状:
    - S1: hook——$13万亿市场 vs 2-5%利润率反差（黄金3秒视觉最强，全片焦点）
    - S2: 建筑业数字化极低（<1% IT 支出占比）
    - S3: 投标决策靠经验，数据空白
    - S4: 1-2%利润提升 = 数百万美元（机会规模）
  part2_失败教训:
    - S5: Katerra 登场——"建筑界 WeWork"，峰值估值约$40亿
    - S6: Katerra 崩溃时间线（2015→2021，烧$1.6-20亿）
    - S7: Katerra 五大失败根因
    - S8: WeWork 同源教训（SoftBank+垂直整合模式）
    - S9: ConTech 死亡公式 vs AI 修复逻辑（对比）
  part3_市场机会:
    - S10: 投标管理软件市场 $5.78B→$10.2B
    - S11: 竞争格局——Procore $1.4B ARR 聚焦大企业，中型留白（陈述对比）
    - S12: 五大教训 → AI 修复逻辑对照
  part4_解决方案:
    - S13: AI 投标决策引擎——只优化决策，不碰施工（核心 thesis）
    - S14: 四大核心能力（分析标书/对标基准/预测中标/优化定价）
    - S15: 技术架构（PDF→OCR→分析→AI决策→报告）
  part5_技术可行性:
    - S16: AI vs 传统——效率 30-50 倍（时间对比）
    - S17: AI vs 传统——成本 100-1000 倍 + 毛利对比
    - S18: 模型选择与单次分析成本（泛化表述，不点品牌名）
  part6_商业模式:
    - S19: 阶梯收费（Starter$500/Pro$2000/Enterprise$5000 月）
    - S20: 单位经济——毛利 85-95% vs 传统咨询 30-50%
    - S21: 收入预测（4阶段 $30K→$25M+）
    - S22: 数据壁垒——四大护城河（稀缺/网络效应/切换成本/时间壁垒）
  part7_风险红线:
    - S23: 风险矩阵（抗拒新技术/数据获取/大厂进入）
    - S24: 死亡红线（毛利<70%、月用<5次、CAC>24月、流失>20%）
  part8_落地实操:
    - S25: Phase 1 验证（0-6月，3-5试点，预算$50-150K）
    - S26: Phase 2 PMF（6-18月，20客户，ARR~$500K）
    - S27: Phase 3 规模化（18-36月，100+客户，ARR~$5M）
    - S28: Phase 4 成熟（3-5年，500+客户，ARR~$25M+）
  part9_展望总结:
    - S29: 核心逻辑闭环（从 Katerra 失败到 AI 决策优化）
    - S30: 行动召唤（数据壁垒是护城河）

## 方向
orientation: portrait
orientation_source: default   # 用户未指定方向，默认竖屏

## 合规备忘（贯穿全 stage）
- 人名：Katerra 创始人真实姓名一律不出现，只用公司名
- 品牌名：GPT-4o/Claude/Llama 一律泛化为"主流大模型/轻量大模型/开源大模型"（成本数字保留）
- 竞品：Procore/Autodesk 用陈述对比（聚焦大企业、定价高），非攻击
- 绝对化：禁"最/第一/唯一"，"峰值估值"替代"最高估值"
- 零 URL / 零搜索引导
- 数据保真：所有数字严格来自报告，零臆测
