import random

items = ["rock", "paper", "scissors"]

def get_computer_choice():
    return random.choice(items)

def get_user_choice():
    while True:
        user_input = input("Rock, paper or scissors? ").lower()
        if user_input in items:
            return user_input
        print("Invalid")

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Same item")
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("You win against to computer!")
    else:
        print("Computer Wins!")
    print(f"Your choice: {user_choice}")
    print(f"Computers choice: {computer_choice}")
        
def start_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner(user_choice, computer_choice)
    
start_game()