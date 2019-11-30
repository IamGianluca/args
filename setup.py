from codecs import open
from pathlib import Path
from setuptools import setup


# get the long description from the README file
path = Path(".")
with open(path / "README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="args",
    version="0.0.1",
    description="Yet another command line argument parser",
    long_description=long_description,
    packages=["args"],
)
