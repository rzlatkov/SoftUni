# Battle of Names

names_count = int(input())
set_odd = set()
set_even = set()

for i in range(1, names_count + 1):
    name = input()
    current_sum = 0
    for w in range(len(name)):
        current_sum += ord(name[w])
    result = current_sum // i
    if result % 2 == 0:
        set_even.add(result)
    else:
        set_odd.add(result)

if sum(set_odd) == sum(set_even):  # union
    modified = [str(el) for el in set_even | set_odd]
    print(f"{', '.join(modified)}")

    # union set A and set B into a new set containing only unique elements.
    # in other words, sum me the iterables and perform set() on the result to remove repetition.
elif sum(set_odd) > sum(set_even):  # difference
    modified = [str(el) for el in set_odd - set_even]
    print(f"{', '.join(modified)}")

    # return me a set of elements that exist only in set A but not in set B OR vice versa.
elif sum(set_odd) < sum(set_even):  # symmetric difference
    modified = [str(el) for el in set_odd ^ set_even]
    print(f"{', '.join(modified)}")

    # between two sets A and B is the set of elements that are in either A or B but NOT in their intersection.
    # in other words, return me a set of the elements that are in set A but not in set B AND vice versa.

    # symmetric diff and diff are the same, except that the diff method return set applies only for one of the sets.
