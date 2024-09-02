class Student:

  # Default constructor
  def __init__(self):
    pass

  # Parameterized constructors 
  def __init__(self,fullname,marks):
    # print(self)
    self.name = fullname
    self.marks = marks
    # print(fullname)
    print("Adding student in database...")

s1 = Student('Karan',89)
print(s1.name,s1.marks)
# print(s1)

s2 = Student("Arjun",76)
print(s2.name,s2.marks)