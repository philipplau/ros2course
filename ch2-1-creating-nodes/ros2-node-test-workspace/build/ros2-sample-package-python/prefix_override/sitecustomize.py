import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/ubuntu/ros2course/ch2-1-creating-nodes/ros2-node-test-workspace/install/ros2-sample-package-python'
