"""
File: setup.py
Author: Bhupeshwar Pathania
Date: 24-09-2024
Description:  

In Python, setup.py is a module used to build and distribute Python packages. 
It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package. 
This information is used by the pip tool, which is a package manager for Python that allows users to install and manage Python packages from the command line. 
By running the setup.py file with the pip tool, you can build and distribute your Python package so that others can use it.

"""

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Text-Summarization-NLP-Project"
AUTHOR_USER_NAME = "bhupeshwar"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "bhupeshwar.singh.pathania@gmail.com"



setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)