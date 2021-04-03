# Even numbers

def even(a_list):
    print(list(filter(lambda x: x % 2 == 0, a_list)))


a_list = [int(num) for num in input().split()]
even(a_list)
