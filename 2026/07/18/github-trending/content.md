# GitHub Trending 内容分析 — 2026-07-18

## 数据概况
- 采集 14 项目（**gh API 14/14 验证通过**，stars_total 准确；用户已 gh auth login 恢复）
- 活跃 13/14（93%），与 07-17 重叠 8、新增 6

## 排除项
- PrismML-Eng/Bonsai-demo（描述仅 "Bonsai Demo"，空壳嫌疑）
- anthropics/cwc-workshops（描述空）
- protocolbuffers/protobuf（+11 涨幅极低，老牌无看点）
- 永久排除表 ruvnet/RuView 未上榜

## 选题（6 个，标记 (入片)）

**前 4 涨幅（hallmark/OpenCut/build-your-own-x/DeepTutor）全是昨日 07-17 做过的** → 按 selection_strategy 霸榜一带而过。优先展开新上榜。结合 evolve（AI 题材 deprecated，控制 AI 类；高收藏率 Delta）。

| # | 项目 | 涨幅 | 受众 | 方向 | 处理 |
|---|------|------|------|------|------|
| 1 | docusealco/docuseal | +91 | A 普通可用 | 文档/法律（电子签名）| 新展开，跨圈 |
| 2 | PostHog/posthog | +438 | B 半可用 | 产品分析平台 | 新展开，跨圈 |
| 3 | RyanCodrai/turbovec | +280 | C 开发者 | 向量基建（Rust 量化）| 新展开 |
| 4 | tirth8205/code-review-graph | +74 | C 开发者 | 代码知识图谱 | 新展开 |
| 5 | Nutlope/hallmark | +1485 | C 开发者 | AI 技能（去 AI 味）| **霸榜一带过**（昨日重点）|
| 6 | OpenCut-app/OpenCut | +1074 | A 普通可用 | 创作工具（剪辑）| **霸榜一带过** |

**配比**：A 档 2（docuseal/OpenCut）+ B 档 1（PostHog）= 3/6 约一半 ✓；C 档 3（turbovec/code-review-graph/hallmark）。跨 6 圈（电子签名/产品分析/向量/代码/AI技能/剪辑）。AI 类 3/6（避开 deprecated 泛 AI 盘点）。霸榜 2 个一带而过维持连续性。

## 合规要点
- **app 名门禁（check_no_app_name）**：OpenCut 中文「开源视频剪辑工具」（禁 CapCut/剪映）；docuseal 中文「开源电子签名工具」（禁 DocuSign 品牌）。raw 原文保真锚点保留（content_ready 不查 app 名，但 narration/画面/文案必泛化）
- **品牌名**：hallmark 中文「主流 AI 编辑器」（不点 Claude Code/Cursor/Codex）；PostHog 不点竞品
- 无 URL/校名/人名/搜索引导；gh 已恢复故 stars_total 准确，无需"约"标注

## design
github 暗色科技风（冷色主 深蓝/深紫 + 暖强调 橙 #FF8C32/金）；text-shadow 极淡；渐变同色系禁白端点
