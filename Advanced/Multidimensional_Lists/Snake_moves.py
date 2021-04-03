# snake

rows, cols = [int(el) for el in input().split()]
word = input()
count = 0
a_list = []

for _ in range(rows*cols):
    if count == len(word):
        count = 0
    a_list.append(word[count])
    count += 1

a_list = ''.join(a_list)
start, stop = 0, cols

for i in range(rows):
    if i % 2 != 0:
        print(a_list[stop-1:start-1:-1])
    else:
        print(a_list[start:stop])
    start += cols
    stop += cols
