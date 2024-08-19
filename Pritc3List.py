# mark = [54.5, 78.65, 69.5, 91.69, 86.78]
# print(mark[2])
# print(mark[-1])
# print(mark)
# print(type(mark))
# print(len(mark))

# list is mutable
# student = ["subha",98,"odisha"]
# print(student)
# print(student[0])
# student[-3]="arjun"
# print(student)

# Slicing of list
# marks = [45, 54, 85, 25, 97]
# print(marks[2:8])
# print(marks[:len(marks)])
# print(marks[:])
# print(marks[-5:-2])
# print(marks[:-1])
# # change value by using slicing
# marks [1:4] = [65,85,71]
# print(marks)
# marks [0:2] = [49]
# print(marks)


# WAP ask to user to enter of 3 fav movies name and store them in a list
# movies = []
# movies.append(input("Enter First movie: "))
# movies.append(input("Enter Second movie: "))
# movies.append(input("Enter third movie: "))
# print(movies)


# WAP to check if the list contains palindrome of element
# list = [1,2,3,2,1,]
list = [1,'abc',"abc",1,'s']
listcopy = list.copy()
listcopy.reverse()
print("Reverse of list is: ",listcopy)
if(list == listcopy):
  print("palindrome")
else:
  print("not palindrome")