import numpy as np



def determine_matrix():
    rows = int(input('Enter the number of rows: '))
    cols = int(input('Enter the number of cols: '))
    matrix = []
    for i in range(rows):
        row = list(map(float, input(f'Row {i+1} (separate elements with space: ): ').split()))
        if len(row) != cols:
            raise ValueError(f'An error occurred! Row{i+1} should have {cols} elements')
        
        matrix.append(row)
        
    matrix = np.array(matrix)


