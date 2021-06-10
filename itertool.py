from itertools import product, permutations, combinations, accumulate, groupby

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
d = [1, 2, 3, 4]
comb = combinations(d, 2)
print(list(comb))  # will print [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# accumulate----add each other with result
# olso we can add module operator and multiplay to each other
# acc = accumulate(ac, func=operator.mul)
ac = [1, 2, 3, 4]
acc = accumulate(ac)
print(a)
print(list(acc))  # will print [1, 3, 6, 10]


# grouby

def smaller(x):
    return x < 3


gr = [1, 2, 3, 4]
grop = groupby(gr, key=smaller)
for key, value in grop:
    print(key, list(value))