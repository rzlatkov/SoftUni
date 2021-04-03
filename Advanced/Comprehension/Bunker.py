# Bunker

def add(category, name, to_be_split):
    quantity, quantity_int = to_be_split[0].split(':')
    quality, quality_int = to_be_split[1].split(':')

    dictionary[category + '@' + name] = {}
    dictionary[category + '@' + name][quantity] = int(quantity_int)
    dictionary[category + '@' + name][quality] = int(quality_int)


categories = {cat: [] for cat in input().split(', ')}
n = int(input())
dictionary = {}

for i in range(n):
    category, item_name, to_be_split = input().split(' - ')
    categories[category].append(item_name)
    to_be_split = to_be_split.split(';')
    add(category, item_name, to_be_split)

count = 0
quality = 0

for value in dictionary.values():
    count += value['quantity']
    quality += value['quality']

print(f"Count of items: {count}")
print(f"Average quality: {quality/len(categories):.2f}")

for key, value in categories.items():
    print(f"{key} -> {', '.join(value)}")
