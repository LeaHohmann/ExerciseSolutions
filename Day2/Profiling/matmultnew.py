import numpy as np

N = 250

@profile
def calculation():
    X = np.random.randint(0,high=100,size=(N,N))
    Y = np.random.randint(0,high=100,size=(N,N+1))
    result = np.zeros((N,N+1))
    for i in range(N):
        for j in range(N+1):
            result[i,j] = np.sum(X[i,:]*Y[:,j])
    print(result)

calculation()

