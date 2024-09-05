'''
Property Decorator:- We use @property decorator on any method in the class to use the method as a property. 
'''
# class Student:
#   def __init__(self,phy,chem,math) -> None:
#     self.phy = phy
#     self.chem = chem
#     self.math = math

#     self.percentage = str((self.chem + self.math + self.phy)/3) + '%'

# std1 = Student(98,97,99)
# print(std1.percentage)
# # if we want to change the subject mark then the percentage does not change it's the problem
# std1.chem = 86
# print(std1.chem)
# print(std1.percentage)    # 98.0% which is wrong


# Solution
# Sol-1 To over come this problem we use the method
# class Student:
#   def __init__(self,phy,chem,math) -> None:
#     self.phy = phy
#     self.chem = chem
#     self.math = math
#     self.percentage = str((self.chem + self.math + self.phy)/3) + '%'

#   def per(self):
#     self.percentage = str((self.chem + self.math + self.phy)/3) + '%'

# std1 = Student(98,97,99)
# print(std1.percentage)
# std1.chem = 86
# print(std1.chem)
# std1.per()
# print(std1.percentage)

# Sol-2 @property decorator
class Student:
  def __init__(self,phy,chem,math) -> None:
    self.phy = phy
    self.chem = chem
    self.math = math
    
  @property
  def percentage(self):
    return str((self.chem + self.math + self.phy)/3) + '%'
  
std1 = Student(98,97,99)
print(std1.percentage)
std1.chem = 86
print(std1.percentage)