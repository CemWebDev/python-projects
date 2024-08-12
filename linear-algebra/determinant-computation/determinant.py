import numpy as np

def get_matrix():
    rows = int(input('Enter the number of rows: '))
    cols = rows
        
    print(f'Enter the elements of the matrix {rows}x{cols}')
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f'Row {i+1} (separate element with space): ').split()))
        if len(row) != cols:
            raise ValueError('Number of elements does not match the number of columns!')
        matrix.append(row)
        
    return np.array(matrix)

matrix = get_matrix()

try:
    determinant = np.linalg.det(matrix)
    print(f'Matrix: {matrix}')
    print(f'Determinant of the matrix: {determinant}')
except ValueError as e:
    print(f'An error occurred {e}')