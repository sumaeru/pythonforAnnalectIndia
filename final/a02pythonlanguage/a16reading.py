f = open("a16file.txt", "r")
print(f.read())
#By default the read() method returns the whole text, but you can also specify how many 
# characters you want to return:

f= open("a16file.txt", "a")
x="hello"  #try to think get json from object.. 
f.write(x)
f.close()

#open and read the file after the appending:
f = open("a16file.txt", "r")
print(f.read())

#checking whether file exists or not..
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")


# removing complete folder
import os
os.rmdir("myfolder")
