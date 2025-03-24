# thislist = ["apple", "banana", "cherry"]
# thislist[1] = "blackcurrant"              #change item value
# print(thislist)


# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]       #Change a Range of Item Values
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]    #Change the second value by replacing it with two new values:
# print(thislist)



#Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
