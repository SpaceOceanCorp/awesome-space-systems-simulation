# Awesome Space Systems Simulation

[中文说明](README.zh-CN.md)

[![Catalog checks](https://github.com/aoezhb/awesome-space-systems-simulation/actions/workflows/catalog-check.yml/badge.svg)](https://github.com/aoezhb/awesome-space-systems-simulation/actions/workflows/catalog-check.yml)
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![CC0](https://img.shields.io/badge/license-CC0%201.0-lightgrey.svg)](LICENSE)

A curated, simulation-first map of open-source space systems tools, models, benchmarks, and validation resources.

This project is for aerospace engineers, researchers, students, and open-source developers. It does not aim to compete with broad space-software lists on item count. Instead, it focuses on simulation depth, model composition, interoperability, and reproducibility.

> For a given space systems simulation problem, which tool, model, or dataset should I choose?

This is an awesome-style curated catalog, not a universal ranking or an
automated recommendation service. Use the task guides to narrow the search,
then inspect the full catalog entry and its evidence.

## Catalog use

Project names alone do not always identify simulation scope, time advancement,
license boundaries, validation evidence, or integration requirements. The
catalog records these fields in a common format and separates runnable
simulation platforms from libraries, middleware, datasets, and reference
integrations.

Use the task guides and catalog pages to compare candidate resources, then
follow the official source and evidence links. The benchmarks provide fixed
inputs and reference procedures for cases that require numerical comparison.

## Start here

1. Choose a task or constraint below.
2. Open the linked catalog page and compare the compact metadata.
3. Follow the official source and evidence links before adopting a tool.

For task-oriented searches, begin with [Choose by Task](#choose-by-task). For
constraint-oriented searches, begin with [Choose by Constraint](#choose-by-constraint).
For a fixed numerical case, see the [two-body orbit propagation benchmark](benchmarks/two-body-orbit-propagation/README.md).

Pending candidates are not recommendations and have not passed catalog review.

## Contents

- [Catalog overview](#catalog-overview)
- [Task guides](guides/README.md)
- [Benchmarks](benchmarks/README.md)
- [Taxonomy](taxonomy/README.md)
- [Contributing](CONTRIBUTING.md)

## Choose by Task

| Task | Starting point | Representative tools |
| --- | --- | --- |
| Orbit propagation | [Open-source orbit simulators](guides/open-source-orbit-simulators.md) | GMAT, Orekit, Tudat |
| Attitude dynamics and control | [Spacecraft attitude simulation](guides/spacecraft-attitude-simulation.md) | Basilisk, 42, MuSCAT |
| Spacecraft GNC | [GNC catalog](tools/gnc.md) | Basilisk, MuSCAT, 42, AcubeSAT ADCS Simulation |
| CubeSat flight software | [Flight software catalog](tools/flight-software-and-ground.md) | NASA cFS, F Prime |
| SIL/HIL testing | [Simulation platforms](tools/simulation-platforms.md) | Trick, NOS3 |
| Space robotics | [Robotics and multiphysics](tools/robotics-and-multiphysics.md) | Gazebo, Space ROS, Project Chrono |
| Co-simulation | [System and co-simulation](tools/system-and-co-simulation.md) | FMI Library, PyFMI, OpenModelica |

## Choose by Constraint

| Constraint | Useful starting points |
| --- | --- |
| Python-first workflow | Tudat/tudatpy, poliastro, PASEOS, Basilisk interfaces |
| Java-based flight dynamics | Orekit |
| Mission-design GUI | GMAT |
| Real-time or HIL execution | Trick, NOS3, selected flight-software platforms |
| Flight-software integration | NASA cFS, F Prime, TrickCFS |
| HLA/DDS distributed simulation | TrickHLA, Portico, Fast DDS |
| Robotics and terrain interaction | Gazebo, Project Chrono, Space ROS |
| Evidence and validation inputs | SPICE Toolkit, JPL HORIZONS, CelesTrak, SPEED+ |

These are curated starting points, not universal rankings. Compare license,
simulation scope, evidence level, interfaces, and maintenance status before
selecting a tool for a project.

## Scope

- Orbit and flight dynamics
- Attitude dynamics and control
- Guidance, navigation, and control (GNC)
- Propulsion systems and engine modeling
- Spacecraft subsystem simulation
- Launch vehicle and mission analysis
- Environment models and space weather
- Multidisciplinary, co-simulation, and real-time simulation
- Hardware-in-the-loop (HIL) and software-in-the-loop (SIL)
- Datasets, standards, textbooks, and validation benchmarks

## Catalog Overview

The table below is the fast path into the catalog. Use it to identify the relevant class of resource, then open the detail page for metadata, scope, and review status.

| Category | Representative entries | What you will find | Details |
| --- | --- | --- | --- |
| Runnable simulation platforms | 42, Basilisk, NOS3, Trick, CSS Simulator, MuSCAT, LunCoSim, SpacecraftSimulator | Integrated spacecraft, mission, flight-software, and autonomy simulation | [Open](tools/simulation-platforms.md) |
| Astrodynamics and spacecraft dynamics | GMAT, Orekit, Tudat, PyKEP, PASEOS, Nyx, ANISE, REBOUND, RocketPy | Orbit propagation, mission analysis, ephemerides, celestial mechanics, and launch dynamics | [Open](tools/orbit-and-flight-dynamics.md) |
| GNC | AcubeSAT ADCS Simulation; Basilisk, MuSCAT, 42, and Orekit cross-references | Guidance, navigation, estimation, control, sensors, and actuators | [Open](tools/gnc.md) |
| Robotics and multiphysics | Gazebo, Project Chrono, Space Robotics Bench, Int-Ball2 Simulator | Rovers, manipulators, terrain, contact, perception, and multiphysics | [Open](tools/robotics-and-multiphysics.md) |
| Middleware and network emulation | Portico, Fast DDS, TrickHLA, OpenSAND, gr-leo, NodalArc, GNU Radio | HLA/RTI, DDS, communications links, and distributed simulation connectivity | [Open](tools/middleware.md) |
| System and co-simulation | FMI Library, PyFMI, OpenModelica, TrickCFS | FMI/FMU integration, equation-based modeling, flight-software integration, and cross-tool execution | [Open](tools/system-and-co-simulation.md) |
| Spacecraft subsystems | NASA Common Model Library, Space Water Logistics | Power, thermal, communications, data handling, life support water, and reusable subsystem models | [Open](tools/spacecraft-subsystems.md) |
| Propulsion and launch | OpenRocket, openMotor | Launch vehicle flight dynamics and solid-motor internal ballistics | [Open](tools/propulsion-and-launch.md) |
| Space environment | Kamodo | Atmosphere, space weather, magnetic-field, and environmental model access | [Open](tools/space-environment.md) |
| Flight software and ground systems | CubeSatSim, NASA cFS, F Prime, Open MCT, Yamcs | Flight software, telemetry, commanding, mission operations, and HIL integration | [Open](tools/flight-software-and-ground.md) |
| Verification and runtime monitoring | Copilot, OGMA | Runtime monitors, generated observers, and assurance workflows | [Open](tools/verification-and-monitoring.md) |
| Data and ephemeris sources | CelesTrak, JPL HORIZONS, Space-Track, NASA PDS | Orbital elements, ephemerides, planetary data, and validation inputs | [Open](tools/data-and-ephemeris.md) |
| Validation resources | SPEED+ | Public benchmarks, reference datasets, and validation baselines | [Open](tools/validation-resources.md) |
| Examples and reference integrations | Space ROS Demos | Runnable integrations and reference system compositions | [Open](examples/README.md) |
| Commercial or restricted references | PANGU | Useful references with license or access constraints | [Open](tools/reference-and-restricted.md) |
| Pending candidates | DARTS, TRON, SPARK | Names retained for follow-up identity and source verification | [Open](tools/pending-candidates.md) |

## Quick Links

- [Taxonomy](taxonomy/README.md)
- [Task guides](guides/README.md)
- [Benchmarks](benchmarks/README.md)
- [Contributing guide](CONTRIBUTING.md)

## Selected Evidence Examples

| Project | Status | Evidence summary | Details |
| --- | --- | --- | --- |
| GMAT | `S3 / V4` | Operational certification and documented use in NASA mission design, operations support, and independent validation | [Open](tools/orbit-and-flight-dynamics.md#gmat) |
| Orekit | `S1-S2 / V4` | Operational ATV rendezvous monitoring and documented reference-frame and relative-geometry validation | [Open](tools/orbit-and-flight-dynamics.md#orekit) |
| ANISE | `S1-S2 / V4` | Validated against SPICE and used by the Blue Ghost Mission 1 flight-dynamics team | [Open](tools/orbit-and-flight-dynamics.md#anise) |
| NASA cFS | `S2-S4 / V4` | Used across numerous NASA missions; the public bundle still requires mission-specific V&V | [Open](tools/flight-software-and-ground.md#nasa-cfs) |
| F Prime | `S2-S4 / V4` | Used by ISS-RapidScat, ASTERIA, Ingenuity, and other flight projects | [Open](tools/flight-software-and-ground.md#f-prime) |

## Scope and Evidence Levels

Simulation scope and validation evidence are recorded independently.

| Scope | Meaning |
| --- | --- |
| `S0` | Reference material, data, or conceptual resource |
| `S1` | Algorithm or component model |
| `S2` | Subsystem simulation or integration |
| `S3` | Spacecraft-, vehicle-, or mission-level simulation |
| `S4` | Documented real-time, SIL, or HIL execution. The specific execution mode must be stated in the entry. |

| Evidence | Meaning |
| --- | --- |
| `V0` | Not yet reviewed |
| `V1` | Repository tests, examples, or regression checks |
| `V2` | Compared with published reference benchmarks |
| `V3` | Validated against experimental or flight data |
| `V4` | Documented operational or flight heritage for at least part of the project; this does not imply that every module or configuration is flight-validated. |

## Curation Principles

We prioritize projects with a clear use case, public documentation, runnable examples, or validation evidence. Each entry should explain, where possible:

- The problem it solves and its intended use
- Supported languages, platforms, and license
- Simulation scope and time-stepping approach
- Support for real-time execution, SIL, or HIL
- Documentation, examples, and validation status

## Standard Entry Metadata

Each reviewed entry should use this compact metadata block:

| Field | Purpose |
| --- | --- |
| `Type` | Platform, library, middleware, data source, benchmark, or reference |
| `Primary category` | The single catalog page that owns the main entry |
| `Simulation scope` | `S0` through `S4` as defined above |
| `Evidence level` | `V0` through `V4` as defined above |
| `Primary domain` | Main engineering problem addressed |
| `Capability tags` | Cross-cutting engineering and integration capabilities |
| `Language` | Main implementation language(s) |
| `License` | Project license or access constraint |
| `Platform` | Supported operating systems, runtimes, or hardware |
| `Time advancement` | Fixed-step, variable-step, event-driven, or pending review |
| `SIL/HIL` | Software-in-the-loop and hardware-in-the-loop support |
| `Validation status` | Evidence of tests, benchmarks, experiments, or flight data |
| `Maintenance status` | Active, archived, restricted, or pending review |
| `Review status` | Identity and category review: `reviewed`, `pending review`, or `reference-only` |

A `reviewed` entry must have complete metadata and no `pending review` fields. Incomplete items remain visible as `pending review` and are excluded from the reviewed-project count.

## Catalog Design

- Simulation scope and validation evidence are recorded as separate fields
- Metadata covers language, license, platform, time advancement, and validation status
- Capability tables provide a cross-category comparison view
- Benchmark pages define reproducible inputs and reference procedures
- Runnable simulation platforms are separated from supporting resources
- Model composition, distributed simulation, and co-simulation are represented through categories and cross-references

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Contributions of tools, benchmarks, datasets, papers, and corrections are welcome.

## Roadmap

- [x] Add the first runnable space systems simulation platforms
- [ ] Review and complete metadata for the initial platform entries
- [x] Add the first orbit, attitude, and GNC tool entries
- [x] Add the first reproducible orbit benchmark definition
- [x] Build a capability comparison matrix
- [x] Track license, maintenance, and validation status
- [x] Add task guides and curated stack guides
- [x] Add issue forms for metadata, evidence, benchmarks, links, and proposals

## License

The directory and documentation are released under [CC0 1.0](LICENSE). Listed projects remain under their respective licenses.
