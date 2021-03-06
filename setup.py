from setuptools import setup, find_packages

setup(
    name="power_simulation",
    version='0.1',
    packages=find_packages(include=['server', 'config', 'simulation', 'output']),
    author='Mariya Shumska, Chris Worthington, Victor Florea, Sjoerd Hilhorst',
    install_requires=[
        'pandas',
        'pymodbus',
        'twisted',
        'numpy',
    ]
)