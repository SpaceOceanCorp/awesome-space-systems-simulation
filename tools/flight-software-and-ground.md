# Flight Software and Ground Systems

These projects support the software, operations, telemetry, commanding, and test environments around a simulation. They are complementary to dynamics engines rather than replacements for them.

## Initial Entries

### CubeSatSim

- [CubeSatSim](https://github.com/alanbjohnston/CubeSatSim) - A low-cost CubeSat hardware and software simulator for education, integration, and hardware-in-the-loop experiments.
- **Type:** hardware simulator
- **Primary category:** flight-software-and-ground
- **Simulation scope:** S2-S4
- **Evidence level:** V0
- **Primary domain:** CubeSat systems and HIL
- **Capability tags:** flight-software, ground-systems, SIL, HIL
- **Language:** pending review
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** HIL-oriented
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### NASA cFS

- [NASA cFS](https://github.com/nasa/cFS) - A reusable flight-software framework commonly integrated with spacecraft simulators and test environments.
- **Type:** flight-software framework
- **Primary category:** flight-software-and-ground
- **Simulation scope:** S2-S4
- **Evidence level:** V4
- **Primary domain:** flight software integration
- **Capability tags:** flight-software, ground-systems, SIL, HIL
- **Language:** C
- **License:** Apache License 2.0
- **Platform:** POSIX, RTEMS, VxWorks, and other OSAL-supported targets
- **Time advancement:** not applicable
- **SIL/HIL:** SIL/HIL integration
- **Validation status:** The cFS architecture has flight heritage across numerous NASA missions. The public bundle is an integration starting point and still requires mission-specific verification and validation before operational use.
- **Flight heritage:** NASA reports use across more than 40 missions, including LRO, LADEE, GPM, MMS, and JWST-related mission software deployments.
- **Evidence:** [NASA cFS capability overview](https://etd.gsfc.nasa.gov/capabilities/capabilities-listing/cfs/) and [NASA cFS repository](https://github.com/nasa/cFS).
- **Maintenance status:** active
- **Review status:** reviewed

### F Prime

- [F Prime](https://github.com/nasa/fprime) - A component-driven flight-software framework with tools for development, deployment, and testing.
- **Type:** flight-software framework
- **Primary category:** flight-software-and-ground
- **Simulation scope:** S2-S4
- **Evidence level:** V4
- **Primary domain:** flight software and embedded systems
- **Capability tags:** flight-software, ground-systems, SIL, HIL
- **Language:** C++
- **License:** Apache License 2.0
- **Platform:** Linux, macOS, and supported embedded flight targets
- **Time advancement:** not applicable
- **SIL/HIL:** SIL/HIL integration
- **Validation status:** Flight-proven framework used by operational spacecraft and technology-demonstration missions; validation remains mission- and deployment-specific.
- **Flight heritage:** Used by missions and instruments including ISS-RapidScat, ASTERIA, and the Ingenuity Mars Helicopter.
- **Evidence:** [F Prime project and mission overview](https://fprime.jpl.nasa.gov/overview/projects/) and [NASA F Prime repository](https://github.com/nasa/fprime).
- **Maintenance status:** active
- **Review status:** reviewed

### Open MCT

- [Open MCT](https://github.com/nasa/openmct) - A mission-control user interface for telemetry, commanding, planning, and simulation displays.
- **Type:** ground-system interface
- **Primary category:** flight-software-and-ground
- **Simulation scope:** S2-S4
- **Evidence level:** V0
- **Primary domain:** mission operations and visualization
- **Capability tags:** flight-software, ground-systems, SIL, HIL
- **Language:** JavaScript and TypeScript
- **License:** pending review
- **Platform:** web
- **Time advancement:** not applicable
- **SIL/HIL:** integration support
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### Yamcs

- [Yamcs](https://github.com/yamcs/yamcs) - A mission-control and telemetry platform for commanding, archiving, monitoring, and simulation integration.
- **Type:** ground-system platform
- **Primary category:** flight-software-and-ground
- **Simulation scope:** S2-S4
- **Evidence level:** V0
- **Primary domain:** telemetry, commanding, and operations
- **Capability tags:** flight-software, ground-systems, SIL, HIL
- **Language:** Java
- **License:** pending review
- **Platform:** JVM
- **Time advancement:** not applicable
- **SIL/HIL:** integration support
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review
