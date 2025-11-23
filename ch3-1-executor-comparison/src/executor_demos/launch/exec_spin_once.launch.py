from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='executor_demos',
            executable='exec_spin_once',
            name='exec_spin_once_driver',
            output='screen'
        )
    ])
