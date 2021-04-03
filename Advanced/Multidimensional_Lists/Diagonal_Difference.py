# Diagonal difference
# NxN matrix

def diagonals(matrix):
    left_diagonal = [matrix[i][i] for i in range(rows)]
    right_diagonal = [matrix[i][~i] for i in range(rows)]
    # ~i in our case is equal to "-(i += 1)"
    return left_diagonal, right_diagonal


def sum(left, right):
    sum_left_diag = 0
    sum_right_diag = 0
    for i in range(rows):
        sum_left_diag += int(left[i])
        sum_right_diag += int(right[i])
    return sum_left_diag, sum_right_diag


rows = int(input())

matrix = [input().split(' ') for row in range(rows)]

left, right = diagonals(matrix)
sum_left, sum_right = sum(left, right)

print(abs(sum_right - sum_left))
