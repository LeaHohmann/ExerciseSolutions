import numpy as np

N = 250

@profile
def calculation():
    X = np.random.randint(0,high=100,size=(N,N))
    Y = np.random.randint(0,high=100,size=(N,N+1))
    result = np.matmul(X,Y)
    print(result)

calculation()

