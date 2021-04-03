# File Manipulator

import os.path


def create(file):
    with open(file, 'w'):
        pass


def add(file, content):
    try:
        with open(file, 'a') as appender:
            appender.write(content + '\n')
    except FileNotFoundError:
        with open(file, 'w') as writer:
            writer.write(content + '\n')


def replace(file, old_str, new_str):
    content = None
    new_content = None
    try:
        with open(file, 'r') as reader:
            content = ''.join(reader.readlines())
            new_content = content.replace(old_str, new_str)
        with open(file, 'w') as writer:
            writer.writelines(new_content.split('  '))
    except FileNotFoundError:
        print("An error occured")


def delete(file):
    try:
        os.remove(file)
    except FileNotFoundError:
        print("An error occured")


command = input()

while command != "End":
    if 'Create' in command:
        command = command.split('-')
        file_name = command[1]
        create(file_name)
    elif 'Add' in command:
        command = command.split('-')
        file_name = command[1]
        content = command[2]
        add(file_name, content)
    elif 'Replace' in command:
        command = command.split('-')
        file_name = command[1]
        old_data = command[2]
        new_data = command[3]
        replace(file_name, old_data, new_data)
    elif 'Delete' in command:
        command = command.split('-')
        file_name = command[1]
        delete(file_name)
    command = input()
