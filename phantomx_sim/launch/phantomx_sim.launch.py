#!/usr/bin/python3

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from launch.actions import ExecuteProcess, IncludeLaunchDescription, RegisterEventHandler
from launch.event_handlers import OnProcessExit

from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    
    viz = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('phantomx_description'), 'launch'), '/viz.launch.py']),)
    
    ign = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('phantomx_ignition'), 'launch'), '/ign.launch.py']),)
    
    return LaunchDescription([viz, ign])

