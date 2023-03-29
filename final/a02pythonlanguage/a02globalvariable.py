x = "awesome"

def myfunc():
   global x  #refers to global variable think about it..
   x = "fantastic"
   print("Python is " +  x)

myfunc()

print("Python is " + x)

#scope of python variables.
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def myfunc1():
  x = 300
  def myinnerfunc1():
    print(x)
  myinnerfunc1()

myfunc1()

#A variable created outside of a function is global and can be used by anyone:

gv=1
def freak():
  global gv  #without thiswe are referring to the local varable.. think 1000 times before using.
  gv=23

def junk():
  print(gv)

freak()
junk()



