import numpy as np

#11. Create a 3x3 identity matrix (★☆☆)
a=np.identity(3, dtype="uint8")
print(a)

#12. Create a 3x3x3 array with random values (★☆☆)

b=np.empty(shape=(3,3,3), dtype="uint8")
print(b)

#13. Create a 10x10 array with random values and find the minimum and maximum values (★

c=np.empty(shape=(10,10), dtype="uint8")

print(c)
print(f"Maximum value: {c.max()}\nMinimum value: {c.min()}")

#14. Create a random vector of size 30 and find the mean value (★☆☆)

d=np.empty(30)
print(d)
print(f"Mean value {d.mean()}")