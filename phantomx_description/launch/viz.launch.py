#!/usr/bin/env python3

"""
This launch file publishes the parsed robot file onto Robot State Publisher Topic, the Joint State Publisher and opens rviz to viz.
"""

import os
import xacro

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def get_xacro_to_doc(xacro_file_path):

    doc = xacro.parse(open(xacro_file_path))
    
    xacro.process_doc(doc)

    return doc

def generate_launch_description():

    """Generate Launch XML to run in the background."""

    use_sim_time = LaunchConfiguration('use_sim_time', default='false')
    
    xacro_path = os.path.join(get_package_share_directory('phantomx_description'), 'urdf', 'phantomx.xacro')

    doc = get_xacro_to_doc(xacro_path)

    robot_state_publisher = Node(
                            package='robot_state_publisher', 
                            executable='robot_state_publisher', 
                            name='robot_state_publisher', 
                            output='screen', 
                            parameters=[{'use_sim_time': use_sim_time}, {'robot_description': doc.toxml()}]
                            )
    
    return LaunchDescription([

        DeclareLaunchArgument('use_sim_time', default_value='false'),

        DeclareLaunchArgument('robot_description', default_value=doc.toxml()),

        robot_state_publisher,

    ])
