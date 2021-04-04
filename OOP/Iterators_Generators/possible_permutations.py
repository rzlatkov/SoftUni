import itertools


def possible_permutations(a_list):
    result = list(itertools.permutations(a_list))
    for perm in result:
        yield list(perm)