# lists are standard collection type.
# Defined by square brackets
# able add/remove modify indexed elements
list = ["Rachel", "Renee", "Beacham"]

# tuples has parenthesis
# cannot add/be modified once created
tuple = ("Rachel", "Renee", "Beacham")

# sets indicated by curly brackets
# sets cannot have duplicates
# sets are like lists but do not have an index/order - so you cannont access an element by index
set = {"Rachel", "Renee", "Beacham"}

list.append('27')
# append method adds an element
print(list)
print(list[0])
list.remove('Renee')
#remove method removes an element
print(list)
