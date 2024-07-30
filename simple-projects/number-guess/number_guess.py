import random



def guess_the_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess_number = int(input("Guess the number: "))
            attempts += 1
        except ValueError:
            print("Only  integer values!")
        if guess_number < number:
            print("Too low!")
        elif guess_number > number:
            print("To high!")
        else:
            if attempts <= 3:
                print("Amazing!")
            elif attempts > 3:
                print(f"You've guessed in {attempts}")
            break
        
guess_the_number()