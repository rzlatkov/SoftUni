# Count symbols

text = input()
text_set = list(set(text))
text_set.sort()

for char in text_set:
    print(f"{char}: {text.count(char)} time/s")
