# Import modules from the main package
from demo_py_pkg.libs.greetings.hello import get_greeting
from demo_py_pkg.libs.maths.math_magic import guessing_game

def main():
    # Execute functions from the modules
    greeting = get_greeting()
    print(greeting)

    trick = guessing_game()
    print(trick)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", str(e))
        exit(1)
