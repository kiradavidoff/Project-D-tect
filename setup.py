from setuptools import find_packages
from setuptools import setup

with open("Requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name='dtect',
      version="0.1",
      description="d-tect_wagon_project",
      install_requires=requirements,
      packages=find_packages())
