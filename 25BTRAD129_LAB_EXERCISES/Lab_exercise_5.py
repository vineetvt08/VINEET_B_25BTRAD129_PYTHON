import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False
    
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100. Try to guess it!")
    
    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                guessed_correctly = True
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    number_guessing_game()
