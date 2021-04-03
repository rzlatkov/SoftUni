
def stock_availability(a_list, *args):
    result = []
    if args[0] == 'delivery':
        result = a_list + list(args[1:])
    elif args[0] == 'sell':
        if len(args) > 1:
            if str(args[1]).isdigit():
                result = a_list[args[1]:]
            else:
                for order in args[1:]:
                    if order in a_list:
                        a_list = list(filter(lambda x: x != order, a_list))
                result = a_list
        else:
            result = a_list[1:]

    return result


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
