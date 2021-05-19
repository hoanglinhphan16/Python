import sys

# HANDLING EXCEPTIONS
'''
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print('D')
    except C:
        print('C')
    except B:
        print('B')

try:
    f = open('mytext.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise

try:
    raise Exception('Egg','Noodles')
except Exception as ints:
    print(type(ints))
    print(ints)
    print(ints.args)

    x, y = ints.args
    print('x = ', x)
    print('y = ' + repr(y))


def this_fails():
    a = 1/0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handling run-time error: ', err)
'''

# EXCEPTIONS CHAINING
'''

def func():
    raise IOError


try:
    func()
except IOError as exc:
    raise RuntimeError('Failed to open database') from exc
'''


# DEFINING CLEAN-UP ACTIONS
def bool_return():
    try:
        return True
    finally:
        return False


bool_return()   # return True after that return False

def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('division by zero')
    else:
        print('result is ', result)
    finally:
        print('Executing finally clause')

divide(4, 0)