# Snake

def find_second_b(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'B':
                matrix[r][c] = 'S'
                return r, c


matrix_size = int(input())
matrix = [list(input()) for r in range(matrix_size)]
pos = []
food_eaten = 0
win = False
lost = False

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'S':
            pos = [r, c]

move = input()
while move:

    next_pos = []

    if move == 'up':
        next_pos = [pos[0] - 1, pos[1]]
    elif move == 'down':
        next_pos = [pos[0] + 1, pos[1]]
    elif move == 'left':
        next_pos = [pos[0], pos[1] - 1]
    elif move == 'right':
        next_pos = [pos[0], pos[1] + 1]

    if 0 <= next_pos[0] < len(matrix) and 0 <= next_pos[1] < len(matrix):
        row, col = next_pos[0], next_pos[1]
        matrix[pos[0]][pos[1]] = '.'
        if matrix[row][col] == '*':
            food_eaten += 1
            matrix[row][col] = 'S'
            pos = [row, col]
            if food_eaten >= 10:
                win = True
                break
        elif matrix[row][col] == 'B':
            matrix[row][col] = '.'
            next_r, next_c = find_second_b(matrix)
            pos = [next_r, next_c]
        elif matrix[row][col] == '-':
            matrix[row][col] = 'S'
            pos = [row, col]
    else:
        matrix[pos[0]][pos[1]] = '.'
        break
    move = input()


if win:
    print("You won! You fed the snake.")
    print(f"Food eaten: 10")
else:
    print("Game over!")
    print(f"Food eaten: {food_eaten}")

for row in matrix:
    print(''.join(row))
