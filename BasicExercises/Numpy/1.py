import numpy as np
x = [1,0]
y = [0,1]
z = []

for n,v in zip(x,y):
    z.append(n+v)

# print(z)

#Vector addition using numpy
u = np.array([1,0])
v = np.array([0,1])
w = u + v
# print(w)

#Vector Multiplication using numpy
a = np.array([2,4])
c = 3*a
# print(c)

#Vector Dot Product using numpy
d = np.array([1,2])
dd = np.array([3,4])
e = np.dot(d, dd)
# print(e)


# Create a numpy array

a = np.array([1, -1, 1, -1])
mean = a.mean()
# print(mean)
standard_deviation=a.std()
# print(standard_deviation)


arr1 = np.array([-1, 1])
arr2 = np.array([1, 1])

print(np.dot(arr1, arr2))  # Output: 0