# Fashion Boutique

stack = [int(el) for el in input().split()]
capacity = int(input())
racks_count = 1
current_sum = 0

for i in range(len(stack) - 1, -1, -1):
    if current_sum + stack[i] < capacity:
        current_sum += stack[i]
    elif current_sum + stack[i] == capacity and i-1 >= 0:
        racks_count += 1
        current_sum = 0
    elif current_sum + stack[i] > capacity:
        racks_count += 1
        current_sum = stack[i]

print(racks_count)
