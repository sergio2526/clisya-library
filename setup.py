from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="clisya",
    version="0.1.0",
    description="flag library of h",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="URL",
    author="Sergio Rubiano",
    author_email="sergioandresrubiano25@gmail.com",
    license="GPL-3.0",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["clisya"],
    include_package_data=True,
    install_requires=["pytz"]
)