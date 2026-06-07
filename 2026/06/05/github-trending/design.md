# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技
mood: 紧凑震撼

## 配色方向
color_direction:
  background: 深色暗调（近纯黑 #0a0a0f）
  accent_cool: 霓虹青/翠绿（用于技术展示场景）
  accent_warm: 金色/琥珀（用于 hook/排名/CTA 场景）
  text: 白色主 + 浅灰辅

## 配乐方向
music_mood: 科技/电子/紧凑

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.3, 0.6, 0.7, 1.0, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook"
    build: "headroom"
    reveal: "vtuber"
    climax: "spec-kit+cosmos"
    settle: "paddleocr"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default

---

## 场景设计

### Scene 0 — hook (3-4s)
- **类型**: hook
- **情感节拍**: grab
- **视觉焦点**: "95%" 大数字 + 反直觉文案
- **视觉意图**: 金色光晕冲击，暗底大字，全片最强视觉

### Scene 1 — headroom (7-8s)
- **类型**: solution
- **情感节拍**: build
- **项目**: chopratejas/headroom
- **8 层信息**:
  - 类别标签: "AI 减肥术"
  - 排名: #1
  - 项目名: headroom
  - 一句话描述: LLM 输入压缩，砍掉 95% token 答案不变
  - 语言: Python
  - 核心指标: +3142 ★/天 | 12.5K ★
  - 三词卖点: 压缩输入·保持质量·多端接入
  - 感性评语: AI 吃一口干一天的活
- **视觉意图**: 深蓝底 + 青色科技光晕，排名数字金色大号

### Scene 2 — Open-LLM-VTuber (4-5s)
- **类型**: features
- **情感节拍**: reveal
- **项目**: Open-LLM-VTuber
- **8 层信息**:
  - 类别标签: "离线 AI 人"
  - 排名: —
  - 项目名: Open-LLM-VTuber
  - 一句话描述: 本地 LLM 虚拟主播，完全离线运行
  - 语言: Python
  - 核心指标: +581 ★/天 | 9.6K ★
  - 三词卖点: 离线运行·语音打断·跨平台
  - 感性评语: 不花钱的 AI 主播
- **视觉意图**: 紫色光晕，快速带过，信息紧凑

### Scene 3 — spec-kit + NVIDIA/cosmos (8-10s)
- **类型**: features
- **情感节拍**: climax
- **项目 1**: github/spec-kit
  - 类别标签: "官方出品"
  - 排名: —
  - 项目名: spec-kit
  - 一句话描述: GitHub 官方 Spec 驱动开发工具
  - 语言: Python
  - 核心指标: 108.6K ★ | +321/天
  - 三词卖点: 官方背书·先写需求·开发革命
  - 感性评语: GitHub 这次站队了
- **项目 2**: NVIDIA/cosmos
  - 类别标签: "物理 AI"
  - 排名: —
  - 项目名: cosmos
  - 一句话描述: 英伟达物理 AI 平台，虚拟训练真实部署
  - 语言: Jupyter
  - 核心指标: 9.0K ★ | +133/天
  - 三词卖点: 虚拟训练·机器人·英伟达
  - 感性评语: 游戏引擎教机器人走路
- **视觉意图**: 双项目信息密集，左侧蓝色光晕 + 右侧绿色光晕

### Scene 4 — PaddleOCR + CTA (6-8s)
- **类型**: cta
- **情感节拍**: settle → summon
- **项目**: PaddlePaddle/PaddleOCR
- **8 层信息**:
  - 类别标签: "国产之光"
  - 排名: —
  - 项目名: PaddleOCR
  - 一句话描述: 百度开源 OCR，100+ 语言秒变结构化数据
  - 语言: Python
  - 核心指标: 79.9K ★ | +141/天
  - 三词卖点: 百度开源·百种语言·秒变数据
  - 感性评语: 图片拖进去就能用
- **视觉意图**: 暖金色收尾，频道名 + CTA

---

## 时长估算
- Scene 0: ~4s (35 字)
- Scene 1: ~8s (75 字)
- Scene 2: ~5s (47 字)
- Scene 3: ~8s (70 字)
- Scene 4: ~6s (52 字)
- **总计**: ~31s, 279 字
