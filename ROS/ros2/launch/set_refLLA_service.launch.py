from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration
from launch.actions import ExecuteProcess


def generate_launch_description():
    # Declare refLLA as a launch argument
    declare_refLLA_argument = DeclareLaunchArgument(
        'refLLA',
        default_value='0.0,0.0,0.0',
        description='Reference Lat, Lon, Alt array as a string'
    )

    # Define the service name and type
    set_reflla_name = "/set_refLLA_value"
    set_reflla_type = "inertial_sense_ros2/srv/RefLLAUpdate"

    # OpaqueFunction to create the command dynamically in the context
    def execute_service_call(context):
        # Get refLLA value in context
        refLLA_value = context.launch_configurations.get('refLLA', '0.0,0.0,0.0')
        refLLA_array = [float(x) for x in refLLA_value.split(',')]

        # Format the command correctly
        command = [
            'ros2', 'service', 'call',
            set_reflla_name,
            set_reflla_type,
            f"lla: {refLLA_array}"
        ]

        # Return ExecuteProcess action
        return [ExecuteProcess(
            cmd=command,
            shell=False,
            output='screen'
        )]

    # Create a LaunchDescription and add actions
    return LaunchDescription([
        declare_refLLA_argument,
        OpaqueFunction(function=execute_service_call)
    ])
