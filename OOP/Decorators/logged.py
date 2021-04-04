def logged(fn):
    def wrapper(*args, **kwargs):
        output = f"you called {fn.__name__}{args}\n"
        res = fn(*args, **kwargs)
        output += f"it returned {res}"

        return output
    return wrapper