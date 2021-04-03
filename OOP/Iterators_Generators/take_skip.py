# take skip

class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            index = self.number
            self.count -= 1
            self.number += self.step
            return index
        else:
            raise StopIteration


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
