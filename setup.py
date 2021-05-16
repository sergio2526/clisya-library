from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="clisya",
    packages=find_packages(include=['clisya']),
    version="1.0",
    description="clisya library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sergio Rubiano",
    license="GPL-3.0",
    tests_require=['pytest==6.2.4'],
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
    include_package_data=True,
    install_requires=["pytz"]
)

