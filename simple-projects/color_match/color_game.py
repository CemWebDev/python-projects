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
                
                
def check_the_guess(guess, arranged_color_code):
    color_counts = {}
    correct_position = 0
    wrong_position = 0
    for color in arranged_color_code:
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1
        
    for guess_color, arranged_color in mix(guess, arranged_color_code):
        if guess_color == arranged_color:
            correct_position += 1
            color_counts[guess_color] -= 1
            
    for guess_color, arranged_color in mix(guess, arranged_color_code):
        if color in color_counts and color_counts[color] > 0:
            wrong_position += 1
            color_counts[guess_color] -= 1
    
    return correct_position, wrong_position