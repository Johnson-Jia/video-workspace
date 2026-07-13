# Design — 2026-07-12 GitHub Trending

style: 暗色科技风（深蓝/深紫渐变底 + 橙金强调色 + 双光晕）
mood: 理性惊叹 + 探索好奇（震撼 → 好奇 → 共鸣 → 互动）
color_direction: 冷色为主（深蓝 #0B1226 / 深紫 #1A1235 渐变底），强调色用暖色（橙 #FF8C32 + 金 #FBBF24），双光晕（暖冷色调，alpha≤0.22 避泛光）；渐变文字同色系高饱和禁白色端点
orientation: portrait
emotion_curve: [震撼, 惊叹, 实用, 好奇, 轻松, 理性]
storyboard: 6 场景（hook → pgrust → PowerToys → fprime → next-ai-draw-io → home-assistant+CTA），contrast-arc 叙事，单段 6-9s，总时长约 39s

## 情绪提炼
- 主题：今日 GitHub 5 个值得关注的项目，覆盖数据库内核 / Windows 效率 / 航天嵌入式 / AI 流程图 / 本地智能家居，多元题材破 AI 疲劳
- 情绪基调：理性惊叹 + 探索好奇（每个项目都有反常识角度，让观众"原来还能这样"）
- 情绪弧线：震撼（hook 数字+反直觉）→ 好奇（每个项目逐步揭示）→ 共鸣（普通人能用的利益）→ 互动（结尾提问）
- 节奏感：紧凑快播，5 段项目每段 6-8s，hook 3-4s 一击即中
- 文化调性：现代科技 / 暗色冷峻

## 视觉风格
- **orientation**: portrait（github 分类默认竖屏 1080×1920）
- **default_style**: 暗色科技风
- **color_bias**: 冷色为主（深蓝 #0B1226 / 深紫 #1A1235 渐变底），强调色用暖色（橙 #FF8C32 + 金 #FBBF24），双光晕（暖冷色调，alpha≤0.22 避泛光）
- **immersion_mode**: contrast-arc（默认叙事弧，多项目盘点 + 反直觉锚点，每段独立卡片强对比）
- **text-shadow**: 极淡 drop `0 2px 6px rgba(30,41,59,0.08)`，禁发光
- **渐变文字**: 禁白色端点，同色系高饱和（橙 #FF8C32→#FB923C→#FDBA74 / 蓝 #4DA8DA→#60A5FA→#93C5FD / 金 #FBBF24→#F59E0B→#FCD34D）

### 黄金 3 秒视觉要求
hook 场景视觉冲击：字号最大（标题 200px+）、对比强烈（橙金渐变文字 vs 深蓝底）、布局精致（数字锚定居中 + fx 光晕辐射）。配 hook 反直觉文案"用 Rust 重写的 Postgres 通过 100% 回归测试"+ 单日 789★ 数字。

## 字体气质
- **fonts.voice**: 紧凑/专业/利落（几何简洁）—— 多项目盘点快播，需要清爽利落的视觉
- **fonts.title**: Inter 900（主标题 / hook 数字锚定）
- **fonts.body**: Noto Sans SC（中文正文，可读性优先）
- **fonts.data**: JetBrains Mono（数据 / star 数 / 涨星）

## 配乐方向
- bgm_style: clean-corporate（首选，低调不抢旁白，github 分类 bgm_style ✅ 首选档）
- 搜索关键词：clean corporate ambient / soft tech / monochrome minimal
- 氛围：科技感靠画面和音色，配乐只做衬底；禁 bold-energetic / epic-trailer（电子激昂抢旁白）

## 素材需求预判
- 数据对比：star 数 / 今日涨星数 → JetBrains Mono 等宽大字 + 强调色胶囊
- 功能列表：每个项目"用途"4-6 字利益标签 → 胶囊样式，纯场景色（不用 clip:text 渐变）
- 氛围感：深蓝/深紫渐变 + 双光晕 + 微粒子
- 纯文字概念：5 个项目用 ProjectFullCard 一屏一项目（avatar 中部锚点 + 项目名 + 用途 + 描述 + 涨星）
- 头像：assets/avatars/{owner}.png 已预下载（圆形 PNG），Stage 6 ProjectFullCard 引用

## 故事板
- **叙事模板**: contrast-arc（平淡→对比→震撼→高潮→沉淀）
- **场景数**: 6（hook → 5 个项目 → 结尾 CTA 合并到第 6 段或独立第 7 段；本期控制在 6 段内：hook + 5 项目，CTA 嵌入最后一段）
- **节奏**: hook 3-4s + 5 项目每段 6-7s，总时长 ~35-40s，字数 250-380
- **沉浸模式**: contrast-arc（每段独立卡片，深色背景 + 暖冷双光晕对比 + 数字大字冲击）

### 场景节奏（emotion_curve）
1. hook（震撼 / 反直觉冲击）— Rust 重写 Postgres 100% 回归测试 + 789★ 数字
2. pgrust（惊叹 / 反常识）— 一个人重写工业级数据库内核
3. PowerToys（实用 / 利益共鸣）— 微软大厂下场效率工具集
4. fprime（好奇 / 平民化航天）— NASA 上天软件开源
5. next-ai-draw-io（轻松 / 创意）— 自然语言画流程图
6. home-assistant + CTA（理性 / 安全感 + 互动）— 本地优先智能家居 + 提问

### 视觉素材清单
- ProjectFullCard 组件 × 5（avatar / 项目名 owner+repo / 用途胶囊 / 中文描述 / 今日涨星大字）
- hook 数字大字 × 1（"+789★" / "100%" 渐变橙金）
- bg 层：hex_grid / scan_grid / diamond_lattice 任选其一（暗色科技底）
- fx 层：脉冲光晕 / 跑马灯流光 / 呼吸光（每段至少 2 个不同类型）
