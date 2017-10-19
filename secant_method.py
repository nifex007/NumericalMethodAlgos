'''
f is input object function as string
p0 and p1 initial approximations to a zero
delta tolerance for p0
epsilon is the tolerance for finction values of y
max1 maximum number of iterations
k is number of iterations
y is the function value of f(p1)

'''
def f(x):
    return (x**2)-x-2

def secant(p0,p1,delta,epsilon):
    for k in range(1, max1):
        p2 = (p1-f(p1) * (p1-p0))/(f(p1)-f(p0))
        err = abs(p2-p1)
        relerr=(2*err)/(abs(p2)+delta)
        p0=p1
        p1=p2
        y=f(p1)
        print("Iteration {0}: p1={1}, y={2}".format(k,p1,y))

        if(err < delta) or (relerr <delta) or (abs(y)<epsilon):
            return
