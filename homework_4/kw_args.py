def create_dict(**kwargs):
    result = {}
    for key, value in kwargs.items():
        hashable_key = key
        if not isinstance(key, (int, float, str, tuple, frozenset)):
            hashable_key = str(key)
        result[hashable_key] = value
    return result
result = create_dict(a=15, b=27, c="TEXT", d=[1, 2, 3])
print(result)