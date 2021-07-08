import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.substitutions import Command

def generate_launch_description():

    pkg_ros_ign_gazebo = get_package_share_directory('ros_ign_gazebo')

    pkg_rugved_ign = get_package_share_directory('phantomx_ignition')

    ign = IncludeLaunchDescription(PythonLaunchDescriptionSource(os.path.join(pkg_ros_ign_gazebo, 'launch', 'ign_gazebo.launch.py'),),)

    spawn = Node(package='ros_ign_gazebo', executable='create', arguments=['-name', 'phantomx', '-topic', '/robot_description'])

    ign_args = DeclareLaunchArgument('ign_args', default_value=[os.path.join(pkg_rugved_ign, 'worlds', 'phntwrld.sdf')])
    
    bridge = Node(
            package='ros_ign_bridge', 
            executable='parameter_bridge', 
            arguments=['/cmd_vel@geometry_msgs/msg/Twist@ignition.msgs.Twist',])

    return LaunchDescription([ign_args, ign, spawn])
