"""A lambda function is a small anonymous function.

A lambda function can take any number of arguments, but can only have one expression."""

print("hi")

#lambda arguments : expression

x = lambda a: a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)#storing functions as variables
mytripler = myfunc(3)#storing functions as variables.

print(mydoubler(11)) 
print(mytripler(11))





