import numpy as np

a = np.zeros(10)
a[4] = 1
print("a =", a)

b = np.arange(10,49)
print("b =", b)

c = np.arange(10)
c = c[::-1]
print("c =", c)

d = np.arange(9).reshape(3,3)
print("d =", d)

e = np.array([1,2,0,0,4,0])
positive = np.where(e!=0)
print("Indices of non-zero values of e:", positive)

f = np.random.random(30)
print("Mean value of random vector f:", np.mean(f))

g = np.array([(1,1,1),(1,0,1),(1,1,1)])
print("g =", g)

h = np.zeros((8,8))
h[::2, ::2] =1
h[1::2, 1::2] = 1
print("h =", h)

i_seed = np.array([(0,1),(0,1)])
i = np.tile(i_seed, (4,4))
print("i =", i)

j = np.arange(11)
j [3:9] *=-1
print("j =", j)

k = np.random.random(10)
k = np.sort(k)
print("k =", k)

l1 = np.random.randint(0,2,5)
l2 = np.random.randint(0,2,5)
l_equal = np.equal(l1,l2)
print(l_equal)

m = np.arange(10, dtype=np.int32)
print(m.dtype)
m = m.astype(float)
print(m.dtype)

nA = np.arange(9).reshape(3,3)
nB = nA + 1
nC = np.dot(nA,nB)
nD = np.diagonal(nC)
print("Diagonal =", nD)
#What difference does it make that it is a dot product? Isn't it just the normal way of getting the diagonal of a matrix?
