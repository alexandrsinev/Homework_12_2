def get_val(collection, key, default='git'):
    if collection == {}:
        return default
    return collection[key]