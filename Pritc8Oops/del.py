class Student:
  def __init__(self,name,roll) -> None:
    self.name = name
    self.roll = roll
  def input_std(self):
    print("Name :",self.name,"and rollno. :"+str(self.roll))

i = Student('sam',34)
i.input_std() 

# attribute delete
# del i.name
# print(i.name," ",i.roll)

# object delete
del i
print(i)