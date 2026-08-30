def get_value(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        print("Key not found in the dictionary.")


dictionary = {'a': 1, 'b': 2, 'c': 3}
print(get_value(dictionary, 'a'))  # Output: 1  
print(get_value(dictionary, 'd'))  # Output: Key not found in the dictionary.     