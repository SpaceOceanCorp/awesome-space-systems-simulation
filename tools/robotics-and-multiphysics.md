# Robotics and Multiphysics

This section covers adjacent platforms that become relevant when spacecraft, landers, rovers, manipulators, terrain, contact, or multiphysics models must be simulated together.

## Initial Entries

### Gazebo

- [Gazebo](https://gazebosim.org/) - An open-source robotics simulator used for physics, sensors, terrain, and robot middleware integration.
- **Type:** adjacent robotics simulator
- **Primary category:** robotics
- **Simulation scope:** S2-S3
- **Evidence level:** V0
- **Primary domain:** robotics and contact dynamics
- **Capability tags:** robotics, autonomy, contact, perception
- **Language:** C++
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### Isaac Sim

- [Isaac Sim](https://developer.nvidia.com/isaac/sim) - A GPU-accelerated robotics simulation platform for perception, autonomy, and manipulation workflows.
- **Type:** adjacent robotics simulator
- **Primary category:** robotics
- **Simulation scope:** S2-S3
- **Evidence level:** V0
- **Primary domain:** robotics, autonomy, and perception
- **Capability tags:** robotics, autonomy, contact, perception
- **Language:** Python and C++ interfaces
- **License:** restricted components; pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** reference-only

### Project Chrono

- [Project Chrono](https://projectchrono.org/) - An open-source multiphysics and multibody dynamics engine for vehicle, robotic, and contact simulations.
- **Type:** multiphysics engine
- **Primary category:** robotics
- **Simulation scope:** S1-S3
- **Evidence level:** V0
- **Primary domain:** multibody, contact, and multiphysics
- **Capability tags:** robotics, autonomy, contact, perception
- **Language:** C++
- **License:** pending review
- **Platform:** pending review
- **Time advancement:** pending review
- **SIL/HIL:** pending review
- **Validation status:** pending review
- **Maintenance status:** pending review
- **Review status:** pending review

### Space Robotics Bench

- [Space Robotics Bench](https://github.com/AndrejOrsula/space_robotics_bench) - A benchmark and task suite for learning and evaluating space-robotics manipulation and autonomy.
- **Type:** benchmark and simulation task suite
- **Primary category:** robotics
- **Simulation scope:** S2-S3
- **Evidence level:** V2
- **Primary domain:** space robotics and autonomy
- **Capability tags:** robotics, autonomy, contact, perception
- **Language:** Python
- **License:** MIT OR Apache License 2.0; project-created assets are CC0 where stated
- **Platform:** Linux with NVIDIA Isaac Lab and supported GPU hardware
- **Time advancement:** Isaac Sim physics simulation
- **SIL/HIL:** software-in-the-loop integration
- **Validation status:** published benchmark tasks and reproducible training/evaluation configurations
- **Maintenance status:** active
- **Review status:** reviewed

### Int-Ball2 Simulator

- [Int-Ball2 Simulator](https://github.com/jaxa/int-ball2_simulator) - JAXA's ROS/Gazebo simulation environment for the Int-Ball2 free-flying robot inside the International Space Station.
- **Type:** space robotics simulation platform
- **Primary category:** robotics
- **Simulation scope:** S2-S3
- **Evidence level:** V2
- **Primary domain:** free-flying robotics and onboard autonomy
- **Capability tags:** robotics, autonomy, perception, navigation, ROS, Gazebo
- **Language:** C++, Python, and ROS launch/configuration files
- **License:** Apache License 2.0
- **Platform:** Ubuntu 18.04, ROS Melodic, and Gazebo 9
- **Time advancement:** Gazebo physics simulation
- **SIL/HIL:** software-in-the-loop integration
- **Validation status:** repository simulator, ground-support interface, and mission publications support representative Int-Ball2 workflows; no public flight-data correlation of the simulator was reviewed
- **Maintenance status:** active
- **Review status:** reviewed
