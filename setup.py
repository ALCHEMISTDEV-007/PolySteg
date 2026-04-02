from setuptools import setup

setup(
    name='polysteg',
    version='0.1.0',
    py_modules=['steg_program'],
    packages=['steg_class'],
    entry_points={
        'console_scripts': [
            'polysteg=steg_program:main',
        ],
    },
)
