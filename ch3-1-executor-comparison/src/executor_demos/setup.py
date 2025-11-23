from setuptools import setup

package_name = 'executor_demos'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', [
            'launch/spin_one.launch.py',
            'launch/exec_two_nodes.launch.py',
            'launch/exec_spin_once.launch.py',
        ]),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='You',
    author_email='you@example.com',
    maintainer='You',
    maintainer_email='you@example.com',
    description='ROS 2 demos comparing rclpy.spin and SingleThreadedExecutor.',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'spin_one = executor_demos.spin_one:main',
            'exec_two_nodes = executor_demos.exec_two_nodes:main',
            'exec_spin_once = executor_demos.exec_spin_once:main',
        ],
    },
)
