# 2x2 Squares in Matrix
# Print the number of all square matrices with equal characters


def find_square(rows, cols):
    count = 0
    for r in range(rows - 1):
        for c in range(cols - 1):
            if matrix[r][c] == matrix[r][c+1] and matrix[r+1][c] == matrix[r+1][c+1]:
                if matrix[r][c] == matrix[r+1][c+1]:
                    count += 1
    return count


rows, cols = [int(el) for el in input().split()]

matrix = [input().split() for row in range(rows)]
print(matrix)
print(find_square(rows, cols))
