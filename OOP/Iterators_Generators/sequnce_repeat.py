# sequence repeat

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 0:
            self.number -= 1
            if self.count < len(self.sequence):
                index = self.count
                self.count += 1
                return self.sequence[index]
            elif self.count == len(self.sequence):
                self.count = 0
                index = self.count
                self.count += 1
                return self.sequence[index]
        else:
            raise StopIteration


result = sequence_repeat('abc', 5)  # creates instance of the class. The iterator is created by the for-loop below!!!

for item in result:  # "in result" runs __iter__ and __next__ of the given instance
    print(item, end='')
