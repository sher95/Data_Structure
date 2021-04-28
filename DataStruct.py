# Big O
"""
def get_squared_num(numbers):
    squared_num = []
    for n in numbers:
        squared_num.append(n*n)
    return squared_num

numbers = [2, 5, 8, 9]
print(get_squared_num(numbers))"""

# Array only dynamic in python
import threading
import time

"""
arr = [65, 45, 43, 23, 22, 47]
print(arr[0])
for i in arr:
    print(i)"""

# Linked List
"""
class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print('Linked list empty')
            return
        itr = self.head
        lstr = ''

        while itr:
            lstr += str(itr.data) + '---->'
            itr = itr.next

        print(lstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begin(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_begin(5)
    ll.insert_at_end(32)
    ll.insert_at_end(43)
    ll.insert_values(["banana", "mango", "orange"])
    ll.print()
    ll.remove_at(1)
    ll.insert_at(2, 'my bad')
    ll.print()
    print(ll.length())"""

# Hash table
# When store some data when hash wor k = key% space   h(k) = [(2k) + 3] % m
# This is collision and to solve it chaining is come WE CANT DELETE ONLY MINIMIZE COLLISION
# open hash(closed addr)  Chaining method use linked list to store other same data
# close hash(open addr)   Lenear probing use lenear check place if busy move to next place
#
"""
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val


hash = HashTable()
print(hash.arr)
hash['march6'] = 130
hash.get_hash(['march6'])
print()"""

# Stack
"""
from collections import deque


class stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)


stack = stack()
stack.push(5)
print(stack.size())
print(stack.peek())"""

# Queue
# Order food and serving with queue
"""
from collections import deque


class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]


q = Queue()


def place_order(orders):
    for order in orders:
        print("Placing order for: ", order)
        q.enqueue(order)
        time.sleep(0.5)


def serve_orders():
    time.sleep(1)
    while True:
        order = q.dequeue()
        print("Now serving: ", order)
        time.sleep(2)


if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'burger']
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_orders)
    t1.start()
    t2.start()"""

# General Tree
# List of electronics using tree
"""
class treeNode:
    def __init__(self, data):
        self.data = data
        self.childr = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.childr.append(child)

        # Will looks like nice
    def level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level


    def print_tree(self):
        space = ' ' * self.level() * 3
        prefix = space + "|__" if self.parent else ""

        print(prefix + self.data)
        if self.childr:
            for child in self.childr:
                child.print_tree()


def build_tree():
    root = treeNode("electronic")

    laptop = treeNode("laptop")
    laptop.add_child(treeNode("mac"))
    laptop.add_child(treeNode("samsung"))

    phones = treeNode("cell phones")
    phones.add_child(treeNode("Iphone"))
    phones.add_child(treeNode("galaxy s8"))
    phones.add_child(treeNode("vivo"))

    tv = treeNode("TV")
    tv.add_child(treeNode("samsung"))
    tv.add_child(treeNode("lg"))

    root.add_child(laptop)
    root.add_child(phones)
    root.add_child(tv)

    return root


if __name__ == '__main__':
    root = build_tree()

    root.print_tree()
    pass"""

# Binary tree
"""
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def inorder_traversal(self):
        elements = []
        # left
        if self.left:
            elements += self.left.inorder_traversal()

        # root
        elements.append(self.data)

        # right
        if self.right:
            elements += self.right.inorder_traversal()

        return elements

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def postorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.postorder_traversal()
        if self.right:
            elements += self.right.postorder_traversal()

        elements.append(self.data)

        return elements

    def preorder_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.preorder_traversal()
        if self.right:
            elements += self.right.preorder_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        left_sum = self.left.calculate_sum() if self.left else 0
        right_sum = self.right.calculate_sum() if self.right else 0
        return self.data + left_sum + right_sum

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)

        return self


def build(elements):
    root = BST(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':
    numbers = [17, 4, 5, 22, 18, 35]
    num_tree = build(numbers)
    print('input numbers: ', numbers)
    num_tree.delete(18)
    print("After delete 18", num_tree.preorder_traversal())
    #print("Min:", num_tree.find_min())
    #print("Max:", num_tree.find_max())
    #print("Sum:", num_tree.calculate_sum())
    #print("In order traversal:", num_tree.inorder_traversal())
    #print("Pre order traversal:", num_tree.preorder_traversal())
    #print("Post order traversal:", num_tree.postorder_traversal())
    #print(num_tree.search(4))"""

# Graph
"""
class graph:
    def __init__(self, edge):
        self.edge = edge
        self.graph_dict = {}
        for start, end in self.edge:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]
        print("graph", self.graph_dict)

    def get_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        for node in self.graph_dict[start]:
            if node not in path:
                new_path = self.get_path(node, end, path)
                for p in new_path:
                    path.append(p)

        return path

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path

        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == '__main__':
    routes = [
        ("Tashkent", "Almata"),
        ("Tashkent", "Tokyo"),
        ("Almata", "Tokyo"),
        ("Almata", "Seoul"),
        ("Tokyo", "Seoul"),
        ("Seoul", "Pekin")
    ]

    route_grapg = graph(routes)

    start = "Tashkent"
    end = "Seoul"

    print(f"shortest path between {start} end {end}:\t", route_grapg.get_shortest_path(start, end))
"""
