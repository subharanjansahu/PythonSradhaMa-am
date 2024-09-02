# class Account:
#   def __init__(self,ac_no,ac_pw) -> None:
#     self.ac_no = ac_no
#     # make ac_pw as private(we use __ for making private variable)
#     self.__ac_pw = ac_pw

#   def reset(self):
#     print(self.__ac_pw)

# acct1 = Account('1234','abcd')
# acct1.reset()
# print(acct1.ac_no)
# print(acct1.reset())
# print(acct1.__ac_pw)


class Person:
  # attribute private
  __name = 'Subha'

  # method private
  def __hello(self):
    return "hello person"

  print(__name)
  def call(self):
    return self.__hello()

p1 = Person()
print(p1.call())
# print(p1.__name)  #gives an error
# print(p1.__hello())   #gives an error