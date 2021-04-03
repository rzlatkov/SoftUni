# execution time

import time


def exec_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        return end - start
    return wrapper


# @exec_time
# def loop(start, end):
#     total = 0
#     for x in range(start, end):
#         total += x
#     return total
#
#
# print(loop(1, 10000000))

@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result


print(concatenate(["a" for i in range(1000000)]))

# test second zero
import unittest

class ExecTimeTests(unittest.TestCase):
    def test_zero_second(self):
        @exec_time
        def concatenate(strings):
            result = ""
            for string in strings:
                result += string
            return result
        self.assertEqual(round(concatenate(["a" for i in range(1000000)])), 0)

if __name__ == '__main__':
    unittest.main()
