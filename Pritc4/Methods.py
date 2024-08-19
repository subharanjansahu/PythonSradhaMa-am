student = {
  'name' : 'Jack',
  'subject' : {
    'phy' : 87,
    'chem' : 79,
    'mth' : 96
  },
  'roll_no.' : 24
}

print(student)
# length of the dictionary
print(len(student))

# keys() return all keys
print(student.keys())

# type cast
print(list(student.keys()))
print(len(list(student.keys())))

# values() return all values
print(student.values())
print(tuple(student.values()))

# items() return all(key,value) pairs as tuple
print(student.items())
pairs = list(student.items())
print(pairs[1])

# get("key") returns the value according to key
print(student.get('roll_no.'))

# compare dic['key'] and dict.get('key')
print(student['name'])
print(student.get('name'))

# print(student['sec'])   # 'sec' key is not present (it gives keyerror)
print(student.get('sec'))

# update(newDict) insert the specified items to the dictionary
new_dict = {'sec':'A','age':16,'name':'subha'}
student.update(new_dict)
# or
student.update({'city':'delhi'})
print(student)