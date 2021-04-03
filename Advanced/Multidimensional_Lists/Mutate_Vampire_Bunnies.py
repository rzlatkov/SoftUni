# Radioactive Mutate Vampire Bunnies

def spread():
    initial_bunny_positions = []
    for r in range(len(original_matrix)):
        for c in range(len(original_matrix[r])):
            if original_matrix[r][c] == 'B':
                initial_bunny_positions.append((r, c))

    for r in range(len(original_matrix)):
        for c in range(len(original_matrix[r])):
            if original_matrix[r][c] == 'B' and (r, c) in initial_bunny_positions:
                bunny_position = [r, c]
                position_up = [bunny_position[0] - 1, bunny_position[1]]
                position_down = [bunny_position[0] + 1, bunny_position[1]]
                position_left = [bunny_position[0], bunny_position[1] - 1]
                position_right = [bunny_position[0], bunny_position[1] + 1]
                if 0 <= position_up[0]:
                    original_matrix[position_up[0]][position_up[1]] = 'B'
                if position_down[0] < len(original_matrix):
                    original_matrix[position_down[0]][position_down[1]] = 'B'
                if 0 <= position_left[1]:
                    original_matrix[position_left[0]][position_left[1]] = 'B'
                if position_right[1] < cols:
                    original_matrix[position_right[0]][position_right[1]] = 'B'


def check_if_dead(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 'P':
                return False
    return True


rows, cols = [int(el) for el in input().split()]
original_matrix = []

for row in range(rows):
    original_matrix.append(list(input()))

movement = list(input())
position = []
win = False

for r in range(len(original_matrix)):
    for c in range(len(original_matrix[r])):
        if original_matrix[r][c] == 'P':
            position = [r, c]

for move in movement:
    next_position = []

    if move == 'U':
        next_position = [position[0] - 1, position[1]]
    elif move == 'D':
        next_position = [position[0] + 1, position[1]]
    elif move == 'L':
        next_position = [position[0], position[1] - 1]
    elif move == 'R':
        next_position = [position[0], position[1] + 1]

    if 0 <= next_position[0] < len(original_matrix) and 0 <= next_position[1] < len(original_matrix[next_position[0]]):
        row, col = next_position[0], next_position[1]
        if original_matrix[row][col] == '.':
            original_matrix[row][col] = 'P'
            original_matrix[position[0]][position[1]] = '.'
            position = next_position
        else:
            original_matrix[position[0]][position[1]] = '.'
            position = next_position
    else:
        win = True
        original_matrix[position[0]][position[1]] = '.'

    spread()

    if win:
        break

    result = check_if_dead(original_matrix)

    if result:
        break

[print(''.join(el)) for el in original_matrix]

if win:
    print(f"won: {position[0]} {position[1]}")
else:
    print(f"dead: {position[0]} {position[1]}")
