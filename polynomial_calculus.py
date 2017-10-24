'''
INPUT N                     {Degree of P(x)}
INPUT A(0), A(1)....A(N)    {Coefficients of P(x)}
INPUT C                     {Constant of integration}
INPUT X                     {Indepedent Variable}
'''

import numpy
# x:@list coefficients of x|
def p(x):
    p = numpy.poly1d(x)
    return p


print(p([-0.002, 0.2, -0.4,1.28]))