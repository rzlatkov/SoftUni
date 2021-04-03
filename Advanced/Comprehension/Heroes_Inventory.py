# Heroes Inventory

def add_to_dict(name, item, cost):
    if item not in dictionary[name]:
        dictionary[name][item] = int(cost)


names = input().split(', ')
line = input()
dictionary = {name: {} for name in names}

while line != "End":
    name, item, cost = line.split('-')
    add_to_dict(name, item, cost)
    line = input()

print(*[f"{name} -> Items: {len(inventory)}, Cost: {sum(inventory.values())}" for name, inventory in dictionary.items()], sep='\n')
