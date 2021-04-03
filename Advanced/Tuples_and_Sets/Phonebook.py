# Phonebook

def fill_phonebook(book, name, phone):
    if name in book:
        book[name] = phone
    else:
        book[name] = phone


phonebook = {}
command = input()
search_count = 0

while True:
    if command.isdigit():
        search_count = int(command)
        break
    n, p = command.split('-')
    fill_phonebook(phonebook, n, p)
    command = input()

for _ in range(search_count):
    searched = input()
    if searched in phonebook:
        print(f"{searched} -> {phonebook[searched]}")
    else:
        print(f"Contact {searched} does not exist.")
