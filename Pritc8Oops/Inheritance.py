# single inheritance
'''
class Car:
  def start(self):
    print("Car start...")

class Toyota(Car):
  def __init__(self,name) -> None:
    super().__init__()
    self.name = name

t = Toyota('fortuner')
print(t.name)
print(t.start())

'''

# multilevel inheritance
'''
class Car:
  def start(self):
    return 'Car started...'

class Enginee(Car):
  def petrol(self):
    print('you choose petrol enginee')
  def ev(self):
    print('you chosse ev enginee')

class Toyota(Enginee):
  def __init__(self,name) -> None:
    super().__init__()
    self.name = name

t = Toyota('Fortuner')
print(t.name)
print(t.start())
print(t.petrol())
'''

# multiple inheritance
'''
class Car:
  @staticmethod
  def start():
    print('car started...')
  
  @staticmethod
  def stop():
    print('car stoped...')

class Enginee:
  @staticmethod
  def petrol():
    print("Petrol enginee")
  @staticmethod
  def ev():
    print('EV enginee')

class BMW(Car,Enginee):
  def call(self):
    print("derived class")
  
  def __init__(self,name) -> None:
    super().__init__()
    self.name = name

b = BMW('zlx')
print(b.name)
b.call()
b.start()
b.stop()
b.ev()

'''

