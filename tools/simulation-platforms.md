# Runnable Simulation Platforms

This section is reserved for open-source applications and frameworks that can run integrated space systems simulations. Libraries that provide only a single model or algorithm belong in their corresponding domain section.

## Initial Platforms

### CSS Simulator

- [CSS Simulator](https://github.com/IRT-Saint-Exupery/CSS-Simulator) - An integrated platform for space systems, constellations, flight software, mission control, the space environment, and space links.
- **Type:** integrated simulation platform
- **Primary category:** platform
- **Simulation scope:** S3
- **Evidence level:** V0
- **Primary domain:** constellations, flight software, operations, environment, and communications
- **Capability tags:** orbit, attitude, GNC, spacecraft, mission
- **Language:** pending review
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### 42

- [42](https://github.com/ericstoneking/42) - A spacecraft dynamics and mission simulation environment for attitude, orbit, multi-spacecraft, and proximity-operations studies.
- **Type:** integrated simulation platform
- **Primary category:** platform
- **Simulation scope:** S3
- **Evidence level:** V0
- **Primary domain:** spacecraft dynamics and mission operations
- **Capability tags:** orbit, attitude, GNC, spacecraft, mission
- **Language:** C/C++
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### Basilisk

- [Basilisk](https://github.com/AVSLab/basilisk) - A modular spacecraft simulation framework for dynamics, flight software, and GNC research.
- **Type:** integrated simulation framework
- **Primary category:** platform
- **Simulation scope:** S2-S3
- **Evidence level:** V2
- **Primary domain:** spacecraft dynamics and GNC
- **Capability tags:** orbit, attitude, GNC, spacecraft, mission
- **Language:** C++ and Python
- **License:** ISC
- **Platform:** Linux, macOS, Windows, and published container images
- **Time advancement:** task-based scheduler with configurable update rates and numerical state integration
- **SIL/HIL:** synchronization and external integration support; deployment-specific
- **Validation status:** extensive unit and integrated tests plus documented cross-tool orbit-propagation comparisons
- **Maintenance status:** active
- **Review status:** reviewed

### NOS3

- [NOS3](https://github.com/nasa/nos3) - A NASA framework for integrating simulated spacecraft dynamics, hardware models, flight software, and test infrastructure.
- **Type:** integrated simulation and test platform
- **Primary category:** platform
- **Simulation scope:** S3-S4
- **Evidence level:** V0
- **Primary domain:** spacecraft systems and flight software
- **Capability tags:** orbit, attitude, GNC, spacecraft, mission
- **Language:** C/C++ and Python
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### Trick

- [Trick](https://github.com/nasa/trick) - A general-purpose simulation framework used for spacecraft and flight-software development, including virtual and hardware-in-the-loop workflows.
- **Type:** simulation framework
- **Primary category:** platform
- **Simulation scope:** S1-S4
- **Evidence level:** V0
- **Primary domain:** system simulation and test infrastructure
- **Capability tags:** orbit, attitude, GNC, spacecraft, mission
- **Language:** C++ and Python
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### MuSCAT

- [MuSCAT](https://github.com/nasa/muscat) - NASA's Multi-Spacecraft Concept and Autonomy Tool for simulating navigation, attitude control, power, communications, and data handling across spacecraft concepts.
- **Type:** integrated multi-spacecraft simulation platform
- **Primary category:** platform
- **Simulation scope:** S2-S3
- **Evidence level:** V0
- **Primary domain:** autonomy, GNC, power, communications, and data handling
- **Capability tags:** orbit, attitude, GNC, spacecraft, mission
- **Language:** pending review
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### LunCoSim

- [LunCoSim](https://github.com/LunCoSim/lunco-sim) - A system-level multiphysics co-simulation platform for lunar mission studies.
- **Type:** integrated co-simulation platform
- **Primary category:** platform
- **Simulation scope:** S3
- **Evidence level:** V0
- **Primary domain:** lunar systems and multiphysics
- **Capability tags:** orbit, attitude, GNC, spacecraft, mission
- **Language:** pending review
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### SpacecraftSimulator

- [SpacecraftSimulator](https://github.com/AlessioNegri/SpacecraftSimulator) - A graphical simulation application focused on orbital flight, launch, and re-entry studies.
- **Type:** vehicle dynamics simulator
- **Primary category:** platform
- **Simulation scope:** S2-S3
- **Evidence level:** V0
- **Primary domain:** orbit, launch, re-entry, and visualization
- **Capability tags:** orbit, attitude, GNC, spacecraft, mission
- **Language:** pending review
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

## Initial Capability Matrix

This table records only capabilities identified during initial triage. Blank cells must not be interpreted as a lack of support.

| Platform | Component | Subsystem | Spacecraft | Multi-spacecraft | Mission | Co-simulation | GUI |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 42 |  |  | Yes | Yes | Yes |  |  |
| Basilisk |  | Yes | Yes |  | Yes |  |  |
| NOS3 |  | Yes | Yes |  | Yes |  |  |
| Trick |  | Yes | Yes |  | Yes |  |  |
| CSS Simulator |  | Yes | Yes | Yes | Yes |  |  |
| MuSCAT |  | Yes | Yes | Yes | Yes |  |  |
| LunCoSim |  | Yes | Yes |  | Yes | Yes |  |
| SpacecraftSimulator |  |  | Yes |  | Yes |  | Yes |

## Required Review Fields

Before an entry is considered fully reviewed, confirm:

- Implementation language and supported operating systems
- License and redistribution constraints
- Time advancement and synchronization model
- Supported standards and middleware
- SIL, HIL, and real-time capabilities
- Test coverage, reference cases, and validation evidence
- Documentation quality and project maintenance status
