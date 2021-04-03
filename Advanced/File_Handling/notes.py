# test.txt

file = 'test.txt'

with open(file, 'r') as reader:
    a_list = reader.readlines()  # stores each line as an element in a list object
    print(a_list)

    # each time we press "enter" for a newline in a txt file,
    # the element (line) stored in the list after readlines()
    # has \n at the end. If we dont need it, we can use .strip() after .join of the list.

    for line in a_list:
        print(line)

    # if we print a_list immediately, the lines now are separated by a second \n.
    # The second \n comes from the print itself. To eliminate it we use end='' in print()

    line = reader.readline()
    while line != '':  # The EOF char is an empty string
        print(line, end='')
        line = reader.readline()

    # if we use readline() only (without 's' at the end) we literally read the file
    # line by line. We can select a certain line to be read if necessary.
    # Again we need to use end=''

    for line in reader:
        print(line, end='')

    # the 'while' variant simplified

    # WE CANNOT ITERATE/PRINT FILE LINES MORE THAN ONCE! If we execute this code,
    # only the 'a_list' list and the 1st for-loop will be printed.
    # we have to choose one way only.
