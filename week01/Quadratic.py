#Quadradic
import math
def quadratic(a,b,c):
    argus = [a,b,c]
    for i in argus:
        if not isinstance(i,(int,float)):
            raise TypeError('bad operand type')
    delta = b*b - 4*a*c
    if delta < 0:
        return "方程无解"
    x1 = (-b+math.sqrt(delta))/2*a
    x2 = (-b-math.sqrt(delta))/2*a
    return x1,x2
print(quadratic(1,-2,2))
