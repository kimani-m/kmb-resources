import os, zipfile, shutil

def extract_data_from_wheel(wheel_file, output_dir, project_name):
    with zipfile.ZipFile(wheel_file, 'r') as wheel_zip:
        for item in wheel_zip.namelist():
            if item.startswith(project_name) and not item.__contains__('dist-info/'):
                rel_item_path = item.replace(f"/data/{project_name}/", '/')
                extracted_path = os.path.join(output_dir, rel_item_path)
                wheel_zip.extract(item, extracted_path)
                print(f"Extracted: {extracted_path}")

if __name__ == "__main__":
    current_directory = os.path.abspath(os.path.curdir)   
    project_name = "multi_proj_pkg"
    version = "1.0.0"
    whl_dir = "dist"
    wheel_file = f"{whl_dir}\{project_name}-{version}-py3-none-any.whl"
    output_directory = os.path.join(current_directory, "output")
    # Clear the existing output directory
    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)
    os.makedirs(output_directory, exist_ok=True)
    extract_data_from_wheel(wheel_file, output_directory, project_name)
