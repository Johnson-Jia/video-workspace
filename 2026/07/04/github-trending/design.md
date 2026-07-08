# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技赛博        # GitHub 分类默认暗色科技风
mood: 紧凑利落·反常识冲击  # caveman 反直觉钩子驱动，节奏快但不激昂

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（接近纯黑，深蓝/深紫渐变基底）
  accent_cool: 霓虹青/电蓝（#4DA8DA 系，用于开发工具场景 caveman/graphify/herdr）
  accent_warm: 琥珀橙（#FF8C32 系，用于 hook/astryx/romm/cs249r 的暖冷对比）
  text: 白色主 + 浅灰辅
  contrast_strategy: 双光晕暖冷对比——开发工具偏冷光（青蓝），应用/教材偏暖光（橙金），形成场景间视觉差异

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"            # caveman 反直觉省 token = 紧凑利落的力量感，几何无衬线匹配
    family: "Inter"
    weight: 900
    rationale: "工具/效率题材 + 反常识钩子，几何简洁字体传递'短小精悍'的视觉调性，与 caveman '少即是多' 主题呼应"
    fallback: "'Inter','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 低调科技衬底（clean-corporate 系，不抢旁白）
bgm_style_hint: 首选 clean-corporate / warm-editorial，避免 bold-energetic（github 分类 bgm_style：激昂配乐抢人声）

## 素材预判
assets_needed: []   # 纯 CSS/HTML 实现，无需外部素材；avatar 已在 assets/avatars/

## 故事板
storyboard:
  narrative_template: "contrast-arc"    # 反直觉钩子（caveman 省 token）→ 项目对比展开 → 收尾中性互动
  emotion_curve: [0.35, 0.5, 0.65, 0.85, 0.6, 0.4]  # grab 中等冲击 → build → reveal → climax（caveman 数据爆发）→ settle → summon
  immersion_mode: "contrast-arc"        # 项目类型分散（工具/UI/自托管/教材），非 AI>50%，按 immersion_mapping 用默认 contrast-arc
  humor_style: "dual-track"             # 旁白+视觉双线，build/reveal/settle 节拍注入类比幽默
  character_presence: true              # GitHub 分类启用码力角色
  beat_mapping:
    grab: "hook"                        # caveman 反直觉钩子
    build: "caveman"                    # 钩子主角展开
    reveal: "graphify"                  # 代码库变知识图谱（反常识揭示）
    climax: "herdr"                     # 终端多 AI 并行（高潮：开发者工具集大成）
    settle: "astryx, romm"              # 大厂设计系统 + 自托管游戏库（沉淀：跨领域应用）
    summon: "cs249r, CTA"               # 教材快速带过 + 中性互动收尾

## 6 项目场景规划（4-7 场景，标准模式）
# S1 hook (4s) — caveman 反直觉：穴居人说话省 65% token，纯钩子不含项目名
# S2 caveman (10s) — 钩子主角展开：Claude Code 技能，让 AI 短话省 token，单日涨 2851
# S3 graphify (9s) — 代码库变知识图谱
# S4 herdr (9s) — Rust 终端 agent 多路复用器
# S5 astryx (8s) — 大厂开源设计系统
# S6 romm + cs249r (10s) — 自托管游戏库 + ML 教材（双项目快速带过）
# S7 CTA (3s) — 中性互动「这6个工具你会试哪个」
# 总字数目标：250-380 字，时长 ~50s

## 方向
orientation: portrait
orientation_source: default
