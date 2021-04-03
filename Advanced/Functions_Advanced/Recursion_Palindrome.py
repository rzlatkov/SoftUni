# Recursion Palindrome

def palindrome(word, index):
    if len(word) % 2 == 0:
        middle = (len(word) % 2) - 1
    else:
        middle = len(word) // 2
    if 0 < len(word) < 2:
        return f"{word} is a palindrome"
    if word[index] == word[-(index+1)] and index < middle:
        return palindrome(word, index+1)
    if index == middle:
        return f"{word} is a palindrome"
    return f"{word} is not a palindrome"


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
