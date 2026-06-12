# design.md — 视觉风格方向 + 故事板（intro 分类）

## 风格
style: 暖色星空风
mood: 真诚→史诗→归港（温暖底色铺底，中段攀升，climax 史诗爆发，you 急转温暖着陆）

## 配色方向（描述性，不指定具体色值，具体由 Stage 6 落地）
color_direction:
  background: 深空黑（接近 #040810），营造深夜对谈氛围
  accent_warm: 琥珀/金色（#FFB800 / #FFD700）—— 光晕、分隔、标题、hook/CTA/climax 强调
  accent_cool: 青色/薄荷（#64FFDA / #4DD0B0）—— 金青渐变强调关键短语，冷暖对比
  accent_fire: 火色（#FF6B00）—— climax 渐变终点，全片最高燃
  text: 奶油白（#F0E8DA）主 + 弱化色（rgba 0.6）辅

> 禁止纯冷色方案——intro 需要暖色建立信任。

## 配乐方向
music_mood: 安静→温暖→希望→史诗→归港
- 开篇安静/温暖（hook~proof）
- 中段渐强/希望（faith~multiply）
- 高潮史诗/燃烧（climax）
- 收束温暖/归港（you~cta）
- 优先 ≥90s 有明确情绪递进的长曲，避免循环短曲

## 素材预判
assets_needed: []   # 纯 CSS 渐变/光效/粒子实现，无外部素材

## 故事板
storyboard:
  narrative_template: "emotional-arc"      # intro 固定八段情感弧
  emotion_curve: [0.4, 0.6, 0.75, 1.0, 0.5, 0.45]
  immersion_mode: "warm-starlight"         # intro 统一沉浸模式
  humor_style: "narration-only"            # intro 幽默权重 ≤20%，仅轻自嘲
  character_presence: false                # intro 第一人称"我/你"对话，无虚拟角色
  beat_mapping:
    grab: "hook"                           # 好奇/温暖
    build: "proof, faith"                  # 敬佩/肃穆，扎根点上升
    reveal: "whatif"                       # 憧憬，打开想象
    climax: "multiply, climax"             # 激昂→史诗，全片最高潮
    settle: "you"                          # 温暖收束，climax 后急转下行
    summon: "cta"                          # 行动号召，低位稳定收尾

## 核心隐喻（贯穿全片）
core_metaphor:
  theme: 星火燎原
  arc:
    - 第一段（proof/faith）：每一行开源代码、每一个组件 = 一颗星火
    - 第二段（multiply/climax）：管线=锻造炉，组件=火种，引擎=鼓风机——星火汇聚成燎原
    - 第三段（you/cta）：你做的每条视频 = 一簇星火
  fx_sync: climax 场景 FX 必须是隐喻可视化（星火→火焰）

## 视觉主题元素（warm-starlight 沉浸模式）
- bg 暖光晕：opacity ≥ 0.25（手机可读底线，<0.15 等同黑屏）
- fx 星点：缓慢漂移（duration = 场景时长）
- fx 光圈：每场景 1 个 ring 缓慢扩张
- climax 特效：≥ 2 种不同类型元素（火星 + 光晕 + 粒子爆发）
- content 淡入：opacity 0→1，duration 0.6-0.8s

## 手机可读性标准（intro 第一优先级，信息流向新观众推荐）
- 正文字号 ≥ 36px
- 标题字号 ≥ 46px（hook 场景更大，钩子文字远距离可读）
- 渐变文字：必须用 background-image，禁止 background 简写
- 渐变文字：不加 text-shadow（HyperFrames 渲染异常）

## 三层架构
- bg (z1)：深空渐变 + 暖光晕（≥0.25）+ 微纹理
- fx (z2)：星点 + 光圈 + 火星/粒子
- content (z3)：文字，phase 用 position:absolute;inset:0 叠加

## 方向
orientation: portrait
orientation_source: default   # intro 分类无 orientation_hint，默认竖屏
