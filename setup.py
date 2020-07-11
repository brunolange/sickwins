from os import path
from setuptools import setup

with open("requirements.txt") as handle:
    requirements = handle.readlines()

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="sickwins",
    version="0.1",
    entry_points={"console_scripts": ["sickwins=sickwins.cli:main"],},
    description="command line tool to capture a sequence of images into a high-quality gif",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Bruno Lange",
    author_email="blangeram@gmail.com",
    url="https://gitlab.com/brunolange/sickwins",
    install_requires=requirements,
    python_requires=">=3",
    extras_require={"dev": ["pylint", "black"]},
)
