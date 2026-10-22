import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node


def generate_launch_description():
    ins_default_config = os.path.join('/config', 'ws_bb_ros2_config', 'params_blueboat_ins.yaml')
    republisher_default_config = os.path.join('/config', 'ws_bb_ros2_config', 'ros2lcm_republisher.yaml')

    ros2lcm_pkg_share = get_package_share_directory('mola_lcm_to_ros2')

    return LaunchDescription([
        DeclareLaunchArgument(
            'ins_config', default_value=ins_default_config,
            description='inertial sense config yaml'
        ),

        DeclareLaunchArgument(
            'ros2lcm_republisher_config', default_value=republisher_default_config,
            description='ros2 to lcm republisher config yaml'
        ),

        # inertial sense
        Node(
            package = 'inertial_sense_ros2',
            executable = 'inertial_sense_ros2_node',
            arguments = [LaunchConfiguration('ins_config')]
        ),

        # ROS 2 to LCM republishing
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(ros2lcm_pkg_share, 'launch', 'ros2lcm_republisher.launch.py'),
            ),
            launch_arguments={'use_sim_time': 'false',
                              'odometry_enable': 'true',
                              'gps_enable': 'true',
                              'gps_config': LaunchConfiguration('ros2lcm_republisher_config'),
                              'odometry_config': LaunchConfiguration('ros2lcm_republisher_config')}.items(),
        ),
    ])
