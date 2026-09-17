#to add or an element to a tuple
my_tup = (1, 2, 3, 4, 5)
my_tup = my_tup + (6,)
print(my_tup)

#to remove an element from a tuple
my_tup = list(my_tup)
my_tup.remove(6)
my_tup = tuple(my_tup)
print(my_tup)

#to update an element in a tuple
my_tup = list(my_tup)
my_tup[0] = 6
my_tup = tuple(my_tup)
print(my_tup)

#to insert a value in a specific index
new_tup = my_tup[:2] + (99, ) + my_tup[2:]
print(new_tup)

#to remove a value from a specific index
new_tup = my_tup[:2] + my_tup[3:]
print(new_tup)
