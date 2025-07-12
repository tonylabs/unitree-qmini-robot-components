# Unitree Qmini Robot Resources

```mermaid
flowchart TD
    subgraph "Qmini Robot"
        Body["Base Link (躯干)"]
        
        %% Left Leg (LL)
        LL_HipYaw["LL Hip Yaw"]
        LL_HipRoll["LL Hip Roll"]
        LL_HipPitch["LL Hip Pitch"]
        LL_Knee["LL Knee"]
        LL_Ankle["LL Ankle"]
        
        %% Right Leg (RL)
        RL_HipYaw["RL Hip Yaw"]
        RL_HipRoll["RL Hip Roll"]
        RL_HipPitch["RL Hip Pitch"]
        RL_Knee["RL Knee"]
        RL_Ankle["RL Ankle"]
        
        %% Left Leg Connections
        Body --> LL_HipYaw
        LL_HipYaw --> LL_HipRoll
        LL_HipRoll --> LL_HipPitch
        LL_HipPitch --> LL_Knee
        LL_Knee --> LL_Ankle
        
        %% Right Leg Connections
        Body --> RL_HipYaw
        RL_HipYaw --> RL_HipRoll
        RL_HipRoll --> RL_HipPitch
        RL_HipPitch --> RL_Knee
        RL_Knee --> RL_Ankle
    end
```

### How to use the qmini_description

1. Navigate to your workspace:

```bash
$ sudo apt-get install python3-colcon-common-extensions
$ pip install catkin_pkg
$ cd /home/ubuntu/Documents/GitHub/unitree-qmini-robot-components/qmini_description
```

2. Build the package:

```bash
$ colcon build --packages-select qmini_description
```

3. Source the workspace:

```bash
$ source install/setup.bash
```

4. Launch the robot description:

```bash
$ ros2 launch qmini_description view_qmini.launch.py
```