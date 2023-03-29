import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x) #JSON string, you can parse it by using the json.loads() method.

# the result is a Python dictionary:
print(y["age"])


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x) #convert python into a json object.
# the result is a JSON string:
print(y)
