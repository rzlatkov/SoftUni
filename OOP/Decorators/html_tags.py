# html tags

def tags(param):
    def inner(func):
        def wrapper(*args, **kwargs):
            result = f"<{param}>{func(*args, **kwargs)}</{param}>"
            return result
        return wrapper
    return inner

# @tags is equivalent  to the next two lines:
# tags = tags(param) -> calling tags() which returns inner (obj)
# function = tags(tags(param)) -> calling inner() which returns wrapper (obj)


@tags('p')
def join_strings(*args):
    return "".join(args)


@tags('h1')
def to_upper(text):
    return text.upper()


@tags('b')
def to_bold(text):
    BOLD = '\033[1m'
    END = '\033[0m'
    return BOLD + text + END

@tags('u')
def to_underline(text):
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    return UNDERLINE + text + END


print(to_upper('hello'))
print(join_strings("Hello", " you!"))
print(to_bold('hello'))
print(to_underline('hello'))
