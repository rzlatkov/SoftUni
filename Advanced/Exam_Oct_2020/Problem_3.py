# List pureness

def best_list_pureness(iterable, k):
    sums = []
    for rotation in range(k+1):
        current_sum = 0
        for i in range(len(iterable)):
            current_sum += iterable[i]*i
        sums.append(current_sum)
        iterable = iterable[-1:] + iterable[:-1]
    return f"Best pureness {max(sums)} after {sums.index(max(sums))} rotations"


test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
