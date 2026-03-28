from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'mypubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob(os.path.join('launch', '*.launch.py'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tyagi55',
    maintainer_email='tyagi55@purdue.edu',
    description='Simple ROS2 publisher subscriber package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher = mypubsub.publisher:main',
            'subscriber = mypubsub.subscriber:main',
        ],
    },
)

