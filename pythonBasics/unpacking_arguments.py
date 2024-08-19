# * signals python to collect the arguments into a single variable called args


def multiply(*args):
  # print(args)
  total = 1
  for arg in args:
    total = total * arg
  return total

# print(multiply(1,3,5))

def add (x, y):
  return x + y

nums = [3,5]
# The * here is ued to destructure the nums value so that one value is used for each parameter
print(add(*nums))

#using named arguments
namedNums = {"x": 15, "y": 25}
## BAD - add(x=namedNums["x"], y=namedNums["y"])

## ** tells python to use each key as a named argument, result is same as line 23
print(add(**namedNums))

## * collects all the arguments into variable called args
# must pass in the operator as a named argument in order to seperated it from the collected args
def apply(*args, operator):
  if operator == "*":
    # must used * here again when calling multiply() so that the collected args are destructured back into individuals rather than the collected tuple
    # then multiply will collect the individuals again into one variable
    return multiply(*args)
  elif operator == "+":
    return sum(args)
  else:
    return "No valid operator provided to apply()."

print(apply(1,3,6,7, operator="*"))
