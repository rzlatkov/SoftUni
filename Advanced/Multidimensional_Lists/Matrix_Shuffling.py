# Matrix Shuffling

def swap(row1, col1, row2, col2):
    # coord1 = matrix[row1][col1]
    # coord2 = matrix[row2][col2]
    if row1 < len(matrix) and col1 < len(matrix[row1]) and row2 < len(matrix) and col2 < len(matrix[row2]):
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        return True
    return False


rows, cols = [int(el) for el in input().split()]
matrix = [input().split() for row in range(rows)]

command = input()

while command != "END":
    command = command.split()
    if command[0] == 'swap' and len(command) == 5:
        valid = swap(int(command[1]), int(command[2]), int(command[3]), int(command[4]))
        if not valid:
            print("Invalid input!")
        else:
            [print(' '.join(matrix[i])) for i in range(rows)]
    else:
        print("Invalid input!")
    command = input()
