# number = 7
# user_input = input("would you like to play? (Y/n) ")
# # while loop
# while user_input != 'n':
#   user_number = int(input("Guess our number: "))
#   if user_number == number:
#     print('You guessed correctly!')
#   elif abs(number - user_number) == 1:
#     print('You were off by one.')
#   else:
#     print("Sorry, it's wrong!")

#   user_input = input("would you like to play? (Y/n) ")
## small issue with this code: lines 2 and 13 are duplicates!

## Refactor while loop
number = 7
# while true creates an infinite loop
# so you must exit the loop at some point within the loop
while True:
  user_input = input("would you like to play? (Y/n) ")
  if user_input == 'n':
    break
    #break keyword allows you to exit/terminate the loop
  user_number = int(input("Guess our number: "))
  if user_number == number:
    print('You guessed correctly!')
  elif abs(number - user_number) == 1:
    print('You were off by one.')
  else:
    print("Sorry, it's wrong!")

## For loops
# allows you to repeat code for each element in a list, tuple or set
friends = ['Stephen', 'Sam', 'Paige', 'Kayla', 'Ruby']
for friend in friends:
  print (f'{friend} is my friend')

grades = [35, 67, 98, 100 , 100]
total = 0
#len method gets the count of elements
amount = len(grades)
for grade in grades:
  total += grade

#don't actually need a for loop in this case:
# python has a sum method that will add all the elements in a list, see refactor below

average = (total / amount)
print(average)

### GRADES REFACTOR:
grades = [35, 67, 98, 100 , 100]
total = sum(grades)
amount = len(grades)

average = (total / amount)
print(average)
