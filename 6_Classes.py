'''
# SCOPES AND NAMESPACES EXAMPLE
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment: ", spam)
    do_nonlocal()
    print("After nonlocal assignment: ", spam)
    do_global()
    print("After global assignment: ", spam)


scope_test()
print("In global scope: ", spam)
'''


# CLASS OBJECT

'''
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


x = Complex(3, 4.5)
print(x.r, x.i)
'''

# CLASS AND INSTANCE VARIABLES
'''
class Dog:
    kind = 'four foot'

    def __init__(self, name):
        self.name = name


d = Dog('Alaska')
e = Dog('Husky')
print(d.name)
print(d.kind)
print(e.name)
print(e.kind)


class Animal:

    def __init__(self, name):
        self.name = name
        self.kind = []

    def add_kind(self, check):
        self.kind.append(check)


d = Animal('Boss')
d.add_kind('dog')

e = Animal('Pet')
e.add_kind('Cat')
print(d.kind)
print(e.kind)
'''

# RANDOM REMARKS
'''
class Name:
    FistName = 'Linh'
    LastName = 'Phan Thanh Hoang'


name = Name()
print(name.FistName, name.LastName)
name2 = Name()
name2.LastName = 'Phan Vo Hoang'
print(name2.FistName, name2.LastName)
'''

# PRIVATE VARIABLES
'''
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(iterable)

    __update = update()  # private copy of original update() method


class MappingSubClass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
'''
# ODDS AND ENDS
'''
class Employee:
    pass

Linh = Employee()
Linh.old = '22'
Linh.sex = 'male'
Linh.birthday = '6/1'
print(Linh)

'''
# ITERATORS
'''
for element in [1, 2, 3]:
    print(element)
for element in (1, 2, 3):
    print(element)
for key in {'one': 1, 'two': 2}:
    print(key)
for char in "123":
    print(char)
for line in open("mytext.txt"):
    print(line, end="")


s = 'abc'
it = iter(s)

print(next(it))
print(next(it))
print(next(it))


class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
        print(self.index)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        print(self.index)
        return self.data[self.index]


rev = Reverse('spam')
iter(rev)
for i in rev:
    print(i)
'''
# GENERATORS
'''

def reverse(data):
    for k in range(len(data) - 1, -1, -1):
        yield data[k]


for m in reverse('floor'):
    print(m)

'''
# GENERATORS EXPRESSIONS

a = sum(i * i for i in range(10))
print(a)  # sum of squares
xvec = [9, 5, 2]
yvec = [7, 6, 4]
b = sum(x * y for x, y in zip(xvec, yvec))  # dot product
print(b)
data3 = 'golf'
list(print(data3[i]) for i in range(len(data3) - 1, -1, -1))
