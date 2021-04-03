# square NxN matrix

initial_str = list(input())
rows = int(input())

matrix = [list(input()) for r in range(rows)]
position = []
movement = []

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'P':
            position = [r, c]

move_count = int(input())

for move in range(move_count):
    movement.append(input())

for move in movement:
    next_position = []

    if move == 'up':
        next_position = [position[0] - 1, position[1]]
    elif move == 'down':
        next_position = [position[0] + 1, position[1]]
    elif move == 'left':
        next_position = [position[0], position[1] - 1]
    elif move == 'right':
        next_position = [position[0], position[1] + 1]

    if 0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix[next_position[0]]):
        row, col = next_position[0], next_position[1]

        if matrix[row][col] != '-':
            initial_str.append(matrix[row][col])
            matrix[row][col] = 'P'
            matrix[position[0]][position[1]] = '-'
            position = next_position
        else:
            matrix[row][col] = 'P'
            matrix[position[0]][position[1]] = '-'
            position = next_position
    else:
        if initial_str:
            initial_str.pop()

print(f"{''.join(initial_str)}")
[print(''.join(el)) for el in matrix]
