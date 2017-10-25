'''
INPUT N                     {Degree of P(x)}
INPUT A(0), A(1)....A(N)    {Coefficients of P(x)}
INPUT C                     {Constant of integration}
INPUT X                     {Indepedent Variable}
'''

import numpy
import copy
#   x:@list coefficients of x
#   note: it is not p of x as in p(4)
def p(x):
    p = numpy.poly1d(x)
    return p

'''
Evaluating p(x)
'''
def eval_polynomial(x, X): 
    equation = p(x)
    A = equation.c      #list of coefficients
    B = copy.copy(A)    
    index = len(A)
    counter = len(A) - 1
    
    B[counter] = A[0]
    print('b({0}) = {1}'.format(counter, A[0])) # B(N):=A(N)
    counter = counter - 1
    for N in range(1,index):
        B[counter] = A[N] + B[counter + 1] * X
        print('b({0}) = {1} +({2})*{3} = {4}'.format(counter, A[N], B[counter + 1], X, B[counter]))
        counter = counter - 1   


    
print(eval_polynomial([-0.02, 0.2, -0.4,1.28], 4))