from setuptools import setup

setup(
    name='igmov-create-cli',
    entry_points={
        "console_scripts": [
            'igmov-create=lib:cli'
        ]
    },
)
