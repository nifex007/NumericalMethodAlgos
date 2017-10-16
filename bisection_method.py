import math

''' 
    a, b are left and right end points
    
'''

def f(x):
    return math.exp(x)-2-x

# iterations = 1
# max_iterations = 100


def bisect(a, b):
    iterations = 1
    max_iterations = 10
    c = float((a+b)/2)
    ya = f(a)
    yb = f(b)
    if (ya * yb) > 0:
        return 
    else:
        while (True):
            yc = f(c)
            if yc == 0:
                # then a = c and b = c
                print("Iteration ", iterations)
                print("ROOT: ", c)
                break
            elif(ya * yc) < 0:
                print("Iteration ", iterations)
                b = c
            else:
                print("Iteration ", iterations)
                a = c
            
            c = float((a+b)/2)
            iterations += 1
    
    return c


print(bisect(0.5, 2.5))

    
        

