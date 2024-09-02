class Student:
  name = 'Karan'
  print(name)
  def roll(self):
    return 45
  def sec(self):
    sec = input("Ent sec = ")
    print(self.name,"is study in sec",sec,"and roll no. is",self.roll())

ob = Student()
print(ob)
print(ob.name)
ob.sec()
print("Roll no. is",ob.roll())