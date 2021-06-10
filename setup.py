from setuptools import setup

setup(
    name='regmatcher',
    entry_points={
        'console_scripts': [
            'regmatcher = main:main',
        ],
    }
)