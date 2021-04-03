# Knight Game

def kills_count(rows, cols):
    # create the L pattern
    kill_count = 0
    pattern_rows = [-2, -2, 2, 2, -1, -1, 1, 1]
    pattern_cols = [-1, 1, -1, 1, -2, 2, -2, 2]
    for i in range(8):
        if 0 <= rows + pattern_rows[i] < len(matrix) and 0 <= cols + pattern_cols[i] < len(matrix[rows + pattern_rows[i]]):
            if matrix[rows + pattern_rows[i]][cols + pattern_cols[i]] == 'K':
                kill_count += 1
    return kill_count


rows = int(input())
cols = rows

matrix = []

for _ in range(rows):
    # splits the string on chars and stores them in a nested list
    # input().split() wont work because of no whitespace between chars
    # this way we can replace a given K with 0 by its coordinates while if the row was a whole string the .replace()
    # function would not do the job properly
    matrix.append(list(input()))

deadliest_coords = []
most_kills = 0
kills = 0
count = 0

while True:
    most_kills = 0
    deadliest_coords = []
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 'K':
                kills = kills_count(r, c)
                if kills > most_kills and kills > 0:
                    most_kills = kills
                    deadliest_coords = [r, c]
    if most_kills > 0:
        matrix[deadliest_coords[0]][deadliest_coords[1]] = '0'
        count += 1
    else:
        break

print(count)
