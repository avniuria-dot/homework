def count_elements_in_tuples(list1):
    dictionary = {}
    for tup in list1:
        for element in tup:
            if element in dictionary:
                dictionary[element] += 1
            else:
                dictionary[element] = 1
    return dictionary

list_of_tuples = [(1, 2), (3, 4), (1, 5), (2, 3)]
result = count_elements_in_tuples(list_of_tuples)
print(result)  # Output: {1: 2, 2: 2, 3: 2, 4: 1, 5: 1}