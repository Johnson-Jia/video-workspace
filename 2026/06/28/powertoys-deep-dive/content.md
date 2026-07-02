# 内容摘要

## 来源
本地源码深度分析：`github-analyze/PowerToys`（microsoft/PowerToys 本地克隆）+ 源码 / 架构文档 / 隐私文档实证。完整分析见本目录 `analysis-report.md`。

## 核心主题
Microsoft PowerToys 深度解析——微软官方维护的 Windows 效率工具全家桶（30+ 工具）。核心架构哲学是**插件化**：一个调度核心（Runner）+ 一堆长得一模一样的标准化插件（Module），把 Windows 该有却没有的高频效率功能打包，统一设置、统一托盘、免费提供。

## 关键信息点
- **真实性**：微软官方仓库 microsoft/PowerToys，MIT 协议，9333 次提交，活跃维护
- **架构哲学**：Runner（主进程/托盘/模块加载/全局热键）统一调度 30+ Module DLL；每个模块实现统一接口（热键/名称/配置/启停/遥测/GPO）
- **四种模块接入方式**：纯逻辑 / 外部应用启动 / 资源管理器右键扩展 / 注册表注册
- **集大成哲学**：整合社区开源（Color Picker 源自社区项目、PowerToys Run 继承自开源启动器）+ 微软自研（FancyZones / Keyboard Manager）
- **旗舰工具**：FancyZones（窗口分区布局引擎，代码库最复杂、有模糊测试）、PowerToys Run（快速启动器，继承开源启动器的插件架构）、Mouse Without Borders（一套键鼠控制多台电脑）、Advanced Paste（AI 增强粘贴，接入外部 AI 服务）
- **技术栈**：C#（WPF / WinUI 3）+ C++（Win32），.NET 8
- **平台限制**：仅 Windows 10 1803+，不支持 macOS / Linux

## 数据
- 30+ 工具；3624 个 C# + 1241 个 C++/头文件 + 289 个 XAML 文件
- 系统要求：Windows 10 1803（2018年4月）及以上，x64 / arm64
- 遥测：v0.86 起默认关闭，事件全部开源透明

## 受众与适用性
普通人适用（官方渠道一键安装，按需开启几个工具即可）。多窗口办公 / 程序员 / 设计师 / 多机用户各有对应工具组合。

## 原始素材路径
- `analysis-report.md`（本目录，完整 10 章报告）
- `github-analyze/PowerToys/`（源码 + 文档）
