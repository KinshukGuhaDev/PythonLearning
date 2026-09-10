# Flatten a nested list
# Input: [1, [2, [3, 4], 5], 6]
# Output: [1, 2, 3, 4, 5, 6]

def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

my_list = [1, [2, [3, 4], 5], 6]
print(flatten(my_list))
