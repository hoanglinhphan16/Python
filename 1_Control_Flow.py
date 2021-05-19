from collections import deque
from math import pi

# if Statement
'''
x = int(input("an integer,PLEASE:"))
if x<0:
    x = 0
    print('Stupid. I will change to Zero:',x)
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else: print('More')
'''

'''
# for Statements
words = ['cat', 'doge', 'safemoon']
for i in words:
    print(i, len(i))

# range() Func
a = ['Linh', 'Khoa', 'Dung']
for i in range(len(a)):
    print(i, a[i])
'''

# Other
'''
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '=', x, '*', n//x)
            break
    else:
        print(n, 'la so nguyen to')

for n in range(2,10):
    if n % 2 == 0:
        print(n, 'la so chan')
        continue
    print(n, 'la so le')
'''

'''
# Defining Funcs
def fib(n):
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        print(result)
    return result

fib(0)
'''
'''
# Keyword Arg
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(110)
'''

'''
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
'''

'''
#Function Annotations
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

f('spam')

'''

# LAMBDA EXPRESSIONS
# DOCUMENTATION STRINGS
