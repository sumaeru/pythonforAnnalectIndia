"""
The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.

The raise keyword is used to raise an exception.

"""
print(1)
x = -1

if x < 0:
  pass
  #raise Exception("Sorry, no numbers below zero")


try:
  f = open("one.txt","a")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  else :
    print("normal flow of code")
  finally:
    print("finally block") #exception occurs or not it will happen
    f.close()
except:
  print("Something went wrong when opening the file")  

