# 自建 CDN 缓存集群 — 开源方案选型与架构设计报告

> **版本**:v1.0
> **日期**:2026-06-18
> **适用场景**:纯自托管、不依赖任何云厂商的内容分发网络(CDN),承载**静态资源 / 视频 / 音频**等大文件的缓存与回源,支持多节点集群、缓存调度、回源策略,并具备向**多地区 / 多国家 / 多机房 / 多网络**扩展的能力。
> **目标技术栈**:Nginx · Java · Lua · OpenResty

---

## 目录

1. [背景与目标](#一背景与目标)
2. [核心结论(TL;DR)](#二核心结论tldr)
3. [开源候选项目全景](#三开源候选项目全景)
4. [技术选型对比矩阵](#四技术选型对比矩阵)
5. [架构与实现原理](#五架构与实现原理)
6. [最佳推荐组合(OpenResty + Java)](#六最佳推荐组合基于-openresty--java)
7. [全球架构扩展(多地区/多国家/多机房/多网络)](#七全球架构扩展多地区多国家多机房多网络)
8. [落地实施步骤](#八落地实施步骤)
9. [避坑指南](#九避坑指南)
10. [参考来源](#十参考来源)

---

## 一、背景与目标

### 1.1 需求

自建一套 CDN 缓存集群,实现:

- **静态资源**(JS / CSS / 图片 / 小文件)的边缘缓存与加速;
- **视频资源**(点播 VOD / 直播)的缓存、切片分发、拖拽体验;
- **音频资源**及各类大文件(安装包、镜像等)的缓存与回源;
- **多节点集群**,支持缓存调度、回源策略、故障转移。

### 1.2 硬约束

- **不依赖任何云厂商**:全部组件自托管、可部署在自有裸机 / IDC;
- **技术栈贴近团队**:Nginx · Java · Lua · OpenResty;
- **可扩展**:面向多地区、多国家、多机房、多网络运营商。

---

## 二、核心结论(TL;DR)

最佳落地路径是 **分层选型**:控制平面 + 数据平面(缓存引擎)+ 流媒体源站,全部用成熟开源组件拼装,避开有安全 / 许可证风险的项目。

| 诉求 | 首选方案 | 备选 |
|------|---------|------|
| 开箱即用的「自建 CDN 平台」(后台+DNS调度+多节点+监控一体) | **Apache Traffic Control**(ATS 引擎) | 自研 Nginx/OpenResty + 调度 |
| 只要纯缓存引擎,调度自己做 | **Apache Traffic Server**(CDN 旗舰)/ **Varnish**(内存极速) | Nginx、Caddy |
| 视频点播 / 直播(HLS/RTMP) | **SRS 做源站 + Nginx/ATS 做边缘切片分发** | ATS 的 slice 插件 |
| 超大文件 / 批量分发(镜像、安装包) | **Dragonfly**(P2P,减轻回源) | ATS parent 分层缓存 |
| ⛔ 曾经热门但要避开 | GoEdge(已转让 + 投毒,见 [第九节](#九避坑指南)) | 任何"开心版"破解 |

**结合团队技术栈的最终推荐**:边缘全部使用 **OpenResty(原生 `proxy_cache` + `slice` + Lua 控制)**,管理 / 调度 / 配置下发使用 **Java(Spring Boot)**,入口使用 **LVS + Keepalived**,源站使用 **MinIO + SRS**。详见 [第六节](#六最佳推荐组合基于-openresty--java)。

---

## 三、开源候选项目全景

### 3.1 完整 CDN 平台(控制平面 + 数据平面一体)

#### 🥇 Apache Traffic Control(ATC)— `apache/trafficcontrol`

- **许可证**:Apache 2.0(Apache 软件基金会顶级项目,前身是 Comcast 内部 CDN,原 `comcast/traffic_control`)
- **定位**:市面上**唯一**真正"开箱即用、组件齐全"的纯开源 CDN 控制平面
- README 原文:*"build a large scale content delivery network using open source... implements all the core functions of a modern CDN"*

| 组件 | 作用 | 技术栈 |
|------|------|--------|
| **Traffic Ops** | 管理 / 监控所有节点的 RESTful API,数据落 PostgreSQL | Go |
| **Traffic Portal** | Web 管理后台 GUI | AngularJS |
| **Traffic Router** | 用 **DNS + HTTP 302** 把用户重定向到"最近可用"的缓存节点(含地理路由) | Java(Tomcat) |
| **Traffic Monitor** | HTTP 轮询各缓存节点健康,喂给 Router 做调度 | Go |
| **Traffic Stats** | 实时指标,存 InfluxDB 用于图表 / 告警 | Go |
| **T3C(cache-config)** | 配置自动下发 / 同步到缓存节点 | Go |
| **Grove** | 可选的 Go 语言缓存代理 | Go |
| **CDN-in-a-Box** | ⭐ 一键沙箱环境,`docker-compose` 起一套完整 CDN | — |

- 缓存层默认是 Apache Traffic Server,blueprint 里有 `varnish-support.md`,可换 Varnish。

### 3.2 缓存引擎 / 数据平面(只做缓存 + 回源,调度自己搞)

| 项目 | 仓库 | 许可证 | 定位 |
|------|------|--------|------|
| **Apache Traffic Server** | `apache/trafficserver` | Apache 2.0 | **CDN 级**缓存代理,Yahoo / Akamai / Wikimedia 在用;C++ |
| **Varnish Cache** | `varnishcache/varnish-cache` | BSD | 内存型 HTTP 加速器,**Fastly CDN 的内核**,VCL 配置 |
| **Nginx** | `nginx/nginx`(社区版) | BSD-2 | 最通用的反代 + `proxy_cache`,部署量最大 |
| **Caddy** | `caddyserver/caddy` | Apache 2.0 | Go 写,自动 HTTPS,适合小规模自托管 |

### 3.3 流媒体源站(视频 / 音频专用)

#### SRS(Simple Realtime Server)— `ossrs/srs`

- 国产开源流媒体服务器,协议覆盖 **RTMP / WebRTC / HLS / HTTP-FLV / SRT / GB28181**
- ⚠️ **关键限制(官方文档确认)**:SRS Edge 集群**只支持直播流(RTMP / HTTP-FLV)**,**不支持 HLS 切片分发**——HLS 必须用 Nginx 或 ATS 做边缘分发。

### 3.4 大文件 P2P 分发

#### Dragonfly — `dragonflyoss/dragonfly`(阿里出品)

- **CNCF 毕业项目**(最高成熟度),Apache 2.0
- 架构:`manager`(管理 + 控制台)+ `scheduler`(P2P 调度)+ `client/dfget`,Go 编写
- 用途:镜像 / AI 模型 / 大文件 P2P 分发,大幅降低回源带宽
- ⚠️ 视频流不是它的主战场,它解决的是"一次性大文件高效分发"

---

## 四、技术选型对比矩阵

| 维度 | Apache Traffic Control | Apache Traffic Server | Varnish | Nginx | Caddy | Dragonfly | SRS |
|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| ⭐ Star 量级(约) | ~800 | ~2.5k | ~3.5k | ~25k | ~60k | ~2.8k | ~26k |
| 许可证 | Apache 2.0 ✅ | Apache 2.0 ✅ | BSD ✅ | BSD ✅ | Apache 2.0 ✅ | Apache 2.0 ✅ | MIT ✅ |
| 主语言 | Go / Java | C++ | C | C | Go | Go | C++ |
| 带管理后台 / 调度 | ✅ 完整 | ❌ | ❌ | ❌ | ❌ | ✅(P2P 调度) | 部分 |
| 多节点 / 分层缓存 | ✅(Router + T3C) | ✅ `parent.config` | ❌(需自组) | ❌(需自组) | ❌ | ✅ P2P | ✅(直播) |
| 视频 Range / 切片 | ✅(ATS 插件) | ✅ slice / range | ✅ | ✅ | ✅ | ⚠️ | ✅(源站) |
| 学习曲线 | 较陡 | 中 | 中(VCL) | 低 | 极低 | 中 | 中 |
| 生产背书 | Comcast | Wikimedia / Akamai | Fastly | 极广泛 | 中小规模 | 阿里 | 腾讯 / 哔哩 |

> Star 数据为公开仓库量级估算,精确值请以 GitHub 实时为准。

---

## 五、架构与实现原理

### 5.1 分层缓存(edge → mid-tier → origin)

真正 CDN 的核心是**多级缓存**。Apache Traffic Server 用 `parent.config` 原生支持父子分层:边缘节点未命中 → 回源到中层缓存 → 再回源站。这样回源带宽被层层收敛,这是单机 Nginx `proxy_cache` 给不了的。ATC 的 **T3C** 组件负责把分层拓扑配置自动同步到所有节点。

### 5.2 视频 / 大文件缓存的命脉:Range 与切片

普通代理缓存遇到视频拖拽(HTTP Range 请求)会缓存爆,因为每个字节区间算独立对象。标准答案有两个:

- **Apache Traffic Server** 的插件:`cache_range_requests`(正确缓存 Range)、`slice`(大文件切块缓存)、`background_fetch` / `prefetch`(预热);
- **Nginx 原生 `ngx_http_slice_module`**:把大文件切成固定大小块缓存,拖拽 / 断点都不怕(标准编译自带)。

### 5.3 调度机制

- **ATC 走 DNS + HTTP 302 调度**:`Traffic Router` 根据用户地理位置(内置 GeoIP)和节点健康状态(Traffic Monitor 上报),用 DNS 解析或 302 跳转把用户导到最优边缘节点。这正是商用 CDN 的同款机制。
- ⚠️ **ATS 的内置 clustering 在 v8 已移除**——多节点不再靠内置集群协调,而是靠外部配置管理(Ansible / Chef 或 ATC 的 T3C)同步。务必注意版本,否则会找错文档。

### 5.4 流媒体的"合并回源"

SRS Edge Cluster(直播场景)支持**合并回源**:同一路流无论多少观众,边缘只向源站拉一次。HLS 场景则由 Nginx / ATS 边缘做切片缓存达成同样效果。

---

## 六、最佳推荐组合(基于 OpenResty + Java)

> 结合团队技术栈(Nginx · Java · Lua · OpenResty),OpenResty 是这一场景的天然首选。核心铁律:**把"缓存"交给 Nginx 原生 C 模块(久经考验),Lua 只做轻量控制,绝不把缓存逻辑塞进 Lua**——稳就稳在这里。

### 6.1 核心思路:控制 / 数据平面分离

| 平面 | 选型 | 技能契合 |
|------|------|---------|
| **数据平面**(边缘缓存 + 回源) | **OpenResty**(Nginx + LuaJIT) | ✅ |
| **控制平面**(管理 + 调度 + 下发) | **Java(Spring Boot)** | ✅ |
| 调度 / 负载均衡 | OpenResty 内 `balancer_by_lua` + 健康检查 | ✅ Lua |
| 监控 | OpenResty 暴露 metrics → Prometheus → Grafana | 通用 |

### 6.2 整体架构(单机房版)

```text
                         [ 用户请求 ]
                              │
              ┌───────────────┴───────────────┐
              │  LVS / HAProxy + Keepalived    │  ← 4层LB + 高可用(入口)
              └───────────────┬───────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ┌────┴────┐           ┌────┴────┐           ┌────┴────┐
   │边缘节点1│           │边缘节点2│           │边缘节点N│   ← 数据平面
   │OpenResty│           │OpenResty│           │OpenResty│     (扛流量)
   │proxy_   │           │proxy_   │           │proxy_   │
   │cache    │           │cache    │           │cache    │
   │+slice   │           │+slice   │           │+slice   │
   │+Lua控制 │           │+Lua控制 │           │+Lua控制 │
   └────┬────┘           └────┬────┘           └────┬────┘
        │   一致性哈希路由(同一 URL 固定到某节点,命中率最高)
        └─────────────────────┼─────────────────────┘
                              │ 回源(未命中)
                    ┌─────────┴─────────┐
                    │  中层 OpenResty    │  ← 可选分层(类 ATS parent)
                    │  或直接源站        │
                    └─────────┬─────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   MinIO/文件源(静态)   SRS源站(视频/直播)   Java文件服务
                              │
                    ┌─────────┴─────────┐
                    │ Java 控制平面      │  ← Spring Boot
                    │ 域名/证书/调度/下发 │     (自研)
                    │ 配置生成 + 推送     │
                    └─────────┬─────────┘
                              │
                    [ Prometheus + Grafana ]
```

**控制平面 ↔ 数据平面通信**:Java 生成 nginx conf + Lua 配置 → 通过 HTTP API 推送到各边缘节点(或边缘定时拉取,更稳)→ `nginx -s reload` 热加载,**全程不中断**。

### 6.3 组件清单

| 层 | 组件 | 用途 | 备注 |
|----|------|------|------|
| 入口 | **LVS + Keepalived**(或 HAProxy) | 四层负载 + VIP 高可用 | 跨机房必备 |
| 边缘缓存 | **OpenResty** | 缓存 + 回源 + Lua 控制 | 核心 |
| 缓存优化 | Nginx 原生 `slice` 模块 | 大文件 / 视频切片缓存 | 原生自带 |
| 缓存优化 | Nginx 原生 `proxy_cache_lock` 等 | 合并回源、故障兜底 | 见 6.4 |
| Lua 库 | `lua-resty-upstream-healthcheck` | 节点健康检查 | OpenResty 官方 |
| Lua 库 | `lua-resty-core` / `lua-resty-lrucache` | 动态路由、热点缓存 | 官方 |
| Lua 库 | `lua-resty-limit-traffic` | 限流 / 防盗链 | 官方 |
| 源站(静态 / 音频) | **MinIO**(对象存储)或 NFS | 源文件 | 纯自托管 |
| 源站(视频 / 直播) | **SRS** | HLS / RTMP 源站 | 只做源站,边缘仍是 OpenResty |
| 控制平面 | **Spring Boot + PostgreSQL** | 管理后台 / 调度 / 下发 | 自研 |
| 大文件加速(可选) | **Dragonfly** | P2P 分发层 | 镜像 / 超大包场景 |
| 监控 | `lua-resty-prometheus` → Prometheus → Grafana | 指标 + 图表 | 通用 |

### 6.4 核心配置示例

#### (1) 缓存定义

```nginx
# nginx.conf
proxy_cache_path /data/cache levels=1:2
                 keys_zone=mycache:200m    # 共享内存(键),200MB 约可放 100 万 key
                 max_size=500g              # 磁盘缓存上限
                 inactive=7d                # 7 天没访问就清
                 use_temp_path=off;         # 少一次拷贝,性能更好
```

#### (2) 静态资源(稳的基本盘)

```nginx
location / {
    access_by_lua_block {
        -- 在这里做:动态缓存键、限流、防盗链、灰度、动态源站选择
        -- 示例:去掉无意义的 query 参数,提升命中率
        local args = ngx.var.args
        -- ... Lua 控制逻辑 ...
    }

    proxy_cache mycache;
    proxy_cache_key "$scheme$request_method$host$request_uri";  # 也可由 Lua 动态设置
    proxy_cache_lock on;            -- ★ 合并回源:并发未命中时只回源 1 次(防击穿)
    proxy_cache_lock_timeout 10s;
    proxy_cache_use_stale error timeout updating http_500 502 503 504;  -- ★ 源站挂了用旧缓存兜底
    proxy_cache_background_update on;  -- ★ 后台异步刷新,用户永远拿到快的
    proxy_cache_valid 200 206 302 12h;
    proxy_cache_valid 404 1m;
    add_header X-Cache-Status $upstream_cache_status;  -- HIT/MISS 一目了然

    proxy_pass http://origin_upstream;
}
```

#### (3) 视频 / 大文件(原生 slice 模块——拖拽、断点都不怕)

```nginx
location /video/ {
    slice 1m;                                   -- ★ 切成 1MB 块缓存,Range 各自缓存不互相覆盖
    proxy_cache mycache;
    proxy_cache_key "$uri$is_args$args$slice_range";  -- ★ key 必须带 slice_range
    proxy_set_header Range $slice_range;        -- 把切片范围透传给源站
    proxy_cache_valid 200 206 30d;
    proxy_cache_lock on;
    add_header X-Cache-Status $upstream_cache_status;
    proxy_pass http://origin_upstream;
}
```

> `ngx_http_slice_module` 是 **Nginx 原生模块**,标准编译就带,不需要 ATS 也能完美处理视频拖拽——正好留在熟悉的 Nginx 栈里。

#### (4) 多节点动态负载 + 健康检查(Lua)

```nginx
init_worker_by_lua_block {
    -- 初始化 upstream 列表(可从 Java 控制平面动态拉取)
}
```

配合 `lua-resty-upstream-healthcheck` 自动剔除故障节点。配置由 Java 控制平面下发。

### 6.5 多节点缓存共享(关键难点)

Nginx 自建 CDN 与"单机 Nginx"的本质区别,三招解决(组合用):

| 招式 | 做法 | 效果 |
|------|------|------|
| **一致性哈希路由** | 网关层 `balancer_by_lua` 按 URL 哈希固定到某边缘节点 | 同一资源只缓存于 1 个节点,命中率最高、磁盘不浪费 |
| **合并回源** | `proxy_cache_lock on` | 即使哈希失效,并发请求也只回源 1 次 |
| **分层缓存** | 边缘未命中 → 中层 OpenResty → 源站 | 回源带宽层层收敛,类 ATS parent 模式 |
| **热点兜底**(可选) | Redis + `lua-resty-lock` 缓存极热小对象 | 防冷启动击穿 |

**生产推荐:一致性哈希 + `proxy_cache_lock`**,覆盖 90% 场景,简单且稳。规模上来再加中层。

### 6.6 为什么不选别的

- **不选 Apache Traffic Control**:功能最全,但控制平面是 Java + Go + 多组件,缓存引擎是 ATS(C++),**全是团队不熟的栈**,运维和学习成本高。自己的 Java + OpenResty 组合能覆盖它 80% 能力,且完全掌控。
- **不选 Varnish**:快,但 VCL 不是 Lua,且内存型不适合大文件 / 视频(磁盘缓存更合适)。
- **不选 GoEdge**:已投毒,⛔。

---

## 七、全球架构扩展(多地区/多国家/多机房/多网络)

### 7.1 结论

架构理念(控制 / 数据平面分离)天然支持横向扩展到全球。第六节的"单机房最小可用版"要扩展到多地区 / 多国家 / 多机房 / 多网络,需再补 **3 个关键层**:

| 维度 | 单机房版够不够 | 要补什么 |
|------|:---:|------|
| 多机房(同城 / 异地) | ❌ LVS / HAProxy 只管单机房内 | 跨机房分层回源 + 专线 |
| 多国家 | ❌ 无地理调度 | **智能 DNS / GSLB**(最关键) |
| 多地区 | ❌ 无地域路由 | 智能 DNS + 区域故障域隔离 |
| 多网络(多 ISP / 多线路) | ❌ 无运营商感知 | 多线路 IP + 按运营商调度 |
| 跨国网络不可靠 | ❌ Java 直连每个节点 | 本地配置 Agent + 异步最终一致 |

**核心:多机房 CDN 的灵魂是「智能 DNS 调度层(GSLB)」**——单机房方案里被 LVS 替代,但 LVS 做不了跨地域 / 跨运营商调度。补上 GSLB,前面的组合即可无缝升级成全球架构。

### 7.2 全球架构(升级版)

```text
                           [ 全球用户 ]
                               │
               ┌───────────────┴────────────────┐
               │  ★ 智能 DNS / GSLB              │  ← 新增,灵魂层
               │  CoreDNS + GeoIP / PowerDNS     │     按地理位置 + 运营商解析
               │  调度策略由 Java 控制平面下发     │     支持 DNS + HTTP 302 双调度
               └───────────────┬────────────────┘
                               │
       ┌───────────────────────┼───────────────────────┐
       │  中国区(电信/联通/移动)  │  北美区        │  欧洲区
       │                        │                │
   ┌───┴────────┐          ┌────┴────┐      ┌────┴────┐
   │ LVS+Keepalived│        │LVS+VIP  │      │LVS+VIP  │  每机房入口 + 高可用
   │ (多线路多IP) │        │         │      │         │
   └───┬────────┘          └────┬────┘      └────┬────┘
   ┌───┴────────┐          ┌────┴────┐      ┌────┴────┐
   │ 边缘OpenResty│        │边缘OR×N │      │边缘OR×N │  各机房数据平面
   │  集群 ×N     │        │         │      │         │  (proxy_cache + slice + Lua)
   └───┬────────┘          └────┬────┘      └────┬────┘
       │ 未命中回源              │                │
   ┌───┴────────┐          ┌────┴────┐      ┌────┴────┐
   │ 中层OpenResty│        │中层OR   │      │中层OR   │  各机房中层(收敛回源)
   │  (本机房)    │        │         │      │         │
   └───┬────────┘          └────┬────┘      └────┬────┘
       │     跨机房专线 / SD-WAN 回源(走优化链路,不走公网)
       └────────────────────────┼──────────────────┘
                                │
                   ┌────────────┴────────────┐
                   │ 中心源站(主备)           │  或:各区域独立源站
                   │ MinIO 集群 + SRS + 文件   │  (合规要求数据不出境时)
                   └────────────┬────────────┘
                                │
       ┌────────────────────────┴───────────────────┐
       │  Java 全球控制平面                          │
       │  + 各机房本地 Agent(应对跨国网络抖动)       │
       │  + 统一配置 / 调度策略 / 全球监控(Prometheus 联邦)│
       └────────────────────────────────────────────┘
```

### 7.3 四个维度逐个拆解

**1) 多机房**
- 每个机房一套**完整的 边缘 + 中层 OpenResty**,前面 `LVS + Keepalived` 做机房内 VIP 高可用;
- **跨机房回源走专线 / SD-WAN,不走公网**——性能和安全的硬要求;
- 设计成**故障域隔离**:任一机房挂掉,不影响其他机房(GSLB 自动摘除)。

**2) 多国家**
- **GSLB 按地理位置解析**:中国用户解析到中国机房,欧洲用户解析到欧洲机房;
- ⚠️ **数据合规(如欧盟 GDPR、数据出境规定)**:架构必须支持"各国 / 各地区独立源站",数据不出境。这是业务 / 法律约束,要提前确认;
- 跨国回源延迟高 → 用**区域中心机房做中层**,跨洲回源只兜底。

**3) 多网络 / 多 ISP(国内经典:电信 / 联通 / 移动)**
- 边缘节点配**多线路多 IP**(每条运营商线路一个 IP),GSLB 按用户运营商返回对应线路 IP;
- 或机房级 **BGP 多线**(需要机房支持);
- OpenResty 里 `balancer_by_lua` 也能做网络亲和性调度。

**4) 多地区 = 地域级隔离 + 调度**
- 区域独立部署、独立缓存、独立监控,中心只做编排;
- 区域间通过 GSLB 和专线串联。

### 7.4 新增组件清单(在 6.3 基础上)

| 层 | 组件 | 解决什么 |
|----|------|---------|
| **★ 智能 DNS / GSLB** | **CoreDNS**(写插件)/ **PowerDNS**(自带 GeoIP 后端)/ dnsdist | 地理 + 运营商调度,多机房入口 |
| 快速故障切换 | HTTP 302 调度(OpenResty + Lua) | DNS TTL 太慢时的秒级切换兜底 |
| 跨机房回源 | 专线 / SD-WAN | 不走公网 |
| 配置 Agent | 每机房 1 个 Java / Go agent(类 ATC 的 t3c) | 应对跨国网络抖动,本地分发配置 |
| 全球监控 | **Prometheus Federation** + Grafana | 跨机房指标汇总 |
| 时钟同步 | NTP / chrony | 分布式缓存键、日志、计费依赖 |

### 7.5 现实的坑

| 坑 | 说明 | 对策 |
|----|------|------|
| **DNS 故障切换慢** | DNS 有 TTL 缓存,切机房可能要几分钟 | 短 TTL(30~60s)+ **HTTP 302 秒级兜底** |
| **多机房命中率下降** | 各机房独立缓存,小文件命中率降低 | 加中层收敛 + 大文件用 slice 共享 |
| **跨国网络抖动** | 配置下发 / 监控跨洲易超时 | **本地 Agent 异步下发**(最终一致,不强同步) |
| **BGP Anycast 自建门槛高** | 要 ASN、与运营商 peering | 一般用 **DNS 调度替代**,Anycast 留给大型 IDC |
| **回源风暴** | 某机房缓存集体失效时全压向源站 | `proxy_cache_lock` 合并回源 + 中层缓冲 |
| **时钟不一致** | 缓存键 / 日志乱 | 全网强制 NTP |

### 7.6 分阶段路径

1. **单机房跑稳**(当前目标)→ OpenResty + Java + MinIO,验证缓存命中;
2. **同城双机房** → 加 Keepalived + 专线,做高可用(低延迟,最简单);
3. **跨地域** → 上 **GSLB(智能 DNS)**,多机房的分水岭;
4. **跨国** → 加区域独立源站(合规)+ 区域中层 + 本地 Agent;
5. **多线路优化** → 多 IP / BGP 多线 + 运营商调度。

---

## 八、落地实施步骤

| 步骤 | 内容 | 验证点 |
|------|------|--------|
| 1 | 单节点 OpenResty + `proxy_cache` + `slice`,挂一个 MinIO 源站 | 静态 / 视频缓存命中(看 `X-Cache-Status` 头) |
| 2 | 加 Java 控制平面:Spring Boot 配置管理 → 生成 conf → API 下发 → 边缘 `reload` | 能下发配置并热加载 |
| 3 | 扩多节点:前置 LVS / HAProxy,网关层上一致性哈希 Lua | 多节点命中率稳定 |
| 4 | 加监控:`lua-resty-prometheus` + Grafana | 命中率 / 回源率 / 带宽可视化 |
| 5 | 按需加:视频直播上 SRS 源站;超大文件上 Dragonfly P2P 层 | 场景全覆盖 |
| 6 | (扩展)同城双机房 → 跨地域 GSLB → 跨国独立源站 | 全球可用 |

---

## 九、避坑指南

1. **GoEdge 不可用于生产**。原项目已被作者转让给"方能系"(社区指其涉黑产),且 **v1.4.1 版边缘节点程序被植入恶意代码(投毒)**。旧版 v1.3.x 无官方维护,DNS 智能调度等关键功能只在商业版。任何"开心版 / 破解版"安全风险极高。要做国产化自建 CDN,目前**没有等价的安全替代**,建议走 ATC 或自研 Nginx / OpenResty 方案。

2. **别拿单机 Nginx 当大规模 CDN**。`proxy_cache` 是单机的,跨节点缓存不共享、无法分层回源。要做集群必须有调度层(ATC / 自研 GSLB)或自己做一致性哈希 + 共享存储。

3. **ATS 集群协调已变**:找文档时注意版本 ≥ 8,clustering 已删,配置同步走外部工具。

4. **SRS 的 HLS 限制**:别指望 SRS Edge 直接分发 HLS,必须配 Nginx / ATS。

5. **缓存逻辑别全塞进 Lua**:核心缓存走 Nginx 原生 C 模块,Lua 只做控制,这是 OpenResty CDN 的稳定性铁律。

6. **多机房 DNS 故障切换慢**:必须配合 HTTP 302 做秒级兜底。

7. **跨国配置下发**:必须走本地 Agent 异步下发,不要控制平面直连每个节点。

---

## 十、参考来源

- [Apache Traffic Control 官方仓库](https://github.com/apache/trafficcontrol) · [官网](https://trafficcontrol.apache.org/)
- [Apache Traffic Server 仓库](https://github.com/apache/trafficserver) · [分层缓存文档](https://docs.trafficserver.apache.org/en/7.1.x/admin-guide/configuration/hierachical-caching.en.html) · [Wikimedia 生产案例](https://wikitech.wikimedia.org/wiki/Apache_Traffic_Server)
- [ATS clustering 移除说明(issue #1899)](https://github.com/apache/trafficserver/issues/1899)
- [Dragonfly 仓库](https://github.com/dragonflyoss/dragonfly) · [CNCF 毕业报道](https://www.infoq.com/news/2026/03/cncf-dragonfly-graduation/)
- [Varnish(Fastly 内核)社区讨论](https://www.reddit.com/r/selfhosted/comments/1lkxeaw/an_open_source_self_hostable_cdn/)
- [SRS HLS 集群文档](https://ossrs.net/lts/zh-cn/docs/v5/doc/nginx-for-hls) · [SRS GitHub](https://github.com/ossrs/srs)
- GoEdge 投毒 / 转让事件:[docker-goedge 开心版说明](https://github.com/icodex/docker-goedge) · [iCodex 技术分析](https://icodex.org/tag/cdn/) · [踩坑记录](https://2x.nz/posts/goedge/)
- [Awesome-Selfhosted(CDN 备选参考)](https://github.com/awesome-selfhosted/awesome-selfhosted)

---

*本报告基于 GitHub 开源项目仓库结构、官方文档及社区资料综合整理。Star 数据为量级估算,许可证 / 安全事件等关键事实建议以官方仓库实时信息为准。*
