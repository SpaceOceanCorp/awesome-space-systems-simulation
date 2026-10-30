# Spacecraft Subsystems

Reusable power, thermal, communications, data-handling, structures, life support, and fault-management models belong here when they are not full mission simulators.

## Initial Entries

### NASA Common Model Library

- [NASA Common Model Library](https://github.com/nasa/cml) - A collection of reusable spacecraft system and subsystem models designed for NASA Trick simulations.
- **Type:** spacecraft model library
- **Primary category:** subsystems
- **Simulation scope:** S1-S3
- **Evidence level:** V2
- **Primary domain:** reusable spacecraft subsystem modeling
- **Capability tags:** spacecraft, power, thermal, communications, dynamics, Trick
- **Language:** C and C++
- **License:** NASA Open Source Agreement 1.3
- **Platform:** Trick-supported Linux environments
- **Time advancement:** provided by the host Trick simulation
- **SIL/HIL:** host-platform integration
- **Validation status:** repository documentation identifies models as verified and validated for reuse
- **Maintenance status:** active
- **Review status:** reviewed

### Space Water Logistics

- [Space Water Logistics](https://github.com/SpaceOceanCorp/space-water-logistics) - Steady-state screening models for crew water loops, lunar settlement water depletion, and Earth versus lunar water delivery mass ratios.
- **Type:** model library
- **Primary category:** subsystems
- **Simulation scope:** S1
- **Evidence level:** V1
- **Primary domain:** life support water budgets and water logistics
- **Capability tags:** life support, ECLSS, water recovery, ISRU, logistics, trade study
- **Language:** Python and JavaScript
- **License:** Apache-2.0
- **Platform:** Python 3 on Linux, macOS, and Windows; browser calculators
- **Time advancement:** steady-state algebraic models, no time stepping
- **SIL/HIL:** not documented
- **Validation status:** repository tests in GitHub Actions and a Python-to-JavaScript parity test; inputs cite NASA/TP-2015-218570 Rev2 (BVAD) Tables 4-20 and 4-21
- **Maintenance status:** active
- **Review status:** reviewed
