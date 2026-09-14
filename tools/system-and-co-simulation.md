# System and Co-Simulation

> Initial entries will be added as the catalog is established. Follow the root contribution guide when submitting a project.

## Curation Dimensions

- Spacecraft- and mission-level digital twins
- Hybrid continuous-time and discrete-event simulation
- FMI/FMU and Modelica
- SIL, HIL, and real-time target systems
- Cross-language and cross-tool co-simulation

## Initial Entries

### FMI Library

- [FMI Library](https://github.com/modelon-community/fmi-library) - A C implementation of the Functional Mock-up Interface for importing and exporting FMUs in model-exchange and co-simulation workflows.
- **Type:** co-simulation interoperability library
- **Primary category:** co-simulation
- **Simulation scope:** S1-S4
- **Evidence level:** V0
- **Primary domain:** FMI/FMU integration
- **Capability tags:** co-simulation, FMI, system-modeling
- **Language:** C
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** FMI model-exchange or co-simulation semantics
- **SIL/HIL:** integration support
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### PyFMI

- [PyFMI](https://github.com/modelon-community/PyFMI) - A Python package for loading, simulating, and interacting with FMUs.
- **Type:** co-simulation interface
- **Primary category:** co-simulation
- **Simulation scope:** S1-S4
- **Evidence level:** V0
- **Primary domain:** FMI/FMU integration and experimentation
- **Capability tags:** co-simulation, FMI, system-modeling
- **Language:** Python and Cython
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** FMI model-exchange or co-simulation semantics
- **SIL/HIL:** integration support
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### OpenModelica

- [OpenModelica](https://github.com/OpenModelica/OpenModelica) - An open-source Modelica environment for equation-based modeling and system-level simulation.
- **Type:** equation-based modeling and simulation environment
- **Primary category:** co-simulation
- **Simulation scope:** S1-S4
- **Evidence level:** V0
- **Primary domain:** system modeling and co-simulation
- **Capability tags:** co-simulation, FMI, system-modeling
- **Language:** C++ and Modelica
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** fixed-step or variable-step solver; pending review
- **SIL/HIL:** integration support
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### TrickCFS

- [TrickCFS](https://github.com/nasa/TrickCFS) - A NASA integration framework for running core Flight System applications with Trick-based spacecraft simulations.
- **Type:** flight-software and simulation integration framework
- **Primary category:** co-simulation
- **Simulation scope:** S3-S4
- **Evidence level:** V1
- **Primary domain:** cFS and Trick co-simulation
- **Capability tags:** Trick, cFS, SIL, HIL, co-simulation
- **Language:** C and C++
- **License:** NASA Open Source Agreement 1.3
- **Platform:** Trick-supported Linux environments
- **Time advancement:** Trick scheduler integrated with cFS execution
- **SIL/HIL:** software-in-the-loop and integration-test support
- **Validation status:** repository integration tests and examples
- **Maintenance status:** active
- **Review status:** reviewed
