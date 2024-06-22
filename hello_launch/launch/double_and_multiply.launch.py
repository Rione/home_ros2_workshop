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
            package='hello_param',
            executable='multiply_node',
            name='multiply_node',
            remappings=[
                ('/number', '/double_number'),
            ],
            parameters=[
                {'m_number': 4},
            ]
        ),
    ])
