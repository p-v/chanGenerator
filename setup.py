from setuptools import setup

version = '1.0.0'

setup(
    name='chanGenerator',
    version=version,
    description='generate changelog for your github repository based on closed issues',
    long_description=open('README.md').read(),
    author='Pratyush Verma',
    keywords="github changelog git command-line cli",
    install_requires=[
        "requests",
    ],
    scripts=['chanGenerator'],
)
