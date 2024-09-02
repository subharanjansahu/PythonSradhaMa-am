'''
create a new file "practice.txt" using python. Add the following data in it.

Hi everyone
we are learning File I/O
using Python.
I like programming in Python.
'''
# with open('practice.txt','w+') as f:
#   f.write("Hi everyone\nwe are learning File I/O\nusing java.\nI like programming in java.")

'''
WAF to replace java with python in above file.
'''
# def replace():
#   with open("practice.txt",'r+') as f:
#     data = f.read()
#     # print(data)
#   new_data = data.replace("java","python")
#   print(new_data)

#   with open("practice.txt",'w+') as f:
#     f.write(new_data)

# replace()

'''
Search the word learning exists in the file or not
'''
# with open("practice.txt",'r+') as f:
#   data = f.read()
# print("learning" in data)
# or

# def check_for_word():
#   word = 'learning'
#   with open('practice.txt','r+') as f:
#     data = f.read()
#     if(data.find(word) != -1):
    # if(word in data): 
#       print("Found")
#     else:
#       print("Not found")

# check_for_word()

'''
Waf to find in which line of the file does the word "learning" occur first.
Print -1 if word not found
'''
def line_num():
  word = 'learning'
  data = True
  line_no = 1
  with open('practice.txt', 'r') as f:
    while data:
      data = f.readline()
      if(word in data):
        print("Found in line no. :",line_no)
        break
      line_no += 1
    else:
      print("Not found -1")

line_num()