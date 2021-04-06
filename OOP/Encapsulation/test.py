def test_sum(num1, *args):
    print(args)
    return num1 + sum(args)


print(test_sum(2,1))
