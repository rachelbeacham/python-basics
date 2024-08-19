# Dictionaries are another data structure in python like lists, tuples, or sets
# used to associate key/value pairs

friend_ages = {"Rolf": 23, 'Adam': 30, 'Anne': 27}
print(friend_ages)
#can access or update values by accessing the keys using subscript notation
adams_age = friend_ages['Adam']
print(f"Adam is {adams_age}")

friend_ages['Rolf'] = 20

print(friend_ages)
