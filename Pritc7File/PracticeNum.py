'''
From a file containing numbers separated by comma, print the count of even numbers.
'''
count  = 0
with open('NumberFile.txt', 'w+') as f:
  f.write("2,83,79,4,76,35")
  f.seek(0)
  data = f.read()
  print(data)
# basic code
  # num = ''
  # for i in range(len(data)):
  #   if(data[i] == ','):
  #     # print(int(num))
  #     num = int(num)
  #     if(num % 2 == 0):
  #       print(num)
  #     num = ''
  #   else:
  #     num += data[i]

  nums = data.split(',')
  for i in nums:
    if(int(i) % 2 == 0):
      print(i)
      count += 1
print("Number of even :",count)