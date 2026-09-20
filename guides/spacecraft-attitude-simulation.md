# Spacecraft Attitude Simulation

This guide covers attitude dynamics, estimation, control, sensors, and
actuators. It distinguishes standalone GNC work from integrated spacecraft
simulation platforms.

## Start with the problem

| Need | Starting points |
| --- | --- |
| Integrated spacecraft dynamics and GNC experiments | Basilisk, 42 |
| Multi-spacecraft autonomy and control studies | MuSCAT |
| CubeSat ADCS subsystem work | AcubeSAT ADCS Simulation |
| Orbit and attitude primitives inside a Java workflow | Orekit |

## Problem type

Attitude dynamics, estimation, control, sensors, actuators, and spacecraft GNC.

## Recommended starting points

Start with Basilisk or 42 for integrated experiments, MuSCAT for
multi-spacecraft autonomy, and the GNC catalog for subsystem-specific work.

## Selection constraints

Compare attitude representation, integrators, sensor and actuator models,
spacecraft scope, SIL/HIL support, and validation evidence.

## Common mistakes

Do not treat one attitude-control example as a complete spacecraft simulator or
compare control performance without common initial conditions and limits.

## Candidate comparison

| Project | Primary use | Catalog entry |
| --- | --- | --- |
| Basilisk | Modular spacecraft dynamics, estimation, guidance, and control | [Simulation platforms](../tools/simulation-platforms.md#basilisk) |
| 42 | Spacecraft attitude and orbit dynamics for GNC experiments | [Simulation platforms](../tools/simulation-platforms.md#42) |
| MuSCAT | Multi-spacecraft navigation, attitude control, and autonomy studies | [Simulation platforms](../tools/simulation-platforms.md#muscat) |
| AcubeSAT ADCS Simulation | Nanosatellite attitude determination and control | [GNC catalog](../tools/gnc.md#acubesat-adcs-simulation) |
| Orekit | Orbit and attitude determination primitives in a dynamics library | [Orbit and flight dynamics](../tools/orbit-and-flight-dynamics.md#orekit) |

## Selection dimensions

Compare the candidates using:

- rigid-body and environmental dynamics;
- attitude representation and numerical integration;
- sensor and actuator models;
- estimation and control interfaces;
- spacecraft or subsystem scope;
- multi-spacecraft support;
- SIL/HIL and real-time support;
- validation evidence and operational heritage.

## Important caveats

- An attitude-control example is not automatically a complete spacecraft
  simulator.
- A platform's catalog scope and evidence level are separate fields.
- Control performance should be compared with common initial conditions,
  actuator limits, sensor assumptions, and numerical tolerances.
- The catalog currently provides selection guidance; it does not claim that the
  listed projects have been jointly validated in one common scenario.

## Next step

Start with the project's primary catalog entry, then define a common attitude
stabilization case using the [benchmark roadmap](../benchmarks/README.md).

## Limitations

The catalog provides selection guidance only; it does not claim joint
validation of the listed projects in a common scenario.
