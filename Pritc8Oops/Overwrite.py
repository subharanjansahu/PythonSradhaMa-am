class A:
  def hello(self):
    print('hello welcome to Class A')

class B(A):
  def hello(self):
    print('hello welcome to Class B')

b = B()
b.hello()
print(super())