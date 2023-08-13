import random
def get_greeting():
    user_name = input("Enter your name: ")
    greetings = ["Hello", "Hi", "Hey", "Greetings"]
    return f"{greetings[random.randint(0, len(greetings) - 1)]}, {user_name}!"
