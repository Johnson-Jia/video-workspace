# design.md — E08 段2.2 微服务闭环·后半+人机边界（流水线）

## orientation

orientation: landscape
orientation_source: category_hint
aspect_ratio: "16:9"
resolution: "1920x1080"

> 教程横屏。微服务闭环后半：后三专项 Agent（自检查→测试→部署 + 测试不过回传闭环箭头）+ 数据底座（RAG 向量库 + 代码知识图谱）+ 人机边界（人定义需求+审核 / AI 执行全流程）+「先跑通阶段零到五再演进，否则空中楼阁」警示条收尾。

## tutorial_reveal_mode

**tutorial_reveal_mode: true**

> §6.16：单 phase + 多 region + data-reveal。1 场景 4 region。标题（左对齐）+ 后三 Agent 流水线（自检查→测试→部署，测试不过回传代码生成 Agent 闭环箭头）+ 数据底座双卡（RAG 向量库 + 代码知识图谱）+ 人机边界左右对比 + 警示条收尾。布局 space-between 撑满画布。

## style

流水线流程图技术风。标题左对齐 + 后三 Agent 节点横向连线（青/蓝/绿渐进 + 测试不过红色回传闭环箭头）+ 数据底座双卡（RAG 业务数据 / 代码知识图谱代码结构，金色边强调底座角色）+ 人机边界左右对比卡（人=决策 / AI=执行，蓝青对照）+ 警示条（橙金边 + 空中楼阁风险）。冷色优先（青/蓝/绿），节点圆角胶囊。

## color_direction

深底 + 五色（青=流水线主轴 / 蓝=数据底座+人 / 绿=测试通过 / 红=测试不过回传 / 金=警示+数据底座锚点）：

| 用途 | 色值 | 角色 |
|------|------|------|
| 流水线主轴 | `#22D3EE` | 青色（自检查/部署节点 + 连线） |
| 数据底座 | `#3B82F6` | 蓝色（RAG + 代码图谱卡片） |
| 测试通过 | `#10B981` | 绿色（部署成功路径） |
| 回传闭环 | `#F87171` | 红色（测试不过 → 回传代码生成） |
| 警示+底座锚点 | `#FBBF24` | 金色（阶段三建 / 空中楼阁警示） |
| 主背景 | `#08080f` | 深蓝黑主底（noise_field 噪点纹理叠层） |

## immersion_mode

教程横屏 reveal — 1 场景 + 4 region（标题+后三流水线+数据底座+人机边界，警示条嵌尾）。region 按 data-reveal 时间点淡入 + 方向。后三 Agent 节点依次连线 reveal + 测试回传箭头 pulse + 数据底座双卡并排 reveal + 人机边界左右对照 reveal。

## bg_component

`noise_field`（SVG 噪点纹理 + 冷调光斑 + 悬浮尘埃，冷色科技感 + 与 E08 其他段做 bg 差异：why=hex_grid / coauthored=contour_lines / microservice-2=noise_field；visual_types 含 noise/glow/gradient/particles，符合 R-R-009 要求非 {gradient,glow,grid} 单一组件；与 contour_lines 异质，避开等高线）

## fx_strategy

冷色优先（青/蓝/绿），fx-aura 静态光晕衬底（禁划过类 scan/stream/beam），≥3 元素/场。流水线节点边缘冷色光晕呼应技术氛围 + 测试回传箭头处红光晕脉冲（alpha≤0.22）。fx-blink 锚点分布于节点 + 数据底座 + 人机边界对照点。
