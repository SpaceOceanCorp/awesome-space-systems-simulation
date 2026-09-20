# CubeSat ADCS Stack

This is a curated composition guide for teams evaluating a CubeSat attitude
determination and control workflow. It describes a possible division of
responsibilities; it does not claim that the projects below form an official,
validated integration.

## Suggested composition

| Responsibility | Starting point | Catalog entry |
| --- | --- | --- |
| Spacecraft dynamics and control experiments | Basilisk | [Simulation platforms](../tools/simulation-platforms.md#basilisk) |
| Independent attitude and orbit dynamics reference | 42 | [Simulation platforms](../tools/simulation-platforms.md#42) |
| CubeSat ADCS subsystem workflow | AcubeSAT ADCS Simulation | [GNC catalog](../tools/gnc.md#acubesat-adcs-simulation) |
| Flight-software integration | NASA cFS or F Prime | [Flight software catalog](../tools/flight-software-and-ground.md) |
| Mission geometry and ephemeris inputs | SPICE Toolkit | [Dynamics catalog](../tools/orbit-and-flight-dynamics.md#spice-toolkit) |

## Problem type

CubeSat attitude determination, control, dynamics, and flight-software integration.

## Recommended starting points

Start with Basilisk for an integrated research workflow, then use 42 and the
GNC entry as independent comparison points.

## Selection constraints

Check state ownership, sample rates, SIL/HIL boundaries, license compatibility,
and the evidence level of each selected component.

## Common mistakes

Do not treat compatible interfaces as a validated end-to-end ADCS stack, and do
not compare results without matching frames and tolerances.

## Integration questions

Before combining tools, define:

- the state and frame exchanged between dynamics and control;
- sensor and actuator sampling rates;
- time synchronization and ownership of propagation;
- fault-injection boundaries;
- the SIL/HIL boundary;
- the test oracle and acceptance tolerances;
- the license compatibility of every component.

## Good fit

- early CubeSat ADCS architecture studies;
- comparison of control and estimation algorithms;
- separating spacecraft dynamics from flight-software experiments;
- building a traceable path from reference dynamics to embedded execution.

## Important limitations

- The catalog entries have different scopes and evidence levels.
- A set of compatible projects is not the same as a validated integration.
- Flight-software heritage does not validate a particular ADCS model or control
  law.
- Use a common attitude-stabilization case before comparing results.

## Related resources

- [Spacecraft attitude simulation](spacecraft-attitude-simulation.md)
- [Two-body orbit propagation benchmark](../benchmarks/two-body-orbit-propagation/README.md)
- [Catalog taxonomy](../taxonomy/README.md)
