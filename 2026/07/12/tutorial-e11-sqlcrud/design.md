# E11 sqlcrud 段 · 设计文档（段5 sql-query + crud-gen，核心段，terminal）

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 55s
category: tutorial
segment: sqlcrud

## 视觉风格
- 主色：深蓝底 #0F172A
- 强调色：蓝 #60A5FA/#93C5FD（sql-query + 只读）+ 翠绿 #34D399/#6EE7B7（crud-gen + 分层生成）+ 金 #FBBF24/#FCD34D（安全护栏/收尾）+ 紫 #A78BFA/#C4B5FD（双工具对比）
- 字体：Inter（大字）/ Noto Sans SC（正文）/ JetBrains Mono（terminal/skill 名/SQL）
- 整体调性：双工具 terminal 演示（sql-query 三模式+护栏 / crud-gen 读表→分层生成）

## 情绪曲线 emotion_curve（5 点）
- 0.45（开篇：两个工具型 skill）
- 0.70（sql-query 只读查询 三模式）
- 0.82（安全护栏：SELECT only / SSH 隧道 / 租户隔离）
- 0.78（crud-gen 读表→分层生成）
- 0.62（高频工具 收尾）

## 沉浸模式 immersion_mode
data_reveal：terminal region 全 data-reveal=0（t=0 全显，不依赖 stagger 时序）

## 叙事模板 narrative_template
工具演示（overview → sql-query → guardrails → crud-gen → synthesis）
- Step 1（0-10s）：两个工具型 skill 总览
- Step 2（10-25s）：sql-query PostgreSQL 只读 + 三模式
- Step 3（25-38s）：安全护栏（SELECT only / SSH 隧道 / 租户隔离）
- Step 4（38-50s）：crud-gen 读表→分层生成 domain/dto/service/dao/controller
- Step 5（50-55s）：高频工具 收尾

## 场景规划（visual_phases）—— 多 phase（terminal）

### Phase 1（0-10s）：两工具总览
- 阶段标签「E11 · 两个工具型 · 核心段」
- 大字「两个工具型 skill」
- 双卡缩略（sql-query / crud-gen）

### Phase 2（10-25s）：sql-query terminal
- terminal 框 + sql-query 命令 + 三模式

### Phase 3（25-38s）：安全护栏
- 三护栏（SELECT only / SSH 隧道 / 租户隔离）

### Phase 4（38-50s）：crud-gen terminal
- terminal 框 + 读表 → 分层生成（domain→dto→service→dao→controller）

### Phase 5（50-55s）：高频工具 收尾

## 布局规则（⛔ terminal 段 E10 教训）
- 多 .phase sqlcrud-scene
- .phase.sqlcrud-scene { justify-content: flex-start !important; padding-top: 188px; padding-bottom: 60px; }（内容从顶排列，过 safe_area gate content_y≥180）
- .phase.sqlcrud-scene > .region { flex-shrink: 0; }
- terminal region 全 data-reveal=0（t=0 全显）
- terminal 内容精简（9-11 行内，避免溢出安全区）
- 字号 ≥32px

## 配色规范
- 渐变文字：同色系亮端（蓝/绿/金/紫），禁白端点 / 禁暗端
- text-shadow：深蓝 rgba(30,41,59,0.32)，alpha ≤ 0.32
- terminal 框：深色底 rgba(15,23,42,0.92) + 边框蓝/绿

## bg 组件
dark_cipher（深靛紫底 + 监控扫描 + 心跳脉冲，匹配「终端/数据/查询」主题）— 保留 `<!-- bg-component: dark_cipher -->`
注：dark_cipher 自带扫描线属 bg 层；fx 层禁划过类

## 禁忌
- 禁划过类 fx（scan/stream/beam）
- 禁「第一」（用「其一/首」）
- 禁 CSS class 切换可见性
- 禁 opacity 入场
- 禁暗端渐变
- 禁创作指令泄露
- 禁「9」（用「九」）
