# we ca use assert than if
"""
x = -5
assert(x >= 0), 'x is not positive'
"""

try:
    a = 5 / '0'
except ZeroDivisionError as e:
    print(e, "\ncant devide to zero")
except TypeError as e:
    print(e)
