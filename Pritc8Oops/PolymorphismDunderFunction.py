'''
Use double underscore before and after the function name
'''

class Complex:
  def __init__(self,real,img) -> None:
    self.real = real
    self.img = img

  def Show(self):
    print(self.real,"i +",self.img,'j')

  # def add(self, self2):
  def __add__(self, self2):   #self -> num1, self2 -> num2
    newReal = self.real + self2.real
    newImg = self.img + self2.img
    return Complex(newReal, newImg)
  
num1 = Complex(1,3)
num1.Show()

num2 = Complex(5,2)
num2.Show()

# num3 = num1.add(num2)
num3 = num1 + num2
num3.Show()