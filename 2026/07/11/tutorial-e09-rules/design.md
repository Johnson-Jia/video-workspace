# E09 rules 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 50s
category: tutorial
segment: rules

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，承接 E09 系列）
- 强调色：暖金 #FBBF24/#FCD34D（编号 + 红线警示强调）+ 冷蓝 #60A5FA/#93C5FD（AI 自动加载 + 标题）
- 警示色：红 #F87171/#FCA5A5（三条红线警示）+ 翠绿 #34D399（新代码强制 / 旧代码宽容对照）
- 终端窗口：黑底 #0D1117 + 红色边框（红线警示）+ 代码语法高亮（关键字蓝/字符串绿/注释灰）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码/编号）
- 整体调性：沉稳科技 + 终端代码权威感（三条红线 + AI 自动加载）

## 情绪曲线 emotion_curve（5 点）
- 0.50（点题「规范资产化 · 三条红线」）
- 0.65（红线1 租户隔离）
- 0.68（红线2 MQ finally 清理）
- 0.65（红线3 事务管理器）
- 0.55（AI 自动加载 + 新强旧宽收尾）

## 沉浸模式 immersion_mode
data_reveal：终端窗口三条红线代码 reveal stagger + AI 自动加载扫描动画

## 叙事模板 narrative_template
规范资产化（intro → 3 red lines → ai auto-load）
- Phase 1（0-8s）：标题「规范资产化」+ 副标「三条红线」
- Phase 2（8-44s）：终端窗口三条红线代码逐条 reveal（每条：编号 + 红线标题 + 代码块 + 注解）
  - 红线1：租户隔离 — 所有 SQL 每表必带 corp_id
  - 红线2：MQ/定时任务 finally 必须清理上下文
  - 红线3：事务必须指定管理器
- Phase 3（44-50s）：AI 自动加载 + 新代码强制 / 旧代码宽容

## 场景规划（visual_phases）

### Phase 1（0-8s）：标题 + 三条红线预告
- 视觉：标题「规范资产化」+ 标签「E09 · 三条红线」+ 副标「写进 rules · AI 自动加载」
- 三条红线编号预告（① ② ③ 红色编号）
- 大字渐变（暖金同色系亮端）+ text-shadow 深蓝 rgba(30,41,59,0.32)

### Phase 2（8-44s）：终端窗口三条红线代码 reveal stagger
- 视觉：终端窗口（黑底 + 红色顶部栏 + 三色圆点）内三条红线代码块逐条 reveal
- 每条红线：红色编号 + 红线标题 + 代码块（语法高亮）+ 注解（何时触发）
- 红线1：租户隔离
  ```
  // 1. 租户隔离：所有 SQL 每表必带 corp_id
  WHERE corp_id = ?
  ```
- 红线2：MQ/定时任务 finally 清理
  ```
  // 2. MQ/定时任务 finally 必须清理上下文
  finally { ExecutionContext.setContextMap(null); }
  ```
- 红线3：事务管理器
  ```
  // 3. 事务必须指定管理器
  @Transactional(transactionManager = "transactionManager")
  ```

### Phase 3（44-50s）：AI 自动加载 + 新强旧宽
- 视觉：AI 自动加载图标 + 「新代码强制 · 旧代码宽容」对照
- rules/ 目录路径 + AI 扫描动画
