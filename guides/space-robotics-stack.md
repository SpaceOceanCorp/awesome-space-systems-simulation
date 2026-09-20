# Space Robotics Stack

This guide is for surface mobility, manipulation, perception, contact, and
autonomy studies. The listed components are curated starting points; they are
not presented as a single validated integration.

## Suggested composition

| Responsibility | Starting point | Catalog entry |
| --- | --- | --- |
| Robot and sensor simulation | Gazebo | [Robotics catalog](../tools/robotics-and-multiphysics.md) |
| Contact and multiphysics modeling | Project Chrono | [Robotics catalog](../tools/robotics-and-multiphysics.md) |
| Space robotics interfaces | Space ROS Demos | [Reference integrations](../examples/README.md) |
| Terrain and manipulation studies | Space Robotics Bench | [Robotics catalog](../tools/robotics-and-multiphysics.md) |
| On-orbit robotics reference | Int-Ball2 Simulator | [Robotics catalog](../tools/robotics-and-multiphysics.md) |

## Problem type

Surface mobility, manipulation, perception, contact, and autonomy studies.

## Recommended starting points

Use Gazebo or Project Chrono for general simulation foundations and consult the
space-specific references for interfaces and mission context.

## Selection constraints

Check physics ownership, sensor and actuator models, coordinate frames,
latencies, ROS interfaces, real-time requirements, and asset licenses.

## Common mistakes

Do not infer space-environment fidelity or flight readiness from a general
robotics demonstration.

## Integration questions

- Which simulator owns time and physics integration?
- Are terrain, contact, and actuator models deterministic and reproducible?
- Which ROS or message interfaces cross the simulation boundary?
- What sensors, latencies, and coordinate frames are modeled?
- Is the target SIL, HIL, real-time, or offline analysis?
- Which assets and licenses can be redistributed?

## Good fit

- rover and manipulator algorithm studies;
- sensor and perception experiments;
- contact and terrain model comparisons;
- ROS-based integration prototypes;
- autonomy workflows that need a repeatable simulated environment.

## Important limitations

- General robotics support does not imply space-environment fidelity.
- A demonstration integration is not evidence of flight readiness.
- Contact, terrain, sensor, and latency assumptions should be recorded with any
  reported result.
- Restricted-access or reference-only projects require separate access review.

## Related resources

- [Robotics and multiphysics catalog](../tools/robotics-and-multiphysics.md)
- [Examples and reference integrations](../examples/README.md)
- [Catalog taxonomy](../taxonomy/README.md)
