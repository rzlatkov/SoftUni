# fibonacci generator

def fibonacci():
    a = 0
    b = 0
    while True:
        if b == 0:
            b += 1
            yield 0
        else:
            yield b
            b = a + b
            a = b - a


generator = fibonacci()
for i in range(5):
    print(next(generator))
