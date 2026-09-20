# Open-Source Orbit Simulators

This guide is for orbit propagation, mission analysis, trajectory design, and
related astrodynamics workflows. It is a navigation aid for the catalog, not a
universal ranking.

## Start with the problem

| Need | Starting points |
| --- | --- |
| Mission-design application and scripting | GMAT |
| Java-based flight-dynamics library | Orekit |
| C++ or Python numerical astrodynamics | Tudat and tudatpy |
| Python interactive astrodynamics | poliastro |
| Interplanetary trajectory design and optimization | PyKEP |
| High-performance orbit determination and propagation | Nyx |
| Ephemerides and mission geometry | SPICE Toolkit, ANISE |

## Problem type

Orbit propagation, trajectory design, mission analysis, and related
astrodynamics workflows.

## Recommended starting points

Start with GMAT, Orekit, or Tudat/tudatpy, then narrow by language, GUI needs,
force models, and evidence requirements.

## Selection constraints

Compare scope, propagation models, frames, time systems, license, maintenance,
SIL/HIL needs, and validation evidence.

## Common mistakes

Do not treat a dynamics library as a complete spacecraft simulator or assume
that flight heritage validates every configuration.

## Comparison dimensions

Before selecting a tool, compare:

- simulation scope: component, subsystem, spacecraft, or mission;
- propagation models and event handling;
- language and integration surface;
- license and access constraints;
- time advancement and numerical solver choices;
- validation evidence and operational heritage;
- maintenance status and documentation quality;
- support for SIL, HIL, or distributed simulation.

## Candidate entries

| Project | Best first question | Catalog entry |
| --- | --- | --- |
| GMAT | Do I need a mission-analysis application with documented mission heritage? | [GMAT](../tools/orbit-and-flight-dynamics.md#gmat) |
| Orekit | Do I need a reusable Java flight-dynamics library? | [Orekit](../tools/orbit-and-flight-dynamics.md#orekit) |
| Tudat/tudatpy | Do I need a research-oriented C++ and Python numerical framework? | [Tudat and tudatpy](../tools/orbit-and-flight-dynamics.md#tudat-and-tudatpy) |
| poliastro | Do I need an interactive Python astrodynamics library? | [poliastro](../tools/orbit-and-flight-dynamics.md#poliastro) |
| PyKEP | Do I need interplanetary trajectory design and optimization primitives? | [PyKEP](../tools/orbit-and-flight-dynamics.md#pykep) |
| Nyx | Do I need a high-performance astrodynamics engine with orbit-determination workflows? | [Nyx](../tools/orbit-and-flight-dynamics.md#nyx) |
| SPICE Toolkit | Do I need mission geometry and ephemeris access rather than a standalone propagator? | [SPICE Toolkit](../tools/orbit-and-flight-dynamics.md#spice-toolkit) |

## Important caveats

- A dynamics library is not automatically a complete spacecraft simulator.
- Mission heritage does not remove the need for project-specific verification.
- Archived or pending entries should not be treated as current operational
  recommendations without additional review.
- Propagator accuracy depends on force models, frames, time systems, initial
  conditions, and numerical settings, not only on the project name.

## Next step

Use the [GMAT vs Orekit vs Tudat comparison](gmat-vs-orekit-vs-tudat.md), then
run the [two-body orbit propagation benchmark](../benchmarks/two-body-orbit-propagation/README.md)
before making a tool-selection decision.

## Limitations

This guide is a navigation aid for the catalog, not a universal ranking or a
claim that the listed tools have been jointly validated.
