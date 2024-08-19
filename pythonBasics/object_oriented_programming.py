## NOT OOP
student = {"name": "Rolf", "grades": (89, 90, 93, 78, 90)}

def average(sequence):
  return sum(sequence)/len(sequence)

print(average(student['grades']))

## Object oriented programming
# A class creates an object, through the init method, and assign the name property of that object
class Student:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades

  def average_grade(self):
    return sum(self.grades)/len(self.grades)


student = Student('Rachel', (89, 90, 93, 100, 90))
#can create multiple objects with different args in a new variable
student2 = Student('Bob', (89, 83, 87, 78, 90))
print(student.name)
print(student.grades)
print(f"{student.name} has an average grade of: {student.average_grade()}")
print(f"{student2.name} has an average grade of: {student2.average_grade()}")
