import setuptools, os
from setuptools import find_packages

package_name = 'multi_proj_pkg'
pkg_ver = '1.0.0'
author_name="Kimani Mbugua",
author_email="kimani.mbugua@kimstrad.com",
description="Demo of multi project package",

def package_files(directory_list):
    data_files = []
    
    for directory in directory_list:
        for (path, _, filenames) in os.walk(directory):
           install_path = os.path.join(package_name, path)
           files = [os.path.join(path, filename) for filename in filenames]
           data_files.append((install_path, files))

    return data_files
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name=package_name,
    version=pkg_ver,
    author=author_name,
    author_email=author_email,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=package_files(['non_py_pkg_one', 'non_py_pkg_two'])
)

print("Setup completed.")