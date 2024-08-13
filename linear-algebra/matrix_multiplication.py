import numpy as np
from matrix_utils import determine_matrix

def matrix_multiplication():
    print('Enter the first matrix: ')
    first_matrix = determine_matrix()
    
    print('Enter the second matrix: ')
    row_length = len(first_matrix[0])
    second_matrix = determine_matrix(rows=row_length)
    
    product = np.dot(first_matrix, second_matrix)
    print(f'(First matrix) x (second matrix): {product}')
    
matrix_multiplication()