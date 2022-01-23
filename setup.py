"""Setup file required by pip to perform installation."""
from setuptools import setup

setup(
    name='asd_helper',
    version='0.1',
    description="""\
        Package containing algorithms and tests required for \
        Algorithm and Data Structures class at AGH University in Kraków
    """,
    license='MIT',
    author='Group of Python enthusiasts from classes of 2019, 2022 and 2021.',
    author_email='przemek.weglik@onet.pl',
    packages=['asd_helper'],  # same as name
    install_requires=[],  # external packages as dependencies
)
