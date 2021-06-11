from functools import reduce

mult = lambda x, y: x * y
print(mul(2, 8))

a = [1, 2, 3, 4]
prod = reduce(lambda x, y: x * y, a)
print(prod)
