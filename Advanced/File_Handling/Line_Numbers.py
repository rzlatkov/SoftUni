# Line Numbers

import re


def get_letters(line):
    r1 = r"[a-zA-Z]"
    return len(re.findall(r1, line))


def get_punctuations(line):
    r2 = r"[\.\,\!\?\-\'\"]"
    return len(re.findall(r2, line))


with open('text.txt', 'r') as reader, open('output.txt', 'w') as writer:
    lines = reader.readlines()
    count = 1
    for line in lines:
        letters_count = get_letters(line)
        punctuation_count = get_punctuations(line)
        writer.write(f"Line {count}: {line.strip()} ({letters_count})({punctuation_count})\n")
        count += 1
