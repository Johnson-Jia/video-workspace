# 内容摘要

## 来源
教程合集 E13 段3「数据驱动」· 对应 demos/ai-test-frame（runner.py + data/cases.json）

## 核心主题
数据驱动调度：用例数据（data/）与执行代码（handlers/）彻底解耦，运营在 JSON 编步骤，开发写 handler，调度器按 type 路由（基础操作走字典 / 模块操作走注册中心），${变量} 跨步骤/跨用例传递。

## 关键信息点
- 用例在 data/cases.json，是纯粹的步骤 JSON（4 条用例：3 跑 1 关），运营在这里编不碰代码
- 代码在 handlers/ 目录，是具体业务实现
- 调度器 runner 读用例，按 type 路由
- 基础操作走字典：BASIC = {text/button/app/selector} → 基类方法
- 模块操作走注册中心：handler_registry.get(type) → 延迟解析类 → 实例化 → 调用方法
- 变量传递：步骤 _save_as 保存到 ctx，${变量名} 引用，步骤间用例间都能传
- 分工清晰：运营编步骤，开发写 handler

## 数据（来自 runner.py 源码 + data/cases.json）
- 4 条用例：3 跑（running=是）1 关（running=否，第 4 条）
- 基础操作 4 类：text/button/app/selector
- 用例 JSON 结构：{"type":"addproduct","val":"实物","_save_as":"pname"}
- ctx 上下文：跨步骤/跨用例变量池

## 原始素材路径
demos/ai-test-frame/runner.py + demos/ai-test-frame/data/cases.json
