
from setuptools import setup
setup(
        name = 'wpli',
        version = '0.1.0',                
        packages = ['wpli'],
        entry_points = {
            'console_scripts': [
                'wpli = wpli.__main__:main'
                ]
            })

