from setuptools import setup

setup(
    name='lotto',
    version='0.0.1',
    py_modules=['lotto'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'lotto = lotto:lotto',
        ],
    },
)