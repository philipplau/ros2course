from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='executor_demos',
            executable='spin_one',
            name='spin_one_node',
            output='screen'
        )
    ])
