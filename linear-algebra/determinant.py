import numpy as np
from matrix_utils import get_square_matrix

matrix = get_square_matrix()

try:
    determinant = np.linalg.det(matrix)
    print(f'Matrix: {matrix}')
    print(f'Determinant of the matrix: {determinant}')
except ValueError as e:
    print(f'An error occurred {e}')