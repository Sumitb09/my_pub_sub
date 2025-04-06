from setuptools import find_packages, setup

package_name = 'my_pubsub'

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
    maintainer='Sumit',
    maintainer_email='bt22eci030@iiitn.ac.in',
    description='A simple ROS 2 publisher and subscriber example',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = my_pubsub.publisher:main',
            'listener = my_pubsub.subscriber:main',
        ],
    },
)
