# Benchmarks

This directory contains reproducible minimum validation cases. Each case should include a problem definition, input parameters, reference results, error metrics, and run instructions.

Suggested initial cases:

1. [Two-body orbit propagation](two-body-orbit-propagation/README.md)
2. Long-term orbital evolution with J2 perturbation
3. Quaternion attitude stabilization control
4. EKF attitude estimation
5. A simplified spacecraft mission mode machine

The first benchmark is defined as a reproducible protocol. Numerical results
must be marked as validated only after a tool has been run against the stated
reference equations and tolerances.

## Benchmark page template

Every benchmark page should include:

- Problem statement
- Reference inputs
- Required outputs
- Error metrics
- Reproduction record
- Validation status and known limitations

Runnable benchmarks should also provide fixed inputs, a reference
implementation, deterministic output, and a requirements file when external
dependencies are needed.
