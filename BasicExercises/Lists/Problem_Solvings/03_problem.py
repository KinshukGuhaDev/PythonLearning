# Rotate a list right by k positions 
# Input: [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

input_list = [1, 2, 3, 4, 5]
k = 2
print(input_list[-k:] + input_list[:k+1])
