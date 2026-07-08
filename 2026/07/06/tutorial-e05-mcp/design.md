# design.md — E05 段6 MCP 网关 + 跳过提示

## orientation

orientation: landscape
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。上半 MCP 网关流程卡（CLI 优先），下半「跳过判断」决策卡（金边强调）。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。4 region（标题 + MCP 网关 + CLI 优先 + 跳过决策卡）。

## color_direction

深蓝 hex_grid 底 + MCP 紫（网关）+ CLI 蓝（优先）+ 跳过决策金（边框强调）+ 跳过条件绿（grep 替代）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 背景 | hex_grid | 六边网格（基础设施结构感） |
| 标题 | `#FCD34D` | 金色 |
| MCP 网关 | `#C4B5FD` | 紫色（封装企业服务） |
| CLI 优先 | `#93C5FD` | 蓝色（命令行优先） |
| 跳过决策 | `#FCD34D` | 金色（金边强调） |
| grep 替代 | `#6EE7B7` | 绿色（降级方案） |

## 视觉区域范式（1 场景）

- **region1 标题**（reveal 0，fade）：标题「MCP 网关」+ 副标「封装企业服务 + 这集可以跳过」
- **region2 MCP 网关流程**（reveal 4，left）：企业内部服务 → MCP 零代码封装 → Agent 调用（3 节点横向流程）
- **region3 CLI 优先提示**（reveal 20，top）：蓝色卡「命令行能搞定的别用 MCP · 定义常驻烧 token · gh/kubectl 优先」
- **region4 跳过决策卡**（reveal 38，fade）：**金边强调**「跳过判断 3 问：代码库大？项目多？业务复杂？→ 都否则跳过 / 用 grep+人审+git diff 替代」

## bg_component

`hex_grid`

## visual_type

`tutorial_mcp_skip`
