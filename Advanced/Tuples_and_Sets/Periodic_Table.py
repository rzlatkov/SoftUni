# Periodic table

result = set()

for _ in range(int(input())):
    for el in input().split():
        result.add(el)

for el in result:
    print(el)
