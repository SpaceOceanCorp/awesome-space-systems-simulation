# Orbit and Flight Dynamics

Libraries and engines in this section provide dynamics, orbit propagation, mission design, or reference-frame services. They are not necessarily integrated spacecraft simulators.

## Curation Dimensions

- Two-body, J2, and higher-order perturbation models
- Numerical orbit propagation and event detection
- Six-degree-of-freedom flight dynamics
- Formation flight, rendezvous, and proximity operations
- Re-entry and atmospheric flight

## Initial Entries

### GMAT

- [GMAT](https://software.nasa.gov/software/GSC-19640-1) - NASA's General Mission Analysis Tool for mission design, orbit propagation, optimization, navigation, and flight-mission support.
- **Type:** mission analysis application
- **Primary category:** dynamics
- **Simulation scope:** S3
- **Evidence level:** V4
- **Primary domain:** mission design and astrodynamics
- **Capability tags:** orbit, astrodynamics, mission
- **Language:** C++ with a domain-specific scripting language
- **License:** Apache License 2.0
- **Platform:** Linux, macOS, and Windows
- **Time advancement:** variable-step numerical propagation and event-driven mission sequencing
- **SIL/HIL:** not documented
- **Validation status:** Operationally certified for ACE and used for mission design, operations support, or independent validation on NASA missions including ARTEMIS, LRO, LCROSS, MAVEN, MMS, OSIRIS-REx, and TESS.
- **Evidence:** [NASA Software Catalog](https://software.nasa.gov/software/GSC-19640-1), [NASA usage](https://gmat.atlassian.net/wiki/spaces/GW/pages/380273244/NASA+Usage), and [project milestones](https://gmat.atlassian.net/wiki/spaces/GW/pages/380273281/Project+Milestones).
- **Maintenance status:** active
- **Review status:** reviewed

### Orekit

- [Orekit](https://www.orekit.org/) - A low-level space-flight dynamics library for orbit propagation, attitude, frames, events, and estimation.
- **Type:** dynamics library
- **Primary category:** dynamics
- **Simulation scope:** S1-S2
- **Evidence level:** V4
- **Primary domain:** astrodynamics
- **Capability tags:** orbit, astrodynamics, mission
- **Language:** Java
- **License:** Apache License 2.0
- **Platform:** JVM
- **Time advancement:** fixed-step or adaptive numerical propagation selected by the application
- **SIL/HIL:** not applicable
- **Validation status:** Used operationally for real-time monitoring of ESA/CNES Automated Transfer Vehicle rendezvous with the ISS; reference-frame and relative-geometry behavior was checked against operational and public reference data, including sub-millimeter relative-geometry checks reported by the project.
- **Evidence:** [Orekit operational use and validation FAQ](https://www.orekit.org/site-orekit-latest/faq.html).
- **Maintenance status:** active
- **Review status:** reviewed

### poliastro

- [poliastro](https://github.com/poliastro/poliastro) - A Python library for interactive astrodynamics and orbital mechanics.
- **Type:** dynamics library
- **Primary category:** dynamics
- **Simulation scope:** S1-S2
- **Evidence level:** V1
- **Primary domain:** astrodynamics
- **Capability tags:** orbit, astrodynamics, mission
- **Language:** Python
- **License:** MIT
- **Platform:** Python-supported environments
- **Time advancement:** analytical and numerical propagation
- **SIL/HIL:** not applicable
- **Validation status:** repository tests and historical examples; no flight-validation claim reviewed
- **Maintenance status:** archived by the maintainers in October 2023
- **Review status:** reviewed

### Open Space Toolkit

- [Open Space Toolkit](https://github.com/open-space-collective/open-space-toolkit) - An open-source ecosystem for space mission analysis, orbital mechanics, physics, and time systems.
- **Type:** dynamics and mission-analysis toolkit
- **Primary category:** dynamics
- **Simulation scope:** S1-S3
- **Evidence level:** V0
- **Primary domain:** astrodynamics and mission analysis
- **Capability tags:** orbit, astrodynamics, mission
- **Language:** C++ and Python
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** not applicable
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### Nyx

- [Nyx](https://github.com/nyx-space/nyx) - A high-performance astrodynamics toolkit for orbit determination, propagation, and mission analysis.
- **Type:** dynamics engine
- **Primary category:** dynamics
- **Simulation scope:** S1-S3
- **Evidence level:** V2
- **Primary domain:** astrodynamics
- **Capability tags:** orbit, astrodynamics, mission
- **Language:** Rust
- **License:** GNU Affero General Public License v3.0 for the open-source core; premium features use separate terms
- **Platform:** Rust-supported environments; Python bindings are project-status dependent
- **Time advancement:** adaptive numerical propagation
- **SIL/HIL:** not applicable
- **Validation status:** compared with published astrodynamics references and external tools in project validation material
- **Maintenance status:** active
- **Review status:** reviewed

### SPICE Toolkit

- [SPICE Toolkit](https://naif.jpl.nasa.gov/naif/toolkit.html) - NASA's toolkit for spacecraft and planetary ephemerides, geometry, kernels, and observation analysis.
- **Type:** reference-data and geometry toolkit
- **Primary category:** dynamics
- **Simulation scope:** S0-S2
- **Evidence level:** V0
- **Primary domain:** ephemerides and mission geometry
- **Capability tags:** orbit, astrodynamics, mission
- **Language:** C, Fortran, IDL, MATLAB, and Python interfaces
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** not applicable
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### ANISE

- [ANISE](https://github.com/nyx-space/anise) - An astrodynamics and ephemeris toolkit in the Nyx ecosystem.
- **Type:** astrodynamics library
- **Primary category:** dynamics
- **Simulation scope:** S1-S2
- **Evidence level:** V4
- **Primary domain:** ephemerides and orbit mechanics
- **Capability tags:** orbit, astrodynamics, mission
- **Language:** Rust
- **License:** Mozilla Public License 2.0
- **Platform:** Rust-supported environments with Python bindings
- **Time advancement:** ephemeris- and query-driven; not a standalone propagator
- **SIL/HIL:** not applicable
- **Validation status:** validation material compares ANISE results against NAIF SPICE; the project reports operational use by the Blue Ghost Mission 1 flight-dynamics team
- **Evidence:** [ANISE validation and flight-heritage documentation](https://github.com/nyx-space/anise/blob/master/anise/README.md).
- **Maintenance status:** active
- **Review status:** reviewed

### REBOUND

- [REBOUND](https://github.com/hannorein/rebound) - An N-body integrator for gravitational dynamics and celestial-mechanics research.
- **Type:** dynamics engine
- **Primary category:** dynamics
- **Simulation scope:** S1-S2
- **Evidence level:** V0
- **Primary domain:** N-body and celestial mechanics
- **Capability tags:** orbit, astrodynamics, mission
- **Language:** C with Python interface
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** not applicable
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### RocketPy

- [RocketPy](https://github.com/RocketPy-Team/RocketPy) - A six-degree-of-freedom rocket flight simulator for launch, ascent, and atmospheric-flight analysis.
- **Type:** vehicle dynamics simulator
- **Primary category:** dynamics
- **Simulation scope:** S2-S3
- **Evidence level:** V0
- **Primary domain:** launch vehicles and re-entry
- **Capability tags:** orbit, astrodynamics, mission
- **Language:** Python
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### Tudat and tudatpy

- [Tudat](https://github.com/tudat-team/tudat) and [tudatpy](https://github.com/tudat-team/tudatpy) - A C++ astrodynamics framework and Python interface for numerical simulation, estimation, and mission analysis.
- **Type:** astrodynamics framework and Python interface
- **Primary category:** dynamics
- **Simulation scope:** S1-S3
- **Evidence level:** V2
- **Primary domain:** numerical astrodynamics and orbit determination
- **Capability tags:** orbit, attitude, propagation, estimation, mission
- **Language:** C++ and Python
- **License:** BSD 3-Clause
- **Platform:** Linux, macOS, and Windows
- **Time advancement:** fixed-step and adaptive numerical integration
- **SIL/HIL:** not documented
- **Validation status:** documented verification and validation against analytical, benchmark, and external-tool reference cases
- **Maintenance status:** active
- **Review status:** reviewed

### PyKEP

- [PyKEP](https://github.com/esa/pykep) - An ESA library for interplanetary trajectory design, Lambert problems, low-thrust optimization, and related astrodynamics computations.
- **Type:** trajectory-design library
- **Primary category:** dynamics
- **Simulation scope:** S1-S2
- **Evidence level:** V1
- **Primary domain:** interplanetary trajectory optimization
- **Capability tags:** orbit, trajectory-optimization, Lambert, low-thrust
- **Language:** C++ and Python
- **License:** GNU General Public License v3.0
- **Platform:** Linux, macOS, and Windows
- **Time advancement:** analytical and optimization-driven trajectory evaluation
- **SIL/HIL:** not applicable
- **Validation status:** repository tests and published examples
- **Maintenance status:** active
- **Review status:** reviewed

### PASEOS

- [PASEOS](https://github.com/aidotse/PASEOS) - An ESA environment for simulating spacecraft operational constraints, onboard autonomy, communications, power, and thermal behavior.
- **Type:** spacecraft operations simulation environment
- **Primary category:** dynamics
- **Simulation scope:** S2-S3
- **Evidence level:** V1
- **Primary domain:** spacecraft operations and autonomy
- **Capability tags:** orbit, autonomy, power, thermal, communications
- **Language:** Python
- **License:** GNU General Public License v3.0
- **Platform:** Python-supported environments
- **Time advancement:** scenario-driven numerical simulation
- **SIL/HIL:** software-in-the-loop integration
- **Validation status:** repository tests and documented examples
- **Maintenance status:** active
- **Review status:** reviewed
