import sys
from setuptools import setup, find_packages

NAME = "chimp"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    description="Chimp, an universal converter",
    author_email="mhetrerajat@gmail.com",
    author="Rajat Mhetre",
    url="",
    keywords=["Chimp", "converter", "unit", "temperature"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""Chimp can convert absolutely anything!
    """
)