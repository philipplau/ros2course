from setuptools import find_packages, setup

package_name = 'broadcast_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='paulwetzel',
    maintainer_email='pjw02@pm.me',
    description='Broadcast publisher for msg_package/ Broadcast.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'broadcast = broadcast_node.broadcast:main',
        ],
    },
)
