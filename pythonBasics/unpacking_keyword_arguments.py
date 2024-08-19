# ** collects named arguments and puts them into a dictionary
def named(**kwargs):
  print (kwargs)

named(name="bob", age=25)

def named2(name, age):
  print(name, age)

details = {"name": "Bob", "age": 25}
## ** in a function call can be used to unpack a dict into keywordf arguments
named2(**details)


def print_nicely(**kwargs):
  # kwargs is a dict containing the named args
  # calling named with collected dict, destructued back into named args
  # named structures named args back into dict and then prints the dict
  named(**kwargs)
  # loop through the collected dict and print out each keyword/value pair
  for arg, value in kwargs.items():
    print(f"{arg}: {value}")

print_nicely(name="bob", age=25)

# you can collect all the positional arguments into one variable called args
# and all the named args into a dict called kwargs
def both(*args, **kwargs):
  print(args)
  print(kwargs)

both(1,2,3, name="Rachel", age=27)
