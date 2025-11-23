from setuptools import find_packages, setup

package_name = 'listener_node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='paulwetzel',
    maintainer_email='pjw02@pm.me',
    description='Python client and listener nodes for Transmit service.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'service_client = listener_node.service_client:main',
            'listener = listener_node.listener:main',
        ],
    },
)
