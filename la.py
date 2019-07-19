from mat import *
import numpy as np

A = readm('A.csv')
b = readm('b.csv')

def solve(A, b):
    """ solve(A,b)
    A = matrix m,k
    b = matrix k,1
    x = list of solution [x_1,x_2,...,x_n]

    using Gauss Method
    1. กำจัดจุดอ่อน -  elimination
    2. แทนค่าย้อนกลับ - back substitution
    """

    # จำนวนสมการ คือ แถว
    # จำนวนตัวแปร คือ หลัก

    # YOUR CODE HERE
    A,b = np.array(A),np.array(b)

    # 1. elimination
    n = len(A[0])
    x = np.array([0]*n)
    for k in range(n-1): # pivot equation(a) ทำให้ตัวแปรตัวที่ 1 หายไป #k
        for j in range(k+1,n):  # pivot eq #j
            lam = A[j][k]/A[k][k]
            
            # update A[j][kเป็นต้นไป]
            A[j,k:n] = A[j,k:n] - lam*A[k,k:n]

            # update b[j]
            b[j] = b[j] - lam*b[k]
    # 2. back substitution
    x[n-1] = b[n-1] / A[n-1][n-1]
    for k in range(n-1, -1, -1):
        x[k] = (b[k] - np.dot(A[k,k+1:n],x[k+1:n]))/A[k,k]

    return x.flatten()


print( solve(A,b) )