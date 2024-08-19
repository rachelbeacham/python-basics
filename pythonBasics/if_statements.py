### IF statements
day_of_week = input('What day of the week is it today? ').lower()
#lower method makes the input value lowercased
if day_of_week == 'monday':
  print('Today is Monday')
elif day_of_week == 'tuesday':
  print('Today is Tuesday')
else:
  print(f'Today is not Monday or Tuesday, it is {day_of_week}')
#indentation matters!!
print('this always runs')
