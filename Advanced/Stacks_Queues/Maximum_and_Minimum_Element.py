# Maximum and miminum element

from collections import deque

lines_count = int(input())
stack = deque()

for _ in range(lines_count):
    line = input()
    if line[0] == '1':
        line = line.split()
        stack.appendleft(int(line[1]))
    elif line[0] == '2' and len(stack) >= 1:
        stack.popleft()
    elif line[0] == '3' and len(stack) >= 1:
        print(max(stack))
    elif line[0] == '4' and len(stack) >= 1:
        print(min(stack))

for i in range(len(stack) - 1):
    print(stack[i], end=', ')

print(stack[-1])
