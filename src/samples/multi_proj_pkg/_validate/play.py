# Import modules from the main package
from demo_py_pkg.greetings.hello import get_greeting
from demo_py_pkg.maths.math_magic import guessing_game

def main():
    # Execute functions from the modules
    greeting = get_greeting()
    print(greeting)

    trick = guessing_game()
    print(trick)

if __name__ == "__main__":
    try:
        main()
        print("Thank you for playing!")
    except Exception as e:
        print("An error occurred:", str(e))
        exit(1)
