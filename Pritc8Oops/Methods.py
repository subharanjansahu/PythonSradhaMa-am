class Student:
  clg = "ABC College"
  def __init__(self,name,mark) -> None:
    self.name = name
    self.mark = mark
    print(name)

  def welcom(self):
    print("Welcom students",self.clg,self.name)
  
  def get_mark(self):
    return self.mark

s1 = Student('karan',84)
s1.welcom()         #callable for 'def welcom(self):'
# Student.welcom()    #callable for 'def welcom():' it is called static methods
print(s1.name,"your mark is",s1.get_mark())