import random

"""
know how to create a list
know how to know the index position.
know how to modify the list.
know how to remove an element
how to view a particular element
how to sort the list.

"""


x=['a','d','c']
index=x.index('b')
del x[index]
print(index,x)

x.append("horror")

randomlist = random.sample(range(10, 30), 5)
print(randomlist,x)

print ("My name is %s and weight is %d kg!" % ('Zara', 21)) 

cars = ['ant', 'Zebra', 'Parrot']
cars.sort()

#list.sort(reverse=True|False, key=myFunc), use myFunc to give the comparison criteria if you got
#objects.


def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort()

print(cars)









