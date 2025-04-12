from setuptools import find_packages, setup

package_name = 'robot_joint_publisher'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tommywu',
    maintainer_email='tommywu052@gmail.com',
    description='A ROS2 node to publish robot joint states to /joint_states',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['joint_state_publisher = robot_joint_publisher.joint_state_publisher:main'
        ],
    },
)
