# content.md — E08 段3 首层 Co-authored-by（终端演示核心段）

## 来源
- 脚本：`workspace/ai-landing-tutorial-series/E08-脚本.md` 段3（首层 Co-authored-by，~70s，终端演示）
- 数据源：coauthored.py（AI 代码占比三层识别算法之首层初筛）

## 核心知识点

### 首层识别：Co-authored-by trailer 初筛
- **最可靠信号**：AI 工具默认会在 commit message 末尾埋 `Co-authored-by:` trailer
- **首层初筛逻辑**：解析 commit message，匹配六个 AI 工具名 → 命中判 AI，置信度 1.0
- **六个 AI 工具名**：claude / copilot / cursor / chatgpt / codeium / gemini

### 误标缺陷（首层盲区）
- **VS Code Copilot 误标**：VS Code 的 Copilot 会对人手写的代码也自动加 `Co-authored-by` trailer
- **后果**：光靠首层，AI 代码占比会虚高（手写代码被误判为 AI 生成）
- **解决**：需要第二层风格学复核 + 第三层注册表组合判定（本段只讲首层及其缺陷）

### 终端示例（commit message 结构）
```
commit a1b2c3d
Author: Alice <alice@team.com>

    feat: add user profile API

    Co-authored-by: Claude <noreply@anthropic.com>
```
- `Co-authored-by: Claude <noreply@anthropic.com>` 这一行 trailer 是 AI 信号锚点

## 教学要点
1. Co-authored-by 是**首层**（不是"第一层"——禁用"第一"违禁词）
2. 六个工具名是穷举匹配列表
3. 首层有缺陷（VS Code Copilot 误标），所以占比会虚高 → 引出第二层风格学
4. 终端视觉要清晰展示 trailer 的金色高亮 + 工具名名单侧栏

## 风格
- 终端演示为主（深底 #0a0a0a + JetBrains Mono + 打字动画）
- 程序员/技术风（圆点红黄绿 + 等宽字体）
- 金色高亮 trailer（信号锚点）+ 红框警示误标缺陷
