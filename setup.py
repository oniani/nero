# see -> https://github.com/pypa/python-packaging-user-guide/blob/master/source/tutorials/packaging-projects.rst

import setuptools

with open("README.md", "r") as file:
    description = file.read()

setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    author="David Oniani",
    author_email="onianidavid.com",
    description="Nero is a tiny app which runs in a terminal and helps manage daily tasks",
    long_description=description,
    long_description_content_type="text/markdown",
    url="https://github.com/oniani/nero",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Linux/macOS/Windows",
    ),
)
