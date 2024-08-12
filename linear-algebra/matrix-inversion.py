import numpy as np
from matrix_utils import get_square_matrix

def compute_inverse(matrix):
    try:
        inverse_matrix = np.linalg.inv(matrix)
        return inverse_matrix
    except np.linalg.LinAlgError:
        raise ValueError('The matrix is not invertible because its determinant is zero.')

matrix = get_square_matrix()

try:
    inverse_matrix = compute_inverse(matrix)
    print(f'Matrix: {matrix}')
    print(f'Inverse matrix: {inverse_matrix}')
except ValueError as e:
    print(f'An error occurred {e}')