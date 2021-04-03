# Sets of Elements

set1_len, set2_len = input().split()
set1_len = int(set1_len)
set2_len = int(set2_len)
set1 = set()
set2 = set()
result = []

for i in range(set1_len + set2_len):
    if i < set1_len:
        set1.add(input())
    else:
        set2.add(input())

for el in set1:
    if el in set2:
        result.append(el)

for el in result:
    print(el)