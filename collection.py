from collections import Counter, namedtuple, OrderedDict, defaultdict, deque

a = "aaaaabbbbbbcccc"
my_counter = Counter(a)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1))

# Tuple
point = namedtuple('point', 'x,y')

pt = point(1, -2)
print(pt)  # will print point(x=1, y=-2)

# Order dict
ordered = OrderedDict()
ordered = {'12': 'wa', 'a': 1, 'b': 1, 'c': 1, 'd': 1, 'e': 1}
print(ordered)

# defaultdict
d = defaultdict(int)
d = {'a': 1, 'b': 2}
print(d)

# deque

de = deque()
de.append(1)
de.append(2)
de.appendleft(5)
print(de)
de.pop()
de.extend([3, 4, 'e'])  # add lifo
print(de)