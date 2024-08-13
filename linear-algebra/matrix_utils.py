import numpy as np


def get_square_matrix():
    rows = int(input('Enter the number of rows: '))
    cols = rows
    
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f'Row {i+1} (separate elements with space): ').split()))
        if len(row) != cols:
            raise ValueError('Number of elements does not match the number of columns!')
        matrix.append(row)
        
    return np.array(matrix)


def non_square_matrix():
    rows = int(input('Enter the number of rows: '))
    cols = int(input('Enter the number of cols: '))
    
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f'Row {i+1}: ').split()))
        matrix.append(row)
        
    return np.array(matrix)

