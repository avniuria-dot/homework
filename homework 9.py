def union_sets(set1, set2):
    return set1.union(set2)

def intersection_sets(set1, set2):
    return set1.intersection(set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", union_sets(set1, set2))  # Output: {1, 2, 3, 4, 5, 6}
print("Intersection:", intersection_sets(set1, set2))  # Output: {3,