# Unique usernames

count = int(input())
unique_names = set()

for i in range(count):
    unique_names.add(input())

for el in unique_names:
    print(el)