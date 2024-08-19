numbers = [1,2,3]
# this line is the same as the for loop below
# list comprehension creates a new list
doubled = [num * 2 for num in numbers]

# for num in numbers:
#   doubled.append(num * 2)

print(doubled)

friends = ['Rolf','Sam', 'Samantha', 'Henry', 'Sara', 'Jen']
# same as for loop below, if statement goes at the end
starts_s = [friend for friend in friends if friend.startswith('S')]

# for friend in friends:
#   if friend.startswith('S'):
#     starts_s.append(friend)

print(starts_s)
