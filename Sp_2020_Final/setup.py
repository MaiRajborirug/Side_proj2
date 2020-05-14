from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("cy_usporf.pyx"))

# To create a module from .pyx file
# For Mac and Linux 
# interminal: python setup.py build_ext --inplace
