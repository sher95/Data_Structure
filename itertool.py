from itertools import product, permutations, combinations

# product
a = [1, 2]
b = [4, 3]
prod = product(a, b)
print(list(prod))  # will print [(1, 4), (1, 3), (2, 4), (2, 3)]

# permutations
c = [1, 2, 3]
perm = permutations(c)
print(list(perm))  # will print [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

# combination
