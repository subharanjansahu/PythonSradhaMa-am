'''
WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary and add one by one. Use subject name as key and mark as value.
'''
# not runable update later
# dict = {}
# x = len(dict)
# if(x <= 3):
#   for i in dict:
#     sub = input("enter sub:")
#     m = int(input("Enter marks:"))
#     dict.update({sub : m})
# print(x)

marks = {}
sub = input("enter sub:")
m = int(input("Enter marks:"))
marks.update({sub : m})

sub = input("enter sub:")
m = int(input("Enter marks:"))
marks.update({sub : m})

sub = input("enter sub:")
m = int(input("Enter marks:"))
marks.update({sub : m})
print(marks)

# marks = {}
# count = 1
# while(count <= 3):
#   sub = input("enter sub:")
#   m = int(input("Enter marks:"))
#   marks.update({sub : m})
#   count +=1
# print(marks)