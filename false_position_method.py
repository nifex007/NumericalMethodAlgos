import math
'''
f is the function input
a and b are left and right end points
max1 is the maximum number of iterations
c is the zero
'''

def f(x):
    # return math.exp(x)-2-x
    # return x**3-x-2
    return math.cos(x)-x**3
    

def false_position(a,b):
    max1 = 100
    ya = f(a)
    yb = f(b)
    
    if(ya * yb) > 0:
        print("Note: f({0})*f({1})>0".format(a,b))
        return
    for iteration in range(1,max1):
        dx  = yb*(b-a)/(yb-ya)
        c   = b-dx
        ac  = c-a
        yc  = f(c)
        print("Iteration {0}: a = {1}, b = {2} c = {3}, f(c) = {4} ".format(iteration, a, b, c, yc))
        if (yc == 0):
            break
        elif (yb*yc) > 0:
            b = c
            yb = yc
        else:
            a = c
            ya = yc

    return c
            
            
      


print(false_position(0,1))