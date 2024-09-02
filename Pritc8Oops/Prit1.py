'''
Create student class that takes name and marks of 3 subjects as argument in constructor.
Then create a method to print the average.
'''

# class Student:
#   def __init__(self,name,phy,che,mth) -> None:  
#     self.phy = phy
#     self.che = che
#     self.mth = mth
#     self.name = name    
#     print(name,"Marks of 3 Subjects are ",phy,che,mth)
  
#   def avg(self):
#     return (self.phy + self.che + self.mth)/3
  
# s1 = Student('karan',10,5,6)
# print("Average mark is",int(s1.avg()))

# or

class Student:
  def __init__(self,name,marks) -> None:
    self.name = name
    self.marks = marks

  def avg(self):
    sum = 0
    for i in self.marks:
      sum = sum + i
    return sum/3

s1 = Student("Tony",[98,75,83])
s1.name = 'ironman'
print(s1.name,"Average mark is ",int(s1.avg()))