### Set Operations
# difference method returns the value in the set that difference is called on
# that is not in the set in the parenthesis
friends = {'Bob', 'Rolf', 'Anne'}
abroad = {'Bob', 'Anne'}
local_friends = friends.difference(abroad)
# print(local_friends)

# the union method returns a set that combines 2 sets
local = {'Rolf'}
abroadd = {'Bob', 'Anne'}
combined = local.union(abroadd)
# print(combined)

# the intersection method returns the values that are in 2 sets
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 12, 9, 30, 21, 44}
common = set1.intersection(set2)
# print(common)
