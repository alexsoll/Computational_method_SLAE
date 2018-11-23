import numpy as np
from fractions import Fraction
import copy

def subtract(x, y, coeff):
    return list(map(lambda a,b: a - coeff * b, x, y))

#Gauss method with numpy arrays and float values, 
#gives not an exact result, but close to the style of Python

def GAUSS(matrix, b, x):
    N = len(b)
    for i, mtrxstr in enumerate(matrix):
        for j,val in enumerate(matrix[i+1:]):
            coeff = float(mtrxstr[i] / val[i])
            b[i+j+1] = b[i+j+1] * coeff - b[i]
            newstr = coeff * val - mtrxstr
            matrix[i+j+1] = np.array(newstr, dtype='f')
    for i, val in enumerate(matrix[::-1]):
        sum = 0.
        for j in range(N-i,N):
            sum += val[j] * x[j]
        x[N-i-1] = (b[N-i-1] - sum) / val[N-i-1]

    return x


def Determinant(matrix):
    N = len(matrix)
    for j in range(N):
        for i in range(j+1,N):
            coeff = matrix[i][j] / matrix[j][j]
            for k in range(j,N):
                matrix[i][k] -= coeff * matrix[j][k]
            #matrix[i] = subtract(matrix[i],matrix[j], coeff)
    res = Fraction(1,1)
    for i in range(N):
        res *= matrix[i][i]
    return res



#Gauss method with Rational numbers, gives exact result
def Gauss(matrix, b, x): 
    matr = copy.deepcopy(matrix)
    N = len(matrix)
    for j in range(N):
        for i in range(j+1,N):
            coeff = matr[i][j] / matr[j][j]
            for k in range(j,N):
                matr[i][k] = matr[i][k] - coeff * matr[j][k]
            #matrix[i] = subtract(matrix[i],matrix[j], coeff)           #"for k" in one string
            b[i] = b[i] - coeff * b[j]
    for i in range(N-1,-1,-1):
        sum = Fraction(0,1)
        for j in range(i+1,N):
            sum = sum + matr[i][j] * x[j]
        x[i] = (b[i] - sum) / matr[i][i]      
    return x

def Kramer(matrix, b , x):
    matr = copy.deepcopy(matrix)
    N = len(matr)
    for i in range(N):
        new_matrix = list(matr)
        for j in range(N):
            new_matrix[j][i] = b[j]
        x[i] = Determinant(new_matrix) / Determinant(matr)
    return x






x = np.zeros(3)      
lst = np.array([[2,4,5],
       [3,-1,2],    
       [-4,1,1]], dtype='f')
b = np.array([11,4,-2], dtype='f')
GAUSS(lst, b, x)
print(lst)
print(b)
print(x)


matrix = [[Fraction(2,1),Fraction(4,1),Fraction(5,1)],
          [Fraction(3,1),Fraction(-1,1),Fraction(2,1)],
          [Fraction(-4,1),Fraction(1,1),Fraction(1,1)]]
b1 = [Fraction(11,1),Fraction(4,1),Fraction(-2,1)]
x1 = [Fraction(0,1),Fraction(0,1),Fraction(0,1)]

res = Gauss(matrix, b1, x1)
res1 = Kramer(matrix, b1, x1)

print("Gauss method")
print(res)
print('\n' + "Kramer method")
print(res1)
print(matrix)

#print(Determinant(matrix))