from setuptools import setup

setup(
    name='calculator',
    version='0.0.1',
    description='A simple calculator for expressions in prefix and infix notation.',
    url='https://github.com/carlocorsa/calculator.git',
    author='Carlo Corsaro',
    author_email='carlo.corsaro@gmail.com',
    license='unlicensed',
    packages=['calculator'],
    install_requires=['Flask']
)
