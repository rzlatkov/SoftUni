# take halves

def solution():
    def integers():  # integers() is being called/iterated by halves() which is called by the caller (e.g. user)
        i = 1  # starts from i=1
        while True:  # infinite loop
            yield i  # yields i, then goes to i+=1 and "pauses" until next call from caller
            i += 1

    def halves():
        for i in integers():  # performs next() on the iterable integers() at each call
            yield i / 2  # yields i / 2 then waits from another call (another next() on integers())

    def take(n, seq):
        result = []  # a list with the first n-halves should be returned, thus we should call halves() n-times
        for i in seq:
            result.append(i)
            if len(result) == n:
                return result

    return take, halves, integers


take = solution()[0]  # solution()[0] refers to take() from the "return take->[0], halves->[1], integers->[3]"
halves = solution()[1]  # solution()[1] refers to halves() from the "return take->[0], halves->[1], integers->[3]"
print(take(5, halves()))  # calls take() directly (not solution()) with the following args which call halves() n-times
