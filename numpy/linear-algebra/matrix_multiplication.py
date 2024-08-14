import numpy as np
from matrix_utils import determine_matrix as matrix

def matrix_multiplication():
    print('Enter the first matrix: ')
    first_matrix = matrix()
    
    print('Enter the second matrix: ')
    row_length = len(first_matrix[0])
    second_matrix = matrix(rows=row_length)
    
    product = np.dot(first_matrix, second_matrix)
    print(f'(First matrix) x (second matrix): {product}')
    
matrix_multiplication()