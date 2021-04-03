# Miner
# NxN square matrix

size = int(input())

movement = input().split()
matrix = [input().split() for row in range(size)]
position = []
collected_coals = 0
total_coals = 0
is_valid = True

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == 's':
            position = [r, c]
        if matrix[r][c] == 'c':
            total_coals += 1

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

    if 0 <= next_position[0] < len(matrix) and 0 <= next_position[1] < len(matrix):
        position = next_position
        if matrix[next_position[0]][next_position[1]] == "s" or matrix[next_position[0]][next_position[1]] == "*":
            pass
        elif matrix[next_position[0]][next_position[1]] == "e":
            print(f"Game over! ({position[0]}, {position[1]})")
            is_valid = False
            break
        elif matrix[next_position[0]][next_position[1]] == "c":
            collected_coals += 1
            matrix[next_position[0]][next_position[1]] = "*"
            if collected_coals == total_coals:
                is_valid = False
                print(f"You collected all coals! ({position[0]}, {position[1]})")
                break

if is_valid:
    print(f"{total_coals - collected_coals} coals left. ({position[0]}, {position[1]})")
