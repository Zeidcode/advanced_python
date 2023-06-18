matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    new_matrix = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        new_matrix.append(new_row)
    return new_matrix

print("Исходная матрица", matrix)
print("Траспонированная матрица", transpose(matrix))