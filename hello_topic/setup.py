from setuptools import find_packages, setup

package_name = 'hello_topic'

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
    maintainer='ri-one',
    maintainer_email='ri-one@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # この2行を追加
            'iteration_node = hello_topic.iteration_node:main',
            'double_node = hello_topic.double_node:main',
        ],
    },
)
