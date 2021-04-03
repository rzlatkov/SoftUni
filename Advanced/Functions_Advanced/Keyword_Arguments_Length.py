# Keyword arguments length

def kwargs_length(**kwargs):  # packs key-value pairs in new dictionary and return its length
    return len(kwargs)


dictionary = {'name': 'Peter', 'age': 25}
print(kwargs_length(**dictionary))  # unpacks dictionary by key-value pairs
