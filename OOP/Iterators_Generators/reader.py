# reader

def read_next(*args):
    for el in args:
        for i in el:
            yield i


for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
