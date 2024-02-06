import sys, os, shutil, logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    logger.INFO("RUNNING POST GENERATION...")

    root_dir = os.path.abspath(os.path.curdir)
    dr = "{{ cookiecutter.debug_run }}"
    pfs = "{{ cookiecutter.placeholder_files }}"
    cloud_platform = "{{ cookiecutter.cloud_platform }}".lower() 
    setup_cloud_platform(root_dir, cloud_platform, drop_parent=True, debug=dr, placeholder_file=pfs)

    return 0

def setup_cloud_platform(root_dir, cloud_platform, drop_parent=False, debug=False, placeholder_file=True):
    module_list = []

    if cloud_platform == "aws":
        module_list.append("azure")
    if cloud_platform == "azure":
        module_list.append("aws")
    if "{{ cookiecutter.cicd }}".lower() == "n":
        module_list.append(".cicd")
    if "{{ cookiecutter.iac }}".lower() == "n":
        module_list.append(".iac")
    if "{{ cookiecutter.orchestration }}".lower() == "n":
        module_list.append(".orchestration")
    if "{{ cookiecutter.ingestion }}".lower() == "n":
        module_list.extend(["ingestion", "airflow"])
    if "{{ cookiecutter.transformation }}".lower() == "n":
        module_list.append("dbt")
    if "{{ cookiecutter.sample_data }}".lower() == "n":
        module_list.append("sample")

    drop_modules(root_dir, module_list, debug)
    
    if drop_parent:
        drop_parent_dir(cloud_platform)

    if placeholder_file == True:
        add_placeholder(root_dir, debug)

def drop_modules(root_dir, module_list, debug=False):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if any(item in file for item in module_list):
                file_to_remove = os.path.join(root, file)
                if debug:
                    logger.DEBUG(f"Removing file: {file_to_remove}")
                os.remove(os.path.join(root, file))
        for dir in dirs:
            if any(item in dir for item in module_list):
                dir_to_remove = os.path.join(root, dir)
                if debug:
                    logger.DEBUG(f"Removing folder: {dir_to_remove}")
                shutil.rmtree(os.path.join(root, dir))
                if debug:
                    logger.DEBUG(f"Removed folder: {dir_to_remove}")

def drop_parent_dir(cloud_platform):
    destination = os.path.abspath(os.path.curdir)
    if os.path.exists(cloud_platform):
        # copy the contents of the child folder to the destination path
        for item in os.listdir(cloud_platform):
            s = os.path.join(cloud_platform, item)
            d = os.path.join(destination, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, False, None)
            else:
                shutil.copy2(s, d)        
        # drop the parent folder
        shutil.rmtree(cloud_platform)
    else:
        logger.ERROR(f"ERROR(3): '{cloud_platform}' does not exist")
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
                    logger.DEBUG(f"Added placeholder file in {subdir}")
            else:
                if debug:
                    logger.DEBUG(f"{subdir} is not empty")

if __name__ == '__main__':
    sys.exit(main())