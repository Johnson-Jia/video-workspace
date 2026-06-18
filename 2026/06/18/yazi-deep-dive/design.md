# design.md — Yazi 深度解析 视觉风格方向 + 故事板

## 风格
style: 暗色终端极客
mood: 理性解构·紧凑利落

## 设计推导（导演 5 必答题）
- Q1 情感内核：**理性/精准/极客**（主导，解构"最快"神话）+ 悬念惊喜（KGP 黑科技揭秘）。观众应感到"原来如此 + 这工程真深"。
- Q3 视觉手段：冷暖色温交替强化解构张力——暖橙承载"近4万星/主打快"的价值钩子，冷青承载"复制不比 cp 快/架构/协议"的理性分析，冷暖切换即"神话→真相"的情绪转折。
- Q4 相邻反差：S1 hook（暖橙大数字+大量留白）→ S2 架构（冷青+信息密集）色温+密度双反转；S5 快的真相（暖）→ S6 限制风险（冷）再次色温反转。
- Q5 焦点（竖屏 1080×1920）：焦点置中上部黄金分割点，架构图/数字/终端窗口居中纵列叠放。

## 配色方向（描述性，stage6 据此定色值）
color_direction:
  background: 接近纯黑的终端暗调（#0a0e14 系），叠加 40px 网格 opacity 0.04 数字纹理
  accent_cool: 霓虹青/翠绿（终端代码色，用于架构/协议/分析场景，理性深邃）
  accent_warm: 琥珀/橙金（用于 hook 数字/星标/CTA/数据强调，价值与紧迫）
  text: 白色主 + 浅灰辅（信息层级：数字/层名 > 正文 > 灰色标注）
  glow: 双光晕一暖（左上）一冷（右下），跟随焦点位置

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "理性/精准/极客"
    family: "JetBrains Mono"
    weight: 800
    rationale: "终端/代码项目的极客内核，等宽体强化代码感与冷静分析气质；中文 fallback 无衬线粗体保力量"
    fallback: "'JetBrains Mono','Noto Sans SC','PingFang SC','Microsoft YaHei',monospace"
  body:
    family: "Noto Sans SC"
    weight: 400
    rationale: "正文优先可读性，无衬线不抢戏"
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    rationale: "数据节拍器，等宽精准对齐，可信感"
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 暗色科技/紧凑电子（cyber electronic，脉冲节奏匹配 contrast-arc 的解构张力，不喧宾夺主）

## 素材预判
assets_needed: []
# 全部纯 CSS/HTML 实现：6 层架构分层条、终端窗口模拟、Unicode 坐标编码示意、滑动窗口预加载示意、限制清单、竞品中性对比表。无需外部图片/视频素材。

## 故事板
storyboard:
  narrative_template: "contrast-arc"
  emotion_curve: [0.7, 0.5, 0.85, 1.0, 0.55, 0.65]
  immersion_mode: "mega-update"
  humor_style: "narration-only"
  character_presence: true
  character_note: "单项目技术深度解析内容硬核（架构/协议/安全审计），码力角色仅 climax 结尾可选轻量闪现，技术主体不塞角色；幽默走旁白 1-2 处克制开发者文化梗（不踩负面/人身）"
  scene_count: 7
  duration_target: "52s（深度解析 45-60s 区间）"
  beat_mapping:
    grab: "S1 hook（近4万星终端文件管理器，主打快但复制大文件不比cp快）"
    build: "S2 零锁单线程架构哲学 / S3 31crate 6层分层架构图"
    reveal: "S4 图像预览KGP黑科技（Unicode编码坐标）/ S5 预加载真相（3页滑动窗口，快的真来源）"
    climax: "S5 后段核心能力集成（SFTP自实现/Lua插件/DDS跨实例）"
    settle: "S6 软硬件限制 + 安全风险（SSH不校验/插件无沙箱/测试欠债，诚实降温）"
    summon: "S7 适用场景 + 中性推荐 + 站队CTA"

## 方向
orientation: portrait
orientation_source: default
