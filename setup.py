import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nero",
    version="1.0.0",
    author="David Oniani",
    author_email="onianidavid@gmail.com",
    description="Tiny app that runs in a terminal and helps manage daily tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/oniani/nero",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
