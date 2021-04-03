# Matrix modification

def is_valid(row, col):
    if 0 <= int(row) <= len(matrix) - 1 and 0 <= int(col) <= len(matrix[int(row)]) - 1:
        return True
    return False


rows = int(input())

matrix = [input().split() for row in range(rows)]

line = input()

while line != "END":
    type, row, col, value = line.split()
    if type == "Add":
        if is_valid(row, col):
            matrix[int(row)][int(col)] = int(matrix[int(row)][int(col)])
            matrix[int(row)][int(col)] += int(value)
            matrix[int(row)][int(col)] = str(matrix[int(row)][int(col)])
        else:
            print("Invalid coordinates")
    elif type == "Subtract":
        if is_valid(row, col):
            matrix[int(row)][int(col)] = int(matrix[int(row)][int(col)])
            matrix[int(row)][int(col)] -= int(value)
            matrix[int(row)][int(col)] = str(matrix[int(row)][int(col)])
        else:
            print("Invalid coordinates")
    line = input()

[print(' '.join(r), sep='\n') for r in matrix]
