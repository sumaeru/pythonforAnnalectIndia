def great(num):
  return num+3;

great(4)
great()# remember argument are compulsorily needed.. else use default arguments..


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")


def my_function(*kids):#indicates that multiple arguments can be passed
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") #keywords for arguments


#Arbitrary Keyword Arguments, **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

#default parameter values.
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#passing default values.. think about it.
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)