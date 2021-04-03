# Balanced Parentheses

opening = ['[', '(', '{']
closing = [']', ')', '}']
input_line = list(input())


def check(input):
    stack = []
    for par in input:
        if par in opening:
            stack.append(par)
        elif par in closing:
            position = closing.index(par)
            if len(stack) > 0 and stack[-1] == opening[position]:
                stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    return False


result = check(input_line)

if result:
    print('YES')
else:
    print('NO')
