# list manipulator

def list_manipulator(a_list, *args):
    result = []
    if args[0] == 'add':
        if args[1] == 'beginning':
            result = list(args[2:]) + a_list
        elif args[1] == 'end':
            result = a_list + list(args[2:])
    elif args[0] == 'remove':
        if args[1] == 'beginning':
            if len(args) > 2:
                result = a_list[args[2]:]
            else:
                result = a_list[1:]
        elif args[1] == 'end':
            if len(args) > 2:
                result = a_list[:-args[2]]
            else:
                result = a_list[:-1]

    return result
