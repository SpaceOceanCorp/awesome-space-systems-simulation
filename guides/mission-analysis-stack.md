# Mission Analysis Stack

This guide describes a task-oriented combination for mission analysis,
propagation, geometry, and reference-data work. It is a curated starting point,
not an official toolchain or a claim of joint validation.

## Suggested composition

| Responsibility | Starting point | Catalog entry |
| --- | --- | --- |
| Mission-design application | GMAT | [GMAT](../tools/orbit-and-flight-dynamics.md#gmat) |
| Reusable flight-dynamics library | Orekit | [Orekit](../tools/orbit-and-flight-dynamics.md#orekit) |
| Research-oriented numerical propagation | Tudat/tudatpy | [Tudat and tudatpy](../tools/orbit-and-flight-dynamics.md#tudat-and-tudatpy) |
| Ephemerides and mission geometry | SPICE Toolkit or ANISE | [Dynamics catalog](../tools/orbit-and-flight-dynamics.md#spice-toolkit) |
| Public orbital and planetary inputs | CelesTrak or JPL HORIZONS | [Data catalog](../tools/data-and-ephemeris.md) |

## Problem type

Mission analysis workflows combining propagation, geometry, ephemerides, and
reference data.

## Recommended starting points

Begin with GMAT, Orekit, or Tudat/tudatpy according to application, language,
and numerical workflow needs.

## Selection constraints

Align frames, epochs, force models, event handling, units, and input-data
provenance before comparing results.

## Common mistakes

Do not combine outputs without documenting time scales, interpolation, force
models, or maneuver conventions.

## Integration questions

Define these interfaces before comparing outputs:

- reference frame and central-body conventions;
- time scale and epoch representation;
- force models and perturbations;
- ephemeris source and interpolation policy;
- event detection and maneuver conventions;
- output units and state-vector ordering;
- reference data and error tolerances.

## Good fit

- mission concept studies;
- independent cross-checks between application and library workflows;
- reproducible propagation and geometry investigations;
- building a traceable chain from public ephemerides to mission analysis.

## Important limitations

- Similar project names do not imply identical force models or time systems.
- Operational heritage is evidence about use, not a guarantee for every model
  configuration.
- A stack must be validated with a defined reference case before results are
  compared across tools.

## Related resources

- [Open-source orbit simulators](open-source-orbit-simulators.md)
- [GMAT vs Orekit vs Tudat](gmat-vs-orekit-vs-tudat.md)
- [Two-body orbit propagation benchmark](../benchmarks/two-body-orbit-propagation/README.md)
