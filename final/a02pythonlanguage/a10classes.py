class MyClass:
  x = 5
  y = 7



print(MyClass)

y=MyClass();  #i=3
z=MyClass();
y.x=3;
z.x=5;
print(y.x,z.x)

#constructor..a functon that gets called when object is created

class Person:
  def __init__(self, name, age): #acts like a constructor
    self.name = name
    self.age = age

  def __str__(self):#function used when used to represent as a string
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)


