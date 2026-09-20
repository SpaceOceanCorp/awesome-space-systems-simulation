"""Run the deterministic two-body reference case."""

import csv
import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parent


def acceleration(state, mu):
    x, y, z, _, _, _ = state
    radius = math.sqrt(x * x + y * y + z * z)
    factor = -mu / (radius ** 3)
    return factor * x, factor * y, factor * z


def derivative(state, mu):
    ax, ay, az = acceleration(state, mu)
    return state[3], state[4], state[5], ax, ay, az


def rk4_step(state, dt, mu):
    k1 = derivative(state, mu)
    s2 = [value + dt * k / 2 for value, k in zip(state, k1)]
    k2 = derivative(s2, mu)
    s3 = [value + dt * k / 2 for value, k in zip(state, k2)]
    k3 = derivative(s3, mu)
    s4 = [value + dt * k for value, k in zip(state, k3)]
    k4 = derivative(s4, mu)
    return [
        value + dt * (a + 2 * b + 2 * c + d) / 6
        for value, a, b, c, d in zip(state, k1, k2, k3, k4)
    ]


def specific_energy(state, mu):
    x, y, z, vx, vy, vz = state
    radius = math.sqrt(x * x + y * y + z * z)
    speed2 = vx * vx + vy * vy + vz * vz
    return speed2 / 2 - mu / radius


def angular_momentum(state):
    x, y, z, vx, vy, vz = state
    return (y * vz - z * vy, z * vx - x * vz, x * vy - y * vx)


def main():
    inputs = json.loads((ROOT / "inputs.json").read_text(encoding="utf-8"))
    mu = inputs["mu_m3_s2"]
    state = inputs["initial_position_m"] + inputs["initial_velocity_m_s"]
    dt = inputs["reference_step_s"]
    output_interval = inputs["output_interval_s"]
    duration = inputs["duration_s"]
    energy0 = specific_energy(state, mu)
    h0 = angular_momentum(state)
    rows = []
    elapsed = 0.0
    next_output = 0.0
    while elapsed <= duration + 1e-12:
        if elapsed + 1e-12 >= next_output:
            rows.append([elapsed, *state, specific_energy(state, mu), *angular_momentum(state)])
            next_output += output_interval
        step = min(dt, duration - elapsed)
        if step <= 1e-12:
            break
        state = rk4_step(state, step, mu)
        elapsed += step
    output = ROOT / "reference_solution.csv"
    with output.open("w", newline="", encoding="ascii") as handle:
        writer = csv.writer(handle)
        writer.writerow(["time_s", "x_m", "y_m", "z_m", "vx_m_s", "vy_m_s", "vz_m_s", "energy_m2_s2", "hx_m2_s", "hy_m2_s", "hz_m2_s"])
        for row in rows:
            writer.writerow([f"{value:.15e}" for value in row])
    final_energy = specific_energy(state, mu)
    hf = angular_momentum(state)
    h0_norm = math.sqrt(sum(value * value for value in h0))
    hf_norm = math.sqrt(sum(value * value for value in hf))
    print(f"final_time_s={elapsed:.3f}")
    print(f"relative_energy_drift={abs((final_energy - energy0) / energy0):.6e}")
    print(f"relative_angular_momentum_drift={abs((hf_norm - h0_norm) / h0_norm):.6e}")
    print(f"output={output}")


if __name__ == "__main__":
    main()
