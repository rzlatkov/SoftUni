# words lengths

strings = input().split(', ')
[print(f"{word} -> {len(word)}, ", end='')for word in strings if strings.index(word) < len(strings) - 1]
print(f"{strings[-1]} -> {len(strings[-1])}")
