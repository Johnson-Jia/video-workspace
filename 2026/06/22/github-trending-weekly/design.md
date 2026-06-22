# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技·霓虹双轨
mood: 紧凑震撼·冷中带暖

## 画布方向
orientation: portrait
orientation_source: default

> github 分类无 orientation_hint，按默认竖屏 1080x1920。竖屏是 GitHub 盘点视频的频道基调，符合抖音就绪规范。

## 配色方向（描述性，不指定具体色值）

color_direction:
  background: 深色暗调（接近纯黑 #0a0e1a，深蓝/深紫渐变基底，全片统一）
  group_ai: 冷色霓虹（青色 #00D4FF / 蓝紫 #4DA8DA）——AI agent 8 个项目（降本/编程/模型/创作四组）用冷色，呼应"AI 智能"语义
  group_tool: 暖色光晕（琥珀金 #FF8C32 / 暖橙）——开发者工具3件套+教育1个用暖色，呼应"人能直接用"的温度感
  accent_highlight: 强调金（周冠军 headroom 数据 + 周次 + CTA 收尾）
  text: 白色主 + 浅灰辅 + 分组色（AI 冷/工具 暖）
  dual_glow: 暖冷双光晕（背景层），强化"双轨"主题

> 分组配色差异是本周视觉核心：AI 项目（占 8/13）冷色密集铺场，工具三件套（A 档普通人可用）切暖色制造温度反差，让观众"看见"AI 与人的关系。这是从内容推导的视觉表达，不是查表。

## 字体（三层 + voice 链接 Q1）

fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1情感内核=震撼紧凑+科技专业，几何粗体标题最贴合 GitHub 盘点的'数据说话'气质"
    fallback: "'Inter','Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技/赛博，紧凑电子，BPM 偏快配合 weekly 盘点节奏

## 素材预判
assets_needed: []  # 纯 CSS/HTML + avatar 即可，无外部素材

## 故事板（7 场景 = hook + 5 内容组 + CTA）

storyboard:
  narrative_template: "hyper-pace"  # 周榜盘点密集剪辑，AI 项目 >50% 触发 hyper-pace
  emotion_curve: [0.5, 0.6, 0.7, 0.85, 0.75, 0.5]  # hook 抓人→内容组逐步抬升→工具组小高潮→CTA 收束
  immersion_mode: "hyper-pace"  # AI/LLM/Agent 类项目 >50%，按 immersion_mapping 自动选
  humor_style: "dual-track"  # 旁白+视觉双线，build/reveal 节拍注入轻幽默
  character_presence: true  # github 分类启用码力角色，climax 节拍出场
  beat_mapping:
    grab: "S1 hook（周冠军砍九成多输入反直觉）"
    build: "S2 AI降本组（headroom+Agent-Reach，给AI省/给AI眼）"
    reveal: "S3 AI编程组（agent-skills+codebase-memory-mcp，给AI技能/记忆）"
    climax: "S4 AI模型与安全（timesfm+SkillSpector，Google/英伟达下场）"
    settle: "S5 AI创作组 + S6 开发者工具三件套（温度反差：AI切暖色工具）"
    summon: "S7 turso+freeCodeCamp+CTA（中性二选一）"

## 7 场景视觉方向（供 stage6 参考）

| 场景 | 内容 | 视觉方向 |
|------|------|---------|
| S1 hook | 周榜开场 + headroom 反直觉钩子 | hero 大字"砍九成多 + 答案还一样" + 周次锚点 + 冷光晕，全片视觉最强画面 |
| S2 AI降本 | headroom + Agent-Reach | 双卡对比（压缩 vs 联网），冷色青蓝霓虹，"给 AI 省钱/给 AI 眼睛"利益标签 |
| S3 AI编程 | agent-skills + codebase-memory-mcp | 双卡（技能包 vs 知识图谱），冷色深紫蓝，"生产级技能/158语言"数据 |
| S4 AI模型安全 | timesfm + SkillSpector | 双卡（时序预测 vs 安全扫描），冷色青绿+警示边，Google/英伟达大厂标识 |
| S5 AI创作 | OpenMontage + flue | 双卡（视频生产 vs 沙箱框架），冷色蓝紫，"12流水线/沙箱" |
| S6 工具三件套 | insomnia + plane + chatwoot | **暖色切换！**琥珀金光晕，3卡横排，"你能直接用"温度感，A档普通人可用 |
| S7 教育+CTA | turso + freeCodeCamp + 总结 | 暖冷过渡，CTA 大字 + 周次收尾，中性二选一互动 |

> S5→S6 的冷暖切换是本周视觉关键反差点：AI 项目冷色密集后，工具三件套切暖色给观众"喘息+温度"，呼应"AI vs 人"的内容张力。
