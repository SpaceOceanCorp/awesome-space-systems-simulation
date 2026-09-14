# Guidance, Navigation and Control

> Initial entries will be added as the catalog is established. Follow the root contribution guide when submitting a project.

## Curation Dimensions

- Guidance laws and trajectory planning
- Attitude and orbit determination
- Kalman filtering and sensor fusion
- Attitude, orbit, and integrated control
- Actuators, sensors, and fault injection

## Initial Cross-References

The following integrated platforms already in this catalog expose GNC-relevant capabilities. Their primary entries remain in the platform index to avoid duplicate project records.

- [Basilisk](simulation-platforms.md) - Modular dynamics, estimation, guidance, and control workflows.
- [MuSCAT](simulation-platforms.md) - Multi-spacecraft autonomy, navigation, and attitude-control studies.
- [42](simulation-platforms.md) - Spacecraft attitude and orbit dynamics for GNC experiments.
- [Orekit](orbit-and-flight-dynamics.md) - Orbit and attitude determination primitives for GNC pipelines.

## Initial Entries

### AcubeSAT ADCS Simulation

- [AcubeSAT ADCS Simulation](https://github.com/AcubeSAT/adcs-simulation) - The attitude and orbit determination and control simulation developed for the AcubeSAT nanosatellite mission.
- **Type:** spacecraft ADCS simulation
- **Primary category:** GNC
- **Simulation scope:** S1-S2
- **Evidence level:** V1
- **Primary domain:** attitude determination and control
- **Capability tags:** attitude, navigation, control, sensors, actuators, CubeSat
- **Language:** MATLAB and supporting analysis files
- **License:** MIT
- **Platform:** MATLAB-compatible environments
- **Time advancement:** scenario-specific numerical simulation
- **SIL/HIL:** not documented
- **Validation status:** documented subsystem analyses and design-review artifacts produced for the AcubeSAT mission; no public flight-data validation was reviewed
- **Maintenance status:** active reference
- **Review status:** reviewed

## Entry Policy

Future standalone GNC entries must provide a reusable algorithm, component model, or runnable subsystem example. Integrated platforms should be cross-referenced here and documented once in their primary category.
