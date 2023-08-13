import setuptools, os
from setuptools import find_packages

package_name = 'multi_proj_pkg'

def package_files(directory_list):
    data_files = []
    
    for directory in directory_list:
        for (path, _, filenames) in os.walk(directory):
            print(f"Processing directory: {directory}")
            print(f"Path: {path}")
            
            install_path = os.path.join(package_name, path)
            print(f"Install path: {install_path}")
            
            files = [os.path.join(path, filename) for filename in filenames]
            print(f"Files: {files}")
            
            data_files.append((install_path, files))
            print(f"Data files: {data_files}")

    return data_files
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name=package_name,
    version='1.0.0',
    author="Kimani Mbugua",
    author_email="kimani.mbugua@kimstrad.com",
    description="Demo of multi project package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=package_files(['non_py_pkg'])
)

print("Setup completed.")