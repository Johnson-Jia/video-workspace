# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗紫周刊开箱        # 周榜「一周时间胶囊」开箱感：深色底 + 大气粒子 + 逐组揭示
mood: 悬念递进·盘点沉淀     # mystery-box 好奇→线索→揭示，结尾趋势洞察沉淀

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（近黑深紫基底，周榜刊物质感）
  accent_cool: 紫罗兰/幽蓝（用于 Agent 基建组与模型组场景，mega-update 大气粒子）
  accent_warm: 琥珀橙（用于 hook/CTA/开发者组，强调对比）
  domain_colors: 四组领域色仅视觉用——蓝 #60A5FA（Agent 基建）/ 浅紫 #A78BFA（模型本地化）/ 暖橙 #FDBA74（开发者效率）/ 翠绿 #34D399（创意与自查），用于卡片色环/边框/标签/渐变标题，旁白与画面文字禁说颜色词
  text: 白色主 + 浅灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "衬线庄重"
    family: "Noto Serif SC"
    weight: 900
    rationale: "周榜=一周刊物的趋势洞察，开箱揭示的悬念配衬线的知识重量感，与日榜几何极客风区分"
    fallback: "'Noto Serif SC','PingFang SC','Microsoft YaHei',serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 低调科技周刊感（clean-corporate / monochrome 系，衬底不抢播报）

## 素材预判（可选）
assets_needed: []       # 全 CSS/HTML 实现：领域分组卡、总星数据卡、粒子背景；avatars 走 assets/avatars/ 引用

## 故事板（新增）
storyboard:
  narrative_template: "mystery-box"        # 差异化：近5期周/日榜均未用（33周榜/日榜高频 contrast-arc，ai-wind 用 showdown）
  emotion_curve: [0.5, 0.6, 0.7, 0.9, 0.6, 0.4]
  immersion_mode: "mega-update"            # 周榜里程碑属性（91K/87K/78K 总星），暗紫 3D 大气粒子，近3天未用
  humor_style: "dual-track"                # 旁白轻梗 + 视觉彩蛋（码力角色）
  character_presence: true                 # 码力角色 climax（组3+组4 信息高潮）出场
  beat_mapping:                            # 节拍 → 场景映射（7 场景折进 6 拍）
    grab: "hook（第34周悬念：一半项目在给 AI 打工）"
    build: "组1 AI Agent 基建（4 项目，第一组线索）"
    reveal: "组2 模型本地化（3 项目，趋势另一面）"
    climax: "组3 开发者效率 + 组4 创意自查（7 项目，信息高潮，码力出场）"
    settle: "趋势总结（Agent 基建潮洞察沉淀）"
    summon: "CTA（周次收尾）"

## 方向（新增）
orientation: portrait   # 竖屏抖音
orientation_source: category_hint  # github 分类：竖屏抖音周榜
