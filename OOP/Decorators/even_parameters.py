def even_parameters(fn):
    def wrapper(*args, **kwargs):
        filtered_strs = [el for el in args if isinstance(el, str)]
        if filtered_strs:
            return "Please use only even numbers!"
        filtered_odds = [el for el in args if el % 2 != 0]
        if filtered_odds:
            return "Please use only even numbers!"
        res = fn(*args, **kwargs)
        return res
    return wrapper