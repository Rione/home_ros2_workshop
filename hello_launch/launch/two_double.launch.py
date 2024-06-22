from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='hello_topic',
            executable='iteration_node',
            name='iteration_node',
        ),
        Node(
            package='hello_topic',
            executable='double_node',
            name='double_node',
        ),
        Node(
            package='hello_topic',
            executable='double_node',
            name='quad_node',
            remappings=[
                ('/number', '/double_number'),
                ('/double_number', '/quad_number'),
            ],
        ),
    ])
