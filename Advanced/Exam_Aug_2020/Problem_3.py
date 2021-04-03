# numbers search

def numbers_searching(*args):
    result = []
    duplicates = []
    unique = set(args)

    for num in range(min(unique), max(unique) + 1):
        if num not in unique:
            result.append(num)
        elif args.count(num) >= 2:
            duplicates.append(num)

    duplicates.sort()
    result.append(duplicates)
    return result
