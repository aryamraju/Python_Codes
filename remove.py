# Remove Specified Item
# The remove() method removes the specified item.
# thislist = ["apple", "banana", "cherry"]
# thislist.remove("banana")       #remove 'banana'
# print(thislist)



thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")                   # Remove the first occurrence of "banana":
print(thislist)


# Remove Specified Index
# The pop() method removes the specified index.

# Example
# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)