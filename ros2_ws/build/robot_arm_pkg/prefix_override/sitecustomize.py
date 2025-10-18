import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/prudy/Task4/ros2_ws/install/robot_arm_pkg'
