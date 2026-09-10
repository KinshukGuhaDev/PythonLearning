# 1. Move all zeros to the end
#    Input: [0, 1, 0, 3, 12]
#    Output: [1, 3, 12, 0, 0]

mylist = [0, 1, 0, 3, 12]
arr1 = []
arr2 = []
for i in mylist:
    if i == 0:
        arr1.append(i)
    else:
        arr2.append(i)
print(arr2 + arr1)