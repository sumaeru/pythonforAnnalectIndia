#operations think about  it
"""
create a dictionary
add a key and value
check whether a key exists
iterate thru the dictionary

"""

y="freak"
z=1
x = { y:z }
print(x)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#add new keys in dictionary
thisdict.update({'country': 'us'})

dic = {'a': 100, 'b':200, 'c':300}

# check if "b" is none or not.
if dic.get('b') == None:
    print("Not Present")
else:
    print("Present")






for key, value in thisdict.items():
    print(key, '<->', value)

# remove the item from the dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


#nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])





#As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

print(len(thisdict))

"""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""