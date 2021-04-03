# Odd or Even

def odd_or_even(a_list, command):
    if command == "Odd":
        print(sum(list(filter(lambda x: x % 2 != 0, a_list))) * len(a_list))
    else:
        print(sum(list(filter(lambda x: x % 2 == 0, a_list))) * len(a_list))


command = input()
a_list = [int(num) for num in input().split()]
odd_or_even(a_list, command)
