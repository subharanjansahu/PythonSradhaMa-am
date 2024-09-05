'''
Define an Employee class with attributes role, department & salary. This class has also showDetails() method.
Create an Engineer class that inherits properties from Employee and has adidtional attributes name & age.
'''

class Employee:
  def __init__(self,role,dept,sal) -> None:
    self.role = role
    self.dept = dept
    self.sal = sal
  
  def showDetails(self):
    print("Role = ",self.role)
    print("Department = ", self.dept)
    print("Salary = ",self.sal)

class Engineer(Employee):
  def __init__(self, role, dept, sal,name,age) -> None:
    super().__init__(role, dept, sal)
    self.name = name
    self.age = age

  def details(self):
    # Call the super class methods
    super().showDetails()
    print('Name is = ',self.name)
    print("Age = ",self.age)

# emp = Employee('ca','act',55000)
# emp.showDetails()

eng = Engineer('ca','act',39000,'Syama',27)
eng.details()