import subprocess, sys, os

root_dir = os.path.abspath(os.path.curdir)
project_name = "multi_proj_pkg"
version = "1.0.0"
whl_dir = "dist"
wheel_file_name = f"{whl_dir}\{project_name}-{version}-py3-none-any.whl"

def run_subprocess(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def build_wheel():
    run_subprocess(["python", "setup.py", "bdist_wheel"])

def check_wheel_contents():
    run_subprocess(["check-wheel-contents", f"{whl_dir}/"])

def reinstall_wheel():
    run_subprocess(["python", "-m", "pip", "install", wheel_file_name, "--force-reinstall"])
    print("Wheel reinstalled successfully!")

def run_prog(sub_dir, prog):
    root_dir = os.path.abspath(os.path.curdir)
    program_path = os.path.join(root_dir, sub_dir)
    os.chdir(program_path)
    print(f"Program executed in {program_path}")
    run_subprocess(["python", prog])

if __name__ == "__main__":
    try:
        build_wheel()
        check_wheel_contents()
        reinstall_wheel()
        run_prog("", "extract_wheel.py")
        run_prog("", "play.py")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

