'''
you are a given list of subjects for students. Assume one classroom is required for 1 subject. how many classrooms are needed by all students.
  "python","java","c++","python","javascript",
  "java","python","java","c++","c"
'''

list = ["python","java","c++","python","javascript","java","python","java","c++","c"]
print(list)
print(len(list))
copy_set = set(list)
print(copy_set)
print('Required classrooms are :',len(copy_set))