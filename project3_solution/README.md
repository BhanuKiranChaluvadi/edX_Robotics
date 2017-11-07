rosnode info /fwk
Node [/fwk]
Publications: 
 * /rosout [rosgraph_msgs/Log]
 * /tf [tf/tfMessage]

Subscriptions: 
 * /joint_states [sensor_msgs/JointState]

Services: 
 * /fwk/set_logger_level
 * /fwk/get_loggers


rosnode info /robot_sim 
Node [/robot_sim]
Publications: 
 * /joint_states [sensor_msgs/JointState]
 * /rosout [rosgraph_msgs/Log]

Subscriptions: 
 * /joint_velocities [unknown type]
 * /joint_positions [unknown type]
 * /joint_command [unknown type]

Services: 
 * /robot_sim/get_loggers
 * /robot_sim/set_logger_level


rosnode info /mover
Node [/mover]
Publications: 
 * /joint_velocities [sensor_msgs/JointState]
 * /rosout [rosgraph_msgs/Log]
 * /ping [std_msgs/Int8]

Subscriptions: None

Services: 
 * /mover/set_logger_level
 * /mover/get_loggers


# Description
1. Joint state publisher publishes at fixed rate (no subscriber call back)
2. rosrun robot_sim position_command.py
	opens up GUI to set /joint_positions and publish.
3. Based on published /joint positions --> /joint_states are computed.
4. From /joint_states forward kinematic node call back is executed.


