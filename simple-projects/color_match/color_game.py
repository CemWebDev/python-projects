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
        