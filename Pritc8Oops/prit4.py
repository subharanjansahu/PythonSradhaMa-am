'''
Create a class called Order which stores items and its price.
Use Dunder function __gt__() to convey that:
    order1 > order2 if price of order1 > price of order2.
'''
# use function
'''
class Order:
  def __init__(self,item,price) -> None:
    self.item = item
    self.price = price

  def gt(self,ord2):
    if(self.price > ord2.price):
      print("order1 > order2")
    else:
      print("order2 > order1")

ord1 = Order('chips', 20)
ord2 = Order('tea', 155)

ord3 = ord1.gt(ord2)
'''

# use dunder function

class Order:
  def __init__(self,item,price) -> None:
    self.item = item
    self.price = price

  def __gt__(self,ord2):
    return self.price > ord2.price

ord1 = Order('chips', 20)
ord2 = Order('tea', 155)

ord3 = ord1 > ord2
print(ord3)
# or
print(ord1 > ord2)