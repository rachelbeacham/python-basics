# Lambda functions are used to operate on inputs and return outputs, never used to perform actions
# Lambdas are function without a name, can give them a name by assigning them to a variable
# Used to return a value calculated from parameter, usually a single line
# most situations, better to define a regular function
def add(x,y):
  return x + y

print(add(5,7))

# below is the above function written as a lambda function.
# this lambda function is assigned to the variable called add

add = lambda x, y: x + y
