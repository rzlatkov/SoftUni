# Revers numbers with a stack

a_list = input().split()
stack = []

# for i in range(len(a_list) - 1, -1, -1):
#     stack.append(a_list[i])
#
# print(' '.join(stack))

while len(a_list) > 0:
    stack.append(a_list.pop()) # pop() remove elements "from the top" stack-alike

print(' '.join(stack))