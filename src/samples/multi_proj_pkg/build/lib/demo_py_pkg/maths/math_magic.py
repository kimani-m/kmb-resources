import random

def guessing_game():
    try:
        answer = random.randint(0, 10)
        attempts = 0
        max_attempts = 3
        
        print("Welcome to the Fun Math Guessing Game!")
        print(f"Can you guess the secret number? You have {max_attempts} attempts.")
        
        while attempts < max_attempts:
            guess = int(input("Enter your guess (between 0 and 10): "))
            
            if guess == answer:
                print("Congratulations! You've guessed the secret number!")
                return 0  # Successful exit
            elif guess < answer:
                print("Too low! Try a higher number.")
            else:
                print("Too high! Try a lower number.")
            
            attempts += 1
        
        if attempts == max_attempts:
            print(f"Sorry, you've reached the maximum number of attempts. The secret number was {answer}.")
    except Exception as e:
        print("An error occurred:", str(e))
        return 1  # Exit with error
