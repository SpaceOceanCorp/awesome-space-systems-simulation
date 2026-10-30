# Awesome Space Systems Simulation

[English README](README.md)

一个以仿真为核心、面向航天系统工程的开源工具、模型、基准和验证资源精选目录。

本项目保持 **Awesome list** 定位：提供经过整理的导航和元数据，不做万能排名，也不建设网站、数据库或自动推荐系统。

## 目录使用

项目名称本身通常不能完整说明仿真层级、时间推进方式、许可证边界、验证证据
和集成要求。本目录使用统一字段记录这些信息，并区分可运行仿真平台、库、
中间件、数据集和参考集成。

可以先通过任务指南和分类页缩小范围，再查看项目的官方来源和证据链接。需要
进行数值比较时，可以使用包含固定输入和参考流程的基准条目。

## 项目定位

本项目关注的问题是：

> 面对一个航天系统仿真问题，应该从哪些工具、模型或数据源开始？

重点覆盖：

- 轨道与飞行动力学
- 姿态动力学与控制
- 制导、导航与控制（GNC）
- 航天器分系统与推进
- 机器人与多物理场仿真
- 联合仿真、实时仿真、SIL/HIL
- 飞行软件、地面系统和任务运行
- 中间件与网络仿真，包括 HLA/RTI 和 DDS
- 环境模型、星历和验证数据

## 从这里开始

1. 按任务选择一个[任务指南](guides/README.md)。
2. 打开对应的[目录分类页](#目录总览)。
3. 查看项目的英文详细条目、官方链接和证据说明。
4. 需要比较数值结果时，使用[基准目录](benchmarks/README.md)。

按任务检索时，可以从任务指南开始；按工程约束检索时，可以从目录总览和元数据
开始。需要固定数值案例时，可以查看[两体轨道传播基准](benchmarks/two-body-orbit-propagation/README.md)。

待审核候选项目不是推荐项目，尚未通过目录审核。

## 目录总览

| 分类 | 代表项目 | 内容 | 详情 |
| --- | --- | --- | --- |
| 可运行仿真平台 | 42、Basilisk、NOS3、Trick、MuSCAT | 整星、任务、飞行软件和自主性仿真平台 | [查看](tools/simulation-platforms.md) |
| 轨道与飞行动力学 | GMAT、Orekit、Tudat、ANISE、Nyx | 轨道传播、任务分析、星历和天体力学 | [查看](tools/orbit-and-flight-dynamics.md) |
| GNC | Basilisk、42、MuSCAT、AcubeSAT ADCS Simulation | 导航、估计、制导、控制、传感器和执行机构 | [查看](tools/gnc.md) |
| 机器人与多物理场 | Gazebo、Project Chrono、Space Robotics Bench | 移动机器人、机械臂、地形、接触和多物理场 | [查看](tools/robotics-and-multiphysics.md) |
| 中间件与网络仿真 | TrickHLA、Portico、Fast DDS、OpenSAND | HLA/RTI、DDS、通信链路和分布式仿真 | [查看](tools/middleware.md) |
| 系统与联合仿真 | FMI Library、PyFMI、OpenModelica、TrickCFS | FMI/FMU、方程建模和跨工具执行 | [查看](tools/system-and-co-simulation.md) |
| 航天器分系统 | NASA Common Model Library, Space Water Logistics | 电源、热控、通信、数据处理等模型 | [查看](tools/spacecraft-subsystems.md) |
| 推进与发射 | OpenRocket、openMotor | 火箭飞行和固体发动机内弹道 | [查看](tools/propulsion-and-launch.md) |
| 空间环境 | Kamodo | 大气、空间天气、磁场和环境模型接口 | [查看](tools/space-environment.md) |
| 飞行软件与地面系统 | NASA cFS、F Prime、Open MCT、Yamcs | 飞行软件、遥测、测控和任务运行 | [查看](tools/flight-software-and-ground.md) |
| 验证与运行时监控 | Copilot、OGMA | 运行时监控、观察器和保障流程 | [查看](tools/verification-and-monitoring.md) |
| 数据与星历 | CelesTrak、JPL HORIZONS、NASA PDS | 轨道根数、星历、行星数据和验证输入 | [查看](tools/data-and-ephemeris.md) |
| 验证资源 | SPEED+ | 基准数据、参考结果和验证基线 | [查看](tools/validation-resources.md) |
| 示例与参考集成 | Space ROS Demos | 可运行示例和参考系统组合 | [查看](examples/README.md) |

## 如何理解条目

每个正式条目使用统一的英文元数据字段：

- `Primary category`：项目的唯一主分类
- `Simulation scope`：`S0` 到 `S4`，表示仿真范围和执行方式
- `Evidence level`：`V0` 到 `V4`，表示验证和任务证据等级
- `Capability tags`：跨分类能力标签，例如 orbit、attitude、SIL、HIL、real-time
- `License`、`Platform`、`Time advancement`：工程选型所需的约束信息
- `Maintenance status`、`Review status`：维护状态和目录审核状态

`S4` 只表示项目有文档记录的实时、SIL 或 HIL 执行能力，具体模式必须在条目中说明。

`V4` 表示项目的至少一部分具有文档记录的运营或飞行继承性，不代表每个模块或配置都经过飞行验证。

## 相关入口

- [任务指南](guides/README.md)
- [基准与复现](benchmarks/README.md)
- [分类法](taxonomy/README.md)
- [贡献指南](CONTRIBUTING.md)
- [Citation](CITATION.cff)

## 贡献

项目条目、证据、基准、数据源和链接修正都欢迎提交。请先阅读[贡献指南](CONTRIBUTING.md)，并使用仓库中的 Issue Form 或 Pull Request 模板。

所有项目的详细描述、元数据和证据记录继续以英文为准，以便保持目录格式一致并方便国际协作。

## 许可证

目录和文档采用 [CC0 1.0](LICENSE)。被收录项目仍分别适用其自身许可证。
