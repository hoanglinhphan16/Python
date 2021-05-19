import math


# MORE ABOUT LISTS
'''
fruits = ['orange', 'apple', 'mango', 'banana', 'kiwi', 'apple', 'orange']

print(fruits.count('orange'))
print(fruits.index('apple', 2))
fruits.reverse()
print(fruits)
fruits.append('sida')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop(0)
print(fruits)
print(len(fruits))
'''

'''
queue = deque(["Marz", "Shirleng", "Hoang Linh"])
queue.append("Duy Trung")
queue.append("Thanh Hieu")
queue.popleft()
queue.popleft()
print(queue)
'''

# LIST COMPREHENSIONS
'''
squares = []
for i in range(10):
    squares.append(i**3)

print(squares)

squares1 = [x**2 for x in range(10)]

print(squares1)

squares2 = list(map(lambda x: x**2, range(10)))

print(squares2)

test = [(x, y) for x in [1, 3, 4] for y in [2, 4, 5] if x != y]

print(test)

test1 = []

for x in range(2, 10):
    for y in range(2, x+1):
        if x == y:
            test1.append((x, y))

print(test1)
'''

'''
vec = [-4, -2, 0, 2, 4]

vec = [x*2 for x in vec]
print(vec)

vec = [x for x in vec if x>=0]
print(vec)

vec = [abs(x) for x in vec]
print(vec)

Ffruits = ['banana', 'apple', 'kiwi']
Ffruits = [x.strip() for x in Ffruits]
print(Ffruits)

lyn = [(x, x**2) for x in range(6)]
print(lyn)

vec1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
vec1 = [num for i in vec1 for num in i]
print(vec1)

var = [str(round(pi, i)) for i in range(1, 6)]
print(var)
'''

'''
# NESTED LIST COMPREHENSIONS
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
# matrix = [[row[i] for row in matrix] for i in range(4)]
# print(matrix)

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

transposed1 = []
for i in range(4):

    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed1.append(transposed_row)

print(transposed1)

# is the best way print(list(zip(*matrix)))
'''

'''
# THE DEL STATEMENT
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
del a[8]
print(a)
'''

'''
# TUPLES AND SEQUENCES
t = 123, 456, 'abc'
print(t)
u = t, (7, 8, 9)
print(u)

empty = ()
singleton = 'hi',
print(len(empty))
print(singleton)
'''

'''
# SETS
a = set('abcdefghiklmnawkgjamsn')
b = set('balzjkajgeaoqwlzn')
print((a-b))         # letters in a but not in b
print((a | b))       # letters in a or b or both
print((a & b))       # letters in both a and b
print((a ^ b))       # letters in a or b but not both

c = [x for x in 'abracadabra' if x not in 'abc']
print(c)
'''


'''
# DICTIONARIES
tel = {'jack': 123, 'linh': 456}
tel['Chan'] = 113
print(tel['linh'])
del tel['jack']
print(tel)
print(list(tel))
print(sorted(tel))

check = dict([('jack', 123), ('linh', 456)])
print(check)

print({x: x**2 for x in (2, 4, 6)})
print(dict(Jack=4139, Linh=4127, Quynh=4098))
'''

'''
# LOOPING TECHNIQUES
who = {'linh': '22', 'quynh': '22'}
for m, n in who.items():
    print(m, n)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

test1 = ['Quynh', 'Long', 'Hoang']
test2 = ['Linh', 'Nghia', 'Trinh']

for i,n in zip(test1, test2):
    print('Hi {0}, Hello {1}'.format(i, n))

for i in reversed(range(1,10,1)):
    print(i)

for i in sorted(test1):
    print(i)

data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
filtered_not_data = []
for value in data:
    if math.isnan((value)):
        filtered_data.append(value)
    else: filtered_not_data.append(value)
print(filtered_not_data)
print(filtered_data)
'''
