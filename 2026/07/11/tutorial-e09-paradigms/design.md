# E09 paradigms 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 90s
category: tutorial
segment: paradigms

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，承接 E09 why）
- 强调色：暖金 #FBBF24/#FCD34D（编排型金边强调）+ 冷蓝 #60A5FA/#93C5FD（工具/规范/平台）+ 翠绿 #34D399/#6EE7B7（流程/记忆）+ 紫 #A78BFA/#C4B5FD（诊断）+ 暖橙 #FB923C/#FDBA74（编排型 devflow 金边）
- 警示色：红 #F87171/#FCA5A5（写操作禁猜测）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（编号/标签）
- 整体调性：沉稳科技 + 范式分卡清晰（七卡网格 + 编排型金边升华）

## 情绪曲线 emotion_curve（5 点）
- 0.50（点题「七种 Skill 范式」）
- 0.62（前四卡：工具/规范/平台/流程，务实高效）
- 0.68（记忆/诊断，沉淀只读）
- 0.80（编排型金边升华，devflow）
- 0.65（总结收尾）

## 沉浸模式 immersion_mode
data_reveal：7 卡片网格 + 编排型金边强调

## 叙事模板 narrative_template
七种范式（intro → 7 paradigms → editor's pick）
- Phase 1（0-6s）：标题「七种 Skill 范式」+ 副标「各管一摊」
- Phase 2（6-78s）：7 卡片网格 reveal stagger，按工具/规范/平台/流程/记忆/诊断/编排顺序逐卡亮起，编排型金边最后强调（devflow 编排 OpenSpec+Superpowers）
- Phase 3（78-90s）：编排型特写 + devflow 六阶段缩略

## 场景规划（visual_phases）

### Phase 1（0-6s）：标题 + 七种范式预告
- 视觉：标题「七种 Skill 范式」+ 标签「E09 · 范式整合」+ 副标「各管一摊」
- 7 范式图标小图标横排预告（工具🔧/规范🎨/平台🏗/流程🔄/记忆🧠/诊断🔍/编排⚙）
- 大字渐变（金色同色系亮端）+ text-shadow 深蓝 rgba(30,41,59,0.32)

### Phase 2（6-78s）：7 卡片网格 reveal stagger
- 视觉：4+3 网格布局（顶行 4 卡：工具/规范/平台/流程；底行 3 卡：记忆/诊断/编排）
- 每卡：图标 + 范式名 + 团队类型 + 一句话核心思路
- 工具型🔧：业务开发团队 / 封装高频开发动作
- 规范型🎨：前端团队 / AI 输出符合设计规范 · 统一 Token
- 平台型🏗：低代码搭建团队 / 严格触发 + 接口白名单 · 绝不猜测写操作
- 流程型🔄：全栈团队 / AI 分析变更生成规范提交 · 自动提交
- 记忆型🧠：跨项目团队 / 持久化记忆 · 跨会话复用 · 按项目隔离
- 诊断分析型🔍：性能团队 / 只读分析不改代码 · 慢 SQL 定位
- 编排型⚙：架构师团队 / 自己不实现 · 串流水线（devflow 编排 OpenSpec+Superpowers）· 金边强调

### Phase 3（78-90s）：编排型特写
- 视觉：编排型卡放大 + devflow 六阶段缩略（OpenSpec → Superpowers → 六阶段）
- 金边光晕强调 + devflow 编排流图
