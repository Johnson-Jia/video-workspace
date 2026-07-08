# Stage 1 — 内容获取与分析

## 内容来源

- 数据源：`raw_trending.json`（github_trending.py daily + gh API 三源验证）
- 日期：2026-07-07
- 候选：16 个项目，15/16 活跃（94%），与昨日 9 重叠 7 新

## 选取结果（6 个，跨圈 + 受众平衡）

| # | 项目 | 涨星 | 受众 | 方向 |
|---|------|------|------|------|
| 1 | Zackriya-Solutions/meetily | +2494 | A | 本地会议记录（隐私不上云）|
| 2 | Leonxlnx/taste-skill | +1458 | C | 给 AI 装审美（agent skill）|
| 3 | asgeirtj/system_prompts_leaks | +1378 | C | 各大 AI 提示词合集 |
| 4 | steipete/CodexBar | +598 | A | macOS 菜单栏看 AI 用量 |
| 5 | alibaba/zvec | +382 | C | 阿里极速向量库 |
| 6 | karakeep-app/karakeep | +199 | A | 自托管 AI 书签 |

**受众配比**：A 档 3（meetily/CodexBar/karakeep）+ C 档 3，符合 audience_filter（A 约一半，C ≤ 一半）。

## 真实性验证（authenticity_verification）

6 项目 gh API 检查结果：

| 项目 | star/fork | watcher% | 账号年龄 | 判定 |
|------|-----------|----------|---------|------|
| meetily | 9.9:1 | 0.46% | 7 月 | ✅ 通过 |
| taste-skill | 14.7:1 | 0.28%⚠️ | 4.5 月 | ✅ 1 警告（skill 用完即走）|
| system_prompts_leaks | 6.1:1 | 1.15% | 14 月 | ✅ 通过（最健康）|
| CodexBar | 12.2:1 | 0.28%⚠️ | 8 月 | ✅ 1 警告（steipete 知名背书）|
| karakeep | 20.4:1 | 0.28%⚠️ | 2.4 年 | ✅ 1 警告（MohamedBassem 原 hoarder）|
| zvec | 16.4:1 | 0.47%⚠️ | 7 月 | ✅ 1 警告（阿里团队）|

**综合**：0 HARD，watcher 偏低是 skill/app 类共性（用完即走，star 但不 watch），配合 star/fork 正常 + 多人贡献 + 知名背书，无刷星信号。6 个全保留。

## 排除项

- 永久排除列表命中 1 个（ruvnet/RuView，WiFi 感知人体，虚假宣传/不可实现），按规则跳过不入选。
- meetily 虽然 last push 31 天前（active=false），但今天涨星 2494 是"老项目被重新发现"的真实爆火模式（非首日集中刷入），保留且为强钩子。

## 题材轮换（供 stage0.5 参考）

- 今日 trending 主题集中：Claude Code / AI agent skills（8+ 个候选）
- 本期跨圈平衡：会议 / AI 审美 / 提示词 / macOS 工具 / 向量库 / 书签，6 方向
- hook 方向：反直觉（meetily 不上云）+ 数字锚定（2494 涨星），符合优先级 1/2
- 结尾提问：中性互动（最想尝试哪个），符合 ending_question 2026-06-21 规则

## 合规

- 无违法工具 / 医疗资质 / 极限形容用语
- system_prompts_leaks 措辞中性（公开整理，不渲染猎奇）
