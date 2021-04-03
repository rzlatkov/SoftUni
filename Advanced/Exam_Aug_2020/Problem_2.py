# Minesweeper generator

import ast

rows = int(input())
mines_count = int(input())
field = []

for r in range(rows):
    field.append([0]*rows)

for i in range(mines_count):
    bomb_location = input()
    bomb_location = ast.literal_eval(bomb_location)
    row = bomb_location[0]
    col = bomb_location[1]
    field[row][col] = '*'

for r in range(len(field)):
    for c in range(len(field[r])):
        if field[r][c] != '*':
            # up
            if r - 1 >= 0:
                if field[r-1][c] == '*':
                    field[r][c] += 1
            # down
            if r + 1 < len(field):
                if field[r+1][c] == '*':
                    field[r][c] += 1
            # left
            if c - 1 >= 0:
                if field[r][c-1] == '*':
                    field[r][c] += 1
            # right
            if c + 1 < len(field[r]):
                if field[r][c+1] == '*':
                    field[r][c] += 1
            # top_left
            if r - 1 >= 0 and c - 1 >= 0:
                if field[r-1][c-1] == '*':
                    field[r][c] += 1
            # top_right
            if r - 1 >= 0 and c + 1 < len(field[r]):
                if field[r-1][c+1] == '*':
                    field[r][c] += 1
            # bot_left
            if r + 1 < len(field) and c - 1 >= 0:
                if field[r+1][c-1] == '*':
                    field[r][c] += 1
            # bot_right
            if r + 1 < len(field) and c + 1 < len(field[r]):
                if field[r+1][c+1] == '*':
                    field[r][c] += 1

new_field = []

for row in field:
    current_row = []
    for el in row:
        if el == '*':
            current_row.append(el)
        else:
            current_row.append(str(el))
    new_field.append(current_row)

[print(' '.join(el)) for el in new_field]
