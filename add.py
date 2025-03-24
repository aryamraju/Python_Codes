# Append Items
# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


# Insert Items
# To insert a list item at a specified index, use the insert() method.

# The insert() method inserts an item at the specified index:



thislist = ["apple", "banana", "cherry"]    #Insert an item as the second position:
thislist.insert(1, "orange")
print(thislist)




# Extend List
# To append elements from another list to the current list, use the extend() method.


thislist = ["apple", "banana", "cherry"]               #Add the elements of tropical to thislist:
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)