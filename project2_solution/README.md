# Transformations
publishing static tranformations and visualizing in Rviz.

# project description: Static transformations:
https://courses.edx.org/courses/course-v1:ColumbiaX+CSMM.103x+1T2017/courseware/c3368f33e7ca49cfb0a2c3275f6fbda0/c64f51da0c2d41b19dc5479f9d74222d/?child=first
1. Node publish static transformation to tf topic.
2. rViz is used to visualize the co-ordinate frames by subscribing to tf and by using markerss.

# marker_publisher.cpp
If we observer the file we find all the position and orientaion of all the markers are set to zero.
But in rViz their poisiton and orientaion are nicely assingned. The trick lies in the "object.header.frame_id" that 
was set accordingly. rViz will handle tansformations accordingly.

# Tutorials:
http://wiki.ros.org/tf2/Tutorials
http://wiki.ros.org/tf2/Tutorials/Writing%20a%20tf2%20static%20broadcaster%20%28Python%29

# Learnings:

1. Rotation and then translation should be performed - operations are performed in the way the matrices are entered in the concatenation matrix.
2. In normal transformation t1.transformation - tranformation is always performed first and then rotaion irrespective of how you enter (in example.py).
3. Yaw-pitch - row angle its zyx. First the operations are performed on the z-axis and then Y , then X.
4. The rotation is performed using axis angle - dot, cross product between the current and desired axis results in axis angle.
4. In transformations.quaternion_about_axis() . The angle is entered in radians.
