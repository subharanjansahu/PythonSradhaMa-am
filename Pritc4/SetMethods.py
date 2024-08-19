collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add('hello')
collection.add(3)
# adding a tuple
collection.add((1,3,5))
# collection.add([7,9,1,3]) # we cann't add list

# remove()/discard()
collection.remove(2)
# collection.remove(4)  #it gives an keyerror if item is not present
collection.discard(4) #it gives None if item is not present 

# pop()
re = collection.pop()
print(re)

# clear() -> gives the empty set
# collection.clear()
print(collection)