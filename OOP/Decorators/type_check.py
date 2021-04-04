def type_check(a_type):
    def inner(fn):
        def wrapper(*args, **kwargs):
            filtered = [el for el in args if not type(el) == a_type]
            if filtered:
                return "Bad Type"
            return fn(*args, **kwargs)
        return wrapper
    return inner