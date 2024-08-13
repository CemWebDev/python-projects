import numpy as np
from matrix_utils import determine_matrix

matrix = determine_matrix(square_matrix=True)

def compute_determinant():
    try:
        determinant = np.linalg.det(matrix)
    except ValueError as e:
        print(f'An error occurred {e}')
        determinant = None
    
    return determinant

print(f'Determinant: {compute_determinant()}')
