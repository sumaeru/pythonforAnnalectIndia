#https://www.w3schools.com/python/python_datatypes.asp

x = 5
print(type(x))  #knowng data type of the variable..


def calculate(x, y, op='sum'):
    if not(isinstance(x, int) and isinstance(y, int)):
        print(f'Invalid Types of Arguments - x:{type(x)}, y:{type(y)}')
        raise TypeError('Incompatible types of arguments, must be integers')
    
    if op == 'difference':
        return x - y
    if op == 'multiply':
        return x * y
    # default is sum
    return x + y


#calculate(2,"Hello","multiply")


#The bool() function allows you to evaluate any value, and give you True or False in return,

"""
Most Values are True
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

#true things
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])



#false things
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


x = 200
print(isinstance(x, int))



