import numpy as np
from matrix_utils import non_square_matrix

first_matrix = non_square_matrix()
second_matrix = non_square_matrix()

if first_matrix.shape[1] != second_matrix.shape[0]:
    print('The number of columns in the first matrix must be equal to the number of rows in the second matrix')
else:
    product = np.dot(first_matrix, second_matrix)
    print(f'[first matrix] x [second matrix]: {product}')