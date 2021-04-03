# # Bombs
# # NxN square matrix

def explode(coord_row, coord_col):
    bomb = matrix[coord_row][coord_col]
    if bomb > 0:
        if coord_row - 1 >= 0 and matrix[coord_row - 1][coord_col] > 0:
            matrix[coord_row - 1][coord_col] -= bomb
        if coord_row + 1 < len(matrix) and matrix[coord_row + 1][coord_col] > 0:
            matrix[coord_row + 1][coord_col] -= bomb
        if coord_col - 1 >= 0 and matrix[coord_row][coord_col - 1] > 0:
            matrix[coord_row][coord_col - 1] -= bomb
        if coord_col + 1 < len(matrix[coord_row]) and matrix[coord_row][coord_col + 1] > 0:
            matrix[coord_row][coord_col + 1] -= bomb

        if coord_row - 1 >= 0 and coord_col - 1 >= 0 and matrix[coord_row - 1][coord_col - 1] > 0:
            matrix[coord_row - 1][coord_col - 1] -= bomb
        if coord_row + 1 < len(matrix) and coord_col + 1 < len(matrix[coord_row + 1]) and matrix[coord_row + 1][coord_col + 1] > 0:
            matrix[coord_row + 1][coord_col + 1] -= bomb
        if coord_row - 1 >= 0 and coord_col + 1 < len(matrix[coord_row - 1]) and matrix[coord_row - 1][coord_col + 1] > 0:
            matrix[coord_row - 1][coord_col + 1] -= bomb
        if coord_row + 1 < len(matrix) and coord_col - 1 >= 0 and matrix[coord_row + 1][coord_col - 1] > 0:
            matrix[coord_row + 1][coord_col - 1] -= bomb

        matrix[coord_row][coord_col] = 0


rows = int(input())
cols = rows
alive_cells = 0
sum_of_alive_cells = 0

matrix = [[int(el) for el in input().split()] for row in range(rows)]
bomb_coordinates = input().split()

for bomb in range(len(bomb_coordinates)):
    row, col = bomb_coordinates[bomb].split(',')
    explode(int(row), int(col))

for r in range(rows):
    for c in range(cols):
        if matrix[r][c] > 0:
            alive_cells += 1
            sum_of_alive_cells += matrix[r][c]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")

[print(' '.join(map(lambda x: str(x), el))) for el in matrix]
