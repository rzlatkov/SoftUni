
matrix_size = int(input())

matrix = [input().split() for r in range(matrix_size)]
position = []
coins = 0
path = []

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'P':
            position = [r, c]

move = input()

while move:
    next_position = []

    if move == 'up':
        next_position = [position[0] - 1, position[1]]
    elif move == 'down':
        next_position = [position[0] + 1, position[1]]
    elif move == 'left':
        next_position = [position[0], position[1] - 1]
    elif move == 'right':
        next_position = [position[0], position[1] + 1]
    else:
        move = input()
        continue

    if 0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix):
        row, col = next_position[0], next_position[1]

        if matrix[row][col] != 'X':
            coins += int(matrix[row][col])
            matrix[row][col] = 'P'
            matrix[position[0]][position[1]] = '0'
            path.append([row, col])
            position = [row, col]
            if coins >= 100:
                break
        else:
            coins = coins // 2
            break
    else:
        coins = coins // 2
        break

    move = input()

if coins >= 100:
    print(f"You won! You've collected {coins} coins.")
else:
    print(f"Game over! You've collected {coins} coins.")

print("Your path:")

for pos in path:
    print(pos)
