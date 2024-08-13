import numpy as np
from matrix_utils import determine_matrix

matrix = determine_matrix(square_matrix=True)

try:
    determinant = np.linalg.det(matrix)
    print(f'Matrix: {matrix}')
    print(f'Determinant of the matrix: {determinant}')
except ValueError as e:
    print(f'An error occurred {e}')