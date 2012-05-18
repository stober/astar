#! /usr/bin/env python
"""
Author: Jeremy M. Stober
Program: SETUP.PY
Date: Friday, May 18 2012
Description: Setup A star search in Python.
"""

from distutils.core import setup

setup(name='astar',
      version='0.01',
      description='A* search using Python',
      author="Jeremy Stober",
      author_email="stober@gmail.com",
      package_dir={"astar" : "src"},
      packages=["astar"]
      )


