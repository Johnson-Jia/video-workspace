# E09 pitfall 段 · 设计文档

## 元数据
orientation: landscape
resolution: 1920x1080
duration: 60s
category: tutorial
segment: pitfall

## 视觉风格
- 主色：深蓝底 #0F172A（沉稳科技感，承接 E09 系列）
- 强调色：红 #F87171/#FCA5A5（错误代码 + 九个月警示）+ 翠绿 #34D399/#6EE7B7（修复代码 + 外部健康检查）+ 暖金 #FBBF24（标题强调）
- 案例卡：左红 ❌ 错误（catch 吞 + handleSuccess）+ 九个月时间线 → 右绿 ✅ 修复（catch 重抛 + handleFail + 外部健康检查）
- 字体：Inter（大字标题）/ Noto Sans SC（正文）/ JetBrains Mono（代码/编号）
- 整体调性：红绿对比警示 + 真实 bug 复盘权威感

## 情绪曲线 emotion_curve（5 点）
- 0.55（点题「真实避坑 · 静默吞异常」）
- 0.75（❌ 错误代码：catch 吞 + handleSuccess）
- 0.80（九个月时间线警示）
- 0.65（✅ 修复：重抛 + handleFail + 外部健康检查）
- 0.55（写进规则收尾）

## 沉浸模式 immersion_mode
data_reveal：红绿对比案例卡 reveal stagger + 九个月时间线

## 叙事模板 narrative_template
真实避坑（intro → bad code → 9 months timeline → fix → ai rules）
- Phase 1（0-8s）：标题「真实避坑 · 静默吞异常」+ 副标「来自生产 bug 复盘」
- Phase 2（8-28s）：❌ 错误代码案例卡（catch 吞异常 + 无条件 handleSuccess）
- Phase 3（28-44s）：九个月时间线警示（SFTP 静默挂 9 个月 · 客户才发现）
- Phase 4（44-60s）：✅ 修复代码（catch 重抛 + handleFail + 外部健康检查）+ 写进规则

## 场景规划（visual_phases）

### Phase 1（0-8s）：标题 + 生产 bug 复盘标签
- 视觉：标题「真实避坑 · 静默吞异常」+ 标签「E09 · 生产 bug 复盘」
- 副标「最典型 · 来自生产」
- 大字渐变（红色同色系亮端）+ text-shadow 深蓝 rgba(30,41,59,0.32)

### Phase 2（8-28s）：❌ 错误代码案例卡
- 视觉：红色边框案例卡 + ❌ 图标 + 「静默吞异常」标题
- 错误代码块（黑底 + 红色高亮）：
  ```
  try { pushSftp(); }
  catch (Exception e) {
      // 吞掉异常 · 不抛出
  }
  handleSuccess(); // 无论如何 · 自报成功
  ```
- 红色警示：「任务自报成功 ≠ 真的成功」

### Phase 3（28-44s）：九个月时间线警示
- 视觉：九个月时间线（横向时间轴 + SFTP 任务图标 + 9 个月跨度）
- 每月节点（M1 M2 ... M9 灰色，最后 M9 红色「客户发现」）
- 红色警示：「SFTP 静默挂 9 个月 · 客户才发现」

### Phase 4（44-60s）：✅ 修复代码 + 写进规则
- 视觉：绿色边框案例卡 + ✅ 图标 + 「修复 + 外部健康检查」标题
- 修复代码块（黑底 + 绿色高亮）：
  ```
  catch (Exception e) {
      throw new RuntimeException(e); // 重抛
  }
  handleFail(); // 失败必须调
  // + 外部健康检查
  ```
- 底部：「写进规则 · AI 自动加载 · 同类不再重犯」
