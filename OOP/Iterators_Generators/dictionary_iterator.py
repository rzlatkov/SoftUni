# Dictionary iterator

class dictionary_iter:
    def __init__(self, a_dict):
        self.dictionary = a_dict
        self.items = list(self.dictionary.items())
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.dictionary):
            index = self.count
            self.count += 1
            return self.items[index]
        else:
            raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
