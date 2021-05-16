from setuptools import setup, find_packages


setup(
    name="clisya",
    packages=find_packages(include=['clisya']),
    version="0.1.1",
    description="flags library",
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

