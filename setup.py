from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='asd_helper',
    version='0.1',
    description='Package containing algorithms and tests required for Algorithm and Data Structures class at AGH University in Kraków',
    long_description=long_description,
    license="MIT",
    author='Group of Python enthusiasts from classes of 2019, 2022 and 2021.',
    author_email='przemek.weglik@onet.pl',
    packages=['asd_helper'],  #same as name
    install_requires=[], #external packages as dependencies
)