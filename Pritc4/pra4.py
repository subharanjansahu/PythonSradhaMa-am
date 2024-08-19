'''
Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built in data types)
'''
nums = {9,9.0,5,9.38,'9.0',}
print(nums)
# or
values = {
  ('float',9.0),
  ('int',9)
}
print(values)
