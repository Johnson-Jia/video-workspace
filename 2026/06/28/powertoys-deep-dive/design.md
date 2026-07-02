# design.md — PowerToys 深度解析 视觉风格方向 + 故事板

## 风格
style: 系统极客科技        # 深色 + 模块化几何，呼应 PowerToys「系统级工具集」与「插件化架构」
mood: 专业 / 有序 / 紧凑    # 效率工具，信息密集但有秩序感

## 配色方向（描述性，具体色值由 Stage 6 定）
color_direction:
  background: 深蓝黑系（接近纯黑的深蓝，Windows 深色模式 + 系统底层感）
  accent_cool: Windows 品牌蓝 + 青绿（主强调色，体现微软官方身份与科技活力；避开 AI 紫色同质化）
  accent_warm: 琥珀金（仅 hook 数字与 CTA 少量点缀，提对比）
  text: 白色主 + 浅蓝灰辅

## 字体（三层 + voice 链接 Q1）
fonts:
  title:
    voice: "几何简洁"              # Q1 情感内核=专业/有序/极客 → 几何利落
    family: "Noto Sans SC"
    weight: 900
    rationale: "系统效率工具的专业利落感，几何无衬线最匹配；中文用 Noto Sans SC 黑体重量"
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  body:
    family: "Noto Sans SC"
    weight: 400
    fallback: "'Noto Sans SC','PingFang SC','Microsoft YaHei',sans-serif"
  data:
    family: "JetBrains Mono"
    weight: 700
    rationale: "代码/系统工具的等宽极客气质，数字与技术标识用等宽体增强可信度"
    fallback: "'JetBrains Mono','Consolas',monospace"

## 配乐方向
music_mood: 科技 / 电子（紧凑、有序、有推进感，匹配效率工具主题；不抢旁白）

## 素材预判
assets_needed: []       # 纯 CSS/HTML 实现模块化卡片、几何分区、工具图标（emoji/内联图形），无需外部素材

## 故事板
storyboard:
  narrative_template: "contrast-arc"   # Windows 缺什么 → PowerToys 补什么 → 震撼工具全景 → 旗舰高潮 → 沉淀用法/限制
  emotion_curve: [0.45, 0.55, 0.7, 0.92, 0.7, 0.5]   # grab→build→reveal→climax→settle→summon
  immersion_mode: "hyper-pace"         # 30+ 工具信息密集呈现，配 settle 节拍留呼吸
  humor_style: "narration-only"        # 深度解析以信息密度为主，幽默克制在旁白
  character_presence: false            # 深度解析纯视觉，不启用角色
  beat_mapping:
    grab: "hook（30+ 工具反直觉：微软亲手补齐 Windows 缺失）"
    build: "项目本质 + 真实性（微软官方/9333提交/MIT）"
    reveal: "架构哲学（Runner 调度 + Module 插件化 + 四种接入方式）"
    climax: "旗舰工具（FancyZones / PowerToys Run / Mouse Without Borders / Advanced Paste）"
    settle: "普通人怎么用 + 平台限制（仅 Windows）"
    summon: "CTA（中性二选一 + 项目名 microsoft/PowerToys）"

## 场景规划（约 11 场景，5-6 分钟，深度解析）
scenes_plan:
  - s1: hook — 「三十多个 Windows 该有却没有的功能，微软亲手做了，还免费」+ PowerToys 大字
  - s2: 项目本质 — 微软官方 Windows 效率工具全家桶（30+ 工具统一框架）
  - s3: 真实性 — 微软官方仓库 / 9333 次提交 / MIT / 活跃维护
  - s4: 架构哲学① — Runner 调度核心（托盘/模块加载/热键/设置桥接）
  - s5: 架构哲学② — Module 插件化（统一接口，新增工具=加一个 DLL）
  - s6: 四种接入方式 — 纯逻辑/外部应用/右键扩展/注册表
  - s7: 集大成 — 社区收编（取色器/启动器）+ 微软自研（布局/键盘）
  - s8: 旗舰 FancyZones — 窗口分区布局引擎（最复杂、有模糊测试）
  - s9: 旗舰 PowerToys Run + Mouse Without Borders — 启动器插件架构 + 一套键鼠控多机
  - s10: 旗舰 Advanced Paste + 工具全景 — AI 增强粘贴 + 其他工具速览
  - s11: 怎么用 + 限制 + CTA — 普通人按需开几个 / 仅 Windows / 中性提问 + 项目名

## 方向
orientation: portrait
orientation_source: user_explicit    # 用户在确认环节确认竖屏/抖音
