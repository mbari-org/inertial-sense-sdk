
from launch import LaunchDescription
from launch.actions import ExecuteProcess


def generate_launch_description():

    return LaunchDescription([

        # ROS 2 Bag
        ExecuteProcess(
            cmd=['ros2', 'bag', 'record',
                 '-s', 'mcap',
                 '--compression-mode=file',
                 '--compression-format=zstd',
                 #'/RTK_cmp/info',
                 #'/RTK_cmp/rel',  # contains AR ratio for compassing
                 #'/RTK_pos/info',
                 #'/RTK_pos/rel',  # contains AR ratio for positioning
                 # turning off to try lower cpu --
                 '/inertial_sense/baro',
                 '/inertial_sense/gps1/NavSatFix',
                 '/inertial_sense/gps1/info',
                 '/inertial_sense/gps1/pos_vel',  # rtk lat/lon, accuracy
                 #'/inertial_sense/gps2/NavSatFix',
                 #'/inertial_sense/gps2/info',
                 # turning off to try lower cpu --
                 '/inertial_sense/imu',
                 #'/inertial_sense/inl2_states',
                 '/inertial_sense/ins_quat_uvw_lla',
                 #'/inertial_sense/ins_quat_ve_ecef',
                 #'/inertial_sense/mag',
                 #'/inertial_sense/odom_ins_ecef',  # rtk fused odometry (NOTE: must set refLLA)
                 #'/inertial_sense/odom_ins_enu',  # rtk fused odometry (NOTE: must set refLLA)
                 '/inertial_sense/odom_ins_ned',  # rtk fused odometry (NOTE: must set refLLA)
                 #'/inertial_sense/pimu',
                 #'/inertial_sense/strobe_in',
                 '/sys_fault',
                 # RTK3B Heading
                 '/aimplusstatus',
                 '/attcoveuler',
                 '/atteuler',
                 '/diagnostics',
                 '/galauthstatus',
                 '/poscovgeodetic',
                 '/pvtgeodetic',
                 '/rfstatus',
            ],
            cwd='/data',
            output='screen'
        )
    ])
