# Design — 2026-08-12 GitHub Trending 日榜（非AI多元专题：老工具长青树 + 学习资源）

## 视觉风格

style: 暗色科技风（github 分类 default_style）
mood: 经典可靠 + 干货获得感，轻快不浮躁
color_direction: 冷色为主（深蓝 #1E293B / 深紫 #2A1B4E 渐变基底），强调色 `#FF8C32` 橙 + `#4DA8DA` 蓝（github 分类 color_bias），双光晕（暖冷色调），无衬线粗体

immersion_mode: fun-tool
- 依据：本期 4 项目全部为工具/资源类（动画引擎 / 软件清单 / 自学清单 / 版本管理器），AI 占比 0%，不命中 hyper-pace；主题是"有趣实用的老工具长青"，匹配 fun-tool（彩色弹跳 + 幽默角色 + 亮色点缀），复古温度由橙色强调色承担

orientation: portrait
orientation_source: 默认竖屏（github 分类无 orientation_hint）

## 情感节奏

emotion_curve: [grab, build, reveal, settle, settle, summon]
- grab (S1 hook): 四个老项目合计 57 万星，数字锚定 + 动作词
- build (S2 manim): 反直觉开场——代码画动画
- reveal (S3 awesome-mac): 11 万人挑过的藏宝图，数据揭示
- settle (S4 project-based-learning): 278K 榜内最高，放慢给足分量
- settle (S5 nvm): 2010 年老工具，收稳讲长青
- summon (S6 cta): 二选一互动提问 + 关注引导

## storyboard

beat_mapping:
  hook: grab
  manim: build
  awesome_mac: reveal
  project_based_learning: settle
  nvm: settle
  cta: summon

humor_style: analogy（类比为主）
- 生活类比：软件清单=藏宝图、自学清单=路线图、manim=拿代码当画笔
- 开发者文化梗：电脑里只装一个 Node 就像衣柜里只挂一件衣服
- 幽默注入在 build/reveal/settle 节拍，grab/summon 保持严肃

narrative_structure: 经典老工具长青 × 学习资源对比（不用 hyper-pace 盘点，呼应 topic_plan.novelty_strategy）

## 场景视觉原则

- 标准模式 ProjectFullCard 一屏一项目，8 层信息（类别标签/排名/项目名/一句话/语言/核心指标/三词卖点/感性评语）
- 视觉类型以 list / hero / highlight 为主，与 fun-tool 沉浸模式一致
- 数字锚点视觉化：57 万（合计）/ 278K / 110K / 94K / 90K 用大号强调色呈现
