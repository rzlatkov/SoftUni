# number classification

numbers = input().split(', ')
even = []
odd = []
positive = []
negative = []

for num in numbers:
    int_num = int(num)
    if int_num >= 0 and int_num % 2 == 0:
        positive.append(num)
        even.append(num)
    elif int_num >= 0 and int_num % 2 != 0:
        positive.append(num)
        odd.append(num)
    elif int_num < 0 and int_num % 2 == 0:
        negative.append(num)
        even.append(num)
        pass
    elif int_num < 0 and int_num % 2 != 0:
        negative.append(num)
        odd.append(num)

print("Positive: " + ', '.join(positive))
print("Negative: " + ', '.join(negative))
print("Even: " + ', '.join(even))
print("Odd: " + ', '.join(odd))
