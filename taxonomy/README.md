# Taxonomy

The catalog uses two complementary dimensions. Every project has one primary category that owns its full entry, while capability tags provide cross-cutting engineering views without duplicating project records.

## Primary Categories

- **Platform**: integrated spacecraft, vehicle, or mission simulators
- **Dynamics**: orbit, attitude, mission design, celestial mechanics, and launch dynamics
- **GNC**: standalone guidance, navigation, estimation, control, sensors, and actuators
- **Subsystems**: power, thermal, structures, communications, data handling, and fault management
- **Propulsion**: engines, propellants, tanks, internal ballistics, and launch vehicles
- **Environment**: atmosphere, magnetic field, radiation, solar activity, and space weather
- **Robotics**: surface mobility, manipulation, contact, perception, and autonomy
- **Middleware**: HLA/RTI, DDS, message buses, network emulation, and interoperability
- **Co-simulation**: FMI/FMU, Modelica, cross-tool orchestration, and time synchronization
- **Flight software and ground systems**: embedded frameworks, telemetry, commanding, and operations
- **Verification**: runtime monitoring, benchmarks, experimental data, and validation baselines
- **Data**: ephemerides, orbital elements, planetary archives, and reference observations

## Capability Tags

Recommended tags include `orbit`, `attitude`, `navigation`, `control`, `thermal`, `power`, `communications`, `propulsion`, `environment`, `autonomy`, `robotics`, `SIL`, `HIL`, `real-time`, `co-simulation`, and `validation`.

## Scope and Evidence

- **Simulation scope:** `S0` reference/data, `S1` component/algorithm, `S2` subsystem, `S3` spacecraft/mission, `S4` real-time/SIL/HIL.
- **Evidence level:** `V0` unreviewed, `V1` repository tests, `V2` reference benchmarks, `V3` experimental/flight-data validation, `V4` operational mission heritage.
