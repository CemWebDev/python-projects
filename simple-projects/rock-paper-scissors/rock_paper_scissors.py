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