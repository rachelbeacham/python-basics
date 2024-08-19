# Function takes in an argument that should be a list, and will return a float
def list_avg(sequence: list) -> float:
  return sum(sequence) / len(sequence)

# print(list_avg(123)) -- WILL RETURN AN ERROR DUE TO THE ARG BEING THE WRONG TYPE
print(list_avg([1,2,3]))
