from itertools import chain
dict_1 = {'a': 2, 'c': 3, 'd': 4}
dict_2 = {'a' : 2, 'b' : 3, 'd' : 5}

def dict_diff(dict1, dict2):
    dict_keys = {}
    for key, value in chain(dict1.items(), dict2.items()) : 
        if key in dict_keys and dict_keys.get(key) != value:
            dict_keys[key] = [dict_keys.get(key), value]
        elif key not in dict_keys :
            dict_keys[key] = value 
        elif key  in dict_keys :
            dict_keys.pop(key)
    return dict_keys

print(dict_diff(dict_1, dict_2))