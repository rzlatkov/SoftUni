# Maximal Sum
# NxM size matrix (rectangular)
# Find the 3x3 square which elements represent the maximal sum

def find_max_sum(rows, cols):
    max_sum = - 1000000
    current_sum = 0
    max_square = [None]*3
    for r in range(rows - 2):
        for c in range(cols - 2):
            first_row = matrix[r][c] + matrix[r][c+1] + matrix[r][c+2]
            second_row = matrix[r+1][c] + matrix[r+1][c+1] + matrix[r+1][c+2]
            third_row = matrix[r+2][c] + matrix[r+2][c+1] + matrix[r+2][c+2]
            current_sum = first_row + second_row + third_row
            if current_sum > max_sum:
                max_sum = current_sum
                max_square[0] = str(matrix[r][c]) + ' ' + str(matrix[r][c+1]) + ' ' + str(matrix[r][c+2])
                max_square[1] = str(matrix[r+1][c]) + ' ' + str(matrix[r+1][c+1]) + ' ' + str(matrix[r+1][c+2])
                max_square[2] = str(matrix[r+2][c]) + ' ' + str(matrix[r+2][c+1]) + ' ' + str(matrix[r+2][c+2])

    return max_sum, max_square


rows, cols = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for row in range(rows)]
result, square = find_max_sum(rows, cols)
print(f"Sum = {result}")
[print(square[i]) for i in range(3)]
