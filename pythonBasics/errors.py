def divide(dividend, divisor):
  if divisor == 0:
    # built in type of error exception object in python
    raise ZeroDivisionError("Divisor cannot be 0.")
  return dividend / divisor

grades = [90, 94, 78, 86, 77, 89, 95]
gradesError = []

print("Welcome to the average grade program")

# Can handle error exceptions using try/except block
# run the function inside the try block
try:
  average = divide(sum(gradesError), len(gradesError))
# if a ZeroDivisionError is found the except code executes
# you can create a variable called e, python will put the value of the error message as the e variable
except ZeroDivisionError as e:
  print(e)
  print('There are no grades yet.')
except ValueError:
  # Can catch multiple errors using different except clauses.
else:
  # else block will run if the except block did NOT run - NO ERROR FOUND
  print(f'The average grade is {average}')
finally:
  # finally block will run always, whether error was found or not
  print('Thank you!')




## Some other types of errors:
# TypeError, ValueError, RuntimeError - can create your own errors
