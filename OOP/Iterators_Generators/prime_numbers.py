def get_primes(a_list):
    for num in a_list:
        if num > 1:
            flag = False
            for i in range(2, num):
                if num % 2 == 0:
                    flag = True
                    break
            if not flag:
                yield num