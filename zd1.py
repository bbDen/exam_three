def func(list_):
    keys_dict = {}
    for i in list_:
        if isinstance(i, bool):
            keys_dict.update({'boolean': i})
        elif isinstance(i, float):
            keys_dict.update({'float': i})
        elif isinstance(i, str):
            keys_dict.update({'str': i})
        elif isinstance(i, int):
            keys_dict.update({'int': i})
        else:
            keys_dict.update({'None': i})
    return keys_dict


value_list = [2, 4.7, "hi", False, None]

print(func(value_list))
