#remove duplicate elements from the list
my_list = [3, 1, 3, 2, 1]
my_list = list(dict.fromkeys(my_list)) #can be done by using dictionary method {this will preserve the original order}
my_list = list(set(my_list)) #can be done by converting the list to set first {set always be unique and in sorted order} and then convert back to list again. 
print(my_list)