# multiple args, kwargs to a func

def a_func(*args, **kwargs):
    user_input = list(args)
    user_input.append(kwargs)
    print(user_input)


a_func('str1', 'str2', [1, 2, 3, 4, 5], {'k1': 420, 'k2': 69}, asd=13)


# check type
a_dict = {'k': 5}
a_list = [1, 2, 3, 4]
a_str = 'abc'
a_tup = (1, 2, 3)
a_set = {2, 3}
print(isinstance(a_dict, dict))  # T
print(isinstance(a_list, dict))  # F
print(isinstance(a_list, list))  # T
print(isinstance(a_str, list))  # F
print(isinstance(a_str, str))  # T
print(isinstance(a_tup, tuple))  # T
print(isinstance(a_set, set))  # T
