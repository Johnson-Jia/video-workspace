# design.md — 视觉风格方向 + 故事板

## 风格
style: 科技赛博
mood: 震撼自豪

## 配色方向
color_direction:
  background: 深色暗调（接近纯黑）
  accent_cool: 霓虹青/翠绿（用于架构/how/comparison 场景）
  accent_warm: 金色/琥珀（用于 hook/capabilities/CTA 场景）
  text: 白色主 + 浅灰辅

## 配乐方向
music_mood: 科技/史诗感

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.6, 0.5, 0.7, 0.8, 0.9, 1.0, 0.7, 0.5, 0.5, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "narration-only"
  character_presence: false
  beat_mapping:
    grab: "hook"
    build: "what, how"
    reveal: "cap-v5, cap-vl, cap-struct"
    climax: "ecosystem"
    settle: "comparison, usecases"
    summon: "cta"

## 方向
orientation: portrait
orientation_source: default

## 场景规划（3分钟深度解析）
scenes:
  - id: hook
    duration: 12
    beat: grab
    topic: "81K Star / 6年 / 427贡献者 / 百度PaddlePaddle团队"
    contrarian_angle: "以为OCR只是文字识别？这是一个完整的文档AI引擎"
  - id: what
    duration: 15
    beat: build
    topic: "PaddleOCR不只是OCR工具，而是一整个OCR生态"
  - id: how
    duration: 20
    beat: build
    topic: "Pipeline编排架构：10条管线 + 13类模型，模型可换管线不变"
  - id: cap-v5
    duration: 18
    beat: reveal
    topic: "PP-OCRv5：100+语言识别，CPU就能跑，比v4提升13%准确率"
  - id: cap-vl
    duration: 18
    beat: reveal
    topic: "PaddleOCR-VL-1.6：0.9B参数VLM，OmniDocBench 96.33% SOTA"
  - id: cap-struct
    duration: 18
    beat: reveal
    topic: "PP-StructureV3：表格/公式/印章/图表，全要素结构化"
  - id: ecosystem
    duration: 18
    beat: climax
    topic: "全栈覆盖：MCP Server/LangChain/浏览器SDK/Go SDK/TS SDK"
  - id: comparison
    duration: 18
    beat: settle
    topic: "vs Tesseract/EasyOCR：中文精度/表格/公式/部署/生态全面领先"
  - id: usecases
    duration: 15
    beat: settle
    topic: "RAG预处理/AI Agent文档理解/批量数字化/浏览器端OCR"
  - id: cta
    duration: 10
    beat: summon
    topic: "pip install paddleocr / Apache 2.0 免费商用"
