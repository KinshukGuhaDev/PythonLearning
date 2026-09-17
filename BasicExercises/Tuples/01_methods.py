my_tup = ('bit', 'new york', 50, 40.5, 'test', 'tuples')

print(my_tup.count(40.5)) #this will print how many times a searched element was fond in the tuple
if 40.5 in my_tup:
    print(my_tup.index(40.5)) #this will print the index of the searched element
else:
    print("not found!")

strings_only = [x for x in my_tup if isinstance(x, str)]
numbers_only = [y for y in my_tup if isinstance(y, (int, float))]
print(len(strings_only)) #this will print the length of the tuple
print(min(strings_only)) #this will print the min element in the tuple
print(max(strings_only)) #this will print the max element in the tuple

print(len(numbers_only)) #this will print the length of the tuple
print(min(numbers_only)) #this will print the min element in the tuple
print(max(numbers_only)) #this will print the max element in the tuple
print(sum(numbers_only)) #this will print the sum of the elements in the tuple
print(sorted(numbers_only, reverse=True)) #this will print the sorted elements in the tuple in descending order
print(sorted(numbers_only, reverse=False)) #this will print the sorted elements in the tuple in ascending order
