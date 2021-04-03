# Even Lines

import re

regex = r"[\-\,\.\?\!]"


def replace(line):
    return re.sub(regex, '@', line)


with open('text.txt', 'r') as reader:
    result = reader.readlines()  # list of the lines
    for line in range(len(result)):
        if line % 2 == 0:
            print(' '.join(replace(result[line]).split()[::-1]))
