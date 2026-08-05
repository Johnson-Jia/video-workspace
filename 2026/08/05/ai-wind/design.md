# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色 AI 电紫科技        # AI 风向标分类默认风格
mood: 紧凑科技·自主冲击          # 情绪基调：AI 自主性主线，数据+反直觉交替冲击

## 配色方向（描述性 + ai-wind 电紫主题锚点）
color_direction:
  background: 深紫渐变底（接近纯黑 #0a0a14 → 深紫 #1a0a2e），双光晕（电紫+青）
  accent_cool: 电紫主色（#A855F7 → 亮紫 #C084FC，hook/CTA/排名数字/总星数据）
  accent_secondary: 霓虹青（#00D4FF，语言标签/三词卖点/辅数据）
  accent_warm: 暖橙点缀（#FF6B35，仅用于「今日涨星」增量数据做强对比）
  text: 白色主 + 浅紫/浅灰辅
  # ⛔ text-shadow 极淡 drop（0 2px 6px rgba(30,41,59,0.08)），禁发光；渐变文字禁白端点用同色系高饱和

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"            # Q1 情感内核：紧凑/专业/利落（AI 科技盘点）
    family: "Inter"
    weight: 900
    rationale: "AI 项目盘点紧凑科技调，几何无衬线放大数字与项目名最具冲击"
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
music_mood: 科技/赛博/电紫（hyper-pace 快速剪辑配密集粒子，BGM 偏电子激昂但经 ai-wind 选曲偏向纠偏，控均值不超旁白）

## 素材预判
assets_needed: []   # 纯 CSS/HTML 电紫光晕 + 粒子，无需外部素材；项目 avatar 已在 assets/avatars/

## 故事板
storyboard:
  narrative_template: "contrast-arc"    # ai-wind 分类 default_template（AI 项目盘点悬念揭晓弧）
  emotion_curve: [0.35, 0.55, 0.8, 1.0, 0.6, 0.4]   # grab 平起 → build 累积 → reveal 数据爆 → climax 安全新方向 → settle 共享脑/剪视频 → summon 收尾
  immersion_mode: "hyper-pace"          # ai-wind 恒满足 AI>50% → 电紫 #A855F7 快速剪辑+密集粒子
  humor_style: "dual-track"             # 双线幽默：旁白类比/反差吐槽 + 视觉
  character_presence: true              # ai-wind 启用码力角色（climax 必出）
  beat_mapping:
    grab: "hook（26万星数字锚 + AI 自主干活利益）"
    build: "superpowers（agentic 方法论，主推新面孔）"
    reveal: "airllm（top2 +1711 爆款数据，本地大模型反直觉）"
    climax: "uber-ADR（AI 安全新方向，Uber 部署，主推新面孔）"
    settle: "TencentDB（top3 团队共享脑）+ video-use（AI 自己剪视频，快速带过）"
    summon: "CTA（中性二选一互动）"

## 反直觉主线（贯穿全片，写入每项目 contrarian_angle）
- superpowers: 给 AI 装技能包+方法论，让 AI 自己干完整套活
- airllm: 4GB 显存普通电脑本地跑 70B 大模型（云端专业显卡集群的活）
- uber-ADR: AI agent 普遍裸奔，这个给它上安全锁（AI 安全新方向）
- TencentDB: 给团队多个 AI 装共享脑，谁学到大家都懂
- video-use: AI 写代码自动剪视频（手动剪辑的活）

## 方向
orientation: portrait        # 竖屏短视频
orientation_source: default  # ai-wind 默认竖屏
