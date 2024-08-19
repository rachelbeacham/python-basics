class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # use the "magic method (noted by __ __) str,
  # when you go to printo out this object it will return the string you define here rather than the one created by python"
  def __str__(self):
    return f"{self.name} is {self.age} years old"

  def __repr__(self):


bob = Person("Bob", 25)
# printing out the object you created returns a default string created by python that represents the string (unless you define a __str__ magic method)
print (bob)
