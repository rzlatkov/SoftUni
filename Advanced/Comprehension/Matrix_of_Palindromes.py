# Matrix of Palindromes

def palindromes(rows, cols):
    matrix = [[alphabet[i]+alphabet[n+i]+alphabet[i] for n in range(cols)] for i in range(rows)]
    return matrix


alphabet = 'abcdefghijklmnopqrstuvwxyz'
rows, cols = [int(el) for el in input().split()]
result = palindromes(rows, cols)
[print(' '.join(row)) for row in result]
