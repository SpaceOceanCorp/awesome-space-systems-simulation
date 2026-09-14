# Simulation Middleware and Interoperability

This section covers infrastructure used to connect simulation components, coordinate distributed execution, exchange state, and support real-time or hardware-in-the-loop environments.

## High Level Architecture and RTI

High Level Architecture (HLA) defines a standard architecture for distributed simulation. A Run-Time Infrastructure (RTI) provides the services used by participating federates, including federation management, object and interaction exchange, ownership, data distribution, and time management.

Entries in this section should identify:

- Supported HLA editions and APIs
- Federation Object Model (FOM) tooling
- Time-regulating and time-constrained execution support
- Transport, discovery, monitoring, and recording facilities
- Language bindings, platforms, license, and real-time suitability

## Data Distribution Service

Data Distribution Service (DDS) is a data-centric publish-subscribe middleware family commonly used for distributed and real-time systems. In simulation environments it can connect subsystem models, flight software, test equipment, operators, and digital twins.

Entries in this section should identify:

- DDS and interoperability profile support
- Quality of Service controls relevant to simulation
- Discovery and deployment model
- Serialization and schema tooling
- Language bindings, platforms, license, and real-time suitability

## Other Middleware

- Message brokers and event buses
- Shared-memory and low-latency transports
- Remote procedure call frameworks
- Simulation gateways and protocol bridges
- Recording, replay, observability, and data distribution tools

## Initial Entries

### Portico

- [Portico](https://github.com/openlvc/portico) - An open-source, cross-platform HLA Run-Time Infrastructure implementation for distributed simulation federations.
- **Type:** HLA/RTI implementation
- **Primary category:** middleware
- **Simulation scope:** S2-S4
- **Evidence level:** V0
- **Primary domain:** distributed simulation and federation interoperability
- **Capability tags:** communications, distributed-simulation, real-time
- **Language:** Java and C++ interfaces
- **License:** CDDL
- **Platform:** cross-platform; verify supported runtimes
- **Time advancement:** HLA time management
- **SIL/HIL:** integration support
- **Validation status:** project tests and examples; detailed evidence pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### Fast DDS

- [Fast DDS](https://github.com/eProsima/Fast-DDS) - An open-source C++ implementation of the OMG DDS standard and RTPS protocol for real-time publish-subscribe communication.
- **Type:** DDS implementation
- **Primary category:** middleware
- **Simulation scope:** S2-S4
- **Evidence level:** V0
- **Primary domain:** distributed real-time data exchange
- **Capability tags:** communications, distributed-simulation, real-time
- **Language:** C++
- **License:** Apache-2.0
- **Platform:** pending review
- **Time advancement:** application-managed; QoS and transport coordination
- **SIL/HIL:** integration support
- **Validation status:** repository examples and tests; detailed evidence pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### OpenDDS

- [OpenDDS](https://github.com/OpenDDS/OpenDDS) - An open-source implementation of the DDS specification for distributed publish-subscribe systems.
- **Type:** DDS implementation
- **Primary category:** middleware
- **Simulation scope:** S2-S4
- **Evidence level:** V0
- **Primary domain:** distributed simulation and telemetry exchange
- **Capability tags:** communications, distributed-simulation, real-time
- **Language:** C++
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** application-managed; QoS and transport coordination
- **SIL/HIL:** integration support
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### Cyclone DDS

- [Cyclone DDS](https://github.com/eclipse-cyclonedds/cyclonedds) - An Eclipse-hosted DDS implementation for data-centric publish-subscribe communication.
- **Type:** DDS implementation
- **Primary category:** middleware
- **Simulation scope:** S2-S4
- **Evidence level:** V0
- **Primary domain:** distributed real-time data exchange
- **Capability tags:** communications, distributed-simulation, real-time
- **Language:** C
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** application-managed; QoS and transport coordination
- **SIL/HIL:** integration support
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### NodalArc

- [NodalArc](https://github.com/dotchance/nodalarc) - A satellite-network emulator for testing routing, link changes, and networked applications against dynamic orbital topologies.
- **Type:** network emulator
- **Primary category:** middleware
- **Simulation scope:** S2-S4
- **Evidence level:** V0
- **Primary domain:** satellite communications and network behavior
- **Capability tags:** communications, distributed-simulation, real-time
- **Language:** pending review
- **License:** pending review
- **Platform:** Linux network namespaces; pending review
- **Time advancement:** pending review
- **SIL/HIL:** SIL-oriented
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### GNU Radio

- [GNU Radio](https://github.com/gnuradio/gnuradio) - A signal-processing and software-defined-radio toolkit for communications modeling, test, and hardware integration.
- **Type:** communications simulation toolkit
- **Primary category:** middleware
- **Simulation scope:** S1-S4
- **Evidence level:** V0
- **Primary domain:** RF, SDR, and communications links
- **Capability tags:** communications, distributed-simulation, real-time
- **Language:** C++ and Python
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** hardware integration
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### TrickHLA

- [TrickHLA](https://github.com/nasa/TrickHLA) - A NASA integration library that connects Trick simulations to an HLA federation through an RTI.
- **Type:** HLA simulation integration library
- **Primary category:** middleware
- **Simulation scope:** S2-S4
- **Evidence level:** V1
- **Primary domain:** distributed Trick simulation
- **Capability tags:** HLA, RTI, Trick, distributed-simulation, real-time
- **Language:** C++
- **License:** NASA Open Source Agreement 1.3
- **Platform:** Trick-supported Linux environments
- **Time advancement:** HLA time management integrated with Trick execution
- **SIL/HIL:** integration support
- **Validation status:** repository tests and example federations
- **Maintenance status:** active
- **Review status:** reviewed

### OpenSAND

- [OpenSAND](https://github.com/CNES/opensand) - A CNES satellite-network emulation platform for evaluating communication protocols and applications over configurable satellite links.
- **Type:** satellite network emulator
- **Primary category:** middleware
- **Simulation scope:** S2-S4
- **Evidence level:** V1
- **Primary domain:** satellite communications and network emulation
- **Capability tags:** communications, satellite-link, network-emulation, SIL
- **Language:** C++ and Python
- **License:** GNU General Public License v3.0
- **Platform:** Linux
- **Time advancement:** real-time network emulation
- **SIL/HIL:** software- and hardware-network integration
- **Validation status:** repository tests, examples, and CNES documentation
- **Maintenance status:** active
- **Review status:** reviewed

### gr-leo

- [gr-leo](https://gitlab.com/librespacefoundation/gr-leo) - A GNU Radio out-of-tree module for simulating and processing low-Earth-orbit satellite communication channels.
- **Type:** communications simulation module
- **Primary category:** middleware
- **Simulation scope:** S1-S2
- **Evidence level:** V1
- **Primary domain:** LEO satellite radio links
- **Capability tags:** communications, GNU-Radio, LEO, Doppler, channel-model
- **Language:** C++ and Python
- **License:** pending review
- **Platform:** GNU Radio-supported environments
- **Time advancement:** GNU Radio stream processing
- **SIL/HIL:** SDR integration support
- **Validation status:** repository examples; detailed validation pending review
- **Maintenance status:** pending review
- **Review status:** pending review

## Selection Notes

HLA/RTI is typically evaluated around federation coordination, simulation time management, and formal interoperability models. DDS is typically evaluated around data-centric exchange, configurable quality of service, and real-time distributed integration. Some system-of-systems simulations may use both through a gateway or integration layer.
