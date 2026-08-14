# Design — 2026-08-13 GitHub Trending 日榜（让生活变简单的开源工具 · 五方向多元专题）

## 视觉风格

style: 暗色科技风（github 分类 default_style）
mood: 轻松实用 + 获得感，把日常麻烦交给开源，轻快不浮躁
color_direction: 冷色为主（深蓝 #1E293B / 深紫 #2A1B4E 渐变基底），强调色 `#FF8C32` 橙 + `#4DA8DA` 蓝（github 分类 color_bias），双光晕（暖冷色调），无衬线粗体

immersion_mode: fun-tool
- 依据：本期 5 项目为多元生活工具（图表模板 / 跨端传输 / 英语自学 / AI 做 PPT / 端侧小模型），主题"让生活变简单的开源工具"匹配 fun-tool（彩色弹跳 + 幽默角色 + 亮色点缀）；非纯 AI 集合，不命中 hyper-pace；橙色强调色承担温度

orientation: portrait
orientation_source: 默认竖屏（github 分类无 orientation_hint）

## 情感节奏

emotion_curve: [grab, build, reveal, climax, settle, summon]
- grab (S1 hook): 反直觉排比——画图不用学设计 / 传文件不用数据线，双"不用"冲突钩子
- build (S2 diagram-design): 二十九套编辑级模板直接套，单日涨星两千八百多，建立"省事"主线
- reveal (S3 localsend): 八万七千人用的跨端互传，数据揭示"开源替代"分量
- climax (S4 everyone-can-use-english): 三万六千人把英语用起来，方法价值高潮
- settle (S5 ppt-master): AI 把文档变成原生 PPT，收稳讲办公自动化
- summon (S6 needle + CTA): 十四兆模型塞进口袋 + 中性二选一提问收尾

## storyboard

storyboard: 6 场景叙事节拍（让日常麻烦外包给开源，非 hyper-pace 盘点）

beat_mapping:
  hook: grab
  diagram_design: build
  localsend: reveal
  everyone_can_use_english: climax
  ppt_master: settle
  needle: summon

humor_style: analogy（类比为主）
- 生活类比：图表模板=给文档穿杂志外衣、跨端互传=没有围墙的隔空投送、英语方法=把英语当工具用、端侧模型=塞进口袋的 AI 大脑
- 反直觉收益：画图不用学设计 / 传文件不用数据线 / 做 PPT 不用一页页排版 / 跑模型不用云端显卡
- 幽默注入在 build/reveal/climax/settle 节拍，grab/summon 保持简洁有力

narrative_structure: 让日常麻烦外包给开源（五方向多元生活工具，不用 hyper-pace 盘点，呼应 topic_plan.novelty_strategy）

## 场景视觉原则

- 标准模式 ProjectFullCard 一屏一项目，8 层信息（类别标签/排名/项目名/一句话/语言/核心指标/三词卖点/感性评语）
- 视觉类型以 list / hero / highlight / data 为主，与 fun-tool 沉浸模式一致
- 数字锚点视觉化：2855（diagram 当日爆点）/ 87K（localsend 总星最高）/ 36K（英语）/ 45K（PPT）/ 14MB（needle）用大号强调色呈现
