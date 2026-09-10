#Given a list and a target number, return every unique pair whose sum equals the target.
# nums = [2, 7, 11, 15]
# target = 9
#Output: [(2, 7)]


nums = [1, 5, 3, 3, 7, 2, 8]
target = 10
result = set()
for i in nums:
    for j in nums:
        if i+j == target:
            result.add(tuple(sorted((i,j))))
print(result)