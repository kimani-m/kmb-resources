import setuptools
from setuptools import find_packages
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name='multi_proj_pkg',
    version='1.0.0',
    author="Kimani Mbugua",
    author_email="kimani.mbugua@kimstrad.com",
    description="Demo of multi project package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    package_data={
        'non-py-pkg': ['*']
    }
)