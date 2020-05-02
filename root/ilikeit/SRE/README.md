SRE - Site Reliability Engineer
===============================
```
SRE 稳定性标准:
  MTBF: Mean Time Between Failure: 平均故障时间间隔
    故障演练 - 容量评估 - 持续交付 - 自动化 - 架构设计 
  MTTR: Mean Time To Repair: 故障平均修复时间
    MTTI: Mean Time To Identify 平均故障发现时间 
    MTTK: Mean Time To Know: 平均故障认知时间
    MTTF: Mean Tiem to Fix: 平均故障解决时间
    MTTV: Mean Time to Verify: 平均故障修复验证时间
    故障发现 - 故障定位 - 故障恢复
    AIOps - 日志分析 - 容灾切换 
    链路跟踪 - 服务降级 - 服务限流 - 监控警告 - 根因定位 
    异常熔断 
  MTBF: 
    故障复盘- 改进验收 - 故障模拟 - 混沌工程 - 容量压测 
SRE 实现的目标就是"提升MTBF，降低MTTR"

系统可用性 Availability:
  目前两种衡量系统可用性方式:
    1. 时间维度 Availability: Uptime/(Uptime + Downtime)
    2. 请求维度 Availability: Successful request / Total request
  ROI: 回报率

SLI: Service Level Indicator: 服务等级指标 -- 监控的指标
SLO: Service Level Objective: 服务等级目标 -- 指标对应的目标

系统中常见的监控指标:
  1. 系统层面: CPU 使用率, Load值,内存使用率,磁盘使用率,磁盘IO，网络IO
  2. 应用服务器层面: 端口存活状态 
  3. 应用运行层面: 请求返回的状态码，时延，引用层QPS，TPS 连接数 
  4. PaaS层面: MySQL, Redis, Kafka, MQ 和分布式文件存储 QPS TPS 时延指标 
  5. 数据层面: 大数据类型的平台 批处理任务或流处理任务，吞吐率，及时率，准确率 

快速识别SLI指标的方式: VALET
  Volume: 容量 - 
  Availability: 可用性 - 
  Latency: 时延 - 
  Error: 错误率
  Ticket: 人工介入

Error Budget: 错误预算
  
故障等级设置: P0~P4 (P0 最高，P4最低)
建立稳定性共识机制：
  Top-Down, 也就是自上而下，至少是从技术VP或CTO角度推行 
告警收敛:
  1.相同相似告警 合并后发送 
  2. 基于错误预算来做告警

达成Met
未达成Missed

系统核心链路Critical Transaction Path:
  
设定SLO原则:
  1. 核心业务的SLO更为严格，非核心应用可以放宽 
  2. 强依赖之间的核心业务，SLO要一致 
  3. 弱依赖中，核心应用对非核心的依赖要降级，熔断和限流等服务治理手段 
  4. Error Budget策略，核心应用的错误预算要共享

验证SLO:
  1. 容量压测 (QPS, TPS) 模拟线上真实用户的访问行为
  2. Chaos Engineering : 混沌工程 模拟故障发生场景
    机房故障: 模拟断电 - 查看是否切换双活活备用机房 
    网络层面: 模拟丢包或网卡流量打满 
    硬件和系统层面: 磁盘写满，CPU跑满
    应用层面: 故障注入，线程池跑满 
  混沌工程是SRE稳定性体系建设的高级阶段，一定是SRE体系在服务治理，容量压测，链路跟踪，监控告警，运维自动化等相对基础和必须的部分非常完善的情况下才会考虑

分布式系统发生故障，策略不一定是找到根因，而是优先恢复业务 

Zabbix:
ELK: 日志系统
Prometheus: Kubernetes
On-Call流程机制:
  1. 确保关键角色在线 
  2. 组织War Room(消防群)应急组织 
  3. 建立合理的呼叫方式 - 熟悉某个系统的最快最好的方式就是参与On-Call; On-Call可以培养和锻炼新人和BackUP角色

故障处理过程中采取的所有手段和行动一切以恢复业务为最高优先级
故障响应：
  1. 技术方面 
  2. 流程方面 

Incident Commander: 故障指挥官 IC: 
Communication Lead: 沟通引导 CL:
Operations Lead: 运维指挥: OL 
Incident Responders: IR 

没有进展也是进展，也要及时反馈 

故障复盘:
  故障根因不止一个，与其争论根因是什么，不如一起看看引起故障的原因都有那些，是不是都有改进的空间
  1. 健壮性原则
  2. 第三方默认无责
    稳定性责任一定是内部角色承担
  3. 分段判定原则:

技术架构图:
  High-Level架构图
    1. 接入层: 四层&七层负载LVS + Nginx + 业务网关  -- 接入层管理 
    2. 业务前台: 
    3. 业务中台:
    4. 技术中台: 分布式架构(服务化|缓存｜消息|对象存储)
    5. 基础设施: - 服务｜存储｜网络｜虚拟化
  技术保证体系:
    1.接入层管理
    2.压测/容量规划
    3.全链路跟踪
    4.限流/降级/预案
    5.监控/AIOps
    6.持续交付
    7.运维自动化
    8.CMDB
SRE是微服务和分布式架构的产物:
应用运维PE(Production Engineer): 技术运营
```
