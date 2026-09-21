#1. Import the numpy package under the name np (★☆☆)
import numpy as np
#2. Print the numpy version and the configuration (★☆☆)
print(np.__version__)
#3. Create a null vector of size 10 (★☆☆)
a=np.zeros(10, dtype="uint8")
#print(a)
#4. How to find the memory size of any array (★☆☆)
b=np.array([1,2,3,4,5], dtype="uint8")
print(b.itemsize)
print(b)
#5. How to get the documentation of the numpy add function from the command line? (★☆☆)
#help(np.add)

#6. Create a null vector of size 10 but the fifth value which is 1 (★☆☆)

#7. Create a vector with values ranging from 10 to 49 (★☆☆)
d=np.arange(10,50, dtype="uint8")
#d=np.random.randint(10,50, size=(1,50)dtype="uint8")
print(d)
#8. Reverse a vector (first element becomes last) (★☆☆)
e=np.arange(1,11, dtype="uint8")
new_d=e[::-1]
#print(type(new_d), type(e))

print(new_d)

#9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)
f=np.random.randint(0,9,size=(3,3))
print(f)