# 内容摘要

## 来源
脚本：workspace/ai-landing-tutorial-series/E13-脚本.md（段：注册中心，对应 demos/ai-test-frame 的 registry.py）

## 核心主题
注册中心模式——@register 装饰器把方法登记进全局表，调度器按 type 自动取 handler；类引用延迟解析（编码期类未定义完，运行期创建实例时再解析）；新增业务模块写完注册，调度器自动发现，零改调度器代码。

## 关键信息点
- 注册中心是这套框架的灵魂
- 写一个装饰器 register，把方法登记进全局表
- 调度器按类型自动取
- 关键细节：类引用延迟解析——装饰器执行时类还没定义完，那时取会拿到空
- 所以类引用放到调度器创建实例时再解析
- 好处：新增业务模块，写完注册，调度器自动发现，零改调度器代码
- 这是企业级测试框架提炼出来的核心模式

## 数据
- 一个装饰器 register（真实，来自 registry.py）
- 一个调度器自动发现（真实，来自 runner.py）
- 零改调度器代码（真实，registry 模式的好处）

## 视觉方向
registry.py @register 装饰器代码片段 + 调度器按 type 取 handler 流程图（type → registry.get → 延迟解析类 → 创建实例 → 调用方法）。深色科技底，冷色 fx。

## 原始素材路径
workspace/ai-landing-tutorial-series/E13-脚本.md
