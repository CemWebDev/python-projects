import random

colors = ['R', 'G', 'B', 'P', 'O', 'W']
attempts = 10
color_code_length = 4

def generate_color_code():
    code = []
    for color in range(color_code_length):
        color = random.choice(colors)
        code.append(color)
        
    return code
        
def guess_color_code():
    while True:
        guess = input("Your guess: ").upper().split(" ")
        if len(guess) != color_code_length:
            print(f"Yu must guess {color_code_length} colors")
            continue
        
        for color in guess:
            if color not in colors:
                print(f"Invalid color: {color}! Try again")
                break
        else:
            break
        
    return guess
                