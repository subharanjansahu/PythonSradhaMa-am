class Student:
  college_name = "ABC College"    #class attribute or variable
  name  = "Subha"

  def __init__(self,name):    #object attribute
    self.name = name
    print("Name is",name)

s1 = Student('karan')
print("Study in",s1.college_name)
clg = s1.college_name
print(clg)
print(s1.name)
print(Student.name)
print(Student.college_name)