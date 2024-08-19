age = int(input("Enter Age = "))
if(age >= 18):
  print("Can vote")
  if age <= 65:
    print("Can drive")
  else:
    print("Can't drive")
else:
  print("Can't drive \nCan't vote")