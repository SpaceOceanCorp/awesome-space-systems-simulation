# Two-Body Orbit Propagation

This benchmark is a deterministic, runnable minimum case for comparing orbit
propagation tools against an analytic two-body reference. It intentionally
excludes J2, drag, third-body forces, maneuvers, and attitude dynamics.

## Problem statement

Propagate a point mass in a central gravitational field using SI units and an
inertial frame. The reference implementation uses a high-accuracy numerical
integration of the two-body equations and writes a CSV state history.

## Inputs

The fixed case is stored in [inputs.json](inputs.json): a low-eccentricity
Earth orbit, a 600 second duration, and 60 second output spacing. Do not change
these values when reporting comparable results.

## Reference implementation

Run the standard-library implementation from this directory:

```text
python run_reference.py
```

It writes `reference_solution.csv` deterministically and prints final-state,
energy-drift, and angular-momentum-drift metrics. The script uses a fixed-step
fourth-order Runge-Kutta integrator with a small reference step; it is a
reference baseline, not a claim that RK4 is the best production propagator.

## Required outputs

Comparisons should report time history, final position and velocity, specific
mechanical energy, specific angular momentum, tool version, integrator and
step-size settings, and the operating environment.

## Error metrics

At minimum report `final_position_error`, `final_velocity_error`,
`maximum_position_error`, `maximum_velocity_error`,
`relative_energy_drift`, `relative_angular_momentum_drift`, and
`runtime_seconds`. State the norm, units, reference state, and evaluation time.

## Cross-tool results

No cross-tool numerical results have been reviewed yet. A result must include
the exact command or script, tool version, configuration, generated metrics,
and any frame or time-system conversion.

## Validation status

The analytic case and deterministic reference implementation are reviewed.
Cross-tool validation is pending reproduction and independent review.

## Reproduction record

Record the input file checksum, Python version, command, runtime, and output
metrics. Keep generated CSV files out of pull requests unless they are needed
to document a reviewed comparison.

## Status

Reference implementation available; cross-tool results pending.

## Last reviewed

2026-09-20

## Known limitations

This case does not test perturbations, event handling, maneuvers, time scales,
or long-duration numerical stability. Those belong in follow-up benchmarks.
