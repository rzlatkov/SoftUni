# Flatten Lists

a_list = input().split('|')[::-1]
result = []

for string in a_list:
    result += string.split()  # list concatenation

print(' '.join(result))
