def make_bold(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args)
        output = '<b>' + res + '</b>'
        return output
    return wrapper


def make_italic(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args)
        output = '<i>' + res + '</i>'
        return output
    return wrapper


def make_underline(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args)
        output = '<u>' + res + '</u>'
        return output
    return wrapper