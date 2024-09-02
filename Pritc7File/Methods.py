'''
# read() method

f = open("demo.txt", 'r')
# data = f.read()
print(f.read())

print(f.tell())   #return the position of the cursor
f.seek(4)   #change the position of the cursor
data = f.read(6)
print(data)
print(f.readline(),end='')
print(f.readline())   #read one line
f.close()

'''

'''
# write() overwrite the data
f = open('demo.txt','w')
f.write("I want to learn Python. 123")
f.close()
'''
'''
# write()
f = open('demo.txt','a')
f.write(" \nThen next to learn JS.")
f.close()
'''

'''
f = open('demo.txt','r+')
# print(f.read())
f.write("Then next to learn JS.")
print(f.read())
f.close()
'''

'''
f = open('demo.txt','w+')
print(f.read())
f.write(" \nThen next to learn JS.")
f.seek(0)
print(f.read())
f.close()
'''

'''
with open("demo.txt","r+") as f:
  print(f.read())
  f.write(" teach by shradha ma'am")
  f.seek(0)
  print(f.read())
'''

'''
with open('sampal.txt', 'w+') as f:
  f.write("Hello world")
'''

# remove a file
import os

os.remove('sampal.txt')