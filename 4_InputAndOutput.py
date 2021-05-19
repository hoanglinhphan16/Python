import math

# 7.1 FANCIER OUT FORMATTING
year = 2021
event = 'Paradox Company'
print(f'This {year} i have been applied {event}')

y_votes = 456789123
n_votes = 465789321

percentage = y_votes/(n_votes + y_votes)
print('{:} YES votes {:2.5%}'.format(y_votes, percentage))

s = 'Hello World'

print(str(s))
print(repr(s))

x = 5*5
y = 10 + 12

s1 = 'The value of x is ' + repr(x) + ' and y is ' + repr(y)
print(s1)

# FORMATTED STRING LITERALS

print(f'Value of pi is approximately {math.pi:.3f}')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for i,n in table.items():
    print(f'{i:10} ===> {n:10}')

her = 'beautiful'
print(f'She so {her}')
print(f'She so {her!r}')        # her!r = repr(her)

# THE STRING FORMAT METHOD

print('The {} Company is so "{}!"'.format('Paradox', 'good'))
print('This {food} is {adjective}'.format(food='egg', adjective='absolutely delicious'))
print('This {0} is {1}'.format('egg', 'absolutely horrible'))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Dcab: {Dcab:d}; Jack: {Jack:d}; Sjoerd: {Sjoerd:d}'.format(**table))

# MANUAL STRING FORMATTING

for i in range(1, 10):
    print('{0:2d} {1:3d} {2:4d}'.format(i, i**2, i*i*i))

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(2))

print('The value of Pi is %5.100f.' % math.pi)
'''
f = open('Test.txt')
with open('Test.txt') as f:
    read_data = f.read()
f.close()
print(read_data)
'''
# METHOD OF FILE OBJECTS
'''
f = open('Test.txt')
with open('Test.txt') as f:
    for line in f:
        print(line, end='')
f.close()
'''

'''
f = open('Test.txt', 'w')
with open('Test.txt', 'w') as f:
    value = ('Seventh line', 42)
    s = str(value)
    f.write(s)
f.close()
'''

f = open('workfile.txt', 'rb+')
f.write(b'0123456789abcdef')

print(f.seek(5))
print(f.read(1))
print(f.seek(-15, 2))
    