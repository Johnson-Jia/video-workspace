# design.md — 视觉风格方向 + 故事板

## 风格
style: 暗色科技风
mood: 激烈紧凑，信息密集但有节奏

## 配色方向
color_direction:
  background: 深色暗调（接近纯黑 #0a0a12），叠加微弱网格纹理
  accent_cool: 霓虹青 #00D4FF / 翠绿 #00E5A0（用于技术说明、功能描述）
  accent_warm: 琥珀金 #FF8C32 / 金色 #FFD700（用于星标数据、排名、hook 数字）
  text: 白色主 + 浅灰辅（描述用灰色降低视觉权重）

## 配乐方向
music_mood: 科技/赛博/紧凑电子

## 素材预判
assets_needed: []

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.7, 0.5, 0.8, 0.9, 0.6, 0.4]
  immersion_mode: "hyper-pace"
  humor_style: "dual-track"
  character_presence: true
  beat_mapping:
    grab: "hook — 数字钩子：最高涨星+3600"
    build: "headroom — AI瘦身95%token"
    reveal: "ECC — 20万星震撼"
    climax: "hermes-webui + markitdown快速 — 涨星加速"
    settle: "flowsint — 网络安全跨圈 + VoxCPM快速"
    summon: "CTA"

## 方向
orientation: portrait
orientation_source: default

## 场景规划（6场景，预估35-45s）

### 场景1: hook（grab）— 5s
- 情感：震撼、好奇
- 内容：6月3日涨星最猛的几个项目，最高一天涨了近四千星
- 视觉：全屏大字「+3618」金色冲击 + 副标题日期

### 场景2: headroom（build）— 8s
- 情感：好奇、颠覆
- 内容：chopratejas/headroom，给AI输入瘦身95%token答案不变，Python，6.6K星
- 反直觉：AI处理的信息95%是冗余的
- 视觉：ProjectFullCard，冷色调，强调"60-95%压缩"数据

### 场景3: ECC（reveal）— 8s
- 情感：惊喜、震撼
- 内容：affaan-m/ECC，20万星AI Agent系统，让编程助手有直觉和记忆
- 反直觉：AI也有"肌肉记忆"
- 视觉：ProjectFullCard，「204K ★」金色大字突出

### 场景4: hermes-webui + markitdown（climax）— 8s
- 情感：激动、节奏加速
- 内容：hermes-webui +1700涨星加速；markitdown连续霸榜又涨3600（快速带过）
- 视觉：双项目快速切换，暖冷交替

### 场景5: flowsint + VoxCPM（settle）— 8s
- 情感：思考、多元
- 内容：flowsint可视化安全调查（跨圈）；VoxCPM无分词器语音克隆（快速带过又涨783）
- 视觉：安全主题用独特色调，节奏稍缓

### 场景6: CTA（summon）— 3s
- 情感：行动意愿
- 内容：关注我，下期见
- 视觉：简洁，频道名+关注引导
