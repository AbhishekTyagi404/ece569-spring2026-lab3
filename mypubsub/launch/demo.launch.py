from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypubsub',
            executable='publisher',
            output='screen'
        ),
        Node(
            package='mypubsub',
            executable='subscriber',
            output='screen'
        ),
    ])
