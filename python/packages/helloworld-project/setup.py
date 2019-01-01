from setuptools import setup
from setuptools import find_packages
from os.path import join
from os.path import dirname
import helloworld

setup(
    name='helloworld',
    ersion=helloworld.__version__,
    include_package_data=True,
    test_suite='tests',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    entry_points={
        'console_scripts': [
            'helloworld = helloworld.core:print_message',
            'serve = helloworld.web:run_server',
        ]
    },
    install_requires=['Flask==1']
)
