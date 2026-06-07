# design.md — OpenTalking 深度解析

## 风格
style: 暗色科技
mood: 理性探索，穿插惊喜

## 配色方向
color_direction:
  background: 深色暗调（接近纯黑，带微弱蓝紫渐变）
  accent_cool: 霓虹青/翠绿（用于架构/技术场景）
  accent_warm: 琥珀金（用于数据亮点/星标数字）
  text: 白色主 + 浅灰辅
  special: 数字人主题可用柔和蓝紫光晕做氛围层

## 配乐方向
music_mood: 科技/电子，中等节奏，不喧宾夺主

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.4, 0.55, 0.75, 0.9, 0.5, 0.35]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: false
  beat_mapping:
    grab: "hook"
    build: "what, pain-point"
    reveal: "architecture, pipeline"
    climax: "models, code-quality"
    settle: "risks, vision"
    summon: "cta"

## 场景规划（9场景，~180s）
scenes:
  - id: hook
    title: "Hook — 48天近千星"
    duration: 12
    content: "数字人编排框架，48天拿到近千星"
    beat: grab

  - id: what
    title: "什么是 OpenTalking"
    duration: 20
    content: "全链路编排框架定位：STT→LLM→TTS→audio2video→WebRTC"
    beat: build

  - id: pain-point
    title: "市场痛点"
    duration: 18
    content: "闭源贵 vs 开源难用，OpenTalking 的差异化"
    beat: build

  - id: architecture
    title: "架构解析"
    duration: 25
    content: "Provider/Registry/Protocol 三层架构，51行核心注册表"
    beat: reveal

  - id: pipeline
    title: "全链路管线"
    duration: 22
    content: "从语音识别到 WebRTC 播放的完整链路拆解"
    beat: reveal

  - id: models
    title: "模型与部署"
    duration: 25
    content: "6种模型 + 4种部署模式，从Mock到OmniRT渐进式"
    beat: climax

  - id: code-quality
    title: "源码质量"
    duration: 22
    content: "42K行Python + 35个测试文件 + CI/CD + 双语文档"
    beat: climax

  - id: risks-vision
    title: "风险与愿景"
    duration: 22
    content: "Bus Factor低/48天太年轻 + 开发者长期路线图"
    beat: settle

  - id: cta
    title: "CTA"
    duration: 8
    content: "关注GitHub星探，下期见"
    beat: summon

## 方向
orientation: portrait
orientation_source: default
