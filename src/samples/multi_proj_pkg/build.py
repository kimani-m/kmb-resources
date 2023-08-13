import subprocess, sys, os
root_dir = os.path.abspath(os.path.curdir)

def run_subprocess(command):
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def build_wheel():
    run_subprocess(["python", "setup.py", "bdist_wheel"])

def check_wheel_contents():
    run_subprocess(["check-wheel-contents", "dist/"])

def reinstall_wheel():
    run_subprocess(["python", "-m", "pip", "install", "./dist/multi_proj_pkg-1.0.0-py3-none-any.whl", "--force-reinstall"])
    print("Wheel reinstalled successfully!")

def run_program(sub_dir, prog):
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
        run_program("_validate", "play.py")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

