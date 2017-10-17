''' 
    a, b are left and right end points
    
'''

def f(x):
    return (x**3)-x-2

# iterations = 1
# max_iterations = 100


def bisect(a, b):
    iterations = 1    
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
                print("Iteration {0}:, a = {1}, b = {2} c = {3}, f(c) = {4} ".format(iterations, a, b, c, yc))
                print("ROOT: ", c)
                break
            elif(ya * yc) < 0:
                b = c
                print("Iteration {0}:, a = {1}, b = {2}, c = {3}, f(c) = {4} ".format(iterations, a, b, c, yc))
            else:
                a = c
                print("Iteration {0}:, a = {1}, b = {2} c = {3}, f(c) = {4} ".format(iterations, a, b, c, yc))
            
            c = float((a+b)/2)
            iterations += 1
    
    return c


print(bisect(1, 2))

    
        

