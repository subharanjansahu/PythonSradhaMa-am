class Car:
  def __init__(self,type) -> None:
    self.type = type

  @staticmethod
  def start():
    print('Car started...')

  @staticmethod
  def stop():
    print('Car stoped...')

class ToyotaCar(Car):
  def __init__(self,name, type) -> None:
    super().__init__(type)
    self.name = name
    super().start()

car1  = ToyotaCar('prius','EV')
print(car1.type)
print(car1.name)