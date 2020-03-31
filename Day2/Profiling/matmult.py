# Program to multiply two matrices using nested loops
import random

N = 250

# NxN matrix
X = []
#@profile
def makeX():
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
#@profile
def makeY():
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
result = []
#@profile
def makeresult():
    for i in range(N):
        result.append([0] * (N+1))

# iterate through rows of X
#@profile
def iteration(X,Y):
    for i in range(N):
        # iterate through columns of Y
        for j in range(N+1):
            # iterate through rows of Y
            for k in range(N):
                result[i][j] += X[i][k] * Y[k][j]

makeX()
makeY()
makeresult()
iteration(X,Y)

for r in result:
    print(r)

