import random


def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess the number in as few attempts as possible.")
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10 

    while True:
        if attempts >= max_attempts:
            print(f"Sorry, you've used all your attempts. The number was {number}.")
            break
        
        try:
            guess_number = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess the number: "))
            if guess_number < 1 or guess_number > 100:
                print("Invalid input! Please enter a number between 1 and 100.")
                continue 
            attempts += 1
        except ValueError:
            print("Only integer values are allowed! Please try again.")
            continue

        if guess_number < number:
            print("Too low! Try a higher number.")
        elif guess_number > number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            if attempts <= 3:
                print("Amazing! You have a great intuition.")
            elif attempts <= 6:
                print("Good job! You found it in a reasonable number of attempts.")
            else:
                print("Well done! It took you some time, but you got it!")
            break
    
    play_again = input("Would you like to play again? (yes/no): ").lower()
    if play_again == 'yes':
        guess_the_number()
    else:
        print("Thank you for playing! Goodbye!")


guess_the_number()
