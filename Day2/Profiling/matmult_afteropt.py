# Program to multiply two matrices using nested loops
import random

N = 250

# NxN matrix
@profile
def makeX():
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X

# Nx(N+1) matrix
@profile
def makeY():
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y

# result is Nx(N+1)
@profile
def makeresult():
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

# iterate through rows of X
@profile
def iteration():
    X = makeX()
    Y = makeY()
    result = makeresult()
    for i in range(N):
        # iterate through columns of Y
        for j in range(N+1):
            # iterate through rows of Y
            for k in range(N):
                result[i][j] += X[i][k] * Y[k][j]
    return result

result = iteration()
print(result)

