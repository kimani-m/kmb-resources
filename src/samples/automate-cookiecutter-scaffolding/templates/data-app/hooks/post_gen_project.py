import sys, os, shutil

def main():
    print("RUNNING POST GENERATION...")

    root_dir = os.path.abspath(os.path.curdir)
    dr = {{ cookiecutter.debug_run }}
    pfs = {{ cookiecutter.placeholder_files }}
    environment = "{{ cookiecutter.environment }}".lower() 
    setup_environment(root_dir, environment, drop_parent=True, debug=dr, placeholder_file=pfs)

    return 0

def setup_environment(root_dir, environment, drop_parent=False, debug=False, placeholder_file=True):
    module_list = []

    if environment == "aws":
        module_list.append("azure")
    if environment == "azure":
        module_list.append("aws")
    if "{{ cookiecutter.devops }}".lower() == "n":
        module_list.append("devops")
    if "{{ cookiecutter.data_ingestion }}".lower() == "n":
        module_list.extend(["adf", "airflow"])
    if "{{ cookiecutter.data_transformation }}".lower() == "n":
        module_list.append("dbt")
    if "{{ cookiecutter.sample_data }}".lower() == "n":
        module_list.append("sample")

    drop_modules(root_dir, module_list, debug)
    
    if drop_parent:
        drop_parent_dir(environment)

    if placeholder_file == True:
        add_placeholder(root_dir, debug)

def drop_modules(root_dir, module_list, debug=False):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if any(item in file for item in module_list):
                file_to_remove = os.path.join(root, file)
                if debug:
                    print(f"Removing file: {file_to_remove}")
                os.remove(os.path.join(root, file))
        for dir in dirs:
            if any(item in dir for item in module_list):
                dir_to_remove = os.path.join(root, dir)
                if debug:
                    print(f"Removing folder: {dir_to_remove}")
                shutil.rmtree(os.path.join(root, dir))

def drop_parent_dir(environment):
    destination = os.path.abspath(os.path.curdir)
    if os.path.exists(environment):
        # copy the contents of the child folder to the destination path
        for item in os.listdir(environment):
            s = os.path.join(environment, item)
            d = os.path.join(destination, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)        
        # drop the parent folder
        shutil.rmtree(environment)
    else:
        print(f"ERROR(3): '{environment}' does not exist")
        sys.exit(3)

    return 0

def add_placeholder(root_dir, debug=False):
    for root, dirs, files in os.walk(root_dir):
        for dir in dirs:
            subdir = os.path.join(root, dir)
            if not os.listdir(subdir):
                placeholder_file_path = os.path.join(subdir, ".gitkeep")
                with open(placeholder_file_path, 'w') as f:
                    f.write(f"Placeholder file: {placeholder_file_path}")
                if debug:
                    print(f"Added placeholder file in {subdir}")
            else:
                if debug:
                    print(f"{subdir} is not empty")

if __name__ == '__main__':
    sys.exit(main())