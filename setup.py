import os
from setuptools import setup, find_packages

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name = 'pretty html table',
    version = '0.1dev',
    license = 'MIT',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    description = 'Make pandas dataframe looking pretty again',
    long_description = read('README.md'),
    url = 'github to add here',
    install_requires = ['pandas'],
    extras_require = {},
    package_data = {}
)
    
