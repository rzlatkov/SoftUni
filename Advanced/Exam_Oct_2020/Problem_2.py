coordinates = []
king_pos = []

matrix = [input().split() for r in range(8)]

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        if matrix[r][c] == 'K':
            king_pos = [r, c]

row = king_pos[0]
col = king_pos[1]
# up
while row > 0:
    row -= 1
    if matrix[row][col] == 'Q':
        coordinates.append([row, col])
        break

row = king_pos[0]
col = king_pos[1]
# down
while row < 7:
    row += 1
    if matrix[row][col] == 'Q':
        coordinates.append([row, col])
        break

row = king_pos[0]
col = king_pos[1]
# left
while col > 0:
    col -= 1
    if matrix[row][col] == 'Q':
        coordinates.append([row, col])
        break

row = king_pos[0]
col = king_pos[1]
# right
while col < 7:
    col += 1
    if matrix[row][col] == 'Q':
        coordinates.append([row, col])
        break

row = king_pos[0]
col = king_pos[1]
# top_left
while row > 0 and col > 0:
    row -= 1
    col -= 1
    if matrix[row][col] == 'Q':
        coordinates.append([row, col])
        break

row = king_pos[0]
col = king_pos[1]
# top_right
while row > 0 and col < 7:
    row -= 1
    col += 1
    if matrix[row][col] == 'Q':
        coordinates.append([row, col])
        break

row = king_pos[0]
col = king_pos[1]
# bot_left
while row < 7 and col > 0:
    row += 1
    col -= 1
    if matrix[row][col] == 'Q':
        coordinates.append([row, col])
        break

row = king_pos[0]
col = king_pos[1]
# bot_right
while row < 7 and col < 7:
    row += 1
    col += 1
    if matrix[row][col] == 'Q':
        coordinates.append([row, col])
        break

if coordinates:
    for coord in coordinates:
        print(coord)
else:
    print(f"The king is safe!")
