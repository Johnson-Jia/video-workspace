# design.md — 第29周 GitHub 周榜（AI agent 体系化）

## 风格
style: 暗色科技·四组领域切片
mood: 紧凑专业·信息密度高

## 配色方向（描述性，不指定具体色值）
color_direction:
  background: 深色暗调（深蓝黑渐变基底，接近纯黑，每组领域切片用对应领域色微染）
  accent_cool: 霓虹青蓝（用于编码 Agent 组 + hook 数字锚点，#4DA8DA 系）
  accent_warm: 琥珀金（用于技能生态组 + CTA 召唤，#F9A825 系）
  accent_orange: 暖橙（用于安全工具组，强调"防御"警示感，#FF8C32 系，alpha 受控不刺眼）
  accent_teal: 青绿（用于应用办公组，A 档普通人可用的友好色，#34D399 系）
  text: 白色主 + 浅灰辅（深色底高对比，不依赖发光浮起）

> 领域色仅视觉：四组各有冷蓝/紫/橙/青绿领域色环+边框+渐变标题，旁白禁说颜色词，用领域名（编码 agent / 技能生态 / 安全工具 / 应用办公）引导。

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"
    family: "Inter"
    weight: 900
    rationale: "Q1 情感内核=信息密集的科技专业感，几何无衬线粗体承载周榜盘点权威感，与紧凑节奏匹配"
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
music_mood: clean-corporate / 低调科技衬底（GitHub 快播报定位，BGM 不抢旁白，避开 bold-energetic 电子激昂）

## 素材预判（可选）
assets_needed:
  - 14 个 owner avatar（已预下载到 assets/avatars/，ProjectFullCard 中部引用）
  - 四组领域色卡（Stage 6 ProjectFullCard 组件按领域色生成色环+边框）

## 故事板
storyboard:
  narrative_template: "hyper-pace"
  emotion_curve: [0.85, 0.55, 0.6, 0.65, 0.7, 0.5]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: true
  beat_mapping:
    grab: "hook（数字锚点：OfficeCLI 周涨近七千 + AI agent 刷屏）"
    build: "组1 编码 Agent（并行编排）"
    reveal: "组2 技能生态（Claude 技能市场）"
    climax: "组3 安全工具（AI 渗透+沙箱，讲防御）"
    settle: "组4 应用办公（A 档普通人可用）"
    summon: "趋势总结 + CTA（中性二选一+周次）"

> emotion_curve 说明：hook grab 高位 0.85（数字锚点冲击），四组 features 在 0.55-0.7 区间紧凑铺陈（信息密度优先，情绪不爆裂避免抢旁白），CTA summon 回落 0.5（中性互动不煽动）。曲线非均匀，匹配周榜快播报节奏。

## 方向
orientation: portrait
orientation_source: category_hint
