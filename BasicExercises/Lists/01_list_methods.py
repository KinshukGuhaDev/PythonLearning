intList = [1, 2, 3, 4, 5]
stringList = ['Kinshuk', 'Arif', 'Kaif', 'Subhojit', 'Swapan']

intList.append(6) #this will append the element as the last element of the list which will alter the original list
# print(intList)

stringList2 = stringList.copy() #this will copy the list as a new list 
stringList.append([0, 10, 'Kuntal', 10.5]) #this will append the list as a single element
stringList2.extend([0, 10, 'Kuntal', 10.5]) #this will append the list as multiple elements
# print('stringList:', stringList, 'stringList2:', stringList2)

newList = ['zebra', 'tiger', 'lion']
newList.insert(1, 'giraffe') #this will insert the element at the specified index
# print(newList)
