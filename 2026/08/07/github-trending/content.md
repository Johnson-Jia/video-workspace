# 内容摘要

## 来源
GitHub Trending daily（2026-08-07，13 个项目，python_requests + gh_api 抓取）

## 核心主题
近 3 期连续 AI（superpowers / computer / TencentDB-Agent-Memory）后强制题材轮换，本期多元基建回归——身份认证 + Java 核心库 + 代码图谱 + agent 状态核，AI 占一半，避开"编码技能框架"同质品类。

## 关键信息点
- google/guava：Google 官方 Java 核心库，出道十几年仍涨星，Java 程序员工具箱标配（集合/缓存/并发），长青基建
- goauthentik/authentik：开源身份认证中台，登录账号自己管，支持主流单点登录协议（OIDC/SAML/LDAP），Web 管理 + Docker 一键，企业自建登录入口
- tirth8205/code-review-graph：给代码库建本地知识图谱，AI 审代码只读关键部分省上下文，MCP/CLI 接入，专治大仓库审查
- huangruiteng/loopx：AI agent 长期运行的状态内核，持久化目标 + 配额自动唤醒 + 证据日志 + 可验证交接，跨多种编码 agent 通用

## 数据（gh api 实时，2026-08-07）
| 项目 | 今日涨星 | 总星 | fork | watcher | 创建 |
|------|---------|------|------|---------|------|
| google/guava | +35 | 51.6K | 11.2K | 2323 | 2014 |
| goauthentik/authentik | +123 | 23K | 1.77K | 70 | 2019 |
| tirth8205/code-review-graph | +232 | 29K | 2.68K | 91 | 2026-02 |
| huangruiteng/loopx | +854 | 2.8K | 208 | 8 | 2026-05 |

## 选材决策
- 非 AI 候选池仅 authentik + guava（ChinaTextbook inactive 292 天 + 无 license + 教材版权敏感剔除；pdf-inspector 近 2 天禁选）
- AI 上限 2（gate ai_project_cap）：选 code-review-graph（代码图谱，角度独特）+ loopx（agent 状态核，角度独特），弃 agent-skills/mattpocock-skills（与 08-05 superpowers 同品类）
- 受众档位：A 档 1（authentik）/ B 档 1（code-review-graph）/ C 档 2（guava + loopx），C 档偏高但跨 4 领域不扎堆，差异化优先

## 反直觉角度（contrarian_angle，stage3 用）
- guava：十几年前的库今天还在涨星，Google 自己用的基建开源出来
- authentik：登录认证自己管，不依赖第三方身份服务
- code-review-graph：AI 审代码只读关键部分，不是全量塞进上下文
- loopx：AI agent 跑久了会失忆，它专门补这个

## 原始素材路径
raw_trending.json（13 项目全集）/ explor​ation_directive.yaml（exploit 模式）
