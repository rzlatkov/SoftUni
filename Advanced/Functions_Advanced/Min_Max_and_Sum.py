# Min Max and Sum

def min_max_sum(a_list):
    print(f"The minimum number is {min(a_list)}")
    print(f"The maximum number is {max(a_list)}")
    print(f"The sum number is: {sum(a_list)}")


a_list = [int(num) for num in input().split()]
min_max_sum(a_list)
