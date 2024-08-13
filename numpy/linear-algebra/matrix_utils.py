import numpy as np

def determine_matrix(rows=None, cols=None, square_matrix=False):
    if rows is None:
        rows = int(input('Enter the number of rows: '))
    if cols is None:
        cols = int(input('Enter the number of columns: '))
    if square_matrix and rows != cols:
        raise ValueError('An error occurred! The matrix must be square.')
    
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f'Row {i+1} (separate elements with space): ').split()))
        if len(row) != cols:
            raise ValueError(f'An error occurred! Row {i+1} should have {cols} elements.')
        matrix.append(row)
    
    return np.array(matrix)