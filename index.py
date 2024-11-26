print('hello world')
# import sys

# print(sys.version)

if 5 > 2:
    print('Python 5 is greater than Python 2')
    print('Python 5 is greater than Python 3')

a = 5
b = 7

print(b % a)

wisdom = 'ajibola'

print(type(a))

# assigning multiple arguments to multiple variables at the same time
x, y, z = 'a', 'b', 'c'
print(x, y, z)

# unpacking a tuple into multiple variables
fruits = ['apple', 'orange', 'banana', 'pawpaw', 'watermelon']
a, b, c, d, e = fruits
print(a)

# Outputting variables
five = 5
four = 4
eleven11 = 'eleven'
ten = 'nine'
# + is use for numbers and comma(,) is used for string or string and number
print(ten  +  eleven11)

#implementing a global variable
def isGlobal(x):
    print(x)

isGlobal('ajibola')

# if statement with strings
if 'wisdo'