# GMAT vs Orekit vs Tudat

This comparison is intended for an initial orbit-propagation or mission-analysis
shortlist. It summarizes task-specific trade-offs; it does not rank the three
projects universally.

## Quick comparison

| Need | Starting point | Why |
| --- | --- | --- |
| GUI-based mission design and scripting | GMAT | Application-oriented mission analysis and documented operational heritage |
| Reusable Java flight-dynamics components | Orekit | Library architecture for propagation, frames, events, attitude, and estimation |
| Research workflows with C++ and Python | Tudat/tudatpy | Numerical astrodynamics framework with Python access and documented reference cases |

## Problem type

Selecting an open-source orbit-propagation or mission-analysis starting point.

## Recommended starting points

Use GMAT for application-centered mission analysis, Orekit for Java library
integration, and Tudat/tudatpy for research-oriented numerical workflows.

## Selection constraints

Compare language, GUI needs, force models, frames, time systems, licensing,
maintenance, and evidence before choosing.

## Common mistakes

Do not treat scope or evidence levels as universal quality scores, and do not
assume that similar outputs imply identical models.

## Comparison dimensions

| Dimension | GMAT | Orekit | Tudat/tudatpy |
| --- | --- | --- | --- |
| Primary form | Mission-analysis application | Flight-dynamics library | Astrodynamics framework and Python interface |
| Typical entry point | Mission script and GUI workflow | Java API integration | C++ or Python numerical workflow |
| Catalog scope | S3 | S1-S2 | S1-S3 |
| Catalog evidence | V4 | V4 | V2 |
| Main language | C++ and domain-specific scripting | Java | C++ and Python |
| Best fit | Mission design and operational analysis | Embedded dynamics services and custom applications | Research, estimation, and numerical simulation |

The scope and evidence values above are the current catalog values. They are
not interchangeable quality scores.

## Good fit and poor fit

### GMAT

Good fit:

- mission-design workflows;
- GUI-assisted analysis;
- scriptable mission scenarios;
- users who value documented mission and operational heritage.

Poor fit:

- a lightweight embedded dynamics library;
- a complete real-time flight-software HIL environment without additional
  integration work.

### Orekit

Good fit:

- Java applications;
- reusable orbit, attitude, frame, event, and estimation services;
- integration into larger mission-analysis software.

Poor fit:

- users who require a standalone GUI-first mission-design application;
- projects that need a complete spacecraft-system simulator from one library.

### Tudat/tudatpy

Good fit:

- research and education workflows;
- custom numerical models;
- C++ and Python experimentation;
- propagation and estimation studies.

Poor fit:

- users who need a turnkey mission-design GUI;
- projects that have not yet defined their force models, frames, and validation
  criteria.

## Selection rule

Choose the starting point based on the surrounding system, not only on
propagator features:

1. Choose GMAT for an application-centered mission-analysis workflow.
2. Choose Orekit for Java-based library integration.
3. Choose Tudat/tudatpy for a research-oriented numerical workflow.
4. Validate the selected configuration with a defined reference case.

Related pages: [orbit simulator guide](open-source-orbit-simulators.md),
[orbit and flight dynamics catalog](../tools/orbit-and-flight-dynamics.md), and
[two-body benchmark](../benchmarks/two-body-orbit-propagation/README.md).

## Limitations

This is a task-specific comparison, not an official integration or a claim of
joint validation.
