Solution to project -3 Robotics couse work for edX by university of columbia
https://courses.edx.org/courses/course-v1:ColumbiaX+CSMM.103x+1T2017/course/

# Description
1. Joint state publisher publishes at fixed rate (no subscriber call back)
2. rosrun robot_sim position_command.py
	opens up GUI and publish set /joint_positions.
3. Based on published /joint positions --> /joint_states are computed.
4. From /joint_states forward kinematic node call back is executed.


# Forward Kinematics Implementaion
1. Check the picture in current folder named "transformation.png"
2. KinematicChain.pdf

# MODIFY:
I am running Ubuntu 16.04 with ROS Kinect, but catkin_make gives out an error
To fix this, you will need to modify the file located in robot_sim/CMakeLists.txt
# replace line 34
link_directories(/opt/ros/indigo/lib/)
# with
link_directories(/opt/ros/kinetic/lib/)


# RUN:
> roslaunch robot_sim kuka_lwr.launch

# IGNORE (if present):
1. Unknown tag: com
   Scalar element defined multiple times: collision
2. The STL file 'package://lwr_defs/meshes/lwr/link_5.STL' is malformed. 
	It starts with the word 'solid', indicating that it's an ASCII STL 
	file, but it does not contain the word 'endsolid' so it is either a
	 malformed ASCII STL file or it is actually a binary STL file. 
	 Trying to interpret it as a binary STL file instead.





